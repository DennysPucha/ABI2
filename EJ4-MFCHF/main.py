import hashlib
import hmac
import time

def hotp(secret, counter):
    return hmac.new(secret.encode(), str(counter).encode(), hashlib.sha1).hexdigest()

def mfchf(password, otp_secret, counter):
    otp = hotp(otp_secret, counter)
    return hashlib.sha512((password + otp).encode()).hexdigest()

hash_val = mfchf("miclave124", "secretoMFA", 1)
print("MFCHF Hash:", hash_val)
