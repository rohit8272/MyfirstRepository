import myModule
import platform

myModule.greeting("rohit")

print(platform)

name = myModule.person1["name"]
# print(name)

os = platform.version()
# print(os)

methodsOfOs = dir(platform)
# print(methodsOfOs)