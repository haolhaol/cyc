def number_length(a: int) -> int:
    digits = 0
    while a:
        digits += 1
        a //= 10
    return digits + (not digits) # 0 has 1 digit
