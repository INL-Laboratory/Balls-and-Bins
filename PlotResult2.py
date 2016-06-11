import matplotlib.pyplot as plt
import numpy as np
import csv


# Choose the simulator. It can be the following values:
# 'one choice'
# 'two choice'
#simulator = 'one choice'
simulator = 'two choice'

#srv_num = 2000
file_num = 500
cache_cz = 100
# Number of runs for computing average values. It is more eficcient that num_of_runs be a multiple of pool_size
num_of_runs = 40

"""
rslt = []
with open('output.csv','rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
        rslt.append((map(float, row)))
"""

result = np.array([])
if simulator == 'one choice':
    with open('rslt2_sim1_fn={}_cs={}_itr={}.txt'.format(file_num,cache_cz,num_of_runs),'rb') as f:
        result = np.loadtxt(f, delimiter=',')
elif simulator == 'two choice':
    with open('rslt2_sim2_fn={}_cs={}_itr={}.txt'.format(file_num,cache_cz,num_of_runs),'rb') as f:
        result = np.loadtxt(f, delimiter=',')


print(result)
#print(rslt)

#result = np.array(rslt)

line_maxload, = plt.plot(result[:,0], result[:,1], label='Maximum Load')
line_avgCost, = plt.plot(result[:,0], result[:,2], label='Average Cost')
#line_maxload.set_label('Label via method')
plt.legend()
plt.xlabel('Number of servers')
plt.title('Simulator: {}. # of files = {}, cache size = {}, # of iterations ={}'.format(simulator,file_num,cache_cz,num_of_runs))
plt.show()