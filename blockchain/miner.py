import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = 0
    
    last_hash = hash_proof(last_proof)
    current_hash = hash_proof(proof)

    while last_hash[-6:] != current_hash[:6]:
        proof += 1
        current_hash = hash_proof(proof)

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    print('last_hash: ' + last_hash, last_hash[-6:])
    print('current_hash: ' + current_hash, current_hash[:6])
    return proof

def hash_proof(proof):
    encoded_proof = str(proof).encode("utf-8")
    return hashlib.sha256(encoded_proof).hexdigest()


# def valid_proof(last_hash, proof):
#     """
#     Validates the Proof:  Multi-ouroborus:  Do the last six characters of
#     the hash of the last proof match the first six characters of the hash
#     of the new proof?

#     IE:  last_hash: ...AE9123456, new hash 123456E88...
#     """

#     # TODO: Your code here!
#     pass


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted

    def mine_coins():
        while True:
        # Get the last proof from the server
            r = requests.get(url=node + "/last_proof")
            print('response', r.content)
            try:
                data = r.json()
            except ValueError:
                print("Error: Non-json response")
                print("Response returned", r)
                return None
                # break

            new_proof = proof_of_work(data.get('proof'))

            post_data = {"proof": new_proof,
                        "id": id}

            r = requests.post(url=node + "/mine", json=post_data)
            try:
                data = r.json()
            except ValueError:
                print("Error: Non-json response")
                print("Response returned", r)
                return None
                # break

            if data.get('message') == 'New Block Forged':
                coins_mined += 1
                print("Total coins mined: " + str(coins_mined))
            else:
                print(data.get('message'))

    while mine_coins() is None:
        mine_coins()


    