def fibonnaci(n):
    fibonnaci_sequence = [0,1]
    
    while len(fibonnaci_sequence) < n:
        fibonnaci_sequence.append(fibonnaci_sequence[-1] + fibonnaci_sequence[-2])
    return fibonnaci_sequence

inp = int(input('Enter nth term: '))
result = fibonnaci(inp)
print(result)    