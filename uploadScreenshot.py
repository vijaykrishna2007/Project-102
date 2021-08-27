import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        

def main():
    num = 1
    while(True):
        access_token = 'WhO8rLtiRgwAAAAAAAAAAR5hVDJK2xmZq4FaXgMkuPrfXEMerUcskBZGg2FuExFx'
        transferData = TransferData(access_token)
    
        file_from = 'C:/Users/gbhan/Videos/Captures/Screenshot'+str(num)+'.png'
        file_to = '/Screenshots/Screenshot'+str(num)+'.png'  

        transferData.upload_file(file_from, file_to)
        print( str(num) + " Screenshot uploaded")

        num = num + 1

main()