from passlib.exc import MalformedHashError, InvalidHashError
from passlib.hash import pbkdf2_sha256


def hash_password(password):
    # Hash the password using PBKDF2
    return pbkdf2_sha256.hash(password)


def verify_password(username, password, hashed_password):
    match_found = False
    try:
        match_found = pbkdf2_sha256.verify(password, hashed_password)
    except (MalformedHashError, InvalidHashError) as e:
        print(f"Malformed / Invalid Hash Error when verifying password for {username}")
    except ValueError as e:
        print(f"Unexpected error when validating password for {username}")
    return match_found
