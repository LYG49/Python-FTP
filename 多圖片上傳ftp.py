from ftplib import FTP
import os 
ftp_args = {
    'host' : 'xxx.xxx.xxx.xxx',
    'user' : 'Guest',
    'paswd' : 'guest'
}

def upload_pic_to_ftp():
    f = FTP()
    f.set_pasv(False)                                                  #默認是True,手動關閉被動模式
    f.connect(ftp_args['host'])
    f.login(ftp_args['user'],ftp_args['paswd'])
    print('Welcom: ',f.getwelcome())
    buf_size = 1024
    path_name = "12011735_img"
    path = "12011735_path"
    path1 = "12011735"
    imgs_path = open(path_name+'/'+path + '.txt').readlines()          #這個txt檔案裡有所有圖片的路徑  readlines可以讀取一行
    
    if path_name in f.nlst():
        print("路徑存在。")
    else:
        print("路徑不存在。")
        f.mkd(path_name)
    
    n = 1
    for i in range(len(imgs_path)):                                   #讀取txt裡面所有路徑
        full_path = imgs_path[i].strip()
        sub_paths = full_path.split('/')
        full_path_prefix = sub_paths[-1]
        print('%d\t%s' % (i, sub_paths[-1]))
        num = str(n)
        remote_file ='/'+path_name +'/'+path1 +'_'+ num.zfill(4) + '.jpg'     #ftp
        n += 1
        file_handler = open(path_name + '/'+full_path_prefix, 'rb')           #本機
        f.storbinary('STOR %s' % remote_file, file_handler, buf_size)
        file_handler.close()


upload_pic_to_ftp()
