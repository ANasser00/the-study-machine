# Session: Midterm — Ch2, Ch3, Ch5, Ch6, Ch9, Ch11

**Subject:** ITCS-441-Crypto
**Date:** 2026-04-27
**Source material:**
- [x] Past exams: ITCS411 - Midterm Exams.pdf (3 past midterms)
- [x] Slides: Ch2, Ch3, Ch5, Ch11
- [x] PDFs: Ch6, Ch9

**Status:**
- [x] Phase 1 — Understanding
- [x] Phase 2 — Exam Gold
- [ ] Complete (revisit for final)

**Scope:**
- Chapter 2 — Classical Encryption (symmetric model, attack types, Caesar, steganography)
- Chapter 3 — DES (Feistel, block ciphers, DES structure, F-function, avalanche)
- Chapter 5 — AES (Rijndael, rounds, 4 stages, last round, key schedule)
- Chapter 6 — Modes of Operation (ECB, CBC, CFB, OFB, CTR, Double/Triple DES)
- Chapter 9 — Public Key / RSA (Diffie-Hellman, RSA setup, encrypt/decrypt)
- Chapter 11 — Hash Functions (requirements, attacks, SHA, birthday paradox)

---

## Phase 2 — Exam Gold

### Key Concepts

**Ch2 — Classical Encryption**
- Symmetric cipher model: Y=E(K,X), X=D(K,Y)
- Attack types (least→most info): Ciphertext-only → Known-plaintext → Chosen-plaintext → Chosen-ciphertext
- Passive attacks: read only, hard to detect. Countermeasure: **encryption**
- Active attacks: modify/replay/inject. Countermeasure: detection
- Steganography: hiding the **existence** of the message (not encrypting it)
- Unconditional security: cannot break even with infinite compute → only one-time pad
- Computational security: secure given current compute power → everything else

**Ch3 — DES / Feistel**
- Feistel structure: basis of symmetric block ciphers. Confusion (S-boxes) + Diffusion (P-boxes)
- DES: 64-bit block, 56-bit effective key, 16 rounds
- DES round equations: L_i = R_{i-1} and R_i = L_{i-1} ⊕ F(R_{i-1}, K_i)
- DES F-function (4 steps): Expansion E (32→48) → XOR with subkey K_i (48→48) → 8 S-boxes (48→32) → Permutation P (32→32)
- DES S-boxes: **8 total**, each maps 6-bit → 4-bit
- Avalanche effect: 1-bit change → ~half of output bits change
- DES broken: 1999 in 22 hours

**Ch5 — AES**
- Algorithm: **Rijndael**. NOT Feistel — iterative S-P structure
- 128-bit block. Keys/rounds: 128→10, 192→12, 256→14
- Round 0: AddRoundKey only
- Rounds 1 to N-1: SubBytes → ShiftRows → MixColumns → AddRoundKey
- Last round: SubBytes → ShiftRows → AddRoundKey (**NO MixColumns**)
- AES S-boxes: **16** (one per byte in 4×4 state). DES S-boxes: 8.

| Stage | Uses Key? | In Last Round? | Avalanche? |
|---|---|---|---|
| SubBytes | No | Yes | No |
| ShiftRows | No | Yes | Yes |
| MixColumns | No | **No** | Yes |
| AddRoundKey | **Yes** | Yes | No |

- Memory: MixColumns is the ONLY stage NOT in the last round. AddRoundKey is the ONLY stage using the key.

**Ch6 — Modes of Operation**
- Double-DES broken by **meet-in-the-middle** attack. Cost = O(2^56) not O(2^112)
  - How: encrypt P with all K1 → table. Decrypt C with all K2 → find match at X.
- 3DES-2keys: C = E_K1(D_K2(E_K1(P))). K1=K2 → single DES (backward compatible)
- ECB: same plaintext → same ciphertext. Patterns visible. NOT suitable for long messages.
- CBC: each block depends on all previous blocks. Best for long messages.
- CTR: parallelizable. Same plaintext block → different ciphertext (different counter each time).
- OFB: no error propagation. Good for noisy channels.

**Ch9 — RSA / Public Key**
- Invented: Diffie & Hellman, Stanford, 1976
- RSA: based on difficulty of **factoring large numbers**
- RSA setup: n=pq, ø(n)=(p-1)(q-1), choose e (gcd=1), find d (ed≡1 mod ø(n))
- Encrypt: C = M^e mod n. Decrypt: M = C^d mod n
- Common e: 65537

**Ch11 — Hash Functions**
- h = H(M). Variable input → fixed output. One-way.
- Birthday attack exploits collision probability → cost = O(2^{m/2}) not O(2^m)
- SHA-1: 160 bits, broken 2005
- Uses: digital signatures, password storage, MAC, intrusion detection

**CIA Properties**
- Confidentiality: unauthorized **disclosure**
- Integrity: unauthorized **modification**
- Availability: **denial** of service

**Playfair Cipher**
- Build 5×5 square: write keyword (no repeats), fill rest A→Z skipping used letters. I and J share one cell.
- Prepare plaintext: split into pairs. Same letters in pair → insert X between. Odd length → add X at end. Replace J with I.
- Encrypt rules: Same row → shift right (wrap). Same column → shift down (wrap). Rectangle → same row, other letter's column.

