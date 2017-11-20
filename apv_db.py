import pymysql
import prettytable
from functools import reduce

class APV_DB:
    
    """This module is responsible for querying the results of all apvs"""
    
    def __init__(self):
        
        """Starts the connection with the database"""
        
        self.db_connect = pymysql.connect("localhost","root","October2119981!fat","introse",autocommit=True)
        self.cursor = self.db_connect.cursor(pymysql.cursors.DictCursor)
        
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
    
# AUTOMATICALLY SORTED ALPHABETICALLY
#print(select_statement)
#cursor.execute(select_statement)#Execute
##print(cursor.fetchall())
#query_column_names = cursor.fetchall()
#
#column_names = ['Date','Particulars','APV no.']
#maxArrays = []
#
#maxString = '\tMAX(IF(type_name = \''
#maxString2 = ' \', type_value, NULL)) AS\''

#for i in query_column_names:
#    column_names.append(i['type_name'])
#    #print(i['type_name'])
#    typeString = maxString + i['type_name'] + maxString2 + i['type_name'] + '\',\n'
#    print(typeString)
#    maxArrays.append(typeString)

#column_names.append("CR")
#print(column_names) #FOR THE COLUMN NAMES
#
#select_statement = """SELECT
#\t DATE_FORMAT(vp.date,'%e-%M') AS Date ,
#\t vp.name as Particulars,
#\t ct.id_apv as 'APV no.',
#"""
#    
#temp = reduce(lambda x,y: x+y, maxArrays )
#select_statement += temp
    
#select_statement += """\tsum(type_value) as CR 
#FROM
#  credit_type as ct, `vouchers payable` as vp
#WHERE
#	ct.id_apv = vp.id_apv
#GROUP BY 3"""
#
#cursor.execute(select_statement)#Execute THE ACTUAL RESULTS
#apv_results = cursor.fetchall()


##DISPLAY USING A TABLE
#first = True
#for row in apv_results:
#    if first:
#        result_table = prettytable.PrettyTable(column_names)
#        result_table.align["Particulars"] = "l"
#        first = False
#        
#    row_data = []
#    for i in column_names:
#        if row[i] is not None:
#            row_data.append(row[i])
#        else:
#            row_data.append("")
#    result_table.add_row(row_data)
#
#print(result_table)
    
#ADD CLOUMN TO TABLE
#alter_statement = "ALTER TABLE `introse`.`vouchers payable` ADD COLUMN " +"`"+ Column_name +"`"+" FLOAT NULL DEFAULT '0';" #statement
#print(alter_statement) #check
#cursor.execute(alter_statement)#Execute

# disconnect from server
