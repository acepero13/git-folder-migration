from commands.git.abstract_git_command import AbstractGitCommand


class CreateRepo(AbstractGitCommand):
    def __init__(self, shell, remote_url, repo_name, branch):
        super().__init__(shell)
        self.remote = remote_url
        self.repo = repo_name
        self.branch = branch

    def build_command(self):
        super().add('push').add('--set-upstream').add(self.remote +
                                                      self.repo + '.git').add(self.branch)
