import requests
from tkinter import filedialog
from tkinter import *


def OBD(inp):
    print("reading image")
    # inp = "src/main/resources/images/input/"+str(inp1)
    out = inp.split(".")
    out = out[0]+"_out."+out[1]
    print("applying CNN")
    r = requests.post(
        "https://api.deepai.org/api/deepmask",
        files={
            'image': open(inp, 'rb'),
        },
        headers={'api-key': '586e72bf-eac4-4a0b-9098-d5c320d0d50b'}
    )
    print("Saving output")
    output = r.json()["output_url"]

    # print(output)

    with open(out, 'wb') as f:
        f.write(requests.get(output).content)
    print("Done...!")


root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("JPG","*.jpg"),("JPEG","*.jpeg"),("PNG","*.png*"),("all files","*.*")))
print (root.filename)
OBD(str(root.filename))

print("OBD - Object boundary detection")
print("Using Sharpmask")