# cookiecutter-ansible-kubernetes
A [cookiecutter] template repository to create our style of AWX-compliant
repositories - repositories that contain a playbook (and a role) to deploy a
Kubernetes application.

Use this cookiecutter to quickly *template* new Kubernetes application projects
. The cookiecutter produces an Ansible playbook and associated role with some
preset variables defined in `defaults` and `vars` along with a series of
`tasks` to deploy the application and all its components from Ansible
`templates` that are also created for you.
        
Answer the cookiecutter questions to create pre-formatted templates
for the deployment of a container image application that can be a **CronJob**,
**Deployment**, **Job** or **StatefulSet**. You can also decide whether you
want to get started with a **PVC** (attached to the application) and an
example **Secret** and **ConfigMap**.

Additionally, the generated project contains a `.travis.yml`
to perform lint and ansible checking of the project.

## Creating an application
This is all down to [cookiecutter]. Once you;ve installed cookiecutter
you can prepare an application using this project's GitHub reference: -

    $ cookiecutter gh:informaticsmatters/cookiecutter-ansible-kubernetes
    
## Deploying the application
You might need to adjust the application's role before you can deploy it
but you might, for the very simplest applications, be ready to go
straight out-of-the-box.
 
To run the playbook you need suitable credentials for your Kubernetes cluster,
made available through some standard environment variables: -

    $ export K8S_AUTH_HOST=https://example.com
    $ export K8S_AUTH_API_KEY=000000

Then, run the main playbook...

    $ andible-playbook site.yaml
        
---

[cookiecutter]: https://cookiecutter.readthedocs.io
