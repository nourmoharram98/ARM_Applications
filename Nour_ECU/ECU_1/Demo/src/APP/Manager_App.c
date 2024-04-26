/**
 * @file App.c
 * @author your name (you@domain.com)
 * @brief implementation of initialization functions
 * @version 0.1
 * @date 2024-04-07
 * 
 * @copyright Copyright (c) 2024
 * 
*/

/*--------------------------------Includes----------------------------*/
    #include "Std_Types.h"
    #include "HAL/LCD/HAL_LCD.h"
    #include "HAL/SWITCH/HAL_SWITCH.h"
    #include "APP/Manager.h"
    #include "HAL/LED/LED.h"
    #include "MCAL/USART/STM32F401cc_MCAL_USART.h"
    #include "SERVICE/COMM/UART_COMM.h"
/*---------------------------------------------------------------------*/

/*---------------------Buttons Macros Raw-Data(Without CRC)------------*/
    #define MODE_BUTTON_Data                         7  //r
    #define OK_BUTTON_Data                           5  //Q  
    #define EDIT_BUTTON_Data                         6  //d
    #define UP_BUTTON_Data                           4  //G
    #define DOWN_BUTTON_Data                         2  //#
    #define RIGHT_BUTTON_Data                        1  //UNDEFINED SYMBOL
    #define LEFT_BUTTON_Data                         3  //'5'
/*---------------------------------------------------------------------*/

/*-----------------------------Stop Watch modes------------------------*/
  
/*---------------------------------------------------------------------*/

/*----------------------------Global Variables-----------------------*/
    /**
     * @brief Mode: carry the Mode of operation (Clock-Date or Stop-Watch)
     * @brief Operation_type: carry the type of running operation (check for the enumeration in Manager.h)
     * @brief StopWatch_Status: carry the status of stop Watch STOP_WATCH_STOP or STOP_WATCH_START
     */
    u32 Operation_type=0;

/*--------------------------------------------------------------------*/

/*----------------------------STATIC FUNCTION-------------------------*/


/*--------------------------------------------------------------------*/

/**
 * @brief Manager runnable that check for the system mode and its operation states
 * @note operation state must start at Init_Operation then move to Idle Operation then any state can come
 * in order to prevent any undefined behaviour since before Idle_Operation the digits not all printed yet
 */


/*-------------------------leap Year Handling------------------------*/
    


/*---------------------------------------------Modes Handlers-----------------------------------------------------*/



/*---------------------------------------------Runnables-----------------------------------------------------*/

/*-------------------------------Manager Runnable------------------------------------*/
    void Manager_Runnable(void)
    {
       
        switch(Operation_type)
        {
            case Init_Operation:
               
            break;

            case Idle_Operation:
             
            break;

            case GeneralEdit_Operation:
             
            break;

            case DigitEdit_Operation:

            break;
            
            default:
                /*Do Nothing*/
            break;
        }
      //  Runnable_Execution_time();
    }

/*-------------------------------Control Switch Runnable-----------------------------*/
    void ControlSwitches_Runnable(void)
    { 
    /*Setting Switch Data To be sent*/
        static Ctrl_Switches_Data_t Ctrl_Switches_Data [1] = 
        {
            [SWITCH_ONE]=
            {
                .DATA = 1,
                .Switch_Status = Switch_Released,
                .Switch_PrevStatus = Switch_Released
            }
        };
    /*------------------------------*/

        /*SWITCH Reading and Sending Data*/
        U8 Switches_Iter=0;

        for (Switches_Iter = 0 ;Switches_Iter < Number_Of_Switches ; Switches_Iter++)
        {
            /*Read Switch State*/
                HAL_SWITCH_enuGetSwitchState( Switches_Iter ,&Ctrl_Switches_Data[Switches_Iter].Switch_Status );
            /*---------------------*/ 

            /*Single Realise Press signal handling and sending data via uart*/
                if(Ctrl_Switches_Data[Switches_Iter].Switch_Status == Switch_Pressed)
                {
                    Ctrl_Switches_Data[Switches_Iter].Switch_PrevStatus = Ctrl_Switches_Data[Switches_Iter].Switch_Status;
                }
                else if(Ctrl_Switches_Data[Switches_Iter].Switch_PrevStatus == Switch_Pressed && Ctrl_Switches_Data[Switches_Iter].Switch_Status == Switch_Released)
                {
                    /*Send unique data to TX_Communication_Manager*/
                        TX_Communication_Manager(Ctrl_Switches_Data[Switches_Iter].DATA); 
                    /*-------------------------------------------*/

                    /*------reset the switch status---------*/
                        Ctrl_Switches_Data[Switches_Iter].Switch_PrevStatus=Ctrl_Switches_Data[Switches_Iter].Switch_Status;
                    /*--------------------------------------*/
                }
            /*--------------------------------------------------------------*/    
        }
        /*-------------------------------*/

    }
/*-------------------------------Sender Manager Runnable-----------------------------*/
    void Sender_Manager_Runnable(void)
    {    
            Communication_Sender();
    }

/*-------------------------------Receiver Manager Runnable-------------------------- */
    void Receiver_Manager_Runnable(void)
    {
        Communication_Receiver();
    }



/*-----------------------------------------Command Handler--------------------------------------------------*/
/**
 * @brief function used to handle the input requests received from USART.
 * @note  the function execute every 10 msec periodicity
 * @param command 
 */
void Command_Handler(u8 command)
{
    // static u8 Edit_counter=0;
    switch(command)
    {
        case MODE_BUTTON_Data:
            Mode_Switch_Pressed();
        break;

        case EDIT_BUTTON_Data:
            Edit_Switch_Pressed();
        break;

        case OK_BUTTON_Data:
            OK_Switch_Pressed();
        break;

        case UP_BUTTON_Data:
            UP_Switch_Pressed();
        break;

        case DOWN_BUTTON_Data:
            Down_Switch_Pressed();
        break;

        case RIGHT_BUTTON_Data:  
            Right_Switch_Pressed();
        break;

        case LEFT_BUTTON_Data:
            Left_Switch_Pressed();
        break;

        default:
            /*Nothing*/
        break;
    }
    command=0;
}
/*-----------------------------------------Switches Handlers--------------------------------------------------*/

u32 Get_Switch_Status(u8 Switch_ID)
{
    u32 Switch_Status=0;
    HAL_SWITCH_enuGetSwitchState( Switch_ID ,&Switch_Status);
    return Switch_Status;

}
u8 Get_Led_Status(u8 LED_ID)
{
    u8 Led_status=0;
    LED_GetStatus(LED_ID,&Led_status);
    return Led_status;
}