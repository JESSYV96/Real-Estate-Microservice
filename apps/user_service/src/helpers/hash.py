from passlib.hash import sha256_crypt


def generate_hash(word: str) -> str:
   return sha256_crypt.encrypt(word)

def verify(word_to_check: str, word_hashed: str) -> bool:
   return sha256_crypt.verify(word_to_check, word_hashed)