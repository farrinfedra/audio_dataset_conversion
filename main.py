from multiprocessing import Process
import os
from tqdm import tqdm

inputs = input("Enter input directory and output directory in the following format: /path/to/input /path/to/output\n")
input_dir, output_dir = inputs.split()
species = os.listdir(input_dir)
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

   
for bird in species: #list of species folder
    if os.path.isfile(input_dir + '/' +bird):
        continue
    audios = os.listdir(input_dir + '/' + bird)
    if "in_progress.txt" in audios:
        audios.remove("in_progress.txt")
    
    if not bird in os.listdir(output_dir):
        os.mkdir(output_dir + '/' + bird)
    folders = tqdm(audios)
    for audio in folders:
        folders.set_description("Processing audios in %s" % bird)
        name = audio.split('.')[0]
        #print('lame --decode --quiet ' + input_dir + '/' +  bird + '/' + audio + ' '+ output_dir + '/' + bird + '/' + name + '.wav')
        os.system('lame --decode --quiet ' + input_dir + '/' +  bird +  '/' + audio + ' '+ output_dir + '/' +  bird + '/' + name + '.wav')
    
