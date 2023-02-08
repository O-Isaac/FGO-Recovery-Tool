from libs.network import url, network
from libs.encryption import CertFileDescription
from libs.config import main

import time

if __name__ == "__main__":
    # Load certificate and slice two first character
    certificateFile = open('file/54cc790bf952ea710ed7e8be08049531').read()
    certificateSlice = slice(2, len(certificateFile))
    certificateString = certificateFile[certificateSlice]

    # Decrypt The certificate
    certificateData = CertFileDescription.Decrypt(certificateString)

    # Main options
    main.setConfigCertificate(certificateData)

    # Start Recover
    print("[+] Type the password of bind code")
    password = input()
    
    print("[+] Updating data...")
    url.set_latest_assets()

    print("[+] Generating Bind Code...")
    conf = main
    game = network.Game(conf.userId, conf.authKey, conf.secretKey)
    
    # Login 
    time.sleep(3)
    game.Login()

    # Generate Bind Code
    time.sleep(2)
    bindCode = game.BindCode(password)

    print(f"[+] Your new Bind Code is {bindCode}")
    print(f"[+] The password is {password}")    
