T=int(input())
for _ in range(T):
    S=input()
    if(len(S)<6):
        print(0)
        continue
    Big = False  # 是否有大写字母
    Small = False  # 是否有小写字母
    Digit = False  # 是否有数字
    SpecialSet = set()  # 存储特殊字符（去重）
    NotPass = False  # 是否包含非法字符
    for i in S:
        if(i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            Big=True
        elif(i in 'abcdefghijklmnopqrstuvwxyz'):
            Small=True
        elif(i in '1234567890'):
            Digit=True
        elif(i in '~!@#$%^&*()_'):
            SpecialSet.add(i)
        else:
            NotPass=True
    if(NotPass):
        print(0)
        continue
    if(len(S)>=12):
        if(Big and Small and Digit and SpecialSet):
            print(3)
            continue
        if(int(Big)+int(Small)+int(Digit)>=2 and len(SpecialSet)>=3):
            print(3)
            continue
    if(len(S)>=8):
        if(int(Big)+int(Small)+int(Digit)+int(bool(SpecialSet))>=2):
            print(2)
            continue
    print(1)