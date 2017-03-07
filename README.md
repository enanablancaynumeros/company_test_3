# Current architecture     
To update the graph got to `http://asciiflow.com/` copy this graph and load it there.


```
                                            +-----------------+
                                            |   Graphic UI    |
                                            |                 |
                                            +--------+--------+
                                                     |
                                                     |
                                                     |
                                                     |
                                                     |
                                                     |
                                                     |
                                             +-------+---------
                                             |                |
                                             |                |
                                             |    REST API    |
                                             |                |
                                             |                |
                                             +-------+--------+
                                             |       |
                                             |       |
+------------+      +--------------+         |       |
|            +------+   RabbitMQ   +---------+  +----+---+
|   Celery   |      +-------+------+            |        |
|    Beat    |              |                   |        |
|            |              |                   |        |
+------------+              |                   |        |
                       +----+----+              |Postgres|
                       |         |              |        |
                       | Celery  |              |        |
        +--------------+ Worker  |              |        |
        |              |         |              |        |
        |              +---------+              +--------+
        |
        |
    +---+------+
    | Minio    |
    | (Models  |
    | storage) |
    |          |
    +----------+

```


# Installation
If you are running on Ubuntu or similar just
run `make install_env` that will setup a new environment (qbe_batch) with all the dependencies,
otherwise have a look at the script and follow the steps you need.
It requires sudo permission to install the system libraries needed to install all the python libraries.

# Create and run the application in docker containers

Being on your environment (workon qbe_batch), needed to have docker-compose installed just
run `make run` and wait until it downloads all the docker images needed.
The application will be available in the port 80 of your localhost.
Have a look at the docker-compose file inside the docker folder to understand the different components
of the applications and why it is exposed in the port 80.
This will also run a sqlserver DB inside a docker container, simulating the EI DB.

# Run integrations tests in docker containers
`make integration_tests`

It will print out the different steps undertaken and will indicate the failures from a functional point of view of
the scenarios defined. Check the steps folder, under tests/features and the features files to understand what is being checked.
You will find the basic to extend any more scenarios you need to cover, using selenium to interact graphically with
the interface, or just at the HTTP API level.

# Run the application locally for debugging
Create one terminal and run `make run_local_api`
Set the traces wherever you want and restart to be able to use ipdb.


# Deployment
You can simulate the deployment by typing `make deploy_to_vagrant` which will bring up a virtual machine with CentOS 7,
using vagrant, to simulate the RedHat server. In the make it is indicating to deploy against the vagrant host.
To make the deployment to any other server available by ssh, or just locally, just change the host files or create another one
to point to the current machine if you can get to a server, git clone the repo and do make deploy.

The deployment is using dockerhub images, the login details are on the ansible scripts, under the common role.
Build the images locally after passing tests, run `make docker_push_and_tag` to push the images to dockerhub,
and then run `make deploy` again. The target machine will always pull the latest version of each docker image, with your code inside.
The only difference between the local run of the containers and the deployed version is the sqlserver DB. In the target system we are
expecting to have a SQLServer DB working with the configuration parameters defined in the ansible folder, under group_vars, according to the host/target
machine.

# How to update the machine learning models
The idea was to create a simple to maintain application, where non developers can update the models without digging into the code.
That is why we have minio as a storage solution for serialized models, so data scientist just need to train the model and a preprocessor, 
serialize the models using <a href="http://scikit-learn.org/stable/modules/model_persistence.html" target="_blank">joblib</a> which is part
of the sklearn library, and upload the file through the UI (url of the application, port 9000), replacing the existing model
and preprocessor as convenient. The current preprocessor is a <a href="http://scikit-learn.org/stable/modules/feature_extraction.html#loading-features-from-dicts" target="_blank">DictVectorizer</a>,
which uses one hot encoding for categorical variables. If any additional key is passed to the DictVectorizer will be ignored. Obviously, this
 preprocessor needs to be the same one used for the training stage, to respect the order of the features that the classifier expects.
 The initial preprocessor/model loaded in the solution, and the ones used for testing are under `tests/integration_data/` with the names
 `preprocessor.pkl` and `classifier.pkl`. Another assumption in this part is that the classifier is an xgboost model, so a DMatrix is used
  in the machine_learning.py module under `utils/utils`
 
 The rag status in this solution, or name of the class predicted in general, is done on the task code as serializing user defined code with Minio 
 introduces unnecessary complexity in the solution.

The SQL sentence that is retrieving the information from EI still has to be modified manually in the task code,
under `workers/task/update_records.py`. 

# How to add users
There is a file in `tests/integration_data/users.csv` which contains a set of underwriters valid for the system. Only the
underwriters on this file will have policies updates. This is due to an initial assumption that only an specific set of underwriters will
test the application and each of them will see only their policies. Unless this need to be changed to specific policies only, I don't suggest 
to change it. The emails have to be unique.# farfetch_test
