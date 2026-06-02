s = (
    "tocyjkdzcieoiodfpbgcncsrjbhmugdnojjddhllnofawllbhf"
    "iadgdcdjstemphmnjihecoapdjjrprrqnhgccevdarufmliqij"
    "gihhfgdcmxvicfauachlifhafpdccfseflcdgjncadfclvfmad"
    "vrnaaahahndsikzssoywakgnfjjaihtniptwoulxbaeqkqhfwl"
)
dp = {}
for c in s:
    curr = 1
    for pre,cnt in dp.items():
        if pre < c:
            curr += cnt
    dp[c] = curr
print(sum(dp.values()))