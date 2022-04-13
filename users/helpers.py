
import requests
import random
from django.conf import settings


def send_otp_to_phone(Phone_number, name):
    try:
        otp = random.randint(1000, 9999)
        url = f'https://smsapi.24x7sms.com/api_2.0/SendSMS.aspx?APIKEY=t7zGAOkNY5D&MobileNo={Phone_number}&SenderID=IMINDS&Message=Dear%20{name}%20{otp}%20OTP%20to%20verify%20your%20mobile%20number%20with%20Imageminds.%20Welcome%20to%20Creative%20Exploration&ServiceName=TEMPLATE_BASED&DLTTemplateID=1707163643448129125'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(response.content)
                return otp

            else:
                print(" not otp sent")
                return None
        except Exception as e:
            return None
    except Exception as e:
        return None
