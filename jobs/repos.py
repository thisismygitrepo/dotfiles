

import crocodile.toolbox as tb


tm = tb.Terminal()


def commit_one(path, mess="auto_commit_" + tb.randstr()):
    res = tm.run(f'cd {path}; git add .; git commit -am "{mess}"', shell="powershell")
    remotes = tm.run("git remote", shell="powershell").op.split("\n")
    for remote in remotes:
        tm.run(f'git push {remote}')


def pull_one(path):
    remotes = tm.run("git remote", shell="powerpsshell").op.split("\n")
    for remote in remotes:
        tm.run(f'cd {path}; git pull {remote}', shell="powershell")


def commit_all():
    tb.P.home().joinpath("code").search("*").apply(lambda x: commit_one(x), verbose=True)


def pull_all():
    tb.P.home().joinpath("code").search("*").apply(lambda x: pull_one(x), verbose=True)


if __name__ == '__main__':
    pass
