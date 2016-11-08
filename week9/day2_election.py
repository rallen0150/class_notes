import requests
import time

# import pprint # Not needed for time
# pp = pprint.PrettyPrinter(indent=2) # Not needed for time

from data_miner import DataMiner
from messenger import Messenger

# response = requests.get('http://projects.fivethirtyeight.com/2016-election-forecast/updates.json')
# # pp.pprint(response.json())
# response_json = response.json()
# # pp.pprint(response_json.keys())
# latest = response_json['updates'][0]
# latest_id = latest['added']
# diffs = latest['diffs']
#
# base_sms = ""
#
# for candidate in diffs['now-cast']:
#     current = float(candidate['winprob']['current'])
#     previous = float(candidate['winprob']['prev'])
#     diff = round((current - previous) * 100, 2)
#     base_sms += "{}: {}. Diff: {}\n".format(candidate['candidate'], current * 100, diff)
#
#     # print(candidate['candidate'])
#     # print(current * 100)
#     # print(diff)
# print(base_sms)


######## ******SEND TO PHONE****** ########
# from twilio.rest import TwilioRestClient
#
# account_sid = "ACff0caeefc47a12d87e8ebf519d93431d" # Your Account SID from www.twilio.com/console
# auth_token  = "06ebc1380d39b59bf754c4d51397ae0e"  # Your Auth Token from www.twilio.com/console
#
# client = TwilioRestClient(account_sid, auth_token)
#
# message = client.messages.create(body=base_sms,
#     to="+18645618074",    # Replace with your phone number
#     from_="+18645010618") # Replace with your Twilio number
#
# print(message.sid)


### REFACTERED WAY ###
messenger = Messenger()
dm = DataMiner()
while True:
    if dm.is_new_data:
        base_sms = dm.message
        print(base_sms)
        messenger.send(base_sms)
    time.sleep(60)
# dm.get_data() # Used before the 4 print and time lines were added in
