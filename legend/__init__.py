import os

LEGEND_HOME_NAME = ".legend"

LEGEND_HOME = os.environ.get(
    "LEGEND_HOME", os.path.join(
        os.path.expanduser("~"), LEGEND_HOME_NAME)
)

GRAFONNET_REPO_URL = "https://github.com/grofers/grafonnet-lib"
GRAFONNET_REPO_NAME = "grafonnet-lib"