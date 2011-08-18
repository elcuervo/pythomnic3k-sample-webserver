config = dict \
(
interfaces = ("http", "https"),
request_timeout = 10.0,
thread_count = 10,
sweep_period = 15.0,
log_level = "INFO",
)

# DO NOT TOUCH BELOW THIS LINE

__all__ = [ "get", "copy" ]

get = lambda key, default = None: pmnc.config.get_(config, {}, key, default)
copy = lambda: pmnc.config.copy_(config, {})

# EOF