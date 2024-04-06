# MetasploitCollaboration

## Server Start:
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
msfconsole -r server.rc
```

## Client
```
python3 client.py
```
![图片](https://github.com/R4be1/MetasploitCollaboration/assets/110738599/aa04923c-eea7-4681-b03f-7c34b120137e)
