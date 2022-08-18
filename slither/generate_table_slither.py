import slither_constants_file as scf
import xlsxwriter as xls

# Gets the name of the contract being analyzed
def get_contract_name_from_line(charList: list()):
    index = charList.index(':')
    index = index + 2
    temp = charList[index:]
    return ''.join(temp)

# Instances
vulnerabilities_object = scf.Vulnerabiltiies()
severities_object = scf.Severities()

# List with the name of which vulnerability from Slither reference
vulnerabilities = [
    vulnerabilities_object.ABI_ENCODER, vulnerabilities_object.ARBITRARY, vulnerabilities_object.ARRAY_BY_REFERENCE, vulnerabilities_object.ABI_ENCODED_COLLISION,
    vulnerabilities_object.INCORRECT_SHIFT_IN_ASSEMBLY, vulnerabilities_object.MISSING_RETURN_STATEMENTS, vulnerabilities_object.MULTIPLE_CONSTRUCTOR_SCHEMES, 
    vulnerabilities_object.PROTECTED_VARIABLES, vulnerabilities_object.PUBLIC_MAPPING_WITH_NESTED_VARIABLES, vulnerabilities_object.RIGHT_TO_LEFT_OVERRIDE_CHAR,
    vulnerabilities_object.STATE_VARIABLE_SHADOWING, vulnerabilities_object.SUICIDAL, vulnerabilities_object.UNINTIALIZED_STATE_VARIABLES, vulnerabilities_object.UNINTIALIZED_STORAGE_VARIABLES,
    vulnerabilities_object.UNPROTECTED_UPGRADABLE_CONTRACT, vulnerabilities_object.ARBITRARY_FROM_IN_TRANSFERFROM, vulnerabilities_object.SEND_ETHER_TO_ARBITRARY,
    vulnerabilities_object.ARRAY_LEGNTH_ASSIGNMENT, vulnerabilities_object.CONTROLLED_DELEGATECALL, vulnerabilities_object.PAYABLE_USING_DELEGATECALL_LOOP,
    vulnerabilities_object.INCORRECT_FUNCTION_VISIBILITY, vulnerabilities_object.INCORRECT_FUNCTION_EXPONENTATION, vulnerabilities_object.INCORRECT_RETURN_IN_ASSEMBLY,
    vulnerabilities_object.INCORRECT_MSGSENDER_CHECK, vulnerabilities_object.MISSING_CUNSTRUCTOR, vulnerabilities_object.MODIFIER_LOOK_LIKE_SOL_KEYWORK,
    vulnerabilities_object.MSGVALUE_INSIDE_LOOP, vulnerabilities_object.OVERFLOW_ERC20_BALANCE, vulnerabilities_object.UNPROTECTED_ECRECOVER_LEADING_RACE_CONDITION,
    vulnerabilities_object.RACE_CONDITION_AT_CONTRACT_INIT, vulnerabilities_object.REENTRANCY, vulnerabilities_object.STORAGE_SIGNED_INTEGER_ARRAY, vulnerabilities_object.UNCHECKED_TRANSFER,
    vulnerabilities_object.UNPROTECTED_FUNCTIONS, vulnerabilities_object.WEAK_PRNG, vulnerabilities_object.DANGEROUS_ENUM_CONVERSION, vulnerabilities_object.INCORRECT_ERC20_CONVERSION,
    vulnerabilities_object.INCORRECT_ERC721_INTERFACE, vulnerabilities_object.DANGEROUS_STRICT_EQUALITIES, vulnerabilities_object.INCORRECT_ISCONTRACT_MODIFIER,
    vulnerabilities_object.CONTRACTS_THAT_LOCKS_ETHER, vulnerabilities_object.DELETION_ON_MAPPING_CONTAINING_STRUCT, 
    vulnerabilities_object.STATE_VARIABLE_SHADOWING_FROM_ABSTRACT_CONTRACT, vulnerabilities_object.TAUTOLOGICAL_COMPARE, vulnerabilities_object.TAUTOLOGY_OR_CONTRADICTION,
    vulnerabilities_object.WRITE_AFTER_WRITE, vulnerabilities_object.INCORRECT_BALANCE_VALUE, vulnerabilities_object.MISUSE_OF_BOOLEAN_CONSTANT,
    vulnerabilities_object.CONSTANT_FUNCTIONS_USING_ASSEMBLY_CODE, vulnerabilities_object.CONSTANT_FUNCTIONS_CHANGING_THE_STATE, vulnerabilities_object.CONTROLLED_LOOP_ITERATION,
    vulnerabilities_object.CONTROLLED_LOWLEVELCALL, vulnerabilities_object.DIVIDE_BEFORE_MULTIPLY, vulnerabilities_object.EMPTY_FUNCTIONS, vulnerabilities_object.LACK_OF_MSGSENDER_USAGE,
    vulnerabilities_object.MSGVALUE_USAGE_ON_NONPAYABLE_FUNCTIONS, vulnerabilities_object.OVERFLOW_ERC20_ALLOWANCE, vulnerabilities_object.ABSENCE_OF_PAUSABLE_MODIFIER,
    vulnerabilities_object.REENTRANCY_VULNERABILITIES_1, vulnerabilities_object.REUSED_BASE_CONSTRUCTORS, vulnerabilities_object.DANGEROUS_USAGE_OF_TXGASPRICE,
    vulnerabilities_object.DANGEROUS_USAGE_OF_TXORIGIN, vulnerabilities_object.UNCHECKED_BLOCKHASH, vulnerabilities_object.UNCHECKED_LOW_LEVEL_CALLS, vulnerabilities_object.UNCHECKED_SEND,
    vulnerabilities_object.UNINITIALIZED_LOCAL_VARIABLES, vulnerabilities_object.UNINITIALIZED_RETURN_STATEMENTS, vulnerabilities_object.UNSPECIFIED_OPERATION_ORDER, vulnerabilities_object.UNUSED_EVENTS,
    vulnerabilities_object.UNUSED_RETURN, vulnerabilities_object.UNUSED_RETURN_INTERNAL, vulnerabilities_object.DETECT_USE_AFTER_DELETE, vulnerabilities_object.INCORRECT_MODIFIER,
    vulnerabilities_object.BUILTIN_SYMBOL_SHADOWING, vulnerabilities_object.LOCAL_VARIABLES_SHADOWING, vulnerabilities_object.UNINITIALIZED_POINTERS_IN_CONSTRUCTORS, vulnerabilities_object.PREDECLARATION_USAGE_OF_LOCAL_VARIABLES,
    vulnerabilities_object.CALLS_INSIDE_LOOP, vulnerabilities_object.MISSING_EVENTS_ACCESS_CONTROL, vulnerabilities_object.MISSING_EVENTS_ARITHMETIC, vulnerabilities_object.DANGEROUS_UNARY_EXPRESSIONS,
    vulnerabilities_object.MISSING_ZERO_ADDRESS_VALIDATION, vulnerabilities_object.REENTRANCY_VULNERABILITIES_2, vulnerabilities_object.BLOCK_TIMESTAMP, vulnerabilities_object.ASSEMBLY_USAGE, vulnerabilities_object.ASSERT_STATE_CHANGE,
    vulnerabilities_object.BOOLEAN_EQUALITY, vulnerabilities_object.UNINDEXED_ERC20_EVENT_PARAMETERS, vulnerabilities_object.LOW_LEVEL_CALLS, vulnerabilities_object.MISSING_INHERITANCE, 
    vulnerabilities_object.CONFORMANCE_TO_NAME_CONVENTIONS, vulnerabilities_object.DIFFERENT_PRAGMA_DIRECTIVES_USED, vulnerabilities_object.REDUNDANT_STATEMENTS, vulnerabilities_object.INCORRECT_VERSIONS_OF_SOLIDITY,
    vulnerabilities_object.UNINPLEMENTED_FUNCTIONS, vulnerabilities_object.UNUSED_STATE_VARIABLE, vulnerabilities_object.COSTLY_OPERATION_INSIDE_LOOP, vulnerabilities_object.DEAD_CODE,
    vulnerabilities_object.REENTRANCY_VULNERABILITIES_3, vulnerabilities_object.REENTRANCY_VULNERABILITIES_4, vulnerabilities_object.VARIABLE_NAMES_TO_SIMILAR, vulnerabilities_object.TOO_MANY_DIGITS,
    vulnerabilities_object.STATE_VARIABLES_THAT_COULD_BE_CONSTANT, vulnerabilities_object.PUBLIC_FUNCTION_THAT_COULD_BE_EXTERNAL, vulnerabilities_object.BLOCKHASH_CURRENT]

