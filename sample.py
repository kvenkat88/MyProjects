__author__ = 'venkat'
from libs import global_variables as run

Test_Status = 1

if run.Test_Status == 0:
    print "Not OK"
else:
    print "OK"