import json
import requests

# # Example input - for real-time usage
text = ["yes",
        "I heard it got some nice features.",
        "yes"]

# # Example input - to annotate conversation, this might take longer,
# about 300 utterances/min for dialogue acts (both), recommended to send max 100 utt/request
# about 10 utterances/min for all, recommended to send max 30 utt/request
_text = ["Hello", "Hello, how are you?", "I am good, how about you", "great!", "Is that a new tv?",
         "yes", "I heard it got some nice features.", "yes"]

value = "\r\n".join(text)  # you can forward only text to server hence joining it with string '\r\n'

link = "http://64.225.94.8:4000"  # This is our server static IP, so we wont change it anywhere soon
# link = "http://api.wiserli.com:4000"  # We also have our own api link, but it takes longer to call over the request,
# hence recommended to use the link with IP address

# Sending request to the dialogue act server
# "mode": "context" --> for context-based prediction < require 3 utterances >
# "mode": "no_context" --> for no-context prediction < any number of utterances >
# "mode": "both" --> for both context and no-context prediction < better minimum 3 utterances >
try:
    results = requests.post(link + '/predict_das', json={"text": value, "mode": "both"})
    print('server response time: ', results.elapsed.total_seconds(), "sec")
    print(json.dumps(results.json()["result"], indent=3, sort_keys=True))
    # for context model you are getting output only for the last utterance in the set of 3 utterances,
    # so use only the last element from the lists in dictionary
except json.decoder.JSONDecodeError:
    print("Input error or the broken link.")

# Sending request to the linguistic features server
# "mode": "politeness" --> how polite are the utterances linguistically >
# "mode": "support" --> how polite are the utterances linguistically >
# "mode": "agreement" --> how polite are the utterances linguistically >
# "mode": "all" --> get all the features in the output >
try:
    results = requests.post(link + '/predict_convo', json={"text": value, "mode": 'all'})
    print('server response time: ', results.elapsed.total_seconds(), "sec")
    print(json.dumps(results.json()["result"], indent=3, sort_keys=True))
except json.decoder.JSONDecodeError:
    print("Input error or the broken link.")
