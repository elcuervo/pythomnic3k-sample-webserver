config = dict \
(
protocol = "http",
listener_address = ("0.0.0.0", 443),
max_connections = 100,
ssl_key_cert_file = "sample_web_server_key_cert.pem",
ssl_ca_cert_file = "sample_web_server_ca_cert.pem",
response_encoding = "utf-8",
original_ip_header_fields = (),
allowed_methods = ("GET", ),
keep_alive_support = True,
keep_alive_idle_timeout = 120.0,
keep_alive_max_requests = 10,
)

# this config file is patched to return SSL keys locations from the cage directory,
# no matter what it is, this is because I don't know where the sample is extracted

__all__ = [ "get", "copy" ]

import os; from os import path as os_path

def get(key, default = None):
    value = pmnc.config.get_(config, {}, key, default)
    if key.endswith("_cert_file"):
        value = os_path.join(__cage_dir__, "ssl_keys", value)
    return value

def copy():
    return { k: k.endswith("_cert_file") and os_path.join(__cage_dir__, "ssl_keys", v) or v
             for k, v in pmnc.config.copy_(config, {}).items() }

# EOF