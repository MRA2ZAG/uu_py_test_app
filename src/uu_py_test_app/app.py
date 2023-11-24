"""
uu_py_test_app.app
"""
from datetime import datetime
import logging
import sys
import argparse

log = logging.getLogger("App")


def mock_function() :
    """
    mock_function
    """
    return None

def _main(*args) :
    parser = argparse.ArgumentParser(prog="Test")
    parser.add_argument("-f", "--fail", action="store_true")
    app_args,extra_args = parser.parse_known_args(args)
    try :
        print(f"INIT test app (start ts: {datetime.utcnow().isoformat()}) - args: {args} --> {app_args} // {extra_args}")
        if app_args.fail :
            raise Exception("Error running app!")
        return 0
    except Exception :
        log.exception("Error running the App")
        return 1
        

if __name__ == "__main__" :
    _main(*sys.argv)
    