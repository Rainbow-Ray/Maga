import os

# os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/spark-3.2.0-bin-hadoop2.7"
# Находим установку Spark
import findspark

findspark.init()
# Подключаем необходимые модули для работы со Spark из Python
from pyspark.sql import SparkSession

# Создаем сессию Spark на локальном компьютере
spark = SparkSession.builder.master("local[*]").getOrCreate()
