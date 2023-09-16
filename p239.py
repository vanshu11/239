import hashlib
import json
from time import time
chain=[]
def block(proof,previous_hash=None):
	transaction={
	'sender':'Sam',
	'recipient':'max',
	'amount':'5 ETH'
	}
	data={
	'block height':1
 	'block reward':'2.5133355502599526952 Ether(2+0.4508550253068+0.0625)',
	'timestamp':time(),
	'transaction':transaction,
	'gas/fee':0.1,
	'gas limit':'14,974,639'
	'proof':proof,
	'previous_hash':previous_hash,
	}
	chain.append(data)
	print("block information:",data)
	string_obect=json.dumps(data)
	block_string=string_obect.encode()
	raw_hash=hashlib.sha256(block_string)
	hex_hash=raw_hash.hexdigest()
	print("hash code of block:",hex_hash)
block(previous_hash="no previous hash since it is a first block which is geniscs",proof=0000)
	 

