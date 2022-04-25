orig = open('results.csv')
new = open('results2.csv')

bigb = set(new) - set(orig)
print(bigb)

orig.close
new.close
