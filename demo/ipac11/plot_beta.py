# This is the example we published in our IPAC'11 paper.

from matplotlib import pyplot as plt
from cern import pymad as pm

# create the service
#pms = pm.init('cpymad')
#pms = pm.init('jpymad', start='gui')
pms = pm.init('jpymad', start='service')
#pms = pm.init('jpymad')

# print the name of all model definitions
print pms.mdefnames

# get one model-definition
model = pms.create_model('lhc')

# obtain get twiss table in a python object
table,summary=model.twiss(columns=['name', 's', 'betx', 'bety'])

# plot the result
plt.plot(table.s,table.betx)
plt.show()
