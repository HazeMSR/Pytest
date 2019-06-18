# Possible exit codes

#Exit code 0:	All tests were collected and passed successfully
#Exit code 1:	Tests were collected and run but some of the tests failed
#Exit code 2:	Test execution was interrupted by the user
#Exit code 3:	Internal error happened while executing tests
#Exit code 4:	pytest command line usage error
#Exit code 5:	No tests were collected 


# Help 
pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options 

# Stopping after failure(s)
pytest -x            # stop after first failure
pytest --maxfail=2    # stop after two failures 

# Specifying tests
pytest test_mod.py # Run test in a module
pytest testing/ # Run test in a directory
pytest -k "MyClass and not method" # Run tests by keywords expression

# Run tests by node ids
pytest test_mod.py::test_func
pytest test_mod.py::TestClass::test_method 

# Run tests by mark expression
pytest -m slow # Run test decorated with the @pytest.mark.slow decorator

# Run tests from packages
pytest --pyargs pkg.testing

# Modifying Python traceback printing
pytest --showlocals # show local variables in tracebacks
pytest -l           # show local variables (shortcut)

pytest --tb=auto    # (default) 'long' tracebacks for the first and last
                     # entry, but 'short' style for the other entries
pytest --tb=long    # exhaustive, informative traceback formatting
pytest --tb=short   # shorter traceback format
pytest --tb=line    # only one line per failure
pytest --tb=native  # Python standard library formatting
pytest --tb=no      # no traceback at all

# Debugg
pytest --pdb # allows one to drop into the PDB prompt via a command line option
pytest -x --pdb   # drop to PDB on first failure, then end test session
pytest --pdb --maxfail=3  # drop to PDB for first three failures<Paste>
pytest --trace # allows one to drop into the PDB prompt immediately at the start of each test via a command line option

# >>> import sys
# >>> sys.last_traceback.tb_lineno
# 42
# >>> sys.last_value
# AssertionError('assert result == "ok"',)

# Profiling test execution duration
pytest --durations=10 # get a list of the slowest 10 test durations

# Creating resultlog format files 
pytest --resultlog=path # To create plain-text machine-readable result files 

# Sending test report to online pastebin service
pytest --pastebin=failed # Creating a URL for each test failure
pytest --pastebin=all # Creating a URL for a whole test session log
#Currently only pasting to the http://bpaste.net service is implemented.

# Early loading plugins
pytest -p mypluginmodule # You can early-load plugins (internal and external) explicitly in the command-line

# Disabling plugins
pytest -p no:doctest # To disable loading specific plugins at invocation time

