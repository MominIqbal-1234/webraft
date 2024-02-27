from cryptography.fernet import Fernet


class GenerateKey:
    """
    The GenerateKey class contains a method to generate key
    """
    def generate_key():
        key = str(Fernet.generate_key())
        _key = key.replace("'", "")
        return _key[1:]
