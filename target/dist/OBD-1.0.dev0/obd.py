import requests


def OBD(inp1):
    print("reading image")
    inp = "src/main/resources/images/input/"+str(inp1)
    out = "src/main/resources/images/output/"+str(inp1)
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
