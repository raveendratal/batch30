# Databricks notebook source
# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

# MAGIC %fs ls /databricks-datasets/asa/airlines

# COMMAND ----------

# MAGIC %python 
# MAGIC df = spark.read.csv("/databricks-datasets/asa/airlines",header=True)
# MAGIC df.count()

# COMMAND ----------

