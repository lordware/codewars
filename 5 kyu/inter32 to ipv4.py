def int32_to_ip(int32):
    to_bin = str(bin(int32))[2::]
    print(to_bin)
    result = ""
    if len(to_bin) > 24:
        result = f"{int(to_bin[:-24], 2)}.{int(to_bin[-24:-16], 2)}.{int(to_bin[-16:-8], 2)}.{int(to_bin[-8:], 2)}"
    elif len(to_bin) > 16:
        result = f"0.{int(to_bin[:-16], 2)}.{int(to_bin[-16:-8], 2)}.{int(to_bin[-8:], 2)}"
    elif len(to_bin) > 8:
        result = f"0.0.{int(to_bin[:-8], 2)}.{int(to_bin[-8:], 2)}"
    elif len(to_bin) <= 8:
        result = f"0.0.0.{int(to_bin, 2)}"
    return result
