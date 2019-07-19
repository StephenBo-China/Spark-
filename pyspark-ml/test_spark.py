
import os
import sys
 
#下面这些目录都是你自己机器的Spark安装目录和Java安装目录
os.environ['SPARK_HOME'] = "/Users/qudian/spark-2.4.3-bin-hadoop2.7/"
 
sys.path.append("/Users/qudian/spark-2.4.3-bin-hadoop2.7/bin")
sys.path.append("/Users/qudian/spark-2.4.3-bin-hadoop2.7/python")
sys.path.append("/Users/qudian/spark-2.4.3-bin-hadoop2.7/python/pyspark")
sys.path.append("/Users/qudian/spark-2.4.3-bin-hadoop2.7/python/lib")
sys.path.append("/Users/qudian/spark-2.4.3-bin-hadoop2.7/python/lib/pyspark.zip")
sys.path.append("/Users/qudian/spark-2.4.3-bin-hadoop2.7/lib/py4j-0.9-src.zip")
# sys.path.append("/Library/Java/JavaVirtualMachines/jdk1.8.0_144.jdk/Contents/Home")
os.environ['JAVA_HOME'] = "/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home"
 
from pyspark import SparkContext
from pyspark import SparkConf
 
 
sc = SparkContext("local","testing")
 
print (sc.version)
print ('hello world!!')


from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as func
import pyspark.ml.feature as ft

from svm_predict import SVMPredict



def skl_predict(spark): 

    print (1111)
    
    
    data = [(list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 1])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0])),
        (list([-0.7016797, 1.22524766, -0.7123829, -0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101,-0.6565101, 0]))
        ]
    labels = ['_1', '_2', '_3', '_4','_5','_6','_7','_8','_9','_10','_11','_12','_13','_14','_15','_16','_17','_18','_19','_20','_21','_22','_23','_24','_25','_26','_27','_28','_29','_30', 'INFANT_ALIVE_AT_REPORT']
    df = spark.createDataFrame(data, schema = labels)

    # df = df.withColumn( "age", df['age']+1 ) 
    df.show()
    # df.select("age").distinct().show() 
    # df.count()

    # 列数据合并
    from pyspark.sql.functions import split, explode, concat, concat_ws
    df_concat = df.withColumn("_concat", concat(df['_1'], df['_2'], df['_3'], df['_4']))
    print ('df_concat>>>>>>>>>>>>>>>>>>>')
    df_concat.show()


    # 将所有的特征整和到一起
    featuresCreator = ft.VectorAssembler( inputCols=[ col for col in labels], outputCol='features' )


    # 创建评估器
    import pyspark.ml.classification as cl
    logistic = cl.LogisticRegression(
        maxIter=10, 
        regParam=0.01, 
        labelCol='INFANT_ALIVE_AT_REPORT')
    print ('logistic:', logistic)


    # 创建一个管道
    from pyspark.ml import Pipeline
    
    pipeline = Pipeline(stages=[
            featuresCreator, 
            logistic
        ])

    # fit 
    births_train, births_test = df.randomSplit([0.7, 0.3], seed=666)

    print ('births_train', births_train)
    print ( 'births_test', births_test )

    # 运行管道，评估模型。
    model = pipeline.fit(births_train)
    test_model = model.transform(births_test)

    print ('test_model:', test_model) 

    
    test_model.take(1)

    print ('test_model.take(1):', test_model.take(1))






    '''
    # prepare the UDFs
    getValue = func.udf( 
        lambda dd: 
            SVMPredict.predict(
                dd
            )
        )
    '''




def geoEncode(spark):
    # read the data in
    uber = spark.read.csv(
        'uber_data_nyc_2016-06_3m_partitioned.csv', 
        header=True, 
        inferSchema=True
        )\
        .repartition(4) \
        # .select('VendorID','tpep_pickup_datetime', 'pickup_longitude', 'pickup_latitude','dropoff_longitude','dropoff_latitude','total_amount')

    # prepare the UDFs
    getDistance = func.udf(
        lambda lat1, long1, lat2, long2: 
            geo.calculateDistance(
                (lat1, long1),
                (lat2, long2)
            )
        )

    convertMiles = func.udf(lambda m: 
        metricImperial.convert(str(m) + ' mile', 'km'))

    # create new columns
    uber = uber.withColumn(
        'miles', 
            getDistance(
                func.col('pickup_latitude'),
                func.col('pickup_longitude'), 
                func.col('dropoff_latitude'), 
                func.col('dropoff_longitude')
            )
        )

    uber = uber.withColumn(
        'kilometers', 
        convertMiles(func.col('miles')))

    # print 10 rows
    # uber.show(10)

    # save to csv (partitioned)
    uber.write.csv(
        'uber_data_nyc_2016-06_new.csv',
        mode='overwrite',
        header=True,
        compression='gzip'
    )




if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName('CalculatingGeoDistances') \
        .getOrCreate()

    print('Session created')


    skl_predict(spark) 
  
    '''
    try:
        skl_predict(spark)

    finally:
        skl_predict.stop()
    '''


