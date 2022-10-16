import ast
import re
import uuid
import json
from collections import deque

class AGENTS:
    object = None
    doneobjects = []

    storedString = ""
    isdone = False

    def add_line(self, line):

        line = self.storedString + line
        self.storedString = ""

        if len(line) == 0:
            return

        if line[:1] == ']':
            self.isdone = True
            return line[1:].strip()

        if line[:1] == '[':
            return line[1:].strip()

        parts = re.split("^'([^']{1,})'(?:,|)(.*)", line)

        if len(parts) <= 2:
            self.storedString = line
            return ""

        self.object = {}
        self.object["name"] = parts[1]
        self.object["_id"] = uuid.uuid4().hex

        self.doneobjects.append(self.object)
        self.object = None

        return parts[2]

    def is_complex(self, key):
        for obj in (self,) + type(self).__mro__:
            if key in obj.__dict__:
                return True
        else:
            return False

    def get_next_object(self):
        return None

    def get_done_objects(self):
        return self.doneobjects

    def clear_objects(self):
        self.doneobjects = []

    def is_done(self):
        return self.isdone


class HISTORY:
    object = None
    doneobjects = []

    storedString = ""
    isdone = False
    storedKey = None

    q = deque()
    tq = deque()

    def add_line(self, line):

        line = line.strip()

        if len(line) == 0:
            return

        if (line[:1] == ']' or line[:1] == '}') and len(self.q) == 2:
            self.q.pop()
            self.doneobjects.append(self.object)
            self.object = {}
            return line[1:].strip()

        if (line[:1] == '[' or line[:1] == '{') and len(self.q) == 1:
            self.q.append('[')
            self.object = {}
            return line[1:].strip()

        if line[:1] == '}' and len(self.q) == 1:
            self.isdone = True
            self.q.pop()
            return line[1:].strip()

        if line[:1] == '{' and len(self.q) == 0:
            self.q.append('{')
            return line[1:].strip()

        if line[:1] == ',' and len(self.q) == 2:
            self.doneobjects.append(self.object)
            self.object = {}
            return line[1:].strip()

        if line[:1] == ',' and len(self.q) == 1:
            self.storedKey = None
            return line[1:].strip()

        if self.storedKey is None:
            parts = re.split("^'([^']{1,})':(?:,|)(.*)", line)

            if len(parts) <= 2:
                self.storedString = line
                return ""

            self.storedKey = parts[1]

            return parts[2]
        else:
            resstring = ""
            index = 0
            until_end = False

            if line[0] not in ['{', '[', '(', '\'']:
                until_end = True

            while index < len(line):
                if line[index] in ['{', '[', '(']:
                    self.tq.append(line[index])

                if line[index] == '}':
                    if self.tq.pop() != '{':
                        raise Exception("Configuration not valid!")

                if line[index] == ')':
                    if self.tq.pop() != '(':
                        raise Exception("Configuration not valid!")

                if line[index] == ']':
                    if self.tq.pop() != '[':
                        raise Exception("Configuration not valid!")

                if line[index] == "'":
                    if len(self.tq) == 0:
                        self.tq.append("'")
                    else:
                        last = self.tq.pop()
                        if not last == "'":
                            self.tq.append(last)
                            self.tq.append("'")

                resstring += line[index]
                index += 1

                if len(self.tq) == 0 and (not until_end or (len(line) > index and line[index] in ['}', ']', ')', ','])):
                    until_end = False
                    break

            if len(self.tq) > 0 or until_end:
                self.storedString = self.storedString + line
                return ""

            parts = re.split("^.'([^']*)',(?: |)'([^']*)',(?: |)((?:-|)\\d*[.]*\\d*).", self.storedString + resstring)

            self.object["parent"] = self.storedKey
            self.object["child"] = parts[1]
            self.object["url"] = parts[2]
            self.object["value"] = float(parts[3])

            self.storedString = ""

            return line[index:]

    def is_complex(self, key):
        for obj in (self,) + type(self).__mro__:
            if key in obj.__dict__:
                return True
        else:
            return False

    def get_next_object(self):
        return None

    def get_done_objects(self):
        return self.doneobjects

    def clear_objects(self):
        self.doneobjects = []

    def is_done(self):
        return self.isdone


