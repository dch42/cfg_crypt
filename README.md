# cfg_crypt
Module to create, encrypt, and decrypt a small config file for email/pw combos.

Mitigates allowing unencrypted sensitive data to live on the HDD, as even environment variables are trivially accessed on a comprimised device. Keys and encrypted config files are stored in hidden directories in the user's home directory, named according to the script that called the functions.

~~~
/Users/user/.cfg_crypt/
├── .cfg_crypt.key
└── .cfg_crypt_cfg
~~~

⚠️ *Although data is stored outside of project directories, the risk of keys being pushed or otherwise accessed is still nonzero and caution should be taken.*  

## Usage
Can be used as a stand-alone script, or imported as a module to larger scripts for more versatility: 
~~~
import cfg_crypt as cc
~~~

For now, scripts importing as a module should declare their name somehow, e.g.:
~~~
import os
script_name = os.path.splitext(os.path.basename(__file__))[0]
~~~

### Functions
`cc.gen_key()`, generates a fernet encryption key:
~~~
Generating encryption key...
==> Key generated at '/Users/user/.script_name/.script_name.key'
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
==> Encrypted file saved at '/Users/user/.script_name/.script_name_cfg'
~~~

`cc.read_key()`, reads encryption key from disk

`cc.decrypt_cfg()`, decrypts encrypted cfg data and returns as a dictionary

Values can be accessed with `cc.cfg['EMAIL']` and `cc.cfg['PW']`
