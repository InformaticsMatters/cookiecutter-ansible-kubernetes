#!/usr/bin/env python

import os
import re
from pathlib import Path

# It's easier to let cookiecutter render the files
# and then remove those that the user doesn't want.
# Optionally including and excluding files
# during the rendering process isn't
# the way to do things.


def delete_template_file(filename):
    os.remove(os.path.join('roles',
                           '{{cookiecutter.role_name|lower}}',
                           'templates',
                           filename + '.yaml.j2'))


# Remove rendered files that the user doesn't want...

if '{{cookiecutter.add_service|lower}}' in ['n']:
    delete_template_file('service')

if '{{cookiecutter.add_ingress|lower}}' in ['n']:
    delete_template_file('ingress')
    delete_template_file('rolebinding-default-sa')

if '{{cookiecutter.add_pvc|lower}}' in ['n']:
    delete_template_file('pvc')

if '{{cookiecutter.add_configmap|lower}}' in ['n']:
    delete_template_file('configmap')

if '{{cookiecutter.add_secret|lower}}' in ['n']:
    delete_template_file('secret')

# Can only be one of deployment, job, statefulset etc.
# Delete files that don't apply...

if '{{cookiecutter.kind}}' == 'cronjob':
    for basename in ['deployment', 'daemonset', 'job', 'statefulset']:
        delete_template_file(basename)
elif '{{cookiecutter.kind}}' == 'daemonset':
    for basename in ['cronjob', 'deployment', 'job', 'statefulset']:
        delete_template_file(basename)
elif '{{cookiecutter.kind}}' == 'deployment':
    for basename in ['cronjob', 'daemonset', 'job', 'statefulset']:
        delete_template_file(basename)
elif '{{cookiecutter.kind}}' == 'job':
    for basename in ['cronjob', 'daemonset', 'deployment', 'statefulset']:
        delete_template_file(basename)
elif '{{cookiecutter.kind}}' == 'statefulset':
    for basename in ['cronjob', 'daemonset', 'deployment', 'job']:
        delete_template_file(basename)

# Now remove consecutive blank lines from all the files in 'roles'...
#
# A recurring problem with jinja2 and not being able to control it
# with 'trim_blocks' until cookiecutter 2.x.
# See https://github.com/cookiecutter/cookiecutter/issues/704
#
# For now this snippet replaces every file with one where multiple blank
# lines are replaced by one...

for path in Path('roles').glob('**/*'):
    if os.path.isfile(path):
        with open(path, 'rt') as source_file:
            path_contents = source_file.read()
        path_contents = re.sub('\n\n\n+', '\n\n', path_contents)
        with open(path, 'wt') as source_file:
            source_file.write(path_contents.strip() + '\n')