severities = [
    severities_object.ABI_ENCODER, severities_object.ARBITRARY, severities_object.ARRAY_BY_REFERENCE, severities_object.ABI_ENCODED_COLLISION,
    severities_object.INCORRECT_SHIFT_IN_ASSEMBLY, severities_object.MISSING_RETURN_STATEMENTS, severities_object.MULTIPLE_CONSTRUCTOR_SCHEMES, 
    severities_object.PROTECTED_VARIABLES, severities_object.PUBLIC_MAPPING_WITH_NESTED_VARIABLES, severities_object.RIGHT_TO_LEFT_OVERRIDE_CHAR,
    severities_object.STATE_VARIABLE_SHADOWING, severities_object.SUICIDAL, severities_object.UNINTIALIZED_STATE_VARIABLES, severities_object.UNINTIALIZED_STORAGE_VARIABLES,
    severities_object.UNPROTECTED_UPGRADABLE_CONTRACT, severities_object.ARBITRARY_FROM_IN_TRANSFERFROM, severities_object.SEND_ETHER_TO_ARBITRARY,
    severities_object.ARRAY_LEGNTH_ASSIGNMENT, severities_object.CONTROLLED_DELEGATECALL, severities_object.PAYABLE_USING_DELEGATECALL_LOOP,
    severities_object.INCORRECT_FUNCTION_VISIBILITY, severities_object.INCORRECT_FUNCTION_EXPONENTATION, severities_object.INCORRECT_RETURN_IN_ASSEMBLY,
    severities_object.INCORRECT_MSGSENDER_CHECK, severities_object.MISSING_CUNSTRUCTOR, severities_object.MODIFIER_LOOK_LIKE_SOL_KEYWORK,
    severities_object.MSGVALUE_INSIDE_LOOP, severities_object.OVERFLOW_ERC20_BALANCE, severities_object.UNPROTECTED_ECRECOVER_LEADING_RACE_CONDITION,
    severities_object.RACE_CONDITION_AT_CONTRACT_INIT, severities_object.REENTRANCY, severities_object.STORAGE_SIGNED_INTEGER_ARRAY, severities_object.UNCHECKED_TRANSFER,
    severities_object.UNPROTECTED_FUNCTIONS, severities_object.WEAK_PRNG, severities_object.DANGEROUS_ENUM_CONVERSION, severities_object.INCORRECT_ERC20_CONVERSION,
    severities_object.INCORRECT_ERC721_INTERFACE, severities_object.DANGEROUS_STRICT_EQUALITIES, severities_object.INCORRECT_ISCONTRACT_MODIFIER,
    severities_object.CONTRACTS_THAT_LOCKS_ETHER, severities_object.DELETION_ON_MAPPING_CONTAINING_STRUCT, 
    severities_object.STATE_VARIABLE_SHADOWING_FROM_ABSTRACT_CONTRACT, severities_object.TAUTOLOGICAL_COMPARE, severities_object.TAUTOLOGY_OR_CONTRADICTION,
    severities_object.WRITE_AFTER_WRITE, severities_object.INCORRECT_BALANCE_VALUE, severities_object.MISUSE_OF_BOOLEAN_CONSTANT,
    severities_object.CONSTANT_FUNCTIONS_USING_ASSEMBLY_CODE, severities_object.CONSTANT_FUNCTIONS_CHANGING_THE_STATE, severities_object.CONTROLLED_LOOP_ITERATION,
    severities_object.CONTROLLED_LOWLEVELCALL, severities_object.DIVIDE_BEFORE_MULTIPLY, severities_object.EMPTY_FUNCTIONS, severities_object.LACK_OF_MSGSENDER_USAGE,
    severities_object.MSGVALUE_USAGE_ON_NONPAYABLE_FUNCTIONS, severities_object.OVERFLOW_ERC20_ALLOWANCE, severities_object.ABSENCE_OF_PAUSABLE_MODIFIER,
    severities_object.REENTRANCY_VULNERABILITIES_1, severities_object.REUSED_BASE_CONSTRUCTORS, severities_object.DANGEROUS_USAGE_OF_TXGASPRICE,
    severities_object.DANGEROUS_USAGE_OF_TXORIGIN, severities_object.UNCHECKED_BLOCKHASH, severities_object.UNCHECKED_LOW_LEVEL_CALLS, severities_object.UNCHECKED_SEND,
    severities_object.UNINITIALIZED_LOCAL_VARIABLES, severities_object.UNINITIALIZED_RETURN_STATEMENTS, severities_object.UNSPECIFIED_OPERATION_ORDER, severities_object.UNUSED_EVENTS,
    severities_object.UNUSED_RETURN, severities_object.UNUSED_RETURN_INTERNAL, severities_object.DETECT_USE_AFTER_DELETE, severities_object.INCORRECT_MODIFIER,
    severities_object.BUILTIN_SYMBOL_SHADOWING, severities_object.LOCAL_VARIABLES_SHADOWING, severities_object.UNINITIALIZED_POINTERS_IN_CONSTRUCTORS, severities_object.PREDECLARATION_USAGE_OF_LOCAL_VARIABLES,
    severities_object.CALLS_INSIDE_LOOP, severities_object.MISSING_EVENTS_ACCESS_CONTROL, severities_object.MISSING_EVENTS_ARITHMETIC, severities_object.DANGEROUS_UNARY_EXPRESSIONS,
    severities_object.MISSING_ZERO_ADDRESS_VALIDATION, severities_object.REENTRANCY_VULNERABILITIES_2, severities_object.BLOCK_TIMESTAMP, severities_object.ASSEMBLY_USAGE, severities_object.ASSERT_STATE_CHANGE,
    severities_object.BOOLEAN_EQUALITY, severities_object.UNINDEXED_ERC20_EVENT_PARAMETERS, severities_object.LOW_LEVEL_CALLS, severities_object.MISSING_INHERITANCE, 
    severities_object.CONFORMANCE_TO_NAME_CONVENTIONS, severities_object.DIFFERENT_PRAGMA_DIRECTIVES_USED, severities_object.REDUNDANT_STATEMENTS, severities_object.INCORRECT_VERSIONS_OF_SOLIDITY,
    severities_object.UNINPLEMENTED_FUNCTIONS, severities_object.UNUSED_STATE_VARIABLE, severities_object.COSTLY_OPERATION_INSIDE_LOOP, severities_object.DEAD_CODE,
    severities_object.REENTRANCY_VULNERABILITIES_3, severities_object.REENTRANCY_VULNERABILITIES_4, severities_object.VARIABLE_NAMES_TO_SIMILAR, severities_object.TOO_MANY_DIGITS,
    severities_object.STATE_VARIABLES_THAT_COULD_BE_CONSTANT, severities_object.PUBLIC_FUNCTION_THAT_COULD_BE_EXTERNAL, vulnerabilities_object.BLOCKHASH_CURRENT]

