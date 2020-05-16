from pathlib import Path
import os
import asyncio
from datetime import datetime

PREPARE_SCENARIO_SEMAPHORE = asyncio.Semaphore(1)
DISTRIBUTOR = "greedy"


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_scenario_run_id():
    return "scenarioRun:" + datetime.now().strftime("%Y-%m-%d_%H:%M:%S")


class Logging:
    LOG_PATH = Path("trustlab/lab/log/")
    if not LOG_PATH.is_dir():
        os.mkdir(LOG_PATH.absolute())

    @staticmethod
    def new_log_path():
        folder_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        Logging.LOG_PATH = Path("trustlab/lab/log/" + folder_name + "/")
        os.mkdir(Logging.LOG_PATH.absolute())

