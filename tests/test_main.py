from action.main import get_version
from action.__version__ import __version__


def test_version():
    version = get_version()
    version.should.be.equal(__version__)
