# Number Convert

Python script that checks a password against the
[Have I Been Pwned](https://haveibeenpwned.com/) database, and reports back on
whether or not it has been listed.

This method may be preferable to putting your password directly into the site
because this script only sends the first 5 characters of the SHA1 hash of your
password over the internet instead of your whole password or hash.

For more info on the API docs, see <https://haveibeenpwned.com/API/v2>

## Running:
* `python is_it_pwned.py` - Prompts you for a single password (echo off).
* `python is_it_pwned.py < file` – reads passwords from a file.
* `cmd | is_it_pwned pwned.py` – reads passwords written to standard output by
  another command.
* `python is_it_pwned.py <password1> [<password2> ...]` – checks passwords given
  as command line arguments
    * **Beware** the password may be saved in shell history and that other users
      on the system ma be able to observe the command line.
