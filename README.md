# A "cookiecutter" for Ansible Kubernetes projects

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/informaticsmatters/cookiecutter-ansible-kubernetes)

A [cookiecutter] template repository to create projects that contain an
[Ansible] **playbook** (and a **role**) using the built-in **k8s** module
to kick-start the deployment of a Kubernetes application.

Use this cookiecutter to quickly *template* new Kubernetes application
projects. The cookiecutter produces a playbook and an associated role with some
preset variables defined in `defaults` and `vars` along with a series of
`tasks` to deploy the application and all its components from the kubernetes
`templates` that are also created for you.

Answer the cookiecutter questions to create a pre-formatted project
for the deployment of a container image application. the application can be
a **CronJob**, **Deployment**, **Job** or **StatefulSet**. You can also decide
whether you want to get started with a **PVC** (attached to the application)
and an example **Secret** and **ConfigMap**.

Additionally, the generated project contains a `.travis.yml`
to perform lint and ansible checking of the project.

## Creating an application
This is all down to [cookiecutter]. Once you've installed cookiecutter
you can prepare an application using this project's GitHub reference and then
answer the prompted questions: -

    $ cookiecutter gh:informaticsmatters/cookiecutter-ansible-kubernetes

The project is created in the current directory will be called after your
chosen **project_name**, e.g. `{{ project_name }}-ansible`.

## Deploying the application
You might need to adjust the application's role before you can deploy it
but, for the very simplest applications, you should be ready to go
straight out-of-the-box.
 
To run the produced playbook you need suitable credentials for your Kubernetes
cluster, made available through some standard environment variables: -

    $ export K8S_AUTH_HOST=https://example.com
    $ export K8S_AUTH_API_KEY=000000
    $ export K8S_AUTH_VERIFY_SSL=no

Then, consider creating a virtual environment to deploy the application
using the generated requirements: -

    $ conda create -n $(basename $PWD) python=3.8
    [...]
    $ conda activate $(basename $PWD)
    $ pip install -r requirements.txt
    
Then run the main playbook from the produced directory...

    $ ansible-playbook site.yaml

## Un-deploying the application
Run the site playbook, setting your application's `state` variable to
`absent`. For the built-in application this would be: -

    $ ansible-playbook site.yaml \
        -e ps_state=absent
    
---

[ansible]: https://github.com/ansible/ansible
[cookiecutter]: https://cookiecutter.readthedocs.io
