import nox

nox.options.envdir = "build/nox"

@nox.session
def tests(session):
    session.install('pytest')
    session.run('pytest', 'proxy_for_interface')
