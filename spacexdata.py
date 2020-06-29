import requests

def main():
    r = requests.get("https://api.spacexdata.com/v3/capsules")
    #print(r.json())

    for capsule in r.json():
        for serial in capsule:
            print(serial)
        #print(capsule.get("capsule_serial"))
        #print(capsule.get("capsule_id"))
        #print(capsule.get("status"))
        #print(space)

main()
