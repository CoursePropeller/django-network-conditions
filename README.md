==============
django-network-conditions
==============

A Django package to simulate different network conditions during local development.

# Set Up

Setting up django-network-conditions is easy. After it is installed in your environemnt and on your path, simply add the middleware class to your MIDDLEWARE_CLASSES list::

    MIDDLEWARE_CLASSES = (
        ...
        'django_network_conditions.middleware.LatencyMiddleware',
        ...
    )

django_network_conditions optionally accepts a settings variable called NETWORK_CONDITIONS. Currently,
NETWORK_CONDITIONS is a dictionary whose keys are 'DEBUG_ONLY', 'LATENCY', 'KB_PER_SECOND', 'JITTER', 'TIMEOUT_PCT', 'PRINT_LOGS'.

For example::

    NETWORK_CONDITIONS = {
        'DEBUG_ONLY': True, # default True. means only runs in DEBUG mode.
        'LATENCY': 20, # millis delay before start sending response
        'KB_PER_SECOND': 1024, # speed to send the response,
        'JITTER': 10, # millis standard deviation in latency. 0 = no jitter otherwise gaussian,
        'TIMEOUT_PCT': 5, #the percentage of requests that time out
        'PRINT_LOGS': False # if True, it shows the status.
    }
