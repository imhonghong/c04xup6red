def conv2Darray(img,kern):
    (height_img,width_img)=np.shape(img)
    (height_kern,width_kern)=np.shape(kern)
    conv=np.zeros(np.shape(img))

    for hi in range(0,height_img-height_kern+1):
        for wi in range(0,width_img-width_kern+1):
            for hk in range(0,height_kern):
                for wk in range(0,width_kern):
                    conv[hi+hk][wi+wk]=conv[hi+hk][wi+wk]+kern[hk][wk]
    new_img=img*conv
    return new_img

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,1]])
c=conv2Darray(a,b)