---

### Active Recall Questions

| # | Question | Difficulty | Last Reviewed | Next Review |
|---|----------|------------|---------------|-------------|
| 1 | What are the 4 AES stages? Which is NOT in the last round? Which uses the key? | 🔴 Hard | 2026-04-27 | 2026-04-28 |
| 2 | Explain meet-in-the-middle attack on Double-DES. Why does it reduce security to 56 bits? | 🔴 Hard | 2026-04-27 | 2026-04-28 |
| 3 | Build the Playfair square for keyword MONARCHY and encrypt HELP. | 🔴 Hard | 2026-04-27 | 2026-04-28 |
| 4 | What are the 4 steps of the DES F-function? What are the bit counts at each step? | 🟡 Medium | 2026-04-27 | 2026-04-30 |
| 5 | DES S-boxes vs AES S-boxes — how many each? | 🟢 Easy | 2026-04-27 | 2026-04-30 |
| 6 | What is steganography? How is it different from cryptography? | 🟢 Easy | 2026-04-27 | 2026-04-30 |
| 7 | Attack types from least to most information — list them in order. | 🟡 Medium | 2026-04-27 | 2026-04-30 |
| 8 | What is the countermeasure against passive attacks? Against active attacks? | 🟢 Easy | 2026-04-27 | 2026-04-30 |
| 9 | AES key sizes and their corresponding round counts. | 🟡 Medium | 2026-04-27 | 2026-04-30 |
| 10 | CIA — what does each property protect against? | 🟢 Easy | 2026-04-27 | 2026-04-30 |
| 11 | What makes the one-time pad unconditionally secure? What is its weakness? | 🟡 Medium | 2026-04-27 | 2026-04-30 |
| 12 | ECB vs CBC — what is the key difference and when is each used? | 🟡 Medium | 2026-04-27 | 2026-04-30 |

<details>
<summary>Answers</summary>

**Q1:** SubBytes, ShiftRows, MixColumns, AddRoundKey. MixColumns is NOT in the last round. AddRoundKey is the only one that uses the key.

**Q2:** Attacker has plaintext P and ciphertext C. Encrypts P with all 2^56 values of K1 → stores in table. Decrypts C with all 2^56 values of K2 → finds match at intermediate value X. Cost = 2^56 + 2^56, not 2^112. That's why Double-DES provides no meaningful security improvement over single DES.

**Q3:** Square: M O N A R / C H Y B D / E F G I K / L P Q S T / U V W X Z. HELP → HE LP. HE=rectangle→CF. LP=same row→PQ. Answer: CFPQ.

**Q4:** Expansion E (32→48) → XOR with subkey K_i (48→48) → 8 S-boxes (48→32) → Permutation P (32→32).

**Q5:** DES = 8 S-boxes. AES = 16 S-boxes.

**Q6:** Steganography = hiding the existence of the message (e.g., inside an image). Cryptography = making the message unreadable. Steganography hides that there IS a message; cryptography just hides the content.

**Q7:** Ciphertext-only → Known-plaintext → Chosen-plaintext → Chosen-ciphertext.

**Q8:** Passive attacks → encryption. Active attacks → detection (firewalls, integrity checks).

**Q9:** 128 bits → 10 rounds. 192 bits → 12 rounds. 256 bits → 14 rounds.

**Q10:** Confidentiality = unauthorized disclosure. Integrity = unauthorized modification. Availability = denial of service.

**Q11:** Key is as long as message, truly random, used only once → mathematically unbreakable. Weakness: key must never be reused and must be securely distributed (key is as long as the message).

**Q12:** ECB = each block encrypted independently, same plaintext → same ciphertext, patterns visible. CBC = each block XORed with previous ciphertext before encrypting, hides patterns. Use CBC for long messages.

</details>

---

### Weak Spots

- **AES table** — kept swapping ShiftRows and MixColumns on the "last round" column. Drill: MixColumns is the ONLY one NOT in the last round.
- **AddRoundKey name** — kept saying "MixRoundKey." It's AddRoundKey.
- **Avalanche effect name** — blanked on the term under pressure. It's the avalanche effect.
- **Playfair keyword letters** — forgot that I is in SECURITY when building the square. Always go letter by letter through the keyword.
- **DES F-function S-boxes step** — blanked on step 3. Order: Expansion → XOR → S-boxes → Permutation.
- **192 bits = 12 rounds** — kept guessing 16. 128→10, 192→12, 256→14.

---

## Session Notes

- Exam was April 27, 2026. Midterm covering Ch2, Ch3, Ch5, Ch6, Ch9, Ch11.
- Past exam patterns: heavy on Ch3 (DES), Ch5 (AES), Ch6 (modes). Ch9 and Ch11 low probability but in scope.
- Playfair cipher appears on every single past exam as a written question.
- AES 4-stage table appears on every exam.
- Meet-in-the-middle appears on every exam (both MCQ and written).
- Passive vs active + CIA appears on every exam.
- Session was exam-day cramming — revisit for final with deeper understanding.