class DETAILS:
    object = None
    doneobjects = []

    storedString = ""
    storedKey = None
    isdone = False
    parentId = ""

    q = deque()

    def __init__(self, parent_id):
        self.parentId = parent_id
        self.object = None
        self.doneobjects = []

        self.storedString = ""
        self.storedKey = None
        self.isdone = False

        q = deque()

    def add_line(self, line):

        line = (self.storedString + line).strip()
        self.storedString = ""

        if len(line) == 0:
            return

        if self.object is None and line[:1] == '{':
            self.q.append('{')
            return line[1:].strip()

        if line[:1] == '}' and len(self.q) == 1:
            self.q.pop()
            self.doneobjects.append(self.object)
            self.object = None
            self.storedKey = None
            self.isdone = True
            return line[1:].strip()

        if line[:1] == ',' and len(self.q) == 1:
            self.doneobjects.append(self.object)
            self.object = None
            self.storedKey = None
            return line[1:].strip()

        if self.storedKey is None:
            parts = re.split("^'([^']{1,})':(?:,|)(.*)", line)

            if len(parts) <= 2:
                self.storedString = line
                return ""

            self.object = {}
            self.object["_id"] = uuid.uuid4().hex
            self.object["observation_id"] = self.parentId

            self.storedKey = parts[1]
            return parts[2]
        else:
            resstring = ""
            index = 0
            tq = deque()
            until_end = False

            if line[0] not in ['{', '[', '(', '\'']:
                until_end = True

            while index < len(line):
                if line[index] in ['{', '[', '(']:
                    tq.append(line[index])

                if line[index] == '}':
                    if tq.pop() != '{':
                        raise Exception("Configuration not valid!")

                if line[index] == ')':
                    if tq.pop() != '(':
                        raise Exception("Configuration not valid!")

                if line[index] == ']':
                    if tq.pop() != '[':
                        raise Exception("Configuration not valid!")

                if line[index] == "'":
                    if len(tq) == 0:
                        tq.append("'")
                    else:
                        last = tq.pop()
                        if not last == "'":
                            tq.append(last)
                            tq.append("'")

                resstring += line[index]
                index += 1

                if len(tq) == 0 and (not until_end or (len(line) > index and line[index] in ['}', ']', ')', ','])):
                    until_end = False
                    break

            if len(tq) > 0 or until_end:
                self.storedString = line
                return ""

            self.object[self.storedKey] = json.loads(resstring.replace("'", '"'))

            return line[index:]

    def is_complex(self, key):
        for obj in (self,) + type(self).__mro__:
            if key in obj.__dict__:
                return True
        else:
            return False

    def get_next_object(self):
        return None

    def get_done_objects(self):
        return self.doneobjects

    def clear_objects(self):
        self.doneobjects = []

    def is_done(self):
        return self.isdone


