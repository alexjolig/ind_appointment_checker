#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime

from pywhatkit import sendwhatmsg
from dotenv import load_dotenv

load_dotenv()


def convert_2_date(date_str: str):
    _date = datetime.strptime(date_str, "%Y-%m-%d")
    return _date


def is_earlier_than(_date: datetime, desired_date: datetime):
    """
    Determines if _date is earlier than the desired_date
    :param _date:
    :param desired_date:
    :return: True if _date < desired_date
    """

    return _date < desired_date


def send_message(message: str):
    phone_number = os.getenv("PHONE_NUMBER_FOR_WHATSAPP_MESSAGE")
    if phone_number is not None:
        sendwhatmsg(
            phone_number,
            message,
            datetime.now().hour,
            datetime.now().minute + 1,
            9,
            True,
            5,
        )
