import enum 

class CANFormat(enum.Enum): 
	CANStandard = 0 
	CANExtended = 1 

class CANType(enum.Enum): 
	CANData = 0 
	CANRemote = 1 

class Mode(enum.Enum): 
	AutoNegotiate = 1 
	HalfDuplex10 = 2 
	FullDuplex10 = 3 
	HalfDuplex100 = 4 
	FullDuplex100 = 5 

class PathType(enum.Enum): 
	FilePathType = 1 
	FileSystemPathType = 2 

class gpio_irq_event(enum.Enum): 
	IRQ_NONE = 1 
	IRQ_RISE = 2 
	IRQ_FALL = 3 

class RxStatus(enum.Enum): 
	NoData = 1 
	MasterGeneralCall = 2 
	MasterWrite = 3 
	MasterRead = 4 

class Acknowledge(enum.Enum): 
	NoACK = 0 
	ACK = 1 

class RxStatus(enum.Enum): 
	NoData = 0 
	ReadAddressed = 1 
	WriteGeneral = 2 
	WriteAddressed = 3 

class Parity(enum.Enum): 
	None = 0 
	Odd = 1 
	Even = 2 
	Forced1 = 3 
	Forced0 = 4 

class IrqType(enum.Enum): 
	RxIrq = 0 
	TxIrq = 1 

class SerialParity(enum.Enum): 
	ParityNone = 0 
	ParityOdd = 1 
	ParityEven = 2 
	ParityForced1 = 3 
	ParityForced0 = 4 

class SerialIrq(enum.Enum): 
	RxIrq = 1 
	TxIrq = 2 

class IRQn(enum.Enum): 
	NonMaskableInt_IRQn = -14 
	MemoryManagement_IRQn = -12 
	BusFault_IRQn = -11 
	UsageFault_IRQn = -10 
	SVCall_IRQn = -5 
	DebugMonitor_IRQn = -4 
	PendSV_IRQn = -2 
	SysTick_IRQn = -1 
	WDT_IRQn = 0 
	TIMER0_IRQn = 1 
	TIMER1_IRQn = 2 
	TIMER2_IRQn = 3 
	TIMER3_IRQn = 4 
	UART0_IRQn = 5 
	UART1_IRQn = 6 
	UART2_IRQn = 7 
	UART3_IRQn = 8 
	PWM1_IRQn = 9 
	I2C0_IRQn = 10 
	I2C1_IRQn = 11 
	I2C2_IRQn = 12 
	SPI_IRQn = 13 
	SSP0_IRQn = 14 
	SSP1_IRQn = 15 
	PLL0_IRQn = 16 
	RTC_IRQn = 17 
	EINT0_IRQn = 18 
	EINT1_IRQn = 19 
	EINT2_IRQn = 20 
	EINT3_IRQn = 21 
	ADC_IRQn = 22 
	BOD_IRQn = 23 
	USB_IRQn = 24 
	CAN_IRQn = 25 
	DMA_IRQn = 26 
	I2S_IRQn = 27 
	ENET_IRQn = 28 
	RIT_IRQn = 29 
	MCPWM_IRQn = 30 
	QEI_IRQn = 31 
	PLL1_IRQn = 32 
	USBActivity_IRQn = 33 
	CANActivity_IRQn = 34 

class ADCName(enum.Enum): 
	ADC0_0 = 0 
	ADC0_1 = 1 
	ADC0_2 = 2 
	ADC0_3 = 3 
	ADC0_4 = 4 
	ADC0_5 = 5 
	ADC0_6 = 6 
	ADC0_7 = 7 

class DACName(enum.Enum): 
	DAC_0 = 0 

class PWMName(enum.Enum): 
	PWM_1 = 1 
	PWM_2 = 2 
	PWM_3 = 3 
	PWM_4 = 4 
	PWM_5 = 5 
	PWM_6 = 6 

class PinDirection(enum.Enum): 
	PIN_INPUT = 1 
	PIN_OUTPUT = 2 

class PinMode(enum.Enum): 
	PullUp = 0 
	PullDown = 3 
	PullNone = 2 
	OpenDrain = 4 

class PortName(enum.Enum): 
	Port0 = 0 
	Port1 = 1 
	Port2 = 2 
	Port3 = 3 
	Port4 = 4 

class icmp_dur_type(enum.Enum): 
	ICMP_DUR_NET = 0 
	ICMP_DUR_HOST = 1 
	ICMP_DUR_PROTO = 2 
	ICMP_DUR_PORT = 3 
	ICMP_DUR_FRAG = 4 
	ICMP_DUR_SR = 5 

