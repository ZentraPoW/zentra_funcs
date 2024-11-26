
import hashlib
import json
import getpass

import web3
import eth_account

import setting

PROVIDER_HOST = 'http://127.0.0.1:8045'

w3 = web3.Web3(web3.Web3.HTTPProvider(PROVIDER_HOST))


function_proposal_sourcecode = open('../funcs/function_proposal.py', 'r').read()

if __name__ == '__main__':
    # committee_init will only be called once and not in global state
    # function_proposal in global state
    # function_vote in global state

    account = setting.account
    nonce = w3.eth.get_transaction_count(account.address)
    print(account.address, nonce)

    # call committee_init
    call = {'p':'zen', 'f': 'committee_init', 'a': []}
    transaction = {
        'from': account.address,
        'to': account.address,
        'value': 0,
        'nonce': w3.eth.get_transaction_count(account.address),
        'data': json.dumps(call).encode('utf8'),
        'gas': 0,
        'maxFeePerGas': 0,
        'maxPriorityFeePerGas': 0,
        'chainId': 1805
    }

    signed = w3.eth.account.sign_transaction(transaction, account.key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print(tx_hash.hex())

    call = {'p': 'zen',
            'f': 'function_proposal',
            'a': ['function_proposal', function_proposal_sourcecode, [], [], []]}
    transaction = {
        'from': account.address,
        'to': account.address,
        'value': 0,
        'nonce': w3.eth.get_transaction_count(account.address),
        'data': json.dumps(call).encode('utf8'),
        'gas': 0,
        'maxFeePerGas': 0,
        'maxPriorityFeePerGas': 0,
        'chainId': 1805
    }

    signed = w3.eth.account.sign_transaction(transaction, account.key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print(tx_hash.hex())


    call = {'p': 'zen',
            'f': "function_vote", 
            'a': ['function_proposal', hashlib.sha256(function_proposal_sourcecode.encode('utf8')).hexdigest()]}
    transaction = {
        'from': account.address,
        'to': account.address,
        'value': 0,
        'nonce': w3.eth.get_transaction_count(account.address),
        'data': json.dumps(call).encode('utf8'),
        'gas': 0,
        'maxFeePerGas': 0,
        'maxPriorityFeePerGas': 0,
        'chainId': 1805
    }

    signed = w3.eth.account.sign_transaction(transaction, account.key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print(tx_hash.hex())
