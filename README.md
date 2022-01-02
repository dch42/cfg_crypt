# cfg_crypt
Module to create, encrypt, and decrypt a small config file for email/pw combos. 


## Usage
Can be used as a stand-alone script, or imported as a module to larger scripts for more versatility: 
~~~
import cfg_crypt as cc
~~~

### Functions
`cc.gen_key()`, generates a fernet encryption key:
~~~
No key detected...
Generating encryption key...
==> Key generated at ./.cfg.key
~~~

`cc.gen_cfg()`, stores email + pw info in a string in memory:
~~~
Generating config file...
Please enter your login email: test@test.com
Please enter your login password: 
~~~

`cc.encrypt_cfg(cfg, key)`, encrypts cfg string using fernet key and writes encrypted file to disk:
~~~
Encrypting config file...
Encryption complete.
==> Encrypted file saved at ./.crypt_cfg
~~~


Decrypted data is returned as a dictionary: `cfg`

Values can be accessed with `cfg['EMAIL']` and `cfg['PW']`
