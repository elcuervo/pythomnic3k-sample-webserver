config = dict \
(
protocol = "http",
listener_address = ("0.0.0.0", 8080),
max_connections = 100,
ssl_key_cert_file = None,
ssl_ca_cert_file = None,
response_encoding = "utf-8",
original_ip_header_fields = (),
allowed_methods = ("GET", ),
keep_alive_support = True,
keep_alive_idle_timeout = 120.0,
keep_alive_max_requests = 10,
)

# DO NOT TOUCH BELOW THIS LINE

__all__ = [ "get", "copy" ]

get = lambda key, default = None: pmnc.config.get_(config, {}, key, default)
copy = lambda: pmnc.config.copy_(config, {})

# EOF
