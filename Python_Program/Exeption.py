
ItemsInCart = 0
'''
# Error rais if requirment is notmatching.

if ItemsInCart != 2:
    raise ("Product Count Cart not matching")
'''

assert (ItemsInCart == 0) #returnt true and automation continue
#assert (ItemsInCart == 2) #return F and automation stop

#   try , except  use to handle errors and and continue the cose
try:
    with open('text_filee.txt', 'r') as read: #file name is wrong the reeal name is text_file.txt
        content = read.readlines()
except Exception as e:      #eather use online exception to and write your own wrror message or u can store in variable and know the python error
    print("Something is wrong")
    print(e)

    #  finally  " no matter where the program will stop but the finally code will always work in a last.

finally:
    print("Cleanup Recort")
