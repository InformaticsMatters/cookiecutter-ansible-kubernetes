# A "cookiecutter" for Ansible Kubernetes projects

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/informaticsmatters/cookiecutter-ansible-kubernetes)

[![CodeFactor](https://www.codefactor.io/repository/github/informaticsmatters/cookiecutter-ansible-kubernetes/badge)](https://www.codefactor.io/repository/github/informaticsmatters/cookiecutter-ansible-kubernetes)

A [cookiecutter] template repository to create projects that contain an
[Ansible] **playbook** (and a **role**) using the built-in [k8s module]
to to deploy container images as Kubernetes applications.

Guided cookiecutter questions enable you to create a pre-formatted project
that can be a Kubernetes **CronJob**, **DaemonSet**, **Deployment**, **Job** or
**StatefulSet**. You can also decide whether you want to get started with
a **PVC** (attached to the application container) and an example **Secret** and
**ConfigMap**.

The cookiecutter wraps this up with a playbook and an associated role with
pre-formatted variables defined in `defaults` and `vars` along with a series of
`tasks` to flexibly deploy the application and all its components from the
kubernetes `templates` that it creates. This is finished-off
with root-level `requirements.txt`, `site.yaml`, `inventory.yaml` and
`ansible.cfg` so you can deploy the application *out-of-the-box*.

Additionally, the generated project contains a `.gitignore`, `workflows`,
`.yamllint` and `build-requirements.txt` to perform CI/CD lint and ansible
checking of the project using GitHub Actions (once you commit the project to GitHub).

## Creating an application
This is all down to cookiecutter. Once you've installed cookiecutter
you can prepare an application using this project's GitHub reference.

>   Importantly **YOU DO NOT NEED TO CLONE THIS REPOSITORY** to use the cookiecutter.
    The cookiecutter will clone and use the repository for you.

Consider creating a virtual environment to run the cookie-cutter and then run it
from a directory where you want your kubernetes-based Ansible project to be created.
You will eventually commit the project you create to GitHub.

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install --upgrade pip
    
    $ pip install cookiecutter==2.*

    $ cd ~/Code
    $ cookiecutter gh:informaticsmatters/cookiecutter-ansible-kubernetes

The resultant project is created in the current directory, in a directory
named after your chosen **project_name**.

## Deploying the application
You'll probably want to adjust the application's role or templates before you
deploy it but, for the very simplest applications, you might be ready to go
straight away.
 
To run the produced playbook you will need a suitable `KUBECONFIG` for your
Kubernetes cluster that allows you to create namespaces and deploy all of
the objects: -

    $ export KUBECONFIG=~/k8s-config/config-local

Then, consider creating a virtual environment to deploy the application
using the project's generated requirements: -

    $ pip install ansible==8.*
    
Then run the `site.yaml` playbook in the project's directory...

    $ cd <project_name>
    $ ansible-playbook site.yaml

## Un-deploying the application
Run the site playbook, setting your application's `state` variable to
`absent`. Depending on what you used for the cookiecutter **var_prefix**
this might be: -

    $ ansible-playbook site.yaml -e ps_state=absent
    
---

[ansible]: https://github.com/ansible/ansible
[cookiecutter]: https://cookiecutter.readthedocs.io
