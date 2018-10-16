from django.shortcuts import render,redirect,reverse
from django.db import connection
# Create your views here.
def get_corsor():
    return connection.cursor()

def add_book(requset):
    if requset.method=='GET':
        return render(requset,'add_book.html')
    else:
        name=requset.POST.get("name")
        author=requset.POST.get("author")
        cursor=get_corsor()
        cursor.execute("insert into book(id,name,author) value(null ,'%s','%s')"%(name,author))
        return redirect(reverse('index'))

def book_detail(requset,book_id):
    cursor=get_corsor()
    cursor.execute("select id,name,author from book where id=%s"%book_id)
    book=cursor.fetchone()
    return render(requset,'book_detail.html',context={"book":book})

def delete_book(requset):
    if requset.method =='POST':
        book_id=requset.POST.get('book_id')
        cursor=get_corsor()
        cursor.execute("delete from book where id=%s"%book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError("删除图书错误")