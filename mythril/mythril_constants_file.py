class VulnerabiltiiesSWC:
    DELEGATECALL_UNTRUSTED_CALLE = "112"
    WEAK_RANDOMNESS = "120"
    TIMESTAMP_DEPENDENCE = "116"
    UNPROTECTED_ETHER_WITHDRAW = "110"
    EXTERNAL_CALLS = "117"
    INTEGER_OVERFLOW_UNDERFLOW = "101"
    DOS_WITH_FAILED_CALL = "113"
    UNPROTECTED_SELFDESCTRUCT = "106"
    REENTRANCY = "107"
    UNCHECKED_CALL_RETURN_VALUE = "104"
    ASSERT_VIOLATION = "110"
    ARBITRATY_STORAGE = "124"
    ARBITRARY_JUMP = "127"
    TX_ORIGIN_USAGE = "115"

class VulnerabilitySeverities:
    DELEGATECALL_UNTRUSTED_CALLE = "High"
    WEAK_RANDOMNESS = "Low"
    TIMESTAMP_DEPENDENCE = "Low"
    UNPROTECTED_ETHER_WITHDRAW = "High"
    EXTERNAL_CALLS = "Low"
    INTEGER_OVERFLOW_UNDERFLOW = "High"
    DOS_WITH_FAILED_CALL = "Low"
    UNPROTECTED_SELFDESCTRUCT = "High"
    REENTRANCY = "Medium"
    UNCHECKED_CALL_RETURN_VALUE = "Medium"
    ASSERT_VIOLATION = "Medium"
    ARBITRATY_STORAGE = "High"
    ARBITRARY_JUMP = "High"
    TX_ORIGIN_USAGE = "Low"

class VulnerabilityNames:
    DELEGATECALL_UNTRUSTED_CALLE = "delegate_untrusted_calle"
    WEAK_RANDOMNESS = "weak_randomness"
    TIMESTAMP_DEPENDENCE = "timestamp_dependence"
    UNPROTECTED_ETHER_WITHDRAW = "unprotected_ether_withdraw"
    EXTERNAL_CALLS = "reentrancy-0"
    INTEGER_OVERFLOW_UNDERFLOW = "interger_overflow_underflow"
    DOS_WITH_FAILED_CALL = "dos_attack"
    UNPROTECTED_SELFDESCTRUCT = "unprotected_selfdestruct"
    REENTRANCY = "reentrancy-1"
    UNCHECKED_CALL_RETURN_VALUE = "unchecked_call_return_value"
    ASSERT_VIOLATION = "assert_violation"
    ARBITRATY_STORAGE = "arbitrary_storage"
    ARBITRARY_JUMP = "arbitrary_jump"
    TX_ORIGIN_USAGE = "tx_origin_usage"