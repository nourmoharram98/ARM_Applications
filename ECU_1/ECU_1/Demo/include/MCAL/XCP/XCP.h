#ifndef XCP_H
#define XCP_H

#include <stdint.h>

typedef enum {
    XCP_CMD_TOGGLE_LED,
    XCP_CMD_SWITCH_STATE,
    // Add more frame types as needed
} XCP_FrameType;

// XCP frame types
// #define XCP_CMD_READ           0x01
// #define XCP_CMD_WRITE          0x02
//#define XCP_CMD_TOGGLE_LED     0x20
//#define XCP_CMD_SWITCH_STATE   0x30
// Define additional frame types as needed

#define MAX_PAYLOAD_SIZE 10

#define XCP_RESPONSE_SUCCESS    0x10
#define XCP_RESPONSE_ERROR      0x11
#define XCP_RESPONSE_DATA       0x12
// Define additional response frame types as needed


// XCP frame structure
typedef struct {
    uint8_t type;          // Frame type (e.g., read, write)
    uint32_t address;      // Memory address for read/write operations
    uint8_t data_length;   // Length of data payload
    uint8_t data[256];     // Data payload
} XCP_Frame;

typedef struct {
    uint8_t frame_type;     // Type of XCP frame
    uint16_t frame_length;  // Length of the frame payload
    // Add any additional fields as needed
} XCP_FrameHeader;

typedef struct {
    XCP_FrameHeader header;  // Frame header
    uint8_t payload[MAX_PAYLOAD_SIZE];  // Frame payload
} XCP_Message;


void xcp_init(void);

// Function to send an XCP frame over UART
void xcp_send_frame(const XCP_Frame *frame);

// Function to receive an XCP frame over UART
void xcp_receive_frame(XCP_Frame *frame);

// Function to handle incoming XCP frames
void xcp_handle_frame(const XCP_Frame *frame);

// // Function to read memory at the specified address
// void xcp_read_memory(uint32_t address, uint8_t *data, uint8_t length);

// // Function to write data to memory at the specified address
// void xcp_write_memory(uint32_t address, const uint8_t *data, uint8_t length);

//void xcp_receive_frame(XCP_Frame *frame);
//void xcp_handle_frame(const XCP_Frame *frame);
//void xcp_send_frame(const XCP_Frame *frame);

#endif /* XCP_H */