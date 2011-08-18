#!/usr/bin/env python
#-*- coding: iso-8859-1 -*-
###############################################################################

__all__ = [ "process_request" ]

###############################################################################

import os; from os import path as os_path

if __name__ == "__main__": # add pythomnic/lib to sys.path
    import os; import sys
    main_module_dir = os.path.dirname(sys.modules["__main__"].__file__) or os.getcwd()
    sys.path.insert(0, os.path.normpath(os.path.join(main_module_dir, "..", "..", "lib")))

import typecheck; from typecheck import by_regex

###############################################################################

valid_url = by_regex("^/(?:(?:[A-Za-z0-9_-]+/)*[A-Za-z0-9_-]+\\.html)?$")

###############################################################################

def process_request(request: dict, response: dict):

    url = request["url"]

    if not valid_url(url):
        raise Exception("invalid URL: {0:s}".format(url))

    if url == "/":
        url = "/index.html"

    filename = os_path.join(__cage_dir__, "html", *(url.split("/")[1:]))

    if os_path.isfile(filename):
        with open(filename, "r") as f:
            response["content"] = f.read()
        response["headers"]["content-type"] = "text/html"
    else:
        response["status_code"] = 404
        response["headers"]["content-type"] = "text/plain"
        response["content"] = "not found"

###############################################################################
# EOF