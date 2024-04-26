#include "MCAL/XCP/XCP.h"
#include "MCAL/USART/STM32F401cc_MCAL_USART.h"
#include "MCAL/GPIO/GPIO.h"
#include "HAL/SWITCH/HAL_SWITCH.h"

void xcp_init(void) {
    // Initialize UART with appropriate baud rate, data bits, stop bits, etc.
    USART_Init();
    // You may also configure other UART settings as needed
    
    // Enable UART interrupt if using interrupt-driven communication
    // UART_EnableInterrupt(UART_PORT_1, UART_RX_INTERRUPT);
}


void xcp_send_frame(const XCP_Frame *frame) {
    // Send frame type
    USART_SendByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->type, .length = 1});

    // Send data length
    USART_SendByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->data_length, .length = 1});
    
    // Send data payload
    for (int i = 0; i < frame->data_length; i++) {
        USART_SendByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->data[i], .length = 1});
    }
    // // Send frame type
    // USART_SendByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->type, .length = 1});

    // // Send memory address (4 bytes)
    // USART_SendByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = (uint8_t*)&frame->address, .length = 4});

    // // Send data length
    // USART_SendByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->data_length, .length = 1});
    
    // // Send data payload
    // for (int i = 0; i < frame->data_length; i++) {
    //     USART_SendByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->data[i], .length = 1});
    // }
}

void xcp_receive_frame(XCP_Frame *frame) {
    // Receive frame type
    USART_GetByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->type, .length = 1});
    
    // Receive data length
    USART_GetByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->data_length, .length = 1});
    
    // Receive data payload
    for (int i = 0; i < frame->data_length; i++) {
        USART_GetByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->data[i], .length = 1});
    }
    // // Receive frame type
    // USART_GetByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->type, .length = 1});
    
    // // Receive memory address (4 bytes)
    // USART_GetByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = (uint8_t*)&frame->address, .length = 4});

    // // Receive data length
    // USART_GetByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->data_length, .length = 1});
    
    // // Receive data payload
    // for (int i = 0; i < frame->data_length; i++) {
    //     USART_GetByte((USART_Request_t){.USART_ID = USART1, .PtrtoBuffer = &frame->data[i], .length = 1});
    // }
}

void xcp_handle_frame(const XCP_Frame *frame) {
     switch (frame->type) {
        case XCP_CMD_TOGGLE_LED:
            // Toggle the LED
            // Implement GPIO control logic here
            // For example, if the LED is connected to GPIO pin 13:
            // Toggle the state of the LED
            GPIO_Set_PinValue(GPIO_PORT_A , GPIO_PIN_0 , GPIO_STATE_SET);
            break;
        case XCP_CMD_SWITCH_STATE:
            // Check switch state
            if (frame->data_length >= 1) {
                if (frame->data[0] == 1) {
                    // Switch is pressed
                    // Read the state of the switch
                    u32 switch_state;
                    HAL_SWITCH_enuGetSwitchState(0, &switch_state); // Assuming switch 0 is the one you want to read
                    // Perform actions based on switch state
                    if (switch_state == Switch_Pressed) {
                    // Switch is pressed, handle accordingly
                    // For example, toggle the LED
                    U8 current_pin_state;
                    GPIO_Get_PinValue(GPIO_PORT_A, GPIO_PIN_1, &current_pin_state);
                    GPIO_Set_PinValue(GPIO_PORT_A, GPIO_PIN_1, current_pin_state ^ GPIO_STATE_SET);

                } else {
                    // Switch is released, handle accordingly
                    // For example, turn off the LED
                    GPIO_Set_PinValue(GPIO_PORT_A, GPIO_PIN_1, GPIO_STATE_RESET);
                }

            }
            break;
        default:
            // Unknown frame type
            break;
    //     // case XCP_CMD_READ:
    //     //     // Handle read command
    //     //     break;
    //     // case XCP_CMD_WRITE:
    //     //     // Handle write command
    //     //     break;
    //     // case XCP_CMD_TOGGLE_LED:
    //     //     // Handle write command
    //     //     break;
    //     case XCP_CMD_SWITCH_STATE:
    //         // Check switch state
    //         if (frame->data_length >= 1) {
    //             if (frame->data[0] == 1) {
    //                 // Switch is pressed, toggle the LED
    //                 // Implement GPIO control logic to toggle the LED
    //                 // For example:
    //                 // Toggle the state of the LED
    //                // GPIO_Set_PinValue(GPIO_PORT_A , GPIO_PIN_0 , GPIO_STATE_SET);
    //                 // Read the state of the switch
    //                 U8 switch_state;
    //                 GPIO_Get_PinValue(GPIO_PORT_A , GPIO_PIN_0 , &switch_state);

    //                 // If switch is pressed (switch_state == 0), toggle the LED
    //                 if (switch_state == 0) {
    //                     // Toggle the state of the LED
    //                     U8 current_led_state;
    //                     GPIO_Get_PinValue(GPIO_PORT_A , GPIO_PIN_1, &current_led_state);
    //                     GPIO_Set_PinValue(GPIO_PORT_A , GPIO_PIN_1, !current_led_state); // Toggle the LED state
    //                 }

                    
    //                 // Generate a response frame with the switch state
    //                 send_data_response_frame(XCP_RESPONSE_DATA, &switch_state, sizeof(switch_state));
    //             }

    //         } else {
    //             // Switch is released, do nothing or handle as needed
    //         }
    //         break;
    //     // Add cases for additional frame types as needed
    //     default:
    //         // Unknown frame type
    //         break;
             }
            
    }


// void xcp_read_memory(uint32_t address, uint8_t *data, uint8_t length) {
//     // Implement logic to read memory from the specified address
//     // and store the result in the data buffer
// }

// void xcp_write_memory(uint32_t address, const uint8_t *data, uint8_t length) {
//     // Implement logic to write data to memory at the specified address
// }

// Send a response frame with no data
void send_response_frame(uint8_t response_type) {
    XCP_Frame response_frame;
    response_frame.type = response_type;
    response_frame.data_length = 0; // No payload
    xcp_send_frame(&response_frame); // Send the response frame
}

// Send a response frame with data
void send_data_response_frame(uint8_t response_type, const uint8_t *data, uint8_t data_length) {
    XCP_Frame response_frame;
    response_frame.type = response_type;
    response_frame.data_length = data_length;
    memcpy(response_frame.data, data, data_length); // Copy data into response frame
    xcp_send_frame(&response_frame); // Send the response frame
}