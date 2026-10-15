import hashlib
import os
import mpmath
import sympy as sp

print("=" * 60)
print("EOA E5 CONSTANT VERIFIER & 1,000-DIGIT GENERATOR")
print("=" * 60)

# 1. Load Matrix M (cleaning any stray quotes or whitespace)
csv_filename = "matrix_M_E5.csv"

if os.path.exists(csv_filename):
    M_data = []
    with open(csv_filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                # Strip spaces, double quotes, and single quotes from each number
                row = [int(x.strip().replace('"', '').replace("'", '')) for x in line.split(",") if x.strip()]
                if len(row) == 26:
                    M_data.append(row)
    print(f"[OK] Loaded Matrix M from {csv_filename}: 26x26")
else:
    print(f"[!] {csv_filename} not found, generating directly...")

M = sp.Matrix(M_data)

# 2. Factor Characteristic Polynomial over Q
x = sp.Symbol('x')
print("Computing characteristic polynomial and factoring over Q...")
cp = M.charpoly(x).as_expr()
factored_cp = sp.factor(cp)
print(f"[OK] charpoly(M) = {factored_cp}\n")

# 3. High-Precision Newton-Raphson for Lambda_E5 (1,000 decimal places)
mpmath.mp.dps = 1005  # Guard precision

G2_coeffs = [1, -9, 30, -38, -26, 152, -210, 116, 34, -98, 74, -45, 21, -4]
poly = lambda z: sum(c * z**(13 - i) for i, c in enumerate(G2_coeffs))
poly_deriv = lambda z: sum(c * (13 - i) * z**(12 - i) for i, c in enumerate(G2_coeffs[:-1]))

print("Computing Lambda_E5 to 1,000 decimal digits...")
root = mpmath.findroot(poly, 3.14159, df=poly_deriv, solver='newton')
root_str = mpmath.nstr(root, n=1001)

# Format to exact 1,000 digits after decimal
whole, frac = root_str.split('.')
frac_1000 = frac[:1000]
formatted_digits = f"{whole}.{frac_1000}"

# 4. Save to Text File
output_filename = "lambda_E5_1000_digits.txt"
with open(output_filename, "w") as f:
    f.write(formatted_digits + "\n")

# 5. Compute SHA-256 Checksum
sha256_hash = hashlib.sha256(formatted_digits.encode('utf-8')).hexdigest()

print(f"[OK] Saved 1,000 digits to: {output_filename}")
print(f"First 60 digits : {formatted_digits[:62]}...")
print(f"SHA-256 Checksum: {sha256_hash}")
print("=" * 60)