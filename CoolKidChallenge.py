#!/usr/bin/python3

def main():

    folks= ["David", "Elena", "Emily", "Chad", "Haley", "Jim", "Jonathan", "Matt", "Mike"]
    coolfolks= []
    
   # for x in folks:
   #     if x != "Chad":
   #         coolfolks.append(x)
    coolfolks=[i for i in folks if i != "Chad"]
    print(coolfolks)

main()
