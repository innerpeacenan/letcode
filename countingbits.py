
import xlrd
import xlwt
from datetime import date,datetime

def read_excel():

  workbook = xlrd.open_workbook(r'F:\recorde.xls')  # the file need be counted
  # print workbook.sheet_names()
  sheet=workbook.sheet_by_index(0)
  print sheet.name
  print sheet.ncols
  print sheet.nrows
  a=[]
  cols=sheet.col_values(2)#col of name
  b=0#count total num
  f=open(r'F:\recorde.txt','w')
  for i in range(len(cols)):
      # print cols[i]
      if cols[i] not in a:
          a.append(cols[i])#if cols[i] not in a,append
          b=b+cols.count(cols[i])
          print cols[i]+":",cols.count(cols[i])#print the num cols show in cols
          line=cols[i]+":"+str(cols.count(cols[i]))+'\n'
          line=line.encode('utf-8')
          f.write(line)
  print b
  f.close()





if __name__ == '__main__':
  read_excel()