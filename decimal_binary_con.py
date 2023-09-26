while True:

    n = int((input("Enter decimal number: ")))
    temp_n = n
    binary_conv = []

    while temp_n > 0:
        rem= temp_n % 2
        binary_conv.append(rem)
        temp_n = temp_n // 2
    
    binary_conv = binary_conv[::-1]
    print(binary_conv)
    
