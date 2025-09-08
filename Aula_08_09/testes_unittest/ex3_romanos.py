ROM_MAP = [
    (1000, "M"),
    (900,  "CM"),
    (500,  "D"),
    (400,  "CD"),
    (100,  "C"),
    (90,   "XC"),
    (50,   "L"),
    (40,   "XL"),
    (10,   "X"),
    (9,    "IX"),
    (5,    "V"),
    (4,    "IV"),
    (1,    "I"),
]

ROM_VAL = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def int_to_roman(n: int) -> str:
    if not (1 <= n <= 3999):
        raise ValueError("n deve estar entre 1 e 3999")
    res = []
    x = n
    for val, sym in ROM_MAP:
        q, x = divmod(x, val)
        res.append(sym * q)
    return "".join(res)

def roman_to_int(s: str) -> int:
    if not s or not isinstance(s, str):
        raise ValueError("Romano inválido")
    s = s.upper()
    if any(ch not in ROM_VAL for ch in s):
        raise ValueError("Romano inválido")

    total, i = 0, 0
    prev = None
    repeat_count = 0
    repeatable = {"I", "X", "C", "M"}

    while i < len(s):
        ch = s[i]
        val = ROM_VAL[ch]

        if prev == ch:
            repeat_count += 1
            if ch not in repeatable or repeat_count >= 3:
                raise ValueError("Repetição inválida")
        else:
            repeat_count = 0

        if i + 1 < len(s):
            ch2 = s[i + 1]
            val2 = ROM_VAL[ch2]
            if val < val2:
                allowed = {("I","V"),("I","X"),("X","L"),("X","C"),("C","D"),("C","M")}
                if (ch, ch2) not in allowed:
                    raise ValueError("Par subtrativo inválido")
                if repeat_count > 0:
                    raise ValueError("Subtração após repetição é inválida")
                total += val2 - val
                i += 2
                prev = None
                continue

        total += val
        prev = ch
        i += 1

    # Exige forma canônica mínima
    if int_to_roman(total) != s:
        raise ValueError("Representação não canônica")
    return total
