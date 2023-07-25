#!/usr/bin/env python3

import jwt
import sys
import json
import base64

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <access-token>" % sys.argv[0])
        sys.exit(1)
        
    access_token = sys.argv[1]
    payload = jwt.decode(access_token, verify=False)
    print(payload)