class icmp_te_type(enum.Enum): 
	ICMP_TE_TTL = 0 
	ICMP_TE_FRAG = 1 

class netconn_type(enum.Enum): 
	NETCONN_INVALID = 0 
	NETCONN_TCP = 16 
	NETCONN_UDP = 32 
	NETCONN_UDPLITE = 33 
	NETCONN_UDPNOCHKSUM = 34 
	NETCONN_RAW = 64 

class netconn_state(enum.Enum): 
	NETCONN_NONE = 1 
	NETCONN_WRITE = 2 
	NETCONN_LISTEN = 3 
	NETCONN_CONNECT = 4 
	NETCONN_CLOSE = 5 

class netconn_evt(enum.Enum): 
	NETCONN_EVT_RCVPLUS = 1 
	NETCONN_EVT_RCVMINUS = 2 
	NETCONN_EVT_SENDPLUS = 3 
	NETCONN_EVT_SENDMINUS = 4 
	NETCONN_EVT_ERROR = 5 

class netconn_igmp(enum.Enum): 
	NETCONN_JOIN = 1 
	NETCONN_LEAVE = 2 

class pbuf_layer(enum.Enum): 
	PBUF_TRANSPORT = 1 
	PBUF_IP = 2 
	PBUF_LINK = 3 
	PBUF_RAW = 4 

class pbuf_type(enum.Enum): 
	PBUF_RAM = 1 
	PBUF_ROM = 2 
	PBUF_REF = 3 
	PBUF_POOL = 4 

class snmp_ifType(enum.Enum): 
	snmp_ifType_other = 1 
	snmp_ifType_regular1822 = 2 
	snmp_ifType_hdh1822 = 3 
	snmp_ifType_ddn_x25 = 4 
	snmp_ifType_rfc877_x25 = 5 
	snmp_ifType_ethernet_csmacd = 6 
	snmp_ifType_iso88023_csmacd = 7 
	snmp_ifType_iso88024_tokenBus = 8 
	snmp_ifType_iso88025_tokenRing = 9 
	snmp_ifType_iso88026_man = 10 
	snmp_ifType_starLan = 11 
	snmp_ifType_proteon_10Mbit = 12 
	snmp_ifType_proteon_80Mbit = 13 
	snmp_ifType_hyperchannel = 14 
	snmp_ifType_fddi = 15 
	snmp_ifType_lapb = 16 
	snmp_ifType_sdlc = 17 
	snmp_ifType_ds1 = 18 
	snmp_ifType_e1 = 19 
	snmp_ifType_basicISDN = 20 
	snmp_ifType_primaryISDN = 21 
	snmp_ifType_propPointToPointSerial = 22 
	snmp_ifType_ppp = 23 
	snmp_ifType_softwareLoopback = 24 
	snmp_ifType_eon = 25 
	snmp_ifType_ethernet_3Mbit = 26 
	snmp_ifType_nsip = 27 
	snmp_ifType_slip = 28 
	snmp_ifType_ultra = 29 
	snmp_ifType_ds3 = 30 
	snmp_ifType_sip = 31 
	snmp_ifType_frame_relay = 32 

class tcp_state(enum.Enum): 
	CLOSED = 0 
	LISTEN = 1 
	SYN_SENT = 2 
	SYN_RCVD = 3 
	ESTABLISHED = 4 
	FIN_WAIT_1 = 5 
	FIN_WAIT_2 = 6 
	CLOSE_WAIT = 7 
	CLOSING = 8 
	LAST_ACK = 9 
	TIME_WAIT = 10 

class lwip_event(enum.Enum): 
	LWIP_EVENT_ACCEPT = 1 
	LWIP_EVENT_SENT = 2 
	LWIP_EVENT_RECV = 3 
	LWIP_EVENT_CONNECTED = 4 
	LWIP_EVENT_POLL = 5 
	LWIP_EVENT_ERR = 6 

class etharp_state(enum.Enum): 
	ETHARP_STATE_EMPTY = 0 
	ETHARP_STATE_PENDING = 1 
	ETHARP_STATE_STABLE = 2 

class slipif_recv_state(enum.Enum): 
	SLIP_RECV_NORMAL = 1 
	SLIP_RECV_ESCAPE = 2 

class script_state(enum.Enum): 
	s_down = 1 
	s_up = 2 

class LinkPhase(enum.Enum): 
	PHASE_DEAD = 0 
	PHASE_INITIALIZE = 1 
	PHASE_ESTABLISH = 2 
	PHASE_AUTHENTICATE = 3 
	PHASE_CALLBACK = 4 
	PHASE_NETWORK = 5 
	PHASE_TERMINATE = 6 

