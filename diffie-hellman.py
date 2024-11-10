import secrets
def generate_private_key(p):
    return secrets.randbelow(p)

def compute_public_key(g, private_key, p):
    return pow(g, private_key, p)

def compute_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)

p = 23  # Prime number
g = 5   # Primitive root modulo p

alice_private_key = generate_private_key(p)
alice_public_key = compute_public_key(g, alice_private_key, p)
print(f"Alice's private key: {alice_private_key}")
print(f"Alice's public key: {alice_public_key}")
bob_private_key = generate_private_key(p)
bob_public_key = compute_public_key(g, bob_private_key, p)
print(f"Bob's private key: {bob_private_key}")
print(f"Bob's public key: {bob_public_key}")
alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, p)
print(f"Alice's shared secret: {alice_shared_secret}")
bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, p)
print(f"Bob's shared secret: {bob_shared_secret}")
assert alice_shared_secret == bob_shared_secret
print("Shared secret successfully established!")