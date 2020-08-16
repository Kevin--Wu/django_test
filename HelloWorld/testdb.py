# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import TestTable
 
# 数据库操作
def testdb(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    listAll = TestTable.objects.all()
    
    # 输出所有数据
    szOutput = ""
    for DataObj in TestTable.objects.raw("SELECT * FROM TestModel_testtable"):
        szOutput += DataObj.name

    
    return HttpResponse("<p>" + szOutput + "</p>")