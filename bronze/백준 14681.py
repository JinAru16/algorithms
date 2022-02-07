numberX = int(input())
numberY = int(input())

if numberX > 0 and numberY > 0:
    print("1")
elif numberX > 0 and numberY < 0:
    print("4")

elif numberX < 0 and numberY >0:
    print("2")

else:
    print("3")