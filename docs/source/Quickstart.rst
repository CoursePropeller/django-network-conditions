*****
Quickstart
*****

pip install django_network_conditions

NETWORK_CONDITIONS = {
        'DEBUG_ONLY': True, # default True. means only runs in DEBUG mode.
        'LATENCY': 20, # millis delay before start sending response
        'KB_PER_SECOND': 1024, # speed to send the response,
        'JITTER': 10, # millis standard deviation in latency. 0 = no jitter otherwise gaussian,
        'TIMEOUT_PCT': 5, #the percentage of requests that time out
        'PRINT_LOGS': False # if True, it shows the status.
    }