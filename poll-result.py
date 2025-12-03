#!/usr/bin/env python3

# ==========================
#  Paillier Key Parameters
# ==========================
# Fill these in:
n = 178861        # modulus
g = 178862        # generator (often g = n + 1)
lam = 89006       # λ = lcm(p−1, q−1)
mu = 131249       # μ = (L(g^λ mod n²))^{-1} mod n

# ==========================
#  Helper functions
# ==========================

def L(u, n):
    """Paillier L-function: L(u) = (u - 1) // n"""
    return (u - 1) // n

def modinv(a, m):
    """Modular inverse using Extended Euclidean Algorithm"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse exists")
    return x % m

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)

# ==========================
#  Paillier Decryption
# ==========================

def paillier_decrypt(c, n, lam, mu):
    """
    Standard Paillier decryption:
    m = L(c^λ mod n²) * μ mod n
    """
    n2 = n * n
    u = pow(c, lam, n2)
    return (L(u, n) * mu) % n

# ==========================
#  Main program
# ==========================

def main():
    #some sanity check on the code
    if None in [n, g, lam, mu]:
        raise ValueError("Please fill in n, g, lam, mu first!")

    n2 = n * n
    total_cipher = 1
    print("Here's a calculation of the poll result of the ski trip destination.")
    # Read ciphertext values from input.txt.
    #Interpret each line as a decimal value
    print("Loading the votes...")
    with open("input.txt", "r") as f:
        print("- Votes Loaded.")
        print("Calculating the ciphertexts...")
        for line in f:
            line = line.strip()
            if not line:
                continue
            c = int(line)
            #combining the ciphertext into one
            #without decrypting individual ciphers 
            total_cipher = (total_cipher * c) % n2

        print("- Ciphertext calculated.")
        print("The collective ciphertext is:", total_cipher,".")
    # Decrypt all votes at once
    message = paillier_decrypt(total_cipher, n, lam, mu)
    print("Decrypted message:", message)

    # Tidy up the look of the output of the message
    if message>100000:
        message = message - 178861
    print("With negative value in mod", n ,", this result is equal to", message)
    print(".")
    print(".")
    print(".")

    if message>0:
        print("Davos is the most polular choice.")
    elif message<0:
        print("Arosa is the most popular choice.")
    else: 
        print("It appears they are equally favourable. :-)")

if __name__ == "__main__":
    main()
