import os
import subprocess

# Path to files folder
WSL_PATH = "<YOUR-PATH>/EtherScan_Smartcontracts"

# Smart contracts names loaded
contracts =  os.listdir(WSL_PATH)

# Iterating through contracts
i = 0
with open('mythril_analysis.txt', 'w') as f:
    for contract in contracts:
        slither_command = f"sudo myth analyze {contract} --max-depth 10 --execution-time 10"
        p1 = subprocess.Popen(slither_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = p1.communicate()

        f.write(f'{i}) CONTRACT ANALYZED: {contract}\n\n')
        f.write(f'OUT: \n\n{out}\n\n ERROR:{err}\n\n')
        # f.close()

        i += 1
        if (i % 10 == 0):
            print(f"\Tested: {i} files.\n")
    f.close()