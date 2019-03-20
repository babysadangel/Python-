# -*-coding:utf-8 -*-

def name_string():
    str1 = 'hello ,world'
    return str1
    
if __name__ == "__main__":
    #计算len函数字符串长度
    print ('length=%d'% len(name_string()))
    #获取首字母大写
    print('capitalize=%s' %name_string().capitalize())
    #获取字符串变大写后copy
    print('upper=%s' % name_string().upper())
    #从字符串中查找子串的位子
    print('childstr=%s' % name_string().find('or'))
    #与find类似，但是找不到会引发异常
    print('inde=%ld'%name_string().index('or'))
    #检测字符串是否以指定字符串开头
    print('startwith=%s'%name_string().startswith('h'))
    #检测字符串是否以指定字符结尾
    print('endwith=%s'%name_string().endswith('d'))
    #将字符串以指定的宽度居中并在两侧填充指定的字符
    print('center=%s'%name_string().center(80,'*'))
    #将字符串以指定的宽度靠右放置右侧填充指定的字符
    print('rightriust=%s'%name_string().rjust(50,'*'))
    #从字符串中取出指定位子字符（下标运算）
    print('array=%s'%name_string()[2])
    