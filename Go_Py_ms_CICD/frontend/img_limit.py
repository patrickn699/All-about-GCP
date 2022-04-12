import os


def remove_imgs(dir):
    os.chdir("static")
    for i,f in enumerate(os.listdir(dir)):
        if i>2:
            os.remove(os.path.join(dir, f))
            print("removed")


def check_n_imgs():

    rec = "E:/go-py-microservice/conversion/received"
    sav = "./saved"

    if len(os.listdir(rec))>2 and len(os.listdir(sav))>2:
        remove_imgs(rec)
        remove_imgs(sav)