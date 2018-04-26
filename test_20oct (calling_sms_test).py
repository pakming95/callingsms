import serial
import time


#------------------------------------------------FUNCTION DEFINITIONS-------------------------------------------
#function for serial read
def serialread():
        read_serial = SerialPort.readline()
        read_decode = read_serial.decode('utf-8')
        return read_decode

#function for sending
def Sending(message, sender):
        SerialPort.write(b'AT+CMGF=1\r')
        time.sleep(1)
        read_1 = serialread()
        print (read_1)
        send_message = bytes('AT+CMGS="'+sender+'"\r\n', 'utf-8')
        SerialPort.write(send_message)
        time.sleep(1)
        message_input = bytes(message+"\x1A", 'utf-8')
        SerialPort.write(message_input)
        read_1 = serialread()
        print (read_1)
        read_1 = serialread()
        print (read_1)
        read_1 = serialread()
        print (read_1)
        print('message sent')


#function for calling
def Calling(number):
        aud_setting = bytes('AT+QAUDMOD=0\r\n','utf-8')
        SerialPort.write(aud_setting)
        read_1 = serialread()
        print (read_1)
        cod_setting = bytes('AT+QDAI=5\r\n','utf-8')
        SerialPort.write(cod_setting)
        read_3 = serialread()
        print (read_3)
        read_5 = serialread()
        print (read_5)
        call_number = bytes('ATD'+number+';\r\n','utf-8')
        SerialPort.write(call_number)
        read_2 = serialread()
        print (read_2)
        read_4 = serialread()
        print (read_4)
        print('Calling......\r\n')


#function for answering calls 
def Answer():
        aud_setting = bytes('AT+QAUDMOD=0\r\n','utf-8')
        SerialPort.write(aud_setting)
        read_3 = serialread()
        print (read_3)
        cod_setting = bytes('AT+QDAI=5\r\n','utf-8')
        SerialPort.write(cod_setting)
        read_3 = serialread()
        print (read_3)
        read_3 = serialread()
        print (read_3)
        read_3 = serialread()
        print (read_3)
        answer_call = bytes('ATA\r\n','utf-8')
        SerialPort.write(answer_call) 
        read_3 = serialread()
        print (read_3)
        print('Call answered....\r\n')

#function for dropping calls 
def Dropped():
        drop_call = bytes('ATH\r\n','utf-8')
        SerialPort.write(drop_call)
        read_4 = serialread()
        print (read_4)
        read_4 = serialread()
        print (read_4)
        read_4 = serialread()
        print (read_4)
        print('Closed call.......\r\n')

#function to read incoming SMS messages
def read_text(indexing):
        text_message = bytes('AT+CSDH=1\r\n','utf-8')
        SerialPort.write(text_message)
        read_5 = serialread()
        print (read_5)
        read_5 = serialread()
        print (read_5)
        time.sleep(1)
        index_message = bytes('AT+CMGR="'+indexing+'"\r\n','utf-8')
        SerialPort.write(index_message)
        while 1:
            read_5 = serialread()
            print(read_5)
            if read_5[:2] =='':
                break
        text_close = bytes('AT+CSDH=0\r\n','utf-8')
        SerialPort.write(text_close)
        read_5 = serialread()
        print (read_5)
        read_5 = serialread()
        print (read_5)
        time.sleep(1)
        
    
#function to read all inbox text messages
def read_all():
        hide_header = bytes('AT+CSDH=0\r\n','utf-8')
        SerialPort.write(hide_header)
        read_7 = serialread()
        print(read_7)
        read_7 = serialread()
        print(read_7)
        echo_mode = bytes('ATE1\r\n','utf-8')
        SerialPort.write(echo_mode)
        read_8 = serialread()
        print(read_8)
        read_8 = serialread()
        print(read_8)
        text_mode = bytes('AT+CMGF=1\r\n','utf-8')
        SerialPort.write(text_mode)
        read_9 = serialread()
        print(read_9)
        read_9 = serialread()
        print(read_9)
        set_storage = bytes('AT+CPMS="SM","SM","SM"\r\n','utf-8')
        SerialPort.write(set_storage)
        read_10 = serialread()
        print(read_10)
        read_10 = serialread()
        print(read_10)
        header_text = bytes('AT+CSDH=1\r\n','utf-8')
        SerialPort.write(header_text)
        read_11 = serialread()
        print(read_11)
        read_11 = serialread()
        print(read_11)
        char_set = bytes('AT+CSCS="GSM"\r\n','utf-8')
        SerialPort.write(char_set)
        read_12 = serialread()
        print(read_12)
        read_12 = serialread()
        print(read_12)
        read_all = bytes('AT+CMGL="ALL"\r\n','utf-8')
        SerialPort.write(read_all)
        while 1:
            read_13 = serialread()
            print(read_13)
            if read_13[:2] =='':
                break
        header_hide = bytes('AT+CSDH=0\r\n','utf-8')
        SerialPort.write(header_hide)
        read_14 = serialread()
        print(read_14)
        read_14 = serialread()
        print(read_14)
            

