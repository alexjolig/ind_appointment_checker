#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from datetime import datetime

from request import check_calendar
from dotenv import load_dotenv

from helpers import send_message


def check_it():
    """
    Checks free slots for biometrics and pickup documents
    """
    print(f"Last checked time: {datetime.now().time()}")

    if os.getenv("BIOMETRICS_CHECK_ACTIVE", True).lower() == "true":
        print("Checking 'biometrics' available time slots:")
        bio_date = datetime.strptime(
            os.getenv("DESIRED_DEADLINE_DATE_FOR_BIOMETRICS", datetime(2099, 1, 1)),
            "%d-%m-%Y",
        )
        check_calendar("BIO", bio_date)
    if os.getenv("PICKUP_DOCUMENTS_CHECK_ACTIVE", True).lower() == "true":
        print("Checking 'pickup document' available time slots:")
        doc_date = datetime.strptime(
            os.getenv(
                "DESIRED_DEADLINE_DATE_FOR_PICKUP_DOCUMENTS", datetime(2099, 1, 1)
            ),
            "%d-%m-%Y",
        )
        check_calendar("DOC", doc_date)


if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("DISPLAY"))
    while True:
        retry_count = 5
        try:
            check_it()
            print("=" * 100)
            retry_count = 5
            time_interval = int(
                os.getenv("TIME_INTERVAL_TO_CHECK_FREE_SLOTS_IN_SECONDS", 30)
            )
            time.sleep(time_interval)
        except Exception as ex:
            if retry_count > 0:
                retry_count -= 1
                check_it()
            else:
                send_message(f"SOMETHING IS WRONG. {str(ex)}")
                raise Exception(ex)
