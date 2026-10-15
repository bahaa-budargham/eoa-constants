# The Budargham Constant $\lambda_{E5}$: Minimal Polynomial, Incidence Matrix M, and 1,000-Digit Expansion

**Author:** Bahaa BuDargham  
**Organization:** Neurolabs R&D, Montreal, Canada  
**ORCID:** [0009-0005-2955-3703](https://orcid.org/0009-0005-2955-3703)  
**License:** Creative Commons Attribution 4.0 International (CC-BY 4.0)

---

## 1. Mathematical Definition

The mathematical constant **$\lambda_{E5}$** (the EOA Limiting Ratio under encoding E5) is defined as the unique strictly dominant real root (Perron root) of the monic, irreducible degree-13 integer polynomial:

$$G_2(x) = x^{13} - 9x^{12} + 30x^{11} - 38x^{10} - 26x^9 + 152x^8 - 210x^7 + 116x^6 + 34x^5 - 98x^4 + 74x^3 - 45x^2 + 21x - 4$$

* **Algebraic Degree:** 13 (Perron number)
* **Galois Group:** Full symmetric group $S_{13}$ of order $13! = 6,227,020,800$ (certified in SageMath)
* **Dominant Root:** $\lambda_{E5} \approx 3.1415932235776478077659351649002756071087111553047325144046...$
* **Proximity to $\pi$:** $|\lambda_{E5} - \pi| \approx 5.70 \times 10^{-7}$ (treated as a numerical coincidence)

---

## 2. The Substitution Matrix M & The 13–13 Spectral Split

$\lambda_{E5}$ arises as the spectral radius of the $26 \times 26$ non-negative integer incidence matrix $M$ provided in `matrix_M_E5.csv`. 

Over $\mathbb{Q}$, the characteristic polynomial factors with an exact equal-degree split ($13 + 13 = 26$):

$$\text{charpoly}(M) = (x - 2) \cdot x^3 \cdot (x - 1)^9 \cdot G_2(x)$$

* **Integer Eigenvalues (Degree 13 total):** $2$ (multiplicity 1), $0$ (multiplicity 3), $1$ (multiplicity 9).
* **Algebraic Factor (Degree 13):** $G_2(x)$ containing the Perron root $\lambda_{E5}$.

---

## 3. Staged Disclosure & IP Scope

The matrix $M$, polynomial $G_2(x)$, and 1,000-digit expansion are fully public and self-contained for mathematical analysis. The underlying phonetic letter-name strings and recursive $\beta$-operator that generated $M$ are withheld under the EOA staged disclosure policy. Researchers seeking access to the generator or collaborative extensions may contact: `bdarghamneurolabs@gmail.com`.

---

## 4. Verification

Run `python verify_e5.py` to factor $M$ and recompute all 1,000 decimal digits in seconds.
