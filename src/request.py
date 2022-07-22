#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime

import requests
from dotenv import load_dotenv

from helpers import convert_2_date, is_earlier_than, send_message

load_dotenv()


def check_calendar(check_type: str, desired_date: datetime):
    """
    Checks free slot in IND calendar (before a specified date) for a certain type of appointment
    :param Str check_type: appointment type to check (BIO, DOC)
    :param desired_date: The deadline date to find a free slot in the calendar
    :return:
    """
    url = f"https://oap.ind.nl/oap/api/desks/{os.getenv('DESK', 'AM')}/slots"
    payload = {
        "productKey": check_type,
        "persons": int(os.getenv("NUMBER_OF_PERSONS", 1)),
    }
    response = requests.get(url=url, params=payload)
    response = response.text[6:]
    response = json.loads(response)
    if not response["data"]:
        return
    first_available_date = response["data"][0]["date"]
    first_available_date = convert_2_date(first_available_date)
    if is_earlier_than(first_available_date, desired_date):
        print("*" * 200)
        print(
            f"One slot is empty for ###{first_available_date.strftime('%Y-%m-%d')}###"
        )
        if os.getenv("WHATSAPP_MESSAGE_ACTIVE", True).lower() == "true":
            send_message(
                f"{check_type} time slot available on {first_available_date.strftime('%Y-%m-%d')}"
            )
    else:
        print(f"Nothing yet for {check_type}, Sorry!")
