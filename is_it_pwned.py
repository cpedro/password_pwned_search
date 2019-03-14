#!/usr/bin/env python3
#######################
# File: is_it_pwned.py
# Description: Checks a password against the Have I Been Pwned database, and
#   reports back on whether or not it has been listed.  For more info on the
#   API docs, see https://haveibeenpwned.com/API/v2
#
# Author: E. Chris Pedro
# Version: 2019-03-14
#######################
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org>
#######################

import sys
import getpass
import hashlib
import requests

# Change if API endpoint changes.
api_url = 'https://api.pwnedpasswords.com/range/'

def hash_password(passwd):
    sha1 = hashlib.sha1()
    sha1.update(passwd.encode('utf-8'))
    return sha1.hexdigest().upper()

def lookup_passwd(passwd):
    sha1 = hash_password(passwd)
    head = sha1[:5]
    tail = sha1[5:]
    
    req = requests.get(api_url + format(head))
    if req.status_code == 200:
        for line in req.text.split('\r\n'):
            val,count = line.split(':')
            if (val == tail):
                return count
    
    return 0

if __name__ == '__main__':
    try:
        passwd = sys.argv[1]
    except IndexError:
        passwd = getpass.getpass("Password to check: ")
    
    count = lookup_passwd(passwd)
    if (count):
        print ("That password has been pwned " + count + " times.")
    else:
        print ("That password has not been pwned.")

exit()
