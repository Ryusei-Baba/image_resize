#ライブラリのインポート
import cv2
import numpy as np
import os
import glob
#新しいフォルダ名
new_fol='new_pic'
#新しいフォルダを作成
os.makedirs(new_fol, exist_ok=True)
#画像ファイル一覧を取得
pics=glob.glob('*.jpg')
#調整後サイズを指定(横幅、縦高さ)
size=(256,768)
#リサイズ処理開始
for pic in pics:
    base_pic=np.zeros((size[1],size[0],3),np.uint8)
    pic1=cv2.imread(pic,cv2.IMREAD_COLOR)
    h,w=pic1.shape[:2]
    ash=size[1]/h
    asw=size[0]/w
    if asw<ash:
        sizeas=(int(w*asw),int(h*asw))
    else:
        sizeas=(int(w*ash),int(h*ash))
    pic1 = cv2.resize(pic1,dsize=sizeas)
    base_pic[int(size[1]/2-sizeas[1]/2):int(size[1]/2+sizeas[1]/2),
    int(size[0]/2-sizeas[0]/2):int(size[0]/2+sizeas[0]/2),:]=pic1
    cv2.imwrite(new_fol+'/'+pic,base_pic)