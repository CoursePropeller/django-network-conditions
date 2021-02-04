import time
import numpy as np
from scipy.stats import norm
from django.conf import settings


class LatencyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
     
        if 'DEBUG_ONLY' in settings.NETWORK_CONDITIONS.keys():
            self.debug = settings.NETWORK_CONDITIONS["DEBUG_ONLY"]
        else:
            self.debug = True
        self.latency = settings.NETWORK_CONDITIONS["LATENCY"] 
        self.jitter = settings.NETWORK_CONDITIONS["JITTER"] 
        self.timeout_pct = settings.NETWORK_CONDITIONS["TIMEOUT_PCT"]
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        delay = np.random.normal(self.latency, self.jitter)
        if self.debug:
            threshold = norm.ppf((1 - self.timeout_pct/100), self.latency, self.jitter)
            print("test", delay, threshold)
            if delay < threshold:
                print("delaying")
                time.sleep(delay)
        print("success")
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
