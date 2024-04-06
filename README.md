# MetasploitCollaboration

## Server Start:
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall

git clone https://github.com/R4be1/MetasploitCollaboration.git
cd MetasploitCollaboration/
msfconsole -r server.rc
```
or msfconsole execute:
```
load msgrpc ServerHost=0.0.0.0 ServerPort=55552 User=R4be1 Pass=47
```
![图片](https://github.com/R4be1/MetasploitCollaboration/assets/110738599/591a96e8-fbb0-4720-8b31-4cdfad2ea824)

## Client:
```
python3 -m pip install pymetasploit3
python3 client.py 127.0.0.1
```
![图片](https://github.com/R4be1/MetasploitCollaboration/assets/110738599/aa04923c-eea7-4681-b03f-7c34b120137e)
```
cls or clear          :
listeners or handlers :
sessions              : list session.
exit                  : exit
msfconsole            : msfconsole
session [number] or session[number] :
```
## !
```
Note that there may be no echo during interaction
because the call is RPC
so it may be that the data echo is not timely
in general, press enter more and it will be echoed
and in special cases, press it a few more times
ha ha ha ha ha~
```
