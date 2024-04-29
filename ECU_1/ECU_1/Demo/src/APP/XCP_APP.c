#include "MCAL/XCP/XCP.h"
#include "MCAL/USART/STM32F401cc_MCAL_USART.h"
#include "MCAL/GPIO/GPIO.h"

// Function prototypes
void xcp_init(void);
void xcp_send_frame(const XCP_Frame *frame);
void xcp_receive_frame(XCP_Frame *frame);
void xcp_handle_frame(const XCP_Frame *frame);
void send_response_frame(uint8_t response_type);
void send_data_response_frame(uint8_t response_type, const uint8_t *data, uint8_t data_length);

int main() {
    // Initialize XCP communication
    xcp_init();
    
    // Initialize GPIO pins for LED and switch
    GPIO_Pin_t led_pin = {.Port = GPIO_PORT_A, .Pin_num = GPIO_PIN_1, .Pin_Mode = GPIO_MODE_OP_PP, .Pin_Speed = GPIO_SPEED_HIGH};
    GPIO_Pin_t switch_pin = {.Port = GPIO_PORT_A, .Pin_num = GPIO_PIN_0, .Pin_Mode = GPIO_MODE_IN_PU};
    
    GPIO_Init(&led_pin);
    GPIO_Init(&switch_pin);
    
    // Main loop
    while (1) {
        // Check if switch is pressed
        U8 switch_state;
        GPIO_Get_PinValue(GPIO_PORT_A, GPIO_PIN_0, &switch_state);
        
        // If switch is pressed (switch_state == 0), toggle the LED
        if (switch_state == 0) {
            U8 current_led_state;
            GPIO_Get_PinValue(GPIO_PORT_A, GPIO_PIN_1, &current_led_state);
            GPIO_Set_PinValue(GPIO_PORT_A, GPIO_PIN_1, !current_led_state); // Toggle the LED state
        }
        
        // Receive and handle XCP frames
        XCP_Frame received_frame;
        xcp_receive_frame(&received_frame);
        xcp_handle_frame(&received_frame);
    }
    
    return 0;
}
