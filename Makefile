#---------------------------------------------------------------------
# Install deps & add exec permissions
#---------------------------------------------------------------------

init:
	pip3 install -r requirements.txt
	chmod +x ./cfg_crypt.py
