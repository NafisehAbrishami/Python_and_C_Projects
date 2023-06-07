inp = input()
inp2 = inp.split()
inp3 = [int(x) for x in inp2]
inp4 = [max(inp3)- min(inp3)]
inp5 = inp4.pop(0)
print(inp5)
