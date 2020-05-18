#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://www.mysqltutorial.org/python-mysql/python-mysql-blob/
"""
Created on Tue May 19 00:38:58 2020

@author: my-python
"""

import pandas as pd
from sklearn import datasets
from sqlalchemy import create_engine, types
    
if __name__ == "__main__":
    config = { 'host' : 'mysql',
               'user' : 'my-python',
               'password' : 'my-Password',
               'database' : 'dbon',
               'auth_plugin': 'mysql_native_password'
               }
    
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    
    engine = create_engine("mysql://root:super@mysql/dbon")
    con = engine.connect()
    df.to_sql('iris', con, index=False, if_exists='replace')
    
    df2 = pd.DataFrame(index=range(5), columns=['Picture'])
    df2.index.name='id'
    df2.reset_index().to_sql('pic', con, index=False, if_exists='replace',
                             dtype={'id': types.BIGINT(),
                                    'Picture':types.BLOB(),
                                    }
                             )
    
    connection = engine.raw_connection()
    cursor = connection.cursor();
    df.plot().get_figure().savefig('sample.png')
    with open('sample.png', 'rb') as image:
        imager = image.read()

    query = "UPDATE pic  SET Picture = %s WHERE id  = %s"
    args = (imager, 2)
    cursor.execute(query, args)
    connection.commit();

