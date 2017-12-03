import pymysql
import prettytable
from functools import reduce

class APV_DB:
    
    """This module is responsible for querying the results of all apvs"""
    
    def __init__(self):
        
        """Starts the connection with the database"""
        
        self.db_connect = pymysql.connect("localhost","root","p@ssword","introse",autocommit=True)
        self.cursor = self.db_connect.cursor(pymysql.cursors.DictCursor)
        self.get_column_names()
        self.initialize_columns()
        
        temp = self.get_apv()
        #print(temp)
        print(self.get_apv_table(temp))
        self.close_database()
        
    def get_column_names(self):
        
        """Gets the column names from the database"""
        
        self.maxArrays = []
        self.select_statement = """SELECT type_name
                                FROM
                                  credit_type
                                GROUP BY
                                 type_name
                                """
        self.cursor.execute(self.select_statement)
        self.db_column_names = self.cursor.fetchall()
        self.column_names = ['Date','Particulars','APV no.']
        self.maxString = '\tMAX(IF(type_name = \''
        self.maxString2 = ' \', type_value, NULL)) AS\''
        
    def initialize_columns(self):
        
        """Initializes the columns for the main query"""
        
        for i in self.db_column_names:
            self.column_names.append(i['type_name'])
            typeString = self.maxString + i['type_name'] + self.maxString2 + i['type_name'] + '\',\n'
            self.maxArrays.append(typeString)
        self.column_names.append("CR")
    
    def get_apv(self):
        
        """Returns all of the APV
        
        Returns:
            [self.cursor.fetchall()]
        
        """
        
        self.select_statement = """SELECT
                                \t DATE_FORMAT(vp.date,'%e-%M') AS Date ,
                                \t vp.name as Particulars,
                                \t ct.id_apv as 'APV no.',
                                """
        temp = reduce(lambda x,y: x+y, self.maxArrays )
        self.select_statement += temp
        self.select_statement += """\tsum(type_value) as CR 
                                FROM
                                  credit_type as ct, `vouchers payable` as vp
                                WHERE
                                    ct.id_apv = vp.id_apv
                                GROUP BY 3"""
        self.cursor.execute(self.select_statement)#Execute THE ACTUAL RESULTS
        return self.cursor.fetchall()

    def get_apv_table(self,apv_results):
        
        """Returns the APV as a table
        
        Args:
            apv_result ({}): the resulting APV
        Returns:
            [result_table]
        
        """
        
        first = True
        for row in apv_results:
            if first:
                result_table = prettytable.PrettyTable(self.column_names)
                result_table.align["Particulars"] = "l"
                first = False

            row_data = []
            for i in self.column_names:
                if row[i] is not None:
                    row_data.append(row[i])
                else:
                    row_data.append("")
            result_table.add_row(row_data) 
            
        return result_table
    
    def close_database(self):
        
        """Ends the connection with the database"""
        
        self.db_connect.close()
        
        
        
if __name__ == "__main__":
    app = APV_DB()

