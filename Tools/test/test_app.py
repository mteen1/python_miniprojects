from sensitive_data import passwd
import hashlib

if hashlib.md5(passwd.encode('utf-8')).hexdigest() == 'e2fe6f800058d3f57fd5f206dfbed056':
    print('pass is correct')
else:
    print('pass is incorrect')