class PPPDevStates(enum.Enum): 
	PDIDLE = 0 
	PDSTART = 1 
	PDADDRESS = 2 
	PDCONTROL = 3 
	PDPROTOCOL1 = 4 
	PDPROTOCOL2 = 5 
	PDDATA = 6 

class NPmode(enum.Enum): 
	NPMODE_PASS = 1 
	NPMODE_DROP = 2 
	NPMODE_ERROR = 3 
	NPMODE_QUEUE = 4 

class pppAuthType(enum.Enum): 
	PPPAUTHTYPE_NONE = 1 
	PPPAUTHTYPE_ANY = 2 
	PPPAUTHTYPE_PAP = 3 
	PPPAUTHTYPE_CHAP = 4 

class State(enum.Enum): 
	Inactive = 1 
	Ready = 2 
	Running = 3 
	WaitingDelay = 4 
	WaitingInterval = 5 
	WaitingOr = 6 
	WaitingAnd = 7 
	WaitingSemaphore = 8 
	WaitingMailbox = 9 
	WaitingMutex = 10 

class osPriority(enum.Enum): 
	osPriorityIdle = -3 
	osPriorityLow = -2 
	osPriorityBelowNormal = -1 
	osPriorityNormal = 0 
	osPriorityAboveNormal = 1 
	osPriorityHigh = 2 
	osPriorityRealtime = 3 

class osStatus(enum.Enum): 
	osOK = 0 
	osEventSignal = 8 
	osEventMessage = 16 
	osEventMail = 32 
	osEventTimeout = 64 
	osErrorParameter = 128 
	osErrorResource = 129 
	osErrorTimeoutResource = 193 
	osErrorISR = 130 
	osErrorISRRecursive = 131 
	osErrorPriority = 132 
	osErrorNoMemory = 133 
	osErrorValue = 134 
	osErrorOS = 255 

class os_timer_type(enum.Enum): 
	osTimerOnce = 0 

class LCDType(enum.Enum): 
	LCD16x2 = 1 
	LCD16x2B = 2 
	LCD20x2 = 3 
	LCD20x4 = 4 

class icmp_dur_type(enum.Enum): 
	ICMP_DUR_NET = 0 
	ICMP_DUR_HOST = 1 
	ICMP_DUR_PROTO = 2 
	ICMP_DUR_PORT = 3 
	ICMP_DUR_FRAG = 4 
	ICMP_DUR_SR = 5 

class icmp_te_type(enum.Enum): 
	ICMP_TE_TTL = 0 
	ICMP_TE_FRAG = 1 

class netconn_type(enum.Enum): 
	NETCONN_INVALID = 0 
	NETCONN_TCP = 16 
	NETCONN_UDP = 32 
	NETCONN_UDPLITE = 33 
	NETCONN_UDPNOCHKSUM = 34 
	NETCONN_RAW = 64 

class netconn_state(enum.Enum): 
	NETCONN_NONE = 1 
	NETCONN_WRITE = 2 
	NETCONN_LISTEN = 3 
	NETCONN_CONNECT = 4 
	NETCONN_CLOSE = 5 

class netconn_evt(enum.Enum): 
	NETCONN_EVT_RCVPLUS = 1 
	NETCONN_EVT_RCVMINUS = 2 
	NETCONN_EVT_SENDPLUS = 3 
	NETCONN_EVT_SENDMINUS = 4 
	NETCONN_EVT_ERROR = 5 

class netconn_igmp(enum.Enum): 
	NETCONN_JOIN = 1 
	NETCONN_LEAVE = 2 

class pbuf_layer(enum.Enum): 
	PBUF_TRANSPORT = 1 
	PBUF_IP = 2 
	PBUF_LINK = 3 
	PBUF_RAW = 4 

class pbuf_type(enum.Enum): 
	PBUF_RAM = 1 
	PBUF_ROM = 2 
	PBUF_REF = 3 
	PBUF_POOL = 4 