#defining all options 
def option_1():
        x = input("type the number: \n")
        print('-------------------------------------\r\n')
        y = input("type the message: \n")
        print('-------------------------------------\r\n')
        Sending(y,x) 

def option_2():
        z = input("type the number: \n")
        print('-------------------------------------\r\n')
        Calling(z) 

def option_3():
        Answer()

def option_4():
        Dropped()

def option_5():
        read_all()
            
#map the inputs to the functional blocks 
options = {1: option_1,
            2: option_2,
            3: option_3,
            4: option_4,
            5: option_5,
          }

#----------------------------------------------------INCOMING CALL INTERRUPT----------------------------------------------------------------------------------------
#function for handling incoming calls
def urc_ring():
        while 1:
                        print('Incoming call received!!!!\r\n')
                        print('-------------------------------------\r\n')
                        print('Please select option 3 to answer call or option 4 to drop the call\r\n')
                        choice = input("please type either two options here \r\n")
                        return_serial = serialread()
                        if return_serial[:10] == 'NO CARRIER':
                            print("Called dropped by caller")
                            break
                        if int(choice) == 1 or int(choice)== 2 or int(choice)==5:
                            choice = input(" please respond to incoming call first. Retype option: \r\n")
                        if int(choice) == 3:
                            return_serial = serialread()
                            if return_serial[:10] == 'NO CARRIER':
                                print("Called dropped by caller")
                                break
                            choice_num = int(choice)
                            options[choice_num]()
                            while 1:
                                print( 'Call answered and ongoing ......  \r\n')
                                return_serial = serialread()
                                if return_serial[:10] == 'NO CARRIER':
                                    print("Called dropped by caller")
                                    break
                                choice = input(" please type 4 to end the call \r\n")
                                if int(choice) == 4:
                                    choice_num = int(choice)
                                    options[choice_num]()
                                    break
                            break
                        if int(choice) == 4:
                            choice_num = int(choice)
                            options[choice_num]()
                            print('proceed to choosing your options now \r\n') 
                            break
#------------------------------------------------MAIN PROGRAM------------------------------------------------
#Main program
def main():
        while 1:
                flag_1 = 0
                print('-------------------------------------\r\n')
                print('Please select functions to use \r\n')
                print('-------------------------------------\r\n')
                print('(1) Send SMS to recepient \r\n')
                print('(2) Make a call to recepient \r\n')
                print('(3) Answering incoming call \r\n')
                print('(4) Dropping current call \r\n')
                print('(5) Read all Text Messages \r\n')
                print('-------------------------------------\r\n')
                flag_1 = flag_1 + 1
                choice = input("type the option you want: \n")
                return_serial = serialread()
                if return_serial[:4] =='RING':
                    flag_1 = 0
                    urc_ring()
                if return_serial[:5] =='+CMTI':
                    split_1 = return_serial.split(",")
                    mode,index = split_1
                    read_text(index)
                return_serial = serialread()
                if return_serial[:4] == 'RING':
                    flag_1 = 0
                    urc_ring()
                if return_serial[:5] =='+CMTI':
                    split_1 = return_serial.split(",")
                    mode,index = split_1
                    read_text(index)
                if flag_1 ==1:
                    choice_num = int(choice)
                    options[choice_num]()
            
SerialPort = serial.Serial("COM5",115200, timeout = 1)
main()
