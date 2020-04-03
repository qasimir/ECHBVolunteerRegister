import hashlib
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class SecurityManager:

    password_hash = ""
    salt = None
    ran_hash = 0x1c7545fa4cf5a38dc379a9a196de0cfce66a99eff21928d4c9d6671ec45463b8

    @staticmethod
    def hash_string(string):
        hashed_input = hashlib.sha3_256(string.encode()).hexdigest()
        return str(hex(int(hashed_input, 16) ^ SecurityManager.ran_hash))[2:]

    @staticmethod
    def get_key_from_password():
        if SecurityManager.password_hash is None:
            return None

        password = SecurityManager.password_hash.encode()
        print("the password hash is: " + SecurityManager.password_hash)
        print("the salt is: " + SecurityManager.salt)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=str.encode(SecurityManager.salt),
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        print("Key for decrypting: " + key.decode("utf-8"))
        return key

    @staticmethod
    def load_config(file_path):
        # config file has the format of the salt on the first line, and the password hash on the second
        if not os.path.exists(file_path):
            print("making the config file")
            # TODO add logging here
            SecurityManager.salt = os.urandom(16).hex()
            config_file = open(file_path, 'w')
            config_file.write(SecurityManager.salt + "\n")
            # this password hash is the first "password"
            SecurityManager.password_hash = "dc7338b0b81ddc8d18d5ca1783b624df96338ec2e9a784b38ba522c86da9c73c"
            config_file.write(SecurityManager.password_hash)
        else:
            config_file = open(file_path, 'r+')
            lines = config_file.readlines()
            SecurityManager.salt = lines[0]
            SecurityManager.password_hash = lines[1]
        config_file.close()



