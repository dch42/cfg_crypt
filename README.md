# cfg_crypt
Module to create, encrypt, and decrypt a small config file. 

If no key exists, it will generate a key.

Likewise, if no config file exists, it will generate and encrypt a config file:

~~~
No key detected...
Generating encryption key...
==> Key generated at ./.cfg.key

Generating config file...
Please enter your login email: test@test.com
Please enter your login password: 

Encrypting config file...
Encryption complete.
==> Encrypted file saved at ./.crypt_cfg
~~~

Decrypted data is returned as a dictionary: `cfg`

Values can be accessed with `cfg['EMAIL']` and `cfg['PW']`
