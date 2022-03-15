import os
print(os.getcwd())
print(__file__)

f = open(os.getcwd()+"/Question collection (Antwoorden) - Formulierreacties reserve.tsv", "r")

mcd = {}
oq = {}
sortq = {}
for line in f:
    a = line.split('\t')
    if a[1] == "Multiple Choice":
        mcd[a[0]] = {}
        mcd[a[0]]['q'] = a[2]
        mcd[a[0]]['a'] = a[3]
        mcd[a[0]]['c'] = a[4]
    if a[1] == "Open Question":
        oq[a[0]] = {}
        oq[a[0]]['q'] = a[5]
    if a[1] == "Sorting Answers":
        sortq[a[0]] = {}
        sortq[a[0]]['q'] = a[7]
        sortq[a[0]]['a'] = a[8][:-1]

# Multiple Choice Questions #

print(mcd)

answermap = {'Option 1': '1', 'Option 2': '2', 'Option 3': '3', 'Option 4': '4', 'Option 5': '5', 'Option 6': '6'}

g = open(os.getcwd()+"/Wooclapinput.csv", "w")
g.write("Type,Title,Correct,Choice,Choice,Choice,Choice,Choice,Choice,Choice")
for question in mcd:
    g.write("\nMCQ,"+mcd[question]['q']+","+answermap[mcd[question]['c']]+','+str(",".join(mcd[question]['a'].split(';'))))
    for i in range(0, 7-len(mcd[question]['a'].split(';'))):
        g.write(',')

# Open Questions #

print(oq)

for question in oq:
    g.write("\nOpenQuestion,"+oq[question]['q']+",,,,,")

# Sorting Question #

print(sortq)

for question in sortq:
    g.write("\nSorting,"+sortq[question]['q']+",,"+str(",".join(sortq[question]['a'].split(';'))))
    for i in range(0, 7-len(sortq[question]['a'].split(';'))):
        g.write(',')

g.write('\n')
