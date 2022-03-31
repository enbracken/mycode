
def main():

    folks= ["David", "Elena", "Emily", "Chad", "Haley", "Jim", "Jonathan", "Matt", "Mike"]

    coolfolks= []

    #for x in folks:
    #    if x != "Chad":
    #        coolfolks.append(x)

    #print(coolfolks)

# list comprehensions are lists being built from the inside!
# here is a "ONE LINE" for loop with an "if" conditional built in!
    coolfolks_listcomprehension= [x for x in folks if len(x) >= 5]

    print(coolfolks_listcomprehension)

main()
