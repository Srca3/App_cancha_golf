import assets


def main(): 
    results = assets.access()
    assets.save()
    assets.send_to_arduino(results[1])
if __name__ =='__main__':
    while True:
        main()