class OBSERVATIONS:
    object = None
    doneobjects = []

    storedString = ""
    storedKey = None
    isdone = False
    next_object = None

    details = "DETAILS"

    q = deque()

    def add_line(self, line):

        line = (self.storedString + line).strip()
        self.storedString = ""

        if len(line) == 0:
            return

        if line[:1] == ']' and len(self.q) == 0:
            self.isdone = True
            return line[1:].strip()

        if self.object is None and line[:1] == '[':
            return line[1:].strip()

        if self.object is None and line[:1] == '{':
            self.object = {}
            self.object["_id"] = uuid.uuid4().hex
            return line[1:].strip()

        if line[:1] == '}' and len(self.q) == 0:
            self.doneobjects.append(self.object)
            self.object = None
            return line[1:].strip()

        if line[:1] == ',' and len(self.q) == 0:
            self.storedKey = None
            self.next_object = None
            return line[1:].strip()

        if self.storedKey is None:
            parts = re.split("^'([^']{1,})':(?:,|)(.*)", line)

            if len(parts) <= 2:
                self.storedString = line
                return ""

            if self.is_complex(self, parts[1]):
                self.next_object = eval(getattr(self, parts[1]))
                self.next_object.__init__(self.next_object, self.object["_id"])

            self.storedKey = parts[1]

            return parts[2]
        else:
            resstring = ""
            index = 0
            tq = deque()
            until_end = False

            if line[0] not in ['{', '[', '(', '\'']:
                until_end = True

            while index < len(line):
                if line[index] in ['{', '[', '(']:
                    tq.append(line[index])

                if line[index] == '}':
                    if tq.pop() != '{':
                        raise Exception("Configuration not valid!")

                if line[index] == ']':
                    if tq.pop() != '[':
                        raise Exception("Configuration not valid!")

                if line[index] == ')':
                    if tq.pop() != '(':
                        raise Exception("Configuration not valid!")

                if line[index] == "'":
                    if len(tq) == 0:
                        tq.append("'")
                    else:
                        last = tq.pop()
                        if not last == "'":
                            tq.append(last)
                            tq.append("'")

                resstring += line[index]
                index += 1

                if len(tq) == 0 and (not until_end or (len(line) > index and line[index] in ['}', ']', ')', ','])):
                    until_end = False
                    break

            if len(tq) > 0 or until_end:
                self.storedString = line
                return ""

            self.object[self.storedKey] = json.loads(resstring.replace("'", '"'))

            return line[index:]

    def is_complex(self, key):
        for obj in (self,) + type(self).__mro__:
            if key in obj.__dict__:
                return True
        else:
            return False

    def get_next_object(self):
        return self.next_object

    def get_done_objects(self):
        return self.doneobjects

    def clear_objects(self):
        self.doneobjects = []

    def is_done(self):
        return self.isdone

class SCALES_PER_AGENT:
    object = None
    doneobjects = []

    storedString = ""
    storedKey = None
    parent = None
    isdone = False
    next_object = None

    q = deque()

    def add_line(self, line):

        line = (self.storedString + line).strip()
        self.storedString = ""

        if len(line) == 0:
            return

        if line[:1] == '}' and len(self.q) == 1:
            self.isdone = True
            self.q.pop()
            return line[1:].strip()

        if line[:1] == '{' and len(self.q) == 0:
            self.q.append('{')
            return line[1:].strip()

        if line[:1] == '{' and len(self.q) == 1:
            self.object = {}
            self.q.append('{')
            self.object["_id"] = uuid.uuid4().hex
            self.object["parent"] = self.parent
            return line[1:].strip()

        if line[:1] == '}' and len(self.q) == 2:
            self.doneobjects.append(self.object)
            self.q.pop()
            self.object = None
            return line[1:].strip()

        if line[:1] == ',' and len(self.q) == 1:
            self.parent = None
            self.storedKey = None
            return line[1:].strip()

        if line[:1] == ',' and len(self.q) == 2:
            self.storedKey = None
            return line[1:].strip()

        if self.parent is None:
            parts = re.split("^'([^']{1,})':(?:,|)(.*)", line)

            if len(parts) <= 2:
                self.storedString = line
                return ""

            self.parent = parts[1]

            return parts[2]
        else:
            if self.storedKey is None:
                parts = re.split("^'([^']{1,})':(?:,|)(.*)", line)

                if len(parts) <= 2:
                    self.storedString = line
                    return ""

                self.storedKey = parts[1]

                return parts[2]
            else:
                resstring = ""
                index = 0
                tq = deque()
                until_end = False

                if line[0] not in ['{', '[', '(', '\'']:
                    until_end = True

                while index < len(line):
                    if line[index] in ['{', '[', '(']:
                        tq.append(line[index])

                    if line[index] == '}':
                        if tq.pop() != '{':
                            raise Exception("Configuration not valid!")

                    if line[index] == ')':
                        if tq.pop() != '(':
                            raise Exception("Configuration not valid!")

                    if line[index] == ']':
                        if tq.pop() != '[':
                            raise Exception("Configuration not valid!")

                    if line[index] == "'":
                        if len(tq) == 0:
                            tq.append("'")
                        else:
                            last = tq.pop()
                            if not last == "'":
                                tq.append(last)
                                tq.append("'")

                    resstring += line[index]
                    index += 1

                    if len(tq) == 0 and (not until_end or (len(line) > index and line[index] in ['}', ']', ')', ','])):
                        until_end = False
                        break

                if len(tq) > 0 or until_end:
                    self.storedString = line
                    return ""

                self.object[self.storedKey] = json.loads(resstring.replace("'", '"'))

                return line[index:]

    def is_complex(self, key):
        for obj in (self,) + type(self).__mro__:
            if key in obj.__dict__:
                return True
        else:
            return False

    def get_next_object(self):
        return None

    def get_done_objects(self):
        return self.doneobjects

    def clear_objects(self):
        self.doneobjects = []

    def is_done(self):
        return self.isdone


