def process(content):
    import numpy as np
    f_cont = content[0][0]
    labels = ["no defect","defect"]
    pred_label = labels[np.argmax(f_cont)]
    return {"probability":f_cont.tolist(),"class":pred_label}