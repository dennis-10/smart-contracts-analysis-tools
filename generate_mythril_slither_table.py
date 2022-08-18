import slither_constants_file as scf
import mythril_constants_file as mcf
import xlsxwriter as xls
import pandas as pd
import time

# Instanciating objects with constants
mythril_vulnerabilities = mcf.VulnerabilityNames()
slither_vulnerabilities = scf.Vulnerabiltiies()

# List with the name of which vulnerability from Slither reference
mythril_vulnerabilities_list = [
    mythril_vulnerabilities.ARBITRATY_STORAGE,
    mythril_vulnerabilities.DELEGATECALL_UNTRUSTED_CALLE,mythril_vulnerabilities.UNPROTECTED_ETHER_WITHDRAW,
    mythril_vulnerabilities.UNPROTECTED_SELFDESCTRUCT, mythril_vulnerabilities.WEAK_RANDOMNESS ]

mythril_reentrancy_list = [ 
    mythril_vulnerabilities.EXTERNAL_CALLS, # reentrancy
    mythril_vulnerabilities.REENTRANCY ]

slither_vulnerabilities_list = [
    slither_vulnerabilities.UNINTIALIZED_STORAGE_VARIABLES, slither_vulnerabilities.CONTROLLED_DELEGATECALL,
    slither_vulnerabilities.SEND_ETHER_TO_ARBITRARY, slither_vulnerabilities.SUICIDAL, slither_vulnerabilities.WEAK_PRNG]

slither_reentrancy_list = [ slither_vulnerabilities.REENTRANCY, slither_vulnerabilities.REENTRANCY_VULNERABILITIES_1,
    slither_vulnerabilities.REENTRANCY_VULNERABILITIES_2, slither_vulnerabilities.REENTRANCY_VULNERABILITIES_3, 
    slither_vulnerabilities.REENTRANCY_VULNERABILITIES_4 ]

# Acessing first sheeter of both excel files
mythril_table = pd.read_excel("mythril_results.xlsx", 0)
slither_table = pd.read_excel("slither_results_final.xlsx", 0)

# Renaming first column
mythril_table.rename( columns={'Unnamed: 0': 'contracts'}, inplace=True )
slither_table.rename( columns={'Unnamed: 0': 'contracts'}, inplace=True)

# Passing contract names to lists
slither_contracts_list = slither_table.iloc[:, 0].values.tolist()
mythril_contract_list = mythril_table.iloc[:, 0].values.tolist()

# Analyzed in both tools
shared_contracts_list = []

for contract in mythril_contract_list:
    if (contract in slither_contracts_list):
        shared_contracts_list.append(contract)

# Setting contracts column as index
slither_table.set_index('contracts', inplace=True)
mythril_table.set_index('contracts', inplace=True)

# Generating Excel file
workbook = xls.Workbook("tools_results.xlsx")
worksheet = workbook.add_worksheet("Results - 1")

# File indexes
work_line = 0
work_column = 0

 # Setting first cell (0,0)
cell_format = workbook.add_format()
cell_format.set_bg_color('black')
worksheet.write(0, 0, "", cell_format)

# Insert fake contract for preventing skiping first contract
shared_contracts_list.insert(0, "")

i = 0
for contract in shared_contracts_list:
    # For each mythril vulnerability..
    for sv, mv in zip(slither_vulnerabilities_list, mythril_vulnerabilities_list):
        # Sets first line with vulnerabilities
        if work_line == int(0):
            # Adding style to cell
            cell_format = workbook.add_format()
            
            cell_format.set_bold()
            work_column += 1
            
            # Write slither vulnerability
            sv = f'SLITHER {sv}'
            worksheet.write(work_line, work_column, sv, cell_format)

            # Write mythril vulnerability
            mv = f'MYTHRIL {mv}'
            work_column += 1
            worksheet.write(work_line, work_column, mv, cell_format)        
        else:
            if work_column == int(0):
                cell_format = workbook.add_format()
                cell_format.set_bold()
                cell_format.set_bg_color("D3D3D3")
            
                worksheet.write(work_line, work_column, contract, cell_format)
                work_column += 1

            # Inserting slither vulnerability incidence
            value = slither_table.loc[[contract],[sv]].values[0]
            worksheet.write(work_line, work_column, value)
            work_column += 1

            # Inserting mythril vulnerability incidence
            value = mythril_table.loc[[contract],[mv]].values[0]
            worksheet.write(work_line, work_column, value)
            work_column += 1

    work_line += 1
    work_column = 0

    # Adding cell styles
    cell_format = workbook.add_format()
    cell_format.set_bold()
    cell_format.set_bg_color("gray")

workbook.close()

# Removing fake contract
del shared_contracts_list[0]

# Treating/Merging reentrancy vulnerabilities
# Creating vulnerability that represents the sum of all reentrancies
slither_vulnerabilities_list.append('reentrancy')
mythril_vulnerabilities_list.append('reentrancy')

slither_column_list = []
mythril_column_list = []
for contract in shared_contracts_list:
    value_1 = 0
    value_2 = 0
    for reentrancy in slither_reentrancy_list:
        value_1 += slither_table.loc[[contract],[reentrancy]].values[0][0]

    slither_column_list.append(value_1)

    for reentrancy in mythril_reentrancy_list:
        value_2 += mythril_table.loc[[contract],[reentrancy]].values[0][0]
    
    mythril_column_list.append(value_2)

# Opening new file
results_table = pd.read_excel("tools_results.xlsx", 0)

# Creating a new reentrancy column
results_table['SLITHER reentrancy'] = slither_column_list
results_table['MYTHRIL reentrancy'] = mythril_column_list

# Saving excel with reentrancy data
results_table.to_excel("tools_results.xlsx", sheet_name="Results_1")