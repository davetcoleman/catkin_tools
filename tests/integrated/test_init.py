import os
import shutil
import mock

from catkin_tools import config

from ..utils import assert_raises_regex
from ..utils import in_temporary_directory
from ..utils import redirected_stdio
from ..utils import run_and_succeed, run_and_fail
from ..utils import assert_warning_message
from ..utils import assert_no_warnings
from ..utils import assert_files_exist

@in_temporary_directory
def test_init_local_no_src():
    out = run_and_succeed(['catkin', 'init'])
    assert_warning_message(out, 'Source space .+ does not yet exist')
    assert_files_exist('.', ['.catkin_tools'])

@in_temporary_directory
def test_init_local_empty_src():
    cwd = os.getcwd()
    os.mkdir(os.path.join(cwd, 'src'))
    out = run_and_succeed(['catkin', 'init'])
    assert_no_warnings(out)
    assert_files_exist('.', ['.catkin_tools'])

