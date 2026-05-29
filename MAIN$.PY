def ceaser_encryption(text , shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            start = ord("a") if ch.islower() else ord("a")
            new_char = chr((ord(ch) - 97 + shift)%26 + start)
            result+=new_char

        else:
            result+=ch
    
        # result+= cha

    return result

print(ceaser_encryption("hellz",3))

# new_char = chr((ord("a") - 97 + 3) % 26 + 97)

# print(new_char)

