from web3 import Web3
from web3.middleware import geth_poa_middleware
from contact_info import abi, contract_adress

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=contract_adress, abi=abi)

print(contract_adress)
print(w3.eth.get_balance("0x223487111c8074e851f6AA46D98f13C301940c02"))
print(w3.eth.get_balance("0x0b21fDC853ee5e6A795b5d194359f84229c390F1"))
print(w3.eth.get_balance("0xE97355040b33efac041aa24d49a5e5517bbee750"))
print(w3.eth.get_balance("0x0e8a805d9a497374B34893657eeaBa15eD2ADEB9"))
print(w3.eth.get_balance("0x64336aBA697b3d9d2ffc0Fee8C9BbB9088E035Cb"))