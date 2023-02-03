import getopt
import sys
from models.scenario_ct_random import Scenario


def main(argv):
    observations, agents, outfile, scenario_name = 0, 0, '', ''
    try:
        opts, _ = getopt.getopt(
            argv, "hm:a:o:n:", ["messages=", "agents=", "outfile", "name"])
    except getopt.GetoptError:
        print('gen.py -m <number of messages> -a <number of agents> -o <output file> (-n <scenario name>)')
        sys.exit(2)
    if len(opts) == 0:
        print('gen.py -m <number of messages> -a <number of agents> -o <output file> (-n <scenario name>)')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('gen.py -m <number of messages> -a <number of agents> -o <output file> (-n <scenario name>)')
            sys.exit()
        elif opt in ('-m', '--messages'):
            observations = int(arg)
        elif opt in ('-a', '--agents'):
            agents = int(arg)
        elif opt in ('-o', '--outfile'):
            outfile = arg
        elif opt in ('-n', '--name'):
            scenario_name = arg
    scenario = Scenario(observations, agents, outfile, scenario_name)
    scenario.generate_and_write_to_file()


if __name__ == "__main__":
    main(sys.argv[1:])
