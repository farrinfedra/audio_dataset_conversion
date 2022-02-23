from multiprocessing import Process
import os
from tqdm import tqdm

inputs = input("Enter input directory and output directory in the following format: /path/to/input /path/to/output\n")
input_dir, output_dir = inputs.split()
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for file in tqdm(os.listdir(input_dir), desc = "converting"):
    name = file.split('.')[0]
    print('lame --decode ' + input_dir + '/' + file + ' '+ output_dir + '/' + name + '.wav')
    os.system('lame --decode ' + input_dir + '/' + file + ' '+ output_dir + '/' + name + '.wav')
    
