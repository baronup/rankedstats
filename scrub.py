source = "finales.tsv"
source2 = "xglarryxg.tsv"
target = "data.js"

s = open(source, 'r')
s2 = open(source2, 'r')
t = open(target, 'w')

categories = ['lpchange', 'kills', 'deaths', 'assists']

output = "var finales = ["

game_number = 30

for line in s:
    split_line = line.split('\t')
    output += "{"
    for i in range(4):
        if i < 3:
            output += categories[i] + ":" + split_line[i] + ','
        else:
            output += categories[i] + ":" + split_line[i]
    if game_number == 1:
        output += "}"
    else:
        output += "},"

    game_number -= 1
output += '];\n'

t.write(output)
s.close()

output = "var xglarryxg = ["

game_number = 30

for line in s2:
    split_line = line.split('\t')
    output += "{"
    for i in range(4):
        if i < 3:
            output += categories[i] + ":" + split_line[i] + ','
        else:
            output += categories[i] + ":" + split_line[i]
    if game_number == 1:
        output += "}"
    else:
        output += "},"

    game_number -= 1
output += '];'

t.write(output)
t.close()
s2.close()
