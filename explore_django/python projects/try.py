try:
    a = 10
    ans=10/0
    print(ans)
except Exception as e:
    print("Some error occured", e)
finally:
    print("Your are good to go with finally block")