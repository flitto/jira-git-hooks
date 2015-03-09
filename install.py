#!/usr/bin/env python

# install pip install -r requirements.txt

from subprocess import Popen, PIPE
import sys
import os

def main():
  username = raw_input('Enter Your Jira username(ex: jays.woo) :')
  password = raw_input('Enter Your Jira password :')
  weburl = raw_input('Enter Your Jira web url (ex: http://name.atlassian.net) :')

  Popen(['git', 'config', '--global', 'jira.username', username])
  Popen(['git', 'config', '--global', 'jira.password', password])
  Popen(['git', 'config', '--global', 'jira.weburl', weburl])
 
  use_post_checkout_hook  = (raw_input('use post-checkout hook? (Y | N)').upper() == 'Y') if True else False
  use_post_commit_hook  = (raw_input('use post-commit hook? (Y | N)').upper() == 'Y') if True else False

  project_dir = raw_input('Enter your jira-project git repository full path:')
  copyHooks(project_dir, use_post_commit_hook, use_post_checkout_hook)

def copyHooks(project_dir, use_post_commit_hook, use_post_checkout_hook):
  post_checkout = '.git/hooks/post-checkout'
  post_commit = '.git/hooks/post-commit'
  if use_post_commit_hook:
    Popen(['cp', '-f', './jira-git-hooks', (project_dir) + '/' + post_commit])
  if use_post_checkout_hook:
    Popen(['cp', '-f', './jira-git-hooks', (project_dir) + '/' + post_checkout])


if __name__ == '__main__':
  main()
