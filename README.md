# MetasploitCollaboration

## Server Start:
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
msfconsole -r server.rc
```
or msfconsole execute:
```
load msgrpc ServerHost=127.0.0.1 ServerPort=55552 User=R4be1 Pass=47
```
![图片](https://github.com/R4be1/MetasploitCollaboration/assets/110738599/591a96e8-fbb0-4720-8b31-4cdfad2ea824)

## Client
```
python3 client.py
```
![图片](https://github.com/R4be1/MetasploitCollaboration/assets/110738599/aa04923c-eea7-4681-b03f-7c34b120137e)
