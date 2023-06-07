import hashlib
import time

counter = 1
md5_pass = input('enter md5 password:')
md5_file = input('enter wordlist location:')
#write try except block for handle exception
try:
    md5_file = open(md5_file,'r')# file will read
except:
    print('\nfile not found')
    quit()
# write for loop which is use for matching the hash pass with wordlist pass
for password in md5_file:
    hash_obj = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()

    start = time.time()
    print('\ntrying password %d ------> %s' %(counter,password.strip()))
    counter += 1
    end = time.time()
    t_time = end - start


    if hash_obj == md5_pass:
        print('password found!!!! password is :%s'% password)
        print('total running time:',t_time,'seconds')
        time.sleep(10)
        break
    else:
        print('password not found ')