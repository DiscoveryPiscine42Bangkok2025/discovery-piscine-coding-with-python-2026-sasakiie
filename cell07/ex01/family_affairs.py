def find_the_redheads(x):
    red = filter(lambda name: x[name] == "red", x.keys())
    return list(red)

dupont_family = {
    "florian": "red","marie": "blond","virginie": "brunette","david": "red","franck": "red"
}

print(find_the_redheads(dupont_family))