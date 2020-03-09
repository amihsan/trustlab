from pathlib import Path
import os
from datetime import datetime

folder_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_PATH = Path("trustlab/lab/log/" + folder_name + "/")
os.mkdir(LOG_PATH.absolute())


