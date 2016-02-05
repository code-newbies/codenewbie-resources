import string


ooooooh = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def shift_it(text):

    alpha = string.ascii_lowercase
    maketranz = 'cdefghijklmnopqrztuvwxyz{0}'.format(alpha)

    for word in text:
        for letter in word:
            if letter in alpha:
                pos = alpha.index(letter)
                print(maketranz[pos], end="")
            else:
                print(letter, end="")

shift_it(ooooooh)
shift_it("/pc/def/map.html")
