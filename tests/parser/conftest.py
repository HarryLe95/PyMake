import pytest
import yaml

from PyMake.builder.var.section import VarSection
from PyMake.parser.parser import VarParser


########################################### PARSER 1 TEST ITEMS ########################################################
@pytest.fixture(scope="function")
def parser1() -> VarParser:
    data = """
    basic:
        var1: 100
        var2: 100
        var3: 100
    """
    data = yaml.safe_load(data)
    section = VarSection(data)
    yield section.build()


@pytest.fixture(scope="function")
def valid_parser1_input1():
    return {
        "args": "1 2 3",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input2():
    return {
        "args": "1 2 --var3 3",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input3():
    return {
        "args": "1 --var3 3 --var2 2",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input4():
    return {
        "args": "--var1 1 --var2 2 --var3 3",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input5():
    return {
        "args": "--var1 1 --var3 3 --var2 2",
        "namespace": {"var1": "1", "var2": "2", "var3": "3"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input6():
    return {
        "args": "--var1 1 --var2 2",
        "namespace": {"var1": "1", "var2": "2", "var3": "100"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input7():
    return {
        "args": "--var1 1 --var3 3",
        "namespace": {"var1": "1", "var2": "100", "var3": "3"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input8():
    return {
        "args": "--var1 1",
        "namespace": {"var1": "1", "var2": "100", "var3": "100"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input9():
    return {
        "args": "--var3 3",
        "namespace": {"var1": "100", "var2": "100", "var3": "3"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input10():
    return {
        "args": "",
        "namespace": {"var1": "100", "var2": "100", "var3": "100"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input11():
    return {
        "args": "1",
        "namespace": {"var1": "1", "var2": "100", "var3": "100"}
    }


@pytest.fixture(scope="function")
def valid_parser1_input12():
    return {
        "args": "1 2",
        "namespace": {"var1": "1", "var2": "2", "var3": "100"}
    }


@pytest.fixture(scope="function")
def invalid_parser1_undefined_variable_1():
    return {
        "args": "--var 1 2",
    }


@pytest.fixture(scope="function")
def invalid_parser1_undefined_variable_2():
    return {
        "args": "--var1 2 --var4",
    }


@pytest.fixture(scope="function")
def invalid_parser1_undefined_variable_3():
    return {
        "args": "--flag1",
    }


@pytest.fixture(scope="function")
def invalid_parser1_undefined_variable_4():
    return {
        "args": "--sequence1 1 2 3 4",
    }


@pytest.fixture(scope="function")
def invalid_parser1_invalid_value_1():
    return {
        "args": "--var1 2 3",
    }


@pytest.fixture(scope="function")
def invalid_parser1_invalid_value_2():
    return {
        "args": "1 --var2 2 3",
    }


@pytest.fixture(scope="function")
def invalid_parser1_variable_redefinition_1():
    return {
        "args": "1 --var1 2",
    }


@pytest.fixture(scope="function")
def invalid_parser1_variable_redefinition_2():
    return {
        "args": "--var1 1 --var1 2",
    }


########################################### PARSER 2 TEST ITEMS ########################################################
@pytest.fixture(scope="function")
def parser2() -> VarParser:
    data = """
    basic:
        var1: 100
        var2: REQUIRED
        var3: 100
    flag: 
        flag1: "-A"
    sequence:
        seq1: [1,2,3,4,5]
    """
    data = yaml.safe_load(data)
    section = VarSection(data)
    yield section.build()

@pytest.fixture(scope="function")
def valid_parser2_input1():
    return {
        "args": "1 2 3",
        "namespace": {"var1": "1", "var2": "2", "var3": "3", "seq1": "1 2 3 4 5"}
    }