digits = [2, 3, 5, 7]           # list of allowed digits
for tens in digits:             # tens digit is some allowed digit
    for ones in digits:         # ones digit is some allowed digit
        print(str(tens)+str(ones))
