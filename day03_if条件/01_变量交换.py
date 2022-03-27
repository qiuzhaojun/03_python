"""
    变量交换算法
        a,b = b,a
"""
bridegroom_name = "武大郎"
bride_name = "潘金莲"
# 变量交换原理：借助第三方变量
# temp = bridegroom_name
# bridegroom_name = bride_name
# bride_name = temp
# python变量交换：a,b = b,a
bridegroom_name, bride_name = bride_name, bridegroom_name

print("交换后的新郎：" + bridegroom_name)  #
print("交换后的新娘：" + bride_name)  #
