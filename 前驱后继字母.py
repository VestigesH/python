ch=input("请输入一个字母")
pre=ord('z')-(ord('z')-ord(ch)+1)%26
next=ord('a')+(ord(ch)-ord('a')+1)%26
print("%c的前驱字母是%c,后继字母是%c"%(ch,pre,next))
