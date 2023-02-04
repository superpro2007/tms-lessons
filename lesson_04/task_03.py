# Перепишите алгоритм починки (со слайда про вложенные инструкции) без вложенных инструкций if.

moving = input("is it moving?\n")
should = input("should it?\n")

if moving == "yes" and should == "yes":
    print("dont touch")
elif moving == "yes" and should == "no":
    print("use isolation tape")
elif moving == "no" and should == "yes":
    print("wdshky")
elif moving == ("no") and should == "no":
    print("dont touch")
