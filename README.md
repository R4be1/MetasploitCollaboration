# MetasploitCollaboration

## Server Start:
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
msfconsole -r server.rc
```

msfconsole -r server.rc

## Client
```
python3 client.py
```
