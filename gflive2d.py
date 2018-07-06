def decrypt(encrypt: bytes):
    length = len(encrypt) - 17
    decrypt = bytearray(length)
    pos = bytearray(16)

    for i in range(0, 16):
        pos[i] = encrypt[i * 5 + 1]

    x = 0
    y = -1
    z = 0

    while True:
        if y + 1 > 80:
            f = pos[y - ((y + ((y - 16) >> 31 >> 28) - 16) & 0xFFFFFFF0) - 16]
            decrypt[z] = encrypt[y + 1] ^ f
            z += 1
        else:
            if y == 5 * (y // 5):
                x += 1
            elif y != -1:
                decrypt[z] = encrypt[y + 1] ^ pos[(y - x) % 16]
                z += 1

        y += 1

        if z != length:
            continue

        break

    return decrypt