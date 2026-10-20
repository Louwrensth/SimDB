import pytest
from click.testing import CliRunner
from utils import config_test_file

from simdb.cli.simdb import cli


@pytest.mark.parametrize("command", ["alias", "provenance"])
def test_removed_commands(command):
    config_file = config_test_file()
    runner = CliRunner()
    result = runner.invoke(cli, [f"--config-file={config_file}", command])
    assert result.exit_code == 2
    assert "No such command" in result.output
