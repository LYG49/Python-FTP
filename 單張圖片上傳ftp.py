from ftplib import FTP
import os 
ftp_args = {
    'host' : 'xxx.xxx.xxx.xxx',                 #ftp主機的IP
    'user' : 'Guest',                           #ftp使用者帳號
    'paswd' : 'guest'                           #ftp使用者密碼
}

def upload_pic_to_ftp():
    f = FTP()
    f.set_pasv(False)                           #默認是True,手動關閉被動模式
    f.connect(ftp_args['host'])                 #ftp連線
    f.login(ftp_args['user'],ftp_args['paswd']) #取得ftp帳號密碼登入至ftp
    print('Welcom: ',f.getwelcome())
    buf_size = 1024                             #緩存區
    path_name = "image2"                        #ftp資料夾名稱
    if path_name in f.nlst():                   #判別ftp裡是否有image2這個資料夾
        print("路徑存在。")
    else:
        print("路徑不存在。")
        f.mkd(path_name)                        #沒有image2的話，新建一個新的資料夾
        
    remote_file ='/'+path_name +'/1.jpg'        #ftp裡面存放的位置及名稱(1.jpg可以自行更改) 
    local_file = 'D:/Desktop/images/01H_0.jpg'  #本機存放圖片的位置
    file_handler = open(local_file, 'rb')       #rb為讀取二進制模式    #wb為寫入二進制模式
    f.storbinary('STOR %s' % remote_file, file_handler, buf_size)
    file_handler.close()
    

upload_pic_to_ftp()

