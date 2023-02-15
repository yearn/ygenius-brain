import csv 
import json 

filename = 'all_vaults_and_strats.json' 
templateString = 'The {symbol} yVault version {version} at [{address}](https://yearn.watch/vault/{address}) has a currently a Total Value Locked (TVL) of {tvl[tvl]}, and an annual percentage yield (APY) of {apy[net_apy]}'
output = [] 

# with open(filename) as file: 
#     reader = csv.DictReader(file) 
#     for line in reader: 
#         output.append(templateString.format(**line)) 

with open(filename) as file: 
    data = json.load(file) 
    for line in data: 
      line["apy"]["net_apy"] = "{0:.2f}%".format(line["apy"]["net_apy"] * 100)
      output.append(templateString.format(**line)) 
        

with open('all_vaults_and_strats.md', 'w') as file: 
    for line in output: 
        file.write(line + '\n\n')