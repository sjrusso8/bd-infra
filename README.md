# Big Data Hadoop Environment

Leveraging the repo from [m-semnani/bd-infra](https://github.com/m-semnani/bd-infra) and his blog post in [this article](https://itnext.io/creating-a-big-data-development-platform-using-docker-compose-892f7f4da738). 

This repo allows you to deploy a whole big data infrastructure with just docker-compose. In this platform, you will have HDFS, Hive, Spark, Hue, Zeppelin, Kafka, Zookeeper, and Streamsets connected together.

Just run `docker-compose up` and enjoy!

## Additional Details

- Issue with exited containers. Just restart the container *database*, and then the other containers.
- Zeppelin might not run because it needs a newer version of Java
- Run `apt-get update` on the datanode and then `apt-get install vim`

## Running MapReduce Jobs

I use a local python environment to simulate the MapReduce jobs over the data under the *bank* folder.

Count ages of people in the dataset with MapReduce!

> python ./mapreduce/SimpleMapReduce.py ./bank/bank-full.csv
