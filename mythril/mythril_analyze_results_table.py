import mythril_constants_file as mcf
import xlsxwriter as xls

# Gets the name of the contract being analyzed
def get_contract_name_from_line(charList: list()):
    index = charList.index(':')
    index = index + 2
    temp = charList[index:]
    return ''.join(temp)

# Instanciating objects with constants
SWC_object = mcf.VulnerabiltiiesSWC()
names_object = mcf.VulnerabilityNames()
severities_object = mcf.VulnerabilitySeverities()

# List of severities in order
severities = [severities_object.ARBITRARY_JUMP, severities_object.ARBITRATY_STORAGE, severities_object.ASSERT_VIOLATION, severities_object.DELEGATECALL_UNTRUSTED_CALLE,
    severities_object.DOS_WITH_FAILED_CALL, severities_object.EXTERNAL_CALLS, 
    severities_object.INTEGER_OVERFLOW_UNDERFLOW, severities_object.REENTRANCY, severities_object.TIMESTAMP_DEPENDENCE, severities_object.UNCHECKED_CALL_RETURN_VALUE, 
    severities_object.UNPROTECTED_ETHER_WITHDRAW, severities_object.UNPROTECTED_SELFDESCTRUCT, severities_object.WEAK_RANDOMNESS, severities_object.TX_ORIGIN_USAGE]

# List with the name of which vulnerability from Slither reference
vulnerabilities = [names_object.ARBITRARY_JUMP, names_object.ARBITRATY_STORAGE, names_object.ASSERT_VIOLATION, names_object.DELEGATECALL_UNTRUSTED_CALLE,
    names_object.DOS_WITH_FAILED_CALL, names_object.EXTERNAL_CALLS, 
    names_object.INTEGER_OVERFLOW_UNDERFLOW, names_object.REENTRANCY, names_object.TIMESTAMP_DEPENDENCE, names_object.UNCHECKED_CALL_RETURN_VALUE, 
    names_object.UNPROTECTED_ETHER_WITHDRAW, names_object.UNPROTECTED_SELFDESCTRUCT, names_object.WEAK_RANDOMNESS, names_object.TX_ORIGIN_USAGE]

# SWC code for each vulnerability
SWC_ids = [SWC_object.ARBITRARY_JUMP, SWC_object.ARBITRATY_STORAGE, SWC_object.ASSERT_VIOLATION, SWC_object.DELEGATECALL_UNTRUSTED_CALLE,
    SWC_object.DOS_WITH_FAILED_CALL, SWC_object.EXTERNAL_CALLS, SWC_object.INTEGER_OVERFLOW_UNDERFLOW, SWC_object.REENTRANCY, SWC_object.TIMESTAMP_DEPENDENCE,
    SWC_object.UNCHECKED_CALL_RETURN_VALUE, SWC_object.UNPROTECTED_ETHER_WITHDRAW, SWC_object.UNPROTECTED_SELFDESCTRUCT, SWC_object.WEAK_RANDOMNESS,
    SWC_object.TX_ORIGIN_USAGE]

# Opens the actual .txt file with analysis results
with open('mythril_analysis.txt', 'r') as f1:
    first_line = f1.readline()
    first_line_list = list(first_line)
    contract_name = get_contract_name_from_line(first_line_list)

    # Add column for indicating if contract was analyzed or not (exception)
    vulnerabilities.append("ANALYZED")

    # Dictionary for counting vulnerability incidence
    # EXAMPLE:
    #  { 'vulnerability0': 0, 'vulnerability1': 0, ... ,'vulnerabilityN': 0}
    total_incidence_dic = dict(zip(vulnerabilities, [0] * 15))
    
    # Default as false
    total_incidence_dic["ANALYZED"] = "False"
    
    # Dictionary for containing contract name with each vulnerability and its incidence
    # EXAMPLE:
    #  {'example1.sol' : {'vulnerability0': 3, 'vulnerability1': 1, ..., 'vulnerabilityN': X}}
    #  {'example2.sol' : {'vulnerability0': 0, 'vulnerability1': 2, ..., 'vulnerabilityN': Y}}
    #  ...
    #  {'exampleN.sol' : {'vulnerability0': 1, 'vulnerability1': 0, ..., 'vulnerabilityN': Z}}
    contract_incidence_dic = {contract_name : dict(zip(vulnerabilities, [0] * 105))}

    # counts the number of the contract analyzed
    counter = 1
    result = first_line
    has_vulnerability = False

    for line in f1:
        if 'ANALYZED' in line:
            if counter > 1:
                contract_incidence_dic[contract_name] = dict(zip(vulnerabilities, [0] * 15))
                contract_incidence_dic[contract_name]["ANALYZED"] = "False"

            for swc, v in zip(SWC_ids, vulnerabilities):
                if(f"SWC ID: {swc}" in result):
                    # print(f"\nABI encoder found in file number {counter} and name {contract_name}")
                    contract_incidence_dic[contract_name][v] += 1
                    total_incidence_dic[v] += 1
                    has_vulnerability = True
            
            if ("ERROR:b''" not in result and has_vulnerability is False):
                contract_incidence_dic[contract_name]["ANALYZED"] = "False"
            else:
                contract_incidence_dic[contract_name]["ANALYZED"] = "True"
                has_vulnerability = False

            first_line_list = list(line)
            contract_name = get_contract_name_from_line(first_line_list)
            result = ""
            counter += 1
            continue

        result += line

    # Generating .xlsx file
    workbook = xls.Workbook("mythril_results.xlsx")
    worksheet = workbook.add_worksheet("Mythril")

    # Fulffiling file
    work_line = 0
    work_column = 0
    contracts = list(contract_incidence_dic.keys())
    print(contracts)
    
    # Setting first cell (0,0)
    cell_format = workbook.add_format()
    cell_format.set_bg_color('black')
    worksheet.write(0, 0, "", cell_format)
    
    # Adding severity making easier to iterate both.
    severities.append("")
    contracts.insert(0, "")
    for contract in contracts:
        for v, s in zip(vulnerabilities, severities):
            if work_line == int(0):
                # Adding style to cell
                cell_format = workbook.add_format()
                cell_format.set_bold()
                work_column += 1

                if s == "High":
                    cell_format.set_bg_color('red')

                if s == "Medium":
                    cell_format.set_bg_color('yellow')

                if s == "Low":
                    cell_format.set_bg_color("green")
            
                if s == "":
                    cell_format.set_bg_color("purple")

                worksheet.write(work_line, work_column, v, cell_format)
            else:
                if work_column == int(0):
                    cell_format = workbook.add_format()
                    cell_format.set_bold()
                    cell_format.set_bg_color("D3D3D3")

                    worksheet.write(work_line, work_column, contract, cell_format)
                    work_column += 1

                worksheet.write(work_line, work_column, contract_incidence_dic[contract][v])
                work_column += 1
                
        work_line += 1
        work_column = 0

    # Adding cell styles
    cell_format = workbook.add_format()
    cell_format.set_bold()
    cell_format.set_bg_color("gray")

    # Adding TOTAL number/count of each vulnerability
    worksheet.write(work_line, work_column, "TOTAL", cell_format)
    work_column += 1
    for v in vulnerabilities:
        if v == "ANALYZED":
            break
        worksheet.write(work_line, work_column, total_incidence_dic[v])
        work_column += 1

    workbook.close()
    f1.close()