from libs.network import url, paramBuilder
import hashlib

class Game:
    def __init__(self, user_id: str, auth_key: str, secret_key: str):
        print(f"[+] User Id: {user_id}")
        print(f"[+] Auth Key: {auth_key}")
        print(f"[+] Secret Key: {secret_key}")

        self.name_ = ''
        self.user_id_ = (int)(user_id)
        self.s_ = url.NewSession()
        self.builder_ = paramBuilder.ParameterBuilder(user_id, auth_key, secret_key)
    
    def Post(self, uri):
        res = url.PostReq(self.s_, uri, self.builder_.Build())
        self.builder_.Clean()
        return res

    def Login(self): 
        lastAccessTime = self.builder_.parameter_list_[5][1]
        dataServerFolderCrc = url.data_server_folder_crc_
        userState = (-int(lastAccessTime) >> 2) ^ self.user_id_ & dataServerFolderCrc

        # Adding parameters
        self.builder_.AddParameter('assetbundleFolder', url.asset_bundle_folder_)
        self.builder_.AddParameter('isTerminalLogin', '1')
        self.builder_.AddParameter('userState', str(userState))

        # Logging
        data = self.Post(f'{url.server_addr_}/login/top?_userId={self.user_id_}')
        print("[+] Logged into game!")

        # Name
        self.name_ = hashlib.md5(data['cache']['replaced']['userGame'][0]['name'].encode('utf-8')).hexdigest()
        
    def BindCode(self, password):
        # Add Param
        self.builder_.AddParameter("continuePass", "Americadad2")
        # Make request
        data = self.Post(f'{url.server_addr_}/continue/prepare?_userId={self.user_id_}')
        # Recive Bind Code
        bindCode = data["cache"]["updated"]["userContinue"][0]["continueKey"]
        
        return bindCode
