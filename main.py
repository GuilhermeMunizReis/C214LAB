import sys

sys.path.append("view")

from view.app import *

if __name__ == "__main__":
    app = App()
    app.start()