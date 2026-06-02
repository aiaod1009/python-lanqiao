y = int(input().strip())
t = ['geng','xin','ren','gui','jia','yi','bing','ding','wu','ji']
d = ['zi','chou','yin','mao','chen','si','wu','wei','shen','you','xu','hai']
m = t[(y - 2020)%10]
n = d[(y - 2020)%12]
print(m+n)