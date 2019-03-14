# Number Convert

Python script that checks a password against the
[Have I Been Pwned](https://haveibeenpwned.com/) database, and reports back on
whether or not it has been listed.

This method may be preferable to putting your password directly into the site
because this script only sends the first 5 characters of the SHA1 hash of your
password over the internet instead of your whole password or hash.

For more info on the API docs, see <https://haveibeenpwned.com/API/v2>

## Running:

```
$ python is_it_pwned.py password
password has been pwned 3645804 times.
$ python is_it_pwned.py Password123
Password123 has been pwned 21961 times.
```
