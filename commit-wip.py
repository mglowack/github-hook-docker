from git import Repo

# tralala

repo = Repo('.')
msg = repo.head.reference.commit.message.strip()

if msg == "WIP":
    repo.git.commit('--amend', '--no-edit')
else:
    repo.git.commit('-m', 'WIP')
