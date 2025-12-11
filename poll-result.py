#!/usr/bin/env python3

# ==========================
#  Paillier Key Parameters
# ==========================
# Fill these in:
n = 12247583461        # modulus
g = 12247583462        # generator (often g = n + 1)
lam = 6123681062       # λ = lcm(p−1, q−1)
mu = 11929797136       # μ = (L(g^λ mod n²))^{-1} mod n

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

def sortingFunc(e):
    return e[1]

# ==========================
#  Main program
# ==========================

def main():
    #some sanity check on the code
    if None in [n, g, lam, mu]:
        raise ValueError("Please fill in n, g, lam, mu first!")

    n2 = n * n
    total_cipher = 1
    print("Here's a calculation of the poll result of the most popular group project.")
    # Read ciphertext values from input.txt.
    #Interpret each line as a decimal value
    print("Loading the votes...")
    # DAVOS = 1
    # AROSA = -1
    # Hence if the result is negative, it means AROSA is prefered, and if positive, DAVOS.
    # We collect all the ciphertexts in a input.txt file.
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

    g3 = message % 100
    g4 = (message//100) % 100
    g5 = (message//10000) % 100
    g6 = (message//1000000) % 100
    g10 = (message//100000000) % 100

    resultlist = [
        ("Group 3", g3),
        ("Group 4", g4),
        ("Group 5", g5),
        ("Group 6", g6),
        #("Group 10", g10),
    ]

    resultlist.sort(reverse=True, key=sortingFunc)

    for item in resultlist:
        print(item[0], "has received", item[1],"votes.")

    result_group = ""
    for i in range (1,3):
        if resultlist[i][1] > resultlist[i+1][1]:
            result_group = result_group + " and "+ resultlist[i][0]
            break
        else:
            result_group = result_group + "," + resultlist[i][0]

    print(".")
    print(".")
    print(".")
    print("The most popular groups are", resultlist[0][0],result_group)


if __name__ == "__main__":
    main()
