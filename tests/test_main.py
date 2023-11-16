from action.main import get_param


def test_version():
    param = get_param()
    param.should.be.equal(42)
