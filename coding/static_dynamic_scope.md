## Static v.s. Dynamic Scope Exmaple

#### Example of static scope - C:
```c
#include<stdio.h>
int count = 10;
void func2(){
    printf("In func2=%d\n", count);
}
void func1(){
    int count=20;
    func2();
}
int main()
{
    func1();
    return 0;
}
```
Output:
```
In func2=10
```

#### Example of dynamic scope - Python
```py
count = 20

def func2():
    print("In func2=%d" % count)

def func1():
    count = 20
    func2()

def main():
    func1()
    return 0

if __name__== "__main__":
    main()
```

Output:
```
In func2=20
```

[Home](https://yang-zhang.github.io/)
