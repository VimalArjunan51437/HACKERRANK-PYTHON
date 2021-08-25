import socket

# PROGRAM : USING SOCKET, CALCULATOR PROGRAM FROM CLIENT SIDE

def Servers():

    host = socket.gethostname()

    port = 6666
    s = socket.socket()

    print("Waiting for client to be connected...........")

    s.bind((host,port))

    s.listen(5)

    conn, address = s.accept()

    print("Connectioon from : "+str(address))

    while True:
        
        work = conn.recv(2048).decode()
        
        
        if(work=="1"):

          
            x1="Ente the need values.."

            conn.sendall(x1.encode())

            data= conn.recv(2048).decode()
           

            v=data.split(",")

            ans=str(int(v[0]) + int(v[1]))

            conn.sendall(ans.encode())
            
            break
        elif(work=="2"):
           
            x1="Ente the need values.."
            
            conn.sendall(x1.encode())

            data= conn.recv(2048).decode()
           
            v=data.split(",")

            ans=str(int(v[0]) - int(v[1]))

            conn.sendall(ans.encode())
           
            break
        elif(work=="3"):
            
            x1="Ente the need values.."
            
            conn.sendall(x1.encode())

            data= conn.recv(2048).decode()
            
            v=data.split(",")

            ans=str(int(v[0]) * int(v[1]))

            conn.sendall(ans.encode())
           
            break
        elif(work=="4"):
           

            x1="Ente the need values.."
            
            conn.sendall(x1.encode())

            data= conn.recv(2048).decode()
           

            v=data.split(",")

            ans=str(int(v[0]) / int(v[1]))

            conn.sendall(ans.encode())
           
            break
        else:
            print("SELECTED WORNG OPTION...")
            x1="Ente the correct option.."
            
            conn.sendall(x1.encode())

            break
        
    
    conn.close()


if __name__ =="__main__":
    
    Servers()
