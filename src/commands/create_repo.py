from src.commands.abstract_git_command import AbstractGitCommand


class CreateRepo(AbstractGitCommand):
    def __init__(self, remote_url, repo_name, branch):
        super().__init__()
        self.remote = remote_url
        self.repo = repo_name
        self.branch = branch

    def buildCommand(self):
        super().add('push').add('--set-upstream').add(self.remote +
                                                      self.repo + '.git').add(self.branch)
