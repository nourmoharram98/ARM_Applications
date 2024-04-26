#include "SERVICE/COMM/UART_COMM.h"


//from USART.c and carry the received request
extern u8 Received_Request;



u8 Frame_start_flag=0;
u8 Send_frame_flag=0;
u8 Payload=0;


// Communication Manager function
void TX_Communication_Manager(U8 RAW_DATA) 
{
    //for aly approach
}


Sys_enuErrorStates_t Communication_Sender(void)
{
    Sys_enuErrorStates_t Error_Status=NOT_OK;
    u8 RPC_FRAME[3]={0xAA,0,0x55};
    if(Send_frame_flag)
    {
        RPC_FRAME[1]=Payload;

        //create the local USART Request data to be sent to USART transmiter
        for(u8 index=0;index<3;index++)
        {
            USART_Request_t Local_Data=
            {
                .USART_ID=USART1,
                .PtrtoBuffer=&RPC_FRAME[index],
                .length=1,
                .CallBack=NULL_POINTER
            };

            USART_SendByte(Local_Data);
        }
        Send_frame_flag=0;
        Error_Status=OK;

    }
   
    return Error_Status;
}

Sys_enuErrorStates_t Communication_Receiver(void)
{
    Sys_enuErrorStates_t Error_Status=NOT_OK;
    
    
    if(Received_Request!=0)
    { 
        switch(Received_Request)
        {
            case 0xAA:
                Frame_start_flag=1;
            break;
            
            case 0x55:
                Frame_start_flag=0;
            break;

            default:
                if(Frame_start_flag)
                {
                    Request_Handler(Received_Request);
                }
                else
                {
                    Received_Request=0;
                }
            break;
        }
    }
    else
    {
        Error_Status=NOT_OK;
    }
    return Error_Status;

}

void Request_Handler(u8 data)
{
    u8 switch_status=0;
    u8 led_status=0;
    switch(data)
    {
        case 10://read switch status
            switch_status=Get_Switch_Status(1);
        break;

        case 15: // read led status
            led_status=Get_Led_Status(1);
        break;

        case 20: //read led and switch
            switch_status=Get_Switch_Status(1);
            led_status=Get_Led_Status(1);
        break;

        default:
        
        break;
    }
    Construct_Frame(switch_status,led_status);
    Send_frame_flag=1;
}

void Construct_Frame(u8 dataone,u8 datatwo)
{
    Payload |= dataone;
    Payload |= datatwo<<2;
}