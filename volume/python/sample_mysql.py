#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 00:38:58 2020

@author: my-python

#https://www.mysqltutorial.org/python-mysql/python-mysql-blob/
"""

import pandas as pd
from sklearn import datasets
from sqlalchemy import create_engine, types

if __name__ == "__main__":
    
    #データを用意
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    
    #DB接続
    engine = create_engine("mysql://root:super@mysql/dbon")
    con = engine.connect()
    
    #新しいテーブルを作って上書き
    df.iloc[:100].to_sql('raw-data', con, index=False, if_exists='replace')
    
    #入っているデータを読み出し
    basedf = pd.read_sql_table('raw-data', con)
    
    #差分を書き込みの例
    pd.concat([df,basedf]).drop_duplicates(keep=False).to_sql('raw-data', con, index=False, if_exists='append')

    #空のデータベース書き込み例
    df2 = pd.DataFrame(index=range(5), columns=['Picture'])
    df2.index.name = 'id'
    df2.reset_index().to_sql('pic', con, index=False, if_exists='replace',
                              dtype={'id': types.BIGINT(),
                                    'Picture': types.BLOB(),
                                    }
                              )

    #１箇所を選択して更新
    connection = engine.raw_connection()
    cursor = connection.cursor()
    df.plot().get_figure().savefig('sample.png')
    with open('sample.png', 'rb') as image:
        imager = image.read()

    query = "UPDATE pic  SET Picture = %s WHERE id  = %s"
    args = (imager, 2)
    cursor.execute(query, args)
    connection.commit()