# Opens the actual .txt file with analysis results
with open('slither_analysis.txt', 'r') as f1:
    first_line = f1.readline()
    first_line_list = list(first_line)
    contract_name = get_contract_name_from_line(first_line_list)

    # Add column for indicating if contract was analyzed or not (exception)
    vulnerabilities.append("ANALYZED")

    # Dictionary for counting vulnerability incidence
    # EXAMPLE:
    #  { 'vulnerability0': 0, 'vulnerability1': 0, ... ,'vulnerabilityN': 0}
    total_incidence_dic = dict(zip(vulnerabilities, [0] * 106))

    # Default as false
    total_incidence_dic["ANALYZED"] = "False"

    # Dictionary for containing contract name with each vulnerability and its incidence
    # EXAMPLE:
    #  {'example1.sol' : {'vulnerability0': 3, 'vulnerability1': 1, ..., 'vulnerabilityN': X}}
    #  {'example2.sol' : {'vulnerability0': 0, 'vulnerability1': 2, ..., 'vulnerabilityN': Y}}
    #  ...
    #  {'exampleN.sol' : {'vulnerability0': 1, 'vulnerability1': 0, ..., 'vulnerabilityN': Z}}
    contract_incidence_dic = {contract_name :  dict(zip(vulnerabilities, [0] * 106))}

    # counts the number of the contract analyzed
    counter = 1
    result = ""
    has_vulnerability = False
    for line in f1:
        if 'ANALYZED' in line:
            # print(f"{counter}) {contract_name}")
            # print(result)
            if counter > 1:
                contract_incidence_dic[contract_name] = dict(zip(vulnerabilities, [0] * 106))
                contract_incidence_dic[contract_name]["ANALYZED"] = "False"

            clean_contract_name = contract_name.replace("\n", "")
            if f"{clean_contract_name} analyzed" in result:
                contract_incidence_dic[contract_name]["ANALYZED"] = "True"
            
            for v in vulnerabilities:
                if(f"{scf.REFERENCE_URL}{v}" in result):
                    # print(f"\nABI encoder found in file number {counter} and name {contract_name}")
                    contract_incidence_dic[contract_name][v] += 1
                    total_incidence_dic[v] += 1
                    has_vulnerability = True

            first_line_list = list(line)
            contract_name = get_contract_name_from_line(first_line_list)
            result = ""
            counter += 1
            continue
        
        result += line

    # Generating .xlsx file
    workbook = xls.Workbook("slither_results.xlsx")
    worksheet = workbook.add_worksheet("Slither")

    # Fulffiling file
    work_line = 0
    work_column = 0
    contracts = list(contract_incidence_dic.keys())

    # Setting first cell (0,0)
    cell_format = workbook.add_format()
    cell_format.set_bg_color('black')
    worksheet.write(0, 0, "", cell_format)
    
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
                
                if s == "Informational":
                    cell_format.set_bg_color("blue")

                if s == "Optimization":
                    cell_format.set_bg_color("silver")

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
        worksheet.write(work_line, work_column, total_incidence_dic[v])
        work_column += 1

    workbook.close()
    f1.close()