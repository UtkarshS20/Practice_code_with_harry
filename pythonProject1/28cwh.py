#import sys
#print(sys.path)
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())
import example26cwh       #suggested
print(example26cwh.a)
#from example26cwh import a #not suggested
#print(a)
example26cwh.printjoke("thats me")