class snmp_ifType(enum.Enum): 
	snmp_ifType_other = 1 
	snmp_ifType_regular1822 = 2 
	snmp_ifType_hdh1822 = 3 
	snmp_ifType_ddn_x25 = 4 
	snmp_ifType_rfc877_x25 = 5 
	snmp_ifType_ethernet_csmacd = 6 
	snmp_ifType_iso88023_csmacd = 7 
	snmp_ifType_iso88024_tokenBus = 8 
	snmp_ifType_iso88025_tokenRing = 9 
	snmp_ifType_iso88026_man = 10 
	snmp_ifType_starLan = 11 
	snmp_ifType_proteon_10Mbit = 12 
	snmp_ifType_proteon_80Mbit = 13 
	snmp_ifType_hyperchannel = 14 
	snmp_ifType_fddi = 15 
	snmp_ifType_lapb = 16 
	snmp_ifType_sdlc = 17 
	snmp_ifType_ds1 = 18 
	snmp_ifType_e1 = 19 
	snmp_ifType_basicISDN = 20 
	snmp_ifType_primaryISDN = 21 
	snmp_ifType_propPointToPointSerial = 22 
	snmp_ifType_ppp = 23 
	snmp_ifType_softwareLoopback = 24 
	snmp_ifType_eon = 25 
	snmp_ifType_ethernet_3Mbit = 26 
	snmp_ifType_nsip = 27 
	snmp_ifType_slip = 28 
	snmp_ifType_ultra = 29 
	snmp_ifType_ds3 = 30 
	snmp_ifType_sip = 31 
	snmp_ifType_frame_relay = 32 

class tcp_state(enum.Enum): 
	CLOSED = 0 
	LISTEN = 1 
	SYN_SENT = 2 
	SYN_RCVD = 3 
	ESTABLISHED = 4 
	FIN_WAIT_1 = 5 
	FIN_WAIT_2 = 6 
	CLOSE_WAIT = 7 
	CLOSING = 8 
	LAST_ACK = 9 
	TIME_WAIT = 10 

class lwip_event(enum.Enum): 
	LWIP_EVENT_ACCEPT = 1 
	LWIP_EVENT_SENT = 2 
	LWIP_EVENT_RECV = 3 
	LWIP_EVENT_CONNECTED = 4 
	LWIP_EVENT_POLL = 5 
	LWIP_EVENT_ERR = 6 

class etharp_state(enum.Enum): 
	ETHARP_STATE_EMPTY = 0 
	ETHARP_STATE_PENDING = 1 
	ETHARP_STATE_STABLE = 2 

class slipif_recv_state(enum.Enum): 
	SLIP_RECV_NORMAL = 1 
	SLIP_RECV_ESCAPE = 2 

class script_state(enum.Enum): 
	s_down = 1 
	s_up = 2 

class LinkPhase(enum.Enum): 
	PHASE_DEAD = 0 
	PHASE_INITIALIZE = 1 
	PHASE_ESTABLISH = 2 
	PHASE_AUTHENTICATE = 3 
	PHASE_CALLBACK = 4 
	PHASE_NETWORK = 5 
	PHASE_TERMINATE = 6 

class PPPDevStates(enum.Enum): 
	PDIDLE = 0 
	PDSTART = 1 
	PDADDRESS = 2 
	PDCONTROL = 3 
	PDPROTOCOL1 = 4 
	PDPROTOCOL2 = 5 
	PDDATA = 6 

class NPmode(enum.Enum): 
	NPMODE_PASS = 1 
	NPMODE_DROP = 2 
	NPMODE_ERROR = 3 
	NPMODE_QUEUE = 4 

class pppAuthType(enum.Enum): 
	PPPAUTHTYPE_NONE = 1 
	PPPAUTHTYPE_ANY = 2 
	PPPAUTHTYPE_PAP = 3 
	PPPAUTHTYPE_CHAP = 4 

class State(enum.Enum): 
	Inactive = 1 
	Ready = 2 
	Running = 3 
	WaitingDelay = 4 
	WaitingInterval = 5 
	WaitingOr = 6 
	WaitingAnd = 7 
	WaitingSemaphore = 8 
	WaitingMailbox = 9 
	WaitingMutex = 10 

class osPriority(enum.Enum): 
	osPriorityIdle = -3 
	osPriorityLow = -2 
	osPriorityBelowNormal = -1 
	osPriorityNormal = 0 
	osPriorityAboveNormal = 1 
	osPriorityHigh = 2 
	osPriorityRealtime = 3 

class osStatus(enum.Enum): 
	osOK = 0 
	osEventSignal = 8 
	osEventMessage = 16 
	osEventMail = 32 
	osEventTimeout = 64 
	osErrorParameter = 128 
	osErrorResource = 129 
	osErrorTimeoutResource = 193 
	osErrorISR = 130 
	osErrorISRRecursive = 131 
	osErrorPriority = 132 
	osErrorNoMemory = 133 
	osErrorValue = 134 
	osErrorOS = 255 

class os_timer_type(enum.Enum): 
	osTimerOnce = 0 

class LCDType(enum.Enum): 
	LCD16x2 = 1 
	LCD16x2B = 2 
	LCD20x2 = 3 
	LCD20x4 = 4 

