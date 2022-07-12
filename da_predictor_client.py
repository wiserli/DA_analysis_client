import json
import requests

# Example input - to annotate a conversation
_value = "Hello\r\nHello, how are you?\r\nI am good, how about you\r\ngreat!\r\nis that a new tv?\r\nyes\r\nI heard " \
        "it got some nice features.\r\nyes "

# OR

# Example input - for real-time detection
text = ["yes",
        "I heard it got some nice features.",
        "yes"]
value = "\r\n".join(text)
# This will produce something like below:
# value = "yes\r\nI heard it got some nice features.\r\nyes"
# useful if you are reading a text file line by line

# Sending request to the resting server
try:
    _link = "http://0.0.0.0:4000"      # Local network on computer
    link = "http://tcp.jprq.io:38329"  # Tunnel websocket via jprq
    # "mode": "context" --> for context-based prediction < require 3 utterances >
    # "mode": "no_context" --> for no-context prediction < any number of utterances >
    # "mode": "both" --> for both context and no-context prediction < better minimum 3 utterances >
    results = requests.post(link + '/predict_das', json={"text": value, "mode": "context"})
    print('server response time: ', results.elapsed.total_seconds(), "sec")
    print(json.dumps(results.json()["result"], indent=3, sort_keys=True))
except json.decoder.JSONDecodeError:
    print("Input error or the broken link.")
