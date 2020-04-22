import os
path = 'C:/Users/Ahmed Hamada/Downloads/Compressed/Covid19_Learnng-master/data/test/pred'

i=144

for filename in os.listdir(path):
    newname = filename.replace(".jpeg", ".jpg")
    os.rename(filename,newname)



training_path = './data/training/'
test_path = './data/test/'
pred_path = './data/pred/'




types_code = {'COVID-19':0, 'SARS':1, 'ARDS':2, 'Pneumocystis':3, 'Streptococcus':4, 'No Finding':5}

def get_types_code(n) : 
    for x , y in types_code.items() : 
        if n == y : 
            return x 
        
        
import pandas as pd     
df = pd.read_csv('./metadata.csv')        

for index, row in df.iterrows():
    if(df[index][4] == '')
    
    df[index][10]

from shutil import copyfile
copyfile(src, dst)    