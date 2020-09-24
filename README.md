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

Additionally, the generated project contains a `.gitignore`, `.travis.yml`,
`.yamllint` and `build-requirements.txt` to perform CI/CD lint and ansible
checking of the project using [Travis] (once you commit the project to GitHub
and configure Travis accordingly).

## Creating an application
This is all down to cookiecutter. Once you've [installed] cookiecutter
you can prepare an application using this project's GitHub reference: -

    $ cookiecutter gh:informaticsmatters/cookiecutter-ansible-kubernetes \
        --overwrite-if-exists

The resultant project is created in the current directory, in a directory
named after your chosen **project_name**.

## Deploying the application
You'll probably want to adjust the application's role or templates before you
deploy it but, for the very simplest applications, you might be ready to go
straight away.
 
To run the produced playbook you will need suitable credentials for your
Kubernetes cluster that allow you to create namespaces and deploy all of
the objects. Set the cluster credentials using the environment variables
expected by the [k8s module], i.e.: -

    $ export K8S_AUTH_HOST=https://example.com
    $ export K8S_AUTH_API_KEY=000000
    $ export K8S_AUTH_VERIFY_SSL=no

Then, consider creating a virtual environment to deploy the application
using the project's generated requirements: -

    $ conda create -n $(basename $PWD) python=3.8
    [...]
    $ conda activate $(basename $PWD)
    $ pip install -r requirements.txt
    
Then run the project playbook...

    $ ansible-playbook site.yaml

## Un-deploying the application
Run the site playbook, setting your application's `state` variable to
`absent`. Depending on what you used for the cookiecutter **var_prefix**
this might be: -

    $ ansible-playbook site.yaml \
        -e ps_state=absent
    
---

[ansible]: https://github.com/ansible/ansible
[cookiecutter]: https://cookiecutter.readthedocs.io
[installed]: https://cookiecutter.readthedocs.io/en/1.7.2/installation.html
[k8s module]: https://docs.ansible.com/ansible/latest/modules/k8s_module.html
[travis]: https://travis-ci.com
