# Spark 2.0.2 Setup Steps on CentOS
# Preinstallation Check versions of OS, Java, and python

# 1. OS Version Centos 7+ 
rpm --query centos-release

# 2. Python version 2.7+ 
python -v

# 3. Java version 1.7+
java -version

# Download latest spark .tgz installation file and decompress 
tar xvzf spark-2.0.2-bin-hadoop2.7.tgz

# set enviroment variables
export SPARK_HOME=${INSTALL_DIR}/spark-2.0.2-bin-hadoop2.7
export PATH=${SPARK_HOME}/bin:$PATH

# Run pyspark
pyspark
