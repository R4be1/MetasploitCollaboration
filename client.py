import sys
import readline
from pymetasploit3.msfrpc import MsfRpcClient


print('''\033[1m
           ____
         ,'  , `.   ,----..
      ,-+-,.' _ |  /   /   \\
   ,-+-. ;   , || |   :     :
  ,--.'|'   |  ;| .   |  ;. /
 |   |  ,', |  ': .   ; /--`
 |   | /  | |  || ;   | ;
 '   | :  | :  |, |   : |
 ;   . |  ; |--'  .   | '___
 |   : |  | ,     '   ; : .'|
 |   : '  |/      '   | '/  :
 ;   | |`-'       |   :    /
 |   ;/            \   \ .'
 '---'              `---`    MetasploitCollaboration v1.0 
       \033[0m''')

def succcess_print(String):
    print(f"\033[1;34m[*]\033[0m {String}")

def error_print(String):
    print(f"\033[1;31m[*]\033[0m {String}")

def sessions_print():
    for session in client.sessions.list:
        _session = client.sessions.list[session]
        print(
                f'''\033[1m{str("["+session+"]").ljust(5)}\033[0m {_session["desc"].ljust(15)}  '''
                f'''{str(_session["session_host"] + ":" + str(_session["session_port"])).ljust(21)}  '''
                f'''{_session["username"].ljust(10)}  '''
                f'''{str( _session["platform"].capitalize() + "-" + _session["arch"] if _session.get("platform") else "Unknown" + "-" +_session["arch"] ).ljust(15)}  '''
                f'''{_session["via_payload"].ljust(20)}'''
                )

def session_shell(session):
    shell=client.sessions.session(session)
    while True:
        shell_command = input(f"\033[1;34m[{session}]\033[0m >> ")
        if shell_command.strip()=="break" or shell_command.strip()=="exit" or shell_command.strip()=="bg":
            break
        if command.strip() == "cls" or command.strip() == "clear" :
            print("\033c", end="")
        print( shell.run_with_output(shell_command) )

try:
    client = MsfRpcClient("47", server="127.0.0.1", port=55552, username="R4be1")

except Exception as e:
    error_print("MSFRpc Connect Error...")
    print(e)
    sys.exit(0)

else:
    succcess_print("MSFRpc Connect Succeed.")
    succcess_print(f"Sessions {len(client.sessions.list.keys())}")

def completer(text, state):
    func = ['cls', 'clear', 'sessions', 'session ', 'exit'] + ["session"+str(_) for _ in client.sessions.list.keys()]
    matches = [_ for _ in func if _.startswith(text)]
    if state < len(matches):
        return matches[state]
    else:
        return None

readline.parse_and_bind('tab: complete')
readline.set_completer(completer)
sessions_print()

while True:
    command = input("\033[1;31mMC Client \033[0m>> ")
    if command.strip() == "exit":
        break

    if command.split()[0] == "session" and len(command.split())>1:
        if command.split()[1].isdigit():
            session_shell( command.split()[1] )

    if command.startswith("session") and command.split("session")[1].isdigit():
        session_shell( command.split("session")[1] )

    if command.strip() == "sessions":
        sessions_print()

    if command.strip() == "cls" or command.strip() == "clear" :
        print("\033c", end="")