class METRICS_PER_AGENT:
    object = None
    doneobjects = []

    storedStrings = []
    storedKey = None
    parent = None
    isdone = False
    next_object = None

    q = deque()
    tq = deque()
    tqcount = 0

    def add_line(self, line):

        line = line.strip()

        if len(line) == 0:
            return

        if self.tqcount == 0:

            if line[:1] == '}' and len(self.q) == 1:
                self.isdone = True
                self.q.pop()
                return line[1:].strip()

            if line[:1] == '{' and len(self.q) == 0:
                self.q.append('{')
                return line[1:].strip()

            if line[:1] == '{' and len(self.q) == 1:
                self.object = {}
                self.q.append('{')
                self.object["_id"] = uuid.uuid4().hex
                self.object["parent"] = self.parent
                return line[1:].strip()

            if line[:1] == '}' and len(self.q) == 2:
                self.doneobjects.append(self.object)
                self.q.pop()
                self.object = None
                return line[1:].strip()

            if line[:1] == ',' and len(self.q) == 1:
                self.parent = None
                self.storedKey = None
                return line[1:].strip()

            if line[:1] == ',' and len(self.q) == 2:
                self.storedKey = None
                return line[1:].strip()

        if self.parent is None:
            parts = re.split("^'([^']{1,})':(?:,|)(.*)", line)

            self.parent = parts[1]

            return parts[2]
        else:
            if self.storedKey is None:
                parts = re.split("^'([^']{1,})':(?:,|)(.*)", line)

                self.storedKey = parts[1]

                return parts[2]
            else:
                resstring = ""
                index = 0
                until_end = False

                if line[0] not in ['{', '[', '(', '\'']:
                    until_end = True

                while index < len(line):
                    if line[index] in ['{', '[', '(']:
                        self.tq.append(line[index])
                        self.tqcount+=1

                    if line[index] == '}':
                        if self.tq.pop() != '{':
                            raise Exception("Configuration not valid!")
                        self.tqcount-=1

                    if line[index] == ')':
                        if self.tq.pop() != '(':
                            raise Exception("Configuration not valid!")
                        self.tqcount-=1

                    if line[index] == ']':
                        if self.tq.pop() != '[':
                            raise Exception("Configuration not valid!")
                        self.tqcount-=1

                    if line[index] == "'":
                        if self.tqcount == 0:
                            self.tq.append("'")
                            self.tqcount+=1
                        else:
                            last = self.tq.pop()
                            self.tqcount-=1
                            if not last == "'":
                                self.tq.append(last)
                                self.tq.append("'")
                                self.tqcount+=2

                    resstring += line[index]
                    index += 1

                    if self.tqcount == 0 and (not until_end or (len(line) > index and line[index] in ['}', ']', ')', ','])):
                        until_end = False
                        break

                if self.tqcount > 0 or until_end:
                    self.storedStrings.append(line)
                    return ""

                self.storedStrings.append(resstring)
                self.object[self.storedKey] = json.loads(("".join(self.storedStrings)).replace("'", '"'))
                self.storedStrings = []

                return line[index:]

    def is_complex(self, key):
        for obj in (self,) + type(self).__mro__:
            if key in obj.__dict__:
                return True
        else:
            return False

    def get_next_object(self):
        return None

    def get_done_objects(self):
        return self.doneobjects

    def clear_objects(self):
        self.doneobjects = []

    def is_done(self):
        return self.isdone

