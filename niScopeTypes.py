import ctypes

class ViSession(ctypes.c_ulong):pass 		# long unsigned int
class ViBoolean(ctypes.c_ushort):pass		# short unsigned int
class ViRsrc(ctypes.c_char_p):pass 		# char*
class ViReal64(ctypes.c_double):pass		# double
class ViInt32(ctypes.c_long):pass			# long int
class ViStatus(ctypes.c_long):pass		# long int
class ViConstString(ctypes.c_char_p):pass	# const char*
class ViInt8(ctypes.c_char):pass  		# Binary8 signed char
class ViInt16(ctypes.c_int):pass  		#Binary16     short int
class ViInt32(ctypes.c_long):pass 		#Binary32 long int
class ViChar(ctypes.POINTER(ViConstString)):pass


class wfmInfo(ctypes.Structure):
	_fields_ = [("absoluteInitialX", ViReal64),
				("relativeInitialX", ViReal64),
				("xIncrement", ViReal64),
				("actualSamples", ViInt32 ),
				("offset", ViReal64),
				("gain", ViReal64),
				("reserved1", ViReal64),
				("reserved2", ViReal64)]


#d#efine _VI_FUNC            __stdcall
#d#efine _VI_FUNCC           __cdecl
#d#efine _VI_FUNCH           __stdcall

#coupling
IVISCOPE_VAL_TRIGGER_COUPLING_SPECIFIC_EXT_BASE = 1000L
class COUPLING:
	AC					=	0L                
	DC					=	1L                
	GND					=	2L                
	HF_REJECT			=	3L            
	AC_PLUS_HF_REJECT	= 	1001L 

#slope
class SLOPE :
	POSITIVE = 1L
	NEGATIVE = 0L

#Trigger window
class TRIGGER_WINDOW :
	ENTERING_WINDOW = 0
	LEAVING_WINDOW = 1

IVISCOPE_VAL_ACQUISITION_TYPE_CLASS_EXT_BASE           = 100L
IVISCOPE_VAL_ACQUISITION_TYPE_SPECIFIC_EXT_BASE        = 1000L

class VAL:
	NORMAL = 0L
	FLEXRES = (IVISCOPE_VAL_ACQUISITION_TYPE_SPECIFIC_EXT_BASE + 1)
	DDC = (IVISCOPE_VAL_ACQUISITION_TYPE_SPECIFIC_EXT_BASE + 2)

class ACQ_STATUS:
	COMPLETE = 1L
	IN_PROGRESS = 0L
	UNKOWN = -1L

#/*- Defined values for NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT -*/
IVISCOPE_VAL_TV_SIGNAL_FORMAT_SPECIFIC_EXT_BASE = 1000L
#// SDTV/EDTV
class TV_TRIGGER_SIGNAL_FORMAT :
	VAL_NTSC 							= 1L                            
	VAL_PAL 							= 2L                             
	VAL_SECAM 							= 3L                           
	VAL_M_PAL 							= 1001L                        
	VAL_480I_59_94_FIELDS_PER_SECOND 	= 1010L 
	VAL_480I_60_FIELDS_PER_SECOND 		= 1011L    
	VAL_480P_59_94_FRAMES_PER_SECOND 	= 1015L 
	VAL_480P_60_FRAMES_PER_SECOND 		= 1016L    
	VAL_576I_50_FIELDS_PER_SECOND 		= 1020L    
	VAL_576P_50_FRAMES_PER_SECOND 		= 1025L    		
	VAL_720P_50_FRAMES_PER_SECOND 		= 1031L    
	VAL_720P_59_94_FRAMES_PER_SECOND 	= 1032L  
	VAL_720P_60_FRAMES_PER_SECOND 		= 1033L    
	VAL_1080I_50_FIELDS_PER_SECOND 		= 1040L   
	VAL_1080I_59_94_FIELDS_PER_SECON 	= 1041L 
	VAL_1080I_60_FIELDS_PER_SECOND 		= 1042L   
	VAL_1080P_24_FRAMES_PER_SECOND 		= 1045L   

#/*- Defined values for NISCOPE_ATTR_TV_TRIGGER_EVENT -*/
class TV_TRIGGER_EVENT :
	FIELD1 		= 1L     
	FIELD2 		= 2L     
	ANY_FIELD 	= 3L   
	ANY_LINE 	= 4L   
	LINE_NUMBER = 5L

#/*- Defined values for NISCOPE_ATTR_TV_TRIGGER_POLARITY -*/
class TV_TRIGGER_POLARITY :
	POSITIVE = 1L
	NEGATIVE = 2L


#/*- NISCOPE_ATTR_TRIGGER_SOURCE Values -*/
class TRIGGER_SOURCE:
	"""
	Trigger source types.
	
	"""
	EXTERNAL 	= "VAL_EXTERNAL"         
	TTL0 		= "VAL_TTL0"                 
	TTL1 		= "VAL_TTL1"                 
	TTL2 		= "VAL_TTL2"                 
	TTL3 		= "VAL_TTL3"                 
	TTL4 		= "VAL_TTL4"                 
	TTL5 		= "VAL_TTL5"                 
	TTL6 		= "VAL_TTL6"                 
	TTL7 		= "VAL_TTL7"                 
	ECL0 		= "VAL_ECL0"                 
	ECL1 		= "VAL_ECL1"                 
	PXI_STAR	= "VAL_PXI_STAR"         
	RTSI_0 		= "VAL_RTSI_0"             
	RTSI_1 		= "VAL_RTSI_1"             
	RTSI_2 		= "VAL_RTSI_2"             
	RTSI_3 		= "VAL_RTSI_3"             
	RTSI_4 		= "VAL_RTSI_4"             
	RTSI_5 		= "VAL_RTSI_5"             
	RTSI_6 		= "VAL_RTSI_6"             
	IMMEDIATE 	= "VAL_IMMEDIATE"       
	SW_TRIG_FUNC= "VAL_SW_TRIG_FUNC" 
	RTSI_7 		= "VAL_RTSI_7"             
	PFI_0  		= "VAL_PFI_0"              
	PFI_1  		= "VAL_PFI_1"              
	PFI_2  		= "VAL_PFI_2"



#/****************************************************************************
#*------------------------ Error And Completion Codes ----------------------*
# ****************************************************************************/
class ERROR_BASE:
#/*= Error base constantsvistatype.h========= */ 
	_VI_ERROR=	(-2147483647L-1)##/* 0x80000000 */ visatype.h
#/*= Error base constantsivi.h========= */ 
	IVI_STATUS_CODE_BASE=	0x3FFA0000L 
	IVI_WARN_BASE=	IVI_STATUS_CODE_BASE
	IVI_CROSS_CLASS_WARN_BASE=	IVI_WARN_BASE + 0x1000
	IVI_CLASS_WARN_BASE=	IVI_WARN_BASE + 0x2000
	IVI_SPECIFIC_WARN_BASE=	IVI_WARN_BASE + 0x4000
	IVI_MAX_SPECIFIC_WARN_CODE=	IVI_WARN_BASE + 0x7FFF
	IVI_NI_WARN_BASE=	IVI_WARN_BASE + 0x6000

	IVI_ERROR_BASE =	_VI_ERROR + IVI_STATUS_CODE_BASE
	IVI_CROSS_CLASS_ERROR_BASE=	IVI_ERROR_BASE + 0x1000
	IVI_CLASS_ERROR_BASE=	IVI_ERROR_BASE + 0x2000
	IVI_SPECIFIC_ERROR_BASE=	IVI_ERROR_BASE + 0x4000
	IVI_MAX_SPECIFIC_ERROR_CODE=	IVI_ERROR_BASE + 0x7FFF
	IVI_NI_ERROR_BASE=	IVI_ERROR_BASE + 0x6000
	IVI_SHARED_COMPONENT_ERROR_BASE=	IVI_ERROR_BASE + 0x1000
#/*= Error base constantsiviscope.h========= */ 
	IVISCOPE_WARN_INVALID_WFM_ELEMENT=IVI_CLASS_WARN_BASE+0x0001L
	IVISCOPE_ERROR_CHANNEL_NOT_ENABLED=IVI_CLASS_ERROR_BASE+0x0001L
	IVISCOPE_ERROR_UNABLE_TO_PERFORM_MEASUREMENT=IVI_CLASS_ERROR_BASE+0x0002L
	IVISCOPE_ERROR_MAX_TIME_EXCEEDED=IVI_CLASS_ERROR_BASE+0x0003L
	        
	
	

ERRORS = {
ERROR_BASE.IVI_CLASS_WARN_BASE +0x0001L: "IVISCOPE_WARN_INVALID_WFM_ELEMENT",
ERROR_BASE.IVI_CLASS_ERROR_BASE+0x0001L	: "IVISCOPE_ERROR_CHANNEL_NOT_ENABLED",
ERROR_BASE.IVI_CLASS_ERROR_BASE+0x0002L	: "IVISCOPE_ERROR_UNABLE_TO_PERFORM_MEASUREMENT ",
ERROR_BASE.IVI_CLASS_ERROR_BASE+0x0003L	: "IVISCOPE_ERROR_MAX_TIME_EXCEEDED",
ERROR_BASE.IVI_CLASS_ERROR_BASE+0x0004L	: "IVISCOPE_ERROR_INVALID_ACQ_TYPE",

ERROR_BASE.IVISCOPE_WARN_INVALID_WFM_ELEMENT: "WARN_INVALID_WFM_ELEMENT",
ERROR_BASE.IVI_SPECIFIC_WARN_BASE+0x001L: "WARN_HEATER_CIRCUIT_TEMPERATURE",
ERROR_BASE.IVI_SPECIFIC_WARN_BASE+0x002L: "WARN_INVALID_DATA",
ERROR_BASE.IVI_SPECIFIC_WARN_BASE+0x003L: "WARN_CHANNEL_OVERLOAD",
ERROR_BASE.IVI_SPECIFIC_WARN_BASE+0x004L: "WARN_AUTOSETUP_NO_SIGNAL",
ERROR_BASE.IVI_SPECIFIC_WARN_BASE+0x005L: "WARN_PLL_UNLOCKED",
ERROR_BASE.IVI_SPECIFIC_WARN_BASE+0x006L: "WARN_PLL_UNLOCKED_AND_ADC_OVERLOAD",
ERROR_BASE.IVI_SPECIFIC_WARN_BASE+0x007L: "WARN_TIMESTAMP_ROLLOVER",
ERROR_BASE.IVI_SPECIFIC_WARN_BASE+0x008L: "WARN_ADC_OVERLOAD",
ERROR_BASE.IVISCOPE_ERROR_CHANNEL_NOT_ENABLED: "ERROR_CHANNEL_NOT_ENABLED",
ERROR_BASE.IVISCOPE_ERROR_UNABLE_TO_PERFORM_MEASUREMENT: "ERROR_UNABLE_TO_PERFORM_MEASUREMENT",
ERROR_BASE.IVISCOPE_ERROR_MAX_TIME_EXCEEDED: "ERROR_MAX_TIME_EXCEEDED",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x001L: "ERROR_SOFTWARE_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x002L: "ERROR_HARDWARE_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x003L: "ERROR_INSUFFICIENT_MEMORY",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x004L: "ERROR_INVALID_DATA",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x005L: "ERROR_GAIN_CAL_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x006L: "ERROR_SINE_CAL_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x007L: "ERROR_LIN_CAL_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x008L: "ERROR_ADC_CAL_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x009L: "ERROR_ACQ_IN_PROGRESS",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x00AL: "ERROR_DATA_NOT_AVAILABLE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x00BL: "ERROR_HEATER_CIRCUIT_CAL_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x00CL: "ERROR_FLEXRES_CONFIG_CORRUPT",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x00DL: "ERROR_GAIN_OFFSET_CAL_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x00EL: "ERROR_CREATE_THREAD",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x00FL: "ERROR_WRONG_PASSWORD",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x010L: "ERROR_INVALID_GAIN",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x013L: "ERROR_INVALID_CAL_SESSION",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x014L: "ERROR_BAD_MEASUREMENT",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x015L: "ERROR_BUFFER_NOT_ACQUIRED",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x016L: "ERROR_TRIGGER_HAS_NOT_OCCURRED",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x017L: "ERROR_ILLEGAL_RELATIVE_TO",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x018L: "ERROR_DATA_OVERWRITTEN",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x01AL: "ERROR_INVALID_TIMESTAMP_EVENT_TAG",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x01BL: "ERROR_TIMEOUT_TRANSFERRING_TIMESTAMPS",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x01CL: "ERROR_TIMEOUT_CHECKING_STATUS",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x01DL: "ERROR_TIMEOUT_TRANSFERRING_DATA",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x01EL: "ERROR_PLL_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x01FL: "ERROR_PAR_TO_SER_CONV_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x020L: "ERROR_DMA_CONFIG_ERROR",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x021L: "ERROR_ILLEGAL_USER_OFFSET",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x022L: "ERROR_NOT_A_SCOPE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x023L: "ERROR_TIMEOUT_CLEARING_TIO",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x024L: "ERROR_RIS_DID_NOT_COMPLETE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x025L: "ERROR_INVALID_RIS_METHOD",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x026L: "ERROR_INVALID_RIS_NUM_AVERAGES",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x027L: "ERROR_ILLEGAL_DATATYPE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x028L: "ERROR_ATTRIBUTES_DIFFER_BY_CHANNEL",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x029L: "ERROR_TRIGGER_DELAY_INVALID_WITH_RIS",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x02AL: "ERROR_INITIATE_NOT_CALLED",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x02BL: "ERROR_INVALID_FUNCTION_USE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x02CL: "ERROR_HOLDOFF_DELAY_NONZERO",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x02DL: "ERROR_CHANNEL_NAME_TOO_LONG",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0x02EL: "ERROR_DIGITIZER_ALREADY_IN_USE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0X02FL: "ERROR_SIM_MODEL_NOT_SUPPORTED",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0X030L: "ERROR_SPECIFICDLL_LOAD_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0X031L: "ERROR_SPECIFICDLL_GET_ADDRESS_FAILURE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0X032L: "ERROR_TRIGGER_TYPE_INVALID",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0X033L: "ERROR_INVALID_FETCH_PARAMETERS",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0X034L: "ERROR_EXT_CAL_NOT_COMPLETE",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0X035L: "ERROR_EXT_CAL_CONSTS_INVALID",
ERROR_BASE.IVI_SPECIFIC_ERROR_BASE+0X036L: "ERROR_INVALID_NUM_WAVEFORMS",
0xBFFA1190                                      : "ERROR_INVALID_SESSION   	  ",
 -1073807360 : "VI_ERROR_SYSTEM_ERROR       ",#(_VI_ERROR+0x3FFF0000L) #/* BFFF0000, */
 -1073807346 : "VI_ERROR_INV_OBJECT         ",#(_VI_ERROR+0x3FFF000EL) #/* BFFF000E, */
 -1073807345 : "VI_ERROR_RSRC_LOCKED        ",#(_VI_ERROR+0x3FFF000FL) #/* BFFF000F, */
 -1073807344 : "VI_ERROR_INV_EXPR           ",#(_VI_ERROR+0x3FFF0010L) #/* BFFF0010, */
 -1073807343 : "VI_ERROR_RSRC_NFOUND        ",#(_VI_ERROR+0x3FFF0011L) #/* BFFF0011, */
 -1073807342 : "VI_ERROR_INV_RSRC_NAME      ",#(_VI_ERROR+0x3FFF0012L) #/* BFFF0012, */
 -1073807341 : "VI_ERROR_INV_ACC_MODE       ",#(_VI_ERROR+0x3FFF0013L) #/* BFFF0013, */
 -1073807339 : "VI_ERROR_TMO                ",#(_VI_ERROR+0x3FFF0015L) #/* BFFF0015, */
 -1073807338 : "VI_ERROR_CLOSING_FAILED     ",#(_VI_ERROR+0x3FFF0016L) #/* BFFF0016, */
 -1073807333 : "VI_ERROR_INV_DEGREE         ",#(_VI_ERROR+0x3FFF001BL) #/* BFFF001B, */
 -1073807332 : "VI_ERROR_INV_JOB_ID         ",#(_VI_ERROR+0x3FFF001CL) #/* BFFF001C, */
 -1073807331 : "VI_ERROR_NSUP_ATTR          ",#(_VI_ERROR+0x3FFF001DL) #/* BFFF001D, */
 -1073807330 : "VI_ERROR_NSUP_ATTR_STATE    ",#(_VI_ERROR+0x3FFF001EL) #/* BFFF001E, */
 -1073807329 : "VI_ERROR_ATTR_READONLY      ",#(_VI_ERROR+0x3FFF001FL) #/* BFFF001F, */
 -1073807328 : "VI_ERROR_INV_LOCK_TYPE      ",#(_VI_ERROR+0x3FFF0020L) #/* BFFF0020, */
 -1073807327 : "VI_ERROR_INV_ACCESS_KEY     ",#(_VI_ERROR+0x3FFF0021L) #/* BFFF0021, */
 -1073807322 : "VI_ERROR_INV_EVENT          ",#(_VI_ERROR+0x3FFF0026L) #/* BFFF0026, */
 -1073807321 : "VI_ERROR_INV_MECH           ",#(_VI_ERROR+0x3FFF0027L) #/* BFFF0027, */
 -1073807320 : "VI_ERROR_HNDLR_NINSTALLED   ",#(_VI_ERROR+0x3FFF0028L) #/* BFFF0028, */
 -1073807319 : "VI_ERROR_INV_HNDLR_REF      ",#(_VI_ERROR+0x3FFF0029L) #/* BFFF0029, */
 -1073807318 : "VI_ERROR_INV_CONTEXT        ",#(_VI_ERROR+0x3FFF002AL) #/* BFFF002A, */
 -1073807315 : "VI_ERROR_QUEUE_OVERFLOW     ",#(_VI_ERROR+0x3FFF002DL) #/* BFFF002D, */
 -1073807313 : "VI_ERROR_NENABLED           ",#(_VI_ERROR+0x3FFF002FL) #/* BFFF002F, */
 -1073807312 : "VI_ERROR_ABORT              ",#(_VI_ERROR+0x3FFF0030L) #/* BFFF0030, */
 -1073807308 : "VI_ERROR_RAW_WR_PROT_VIOL   ",#(_VI_ERROR+0x3FFF0034L) #/* BFFF0034, */
 -1073807307 : "VI_ERROR_RAW_RD_PROT_VIOL   ",#(_VI_ERROR+0x3FFF0035L) #/* BFFF0035, */
 -1073807306 : "VI_ERROR_OUTP_PROT_VIOL     ",#(_VI_ERROR+0x3FFF0036L) #/* BFFF0036, */
 -1073807305 : "VI_ERROR_INP_PROT_VIOL      ",#(_VI_ERROR+0x3FFF0037L) #/* BFFF0037, */
 -1073807304 : "VI_ERROR_BERR               ",#(_VI_ERROR+0x3FFF0038L) #/* BFFF0038, */
 -1073807303 : "VI_ERROR_IN_PROGRESS        ",#(_VI_ERROR+0x3FFF0039L) #/* BFFF0039, */
 -1073807302 : "VI_ERROR_INV_SETUP          ",#(_VI_ERROR+0x3FFF003AL) #/* BFFF003A, */
 -1073807301 : "VI_ERROR_QUEUE_ERROR        ",#(_VI_ERROR+0x3FFF003BL) #/* BFFF003B, */
 -1073807300 : "VI_ERROR_ALLOC              ",#(_VI_ERROR+0x3FFF003CL) #/* BFFF003C, */
 -1073807299 : "VI_ERROR_INV_MASK           ",#(_VI_ERROR+0x3FFF003DL) #/* BFFF003D, */
 -1073807298 : "VI_ERROR_IO                 ",#(_VI_ERROR+0x3FFF003EL) #/* BFFF003E, */
 -1073807297 : "VI_ERROR_INV_FMT            ",#(_VI_ERROR+0x3FFF003FL) #/* BFFF003F, */
 -1073807295 : "VI_ERROR_NSUP_FMT           ",#(_VI_ERROR+0x3FFF0041L) #/* BFFF0041, */
 -1073807294 : "VI_ERROR_LINE_IN_USE        ",#(_VI_ERROR+0x3FFF0042L) #/* BFFF0042, */
 -1073807290 : "VI_ERROR_NSUP_MODE          ",#(_VI_ERROR+0x3FFF0046L) #/* BFFF0046, */
 -1073807286 : "VI_ERROR_SRQ_NOCCURRED      ",#(_VI_ERROR+0x3FFF004AL) #/* BFFF004A, */
 -1073807282 : "VI_ERROR_INV_SPACE          ",#(_VI_ERROR+0x3FFF004EL) #/* BFFF004E, */
 -1073807279 : "VI_ERROR_INV_OFFSET         ",#(_VI_ERROR+0x3FFF0051L) #/* BFFF0051, */
 -1073807278 : "VI_ERROR_INV_WIDTH          ",#(_VI_ERROR+0x3FFF0052L) #/* BFFF0052, */
 -1073807276 : "VI_ERROR_NSUP_OFFSET        ",#(_VI_ERROR+0x3FFF0054L) #/* BFFF0054, */
 -1073807275 : "VI_ERROR_NSUP_VAR_WIDTH     ",#(_VI_ERROR+0x3FFF0055L) #/* BFFF0055, */
 -1073807273 : "VI_ERROR_WINDOW_NMAPPED     ",#(_VI_ERROR+0x3FFF0057L) #/* BFFF0057, */
 -1073807271 : "VI_ERROR_RESP_PENDING       ",#(_VI_ERROR+0x3FFF0059L) #/* BFFF0059, */
 -1073807265 : "VI_ERROR_NLISTENERS         ",#(_VI_ERROR+0x3FFF005FL) #/* BFFF005F, */
 -1073807264 : "VI_ERROR_NCIC               ",#(_VI_ERROR+0x3FFF0060L) #/* BFFF0060, */
 -1073807263 : "VI_ERROR_NSYS_CNTLR         ",#(_VI_ERROR+0x3FFF0061L) #/* BFFF0061, */
 -1073807257 : "VI_ERROR_NSUP_OPER          ",#(_VI_ERROR+0x3FFF0067L) #/* BFFF0067, */
 -1073807256 : "VI_ERROR_INTR_PENDING       ",#(_VI_ERROR+0x3FFF0068L) #/* BFFF0068, */
 -1073807254 : "VI_ERROR_ASRL_PARITY        ",#(_VI_ERROR+0x3FFF006AL) #/* BFFF006A, */
 -1073807253 : "VI_ERROR_ASRL_FRAMING       ",#(_VI_ERROR+0x3FFF006BL) #/* BFFF006B, */
 -1073807252 : "VI_ERROR_ASRL_OVERRUN       ",#(_VI_ERROR+0x3FFF006CL) #/* BFFF006C, */
 -1073807250 : "VI_ERROR_TRIG_NMAPPED       ",#(_VI_ERROR+0x3FFF006EL) #/* BFFF006E, */
 -1073807248 : "VI_ERROR_NSUP_ALIGN_OFFSET  ",#(_VI_ERROR+0x3FFF0070L) #/* BFFF0070, */
 -1073807247 : "VI_ERROR_USER_BUF           ",#(_VI_ERROR+0x3FFF0071L) #/* BFFF0071, */
 -1073807246 : "VI_ERROR_RSRC_BUSY          ",#(_VI_ERROR+0x3FFF0072L) #/* BFFF0072, */
 -1073807242 : "VI_ERROR_NSUP_WIDTH         ",#(_VI_ERROR+0x3FFF0076L) #/* BFFF0076, */
 -1073807240 : "VI_ERROR_INV_PARAMETER      ",#(_VI_ERROR+0x3FFF0078L) #/* BFFF0078, */
 -1073807239 : "VI_ERROR_INV_PROT           ",#(_VI_ERROR+0x3FFF0079L) #/* BFFF0079, */
 -1073807237 : "VI_ERROR_INV_SIZE           ",#(_VI_ERROR+0x3FFF007BL) #/* BFFF007B, */
 -1073807232 : "VI_ERROR_WINDOW_MAPPED      ",#(_VI_ERROR+0x3FFF0080L) #/* BFFF0080, */
 -1073807231 : "VI_ERROR_NIMPL_OPER         ",#(_VI_ERROR+0x3FFF0081L) #/* BFFF0081, */
 -1073807229 : "VI_ERROR_INV_LENGTH         ",#(_VI_ERROR+0x3FFF0083L) #/* BFFF0083, */
 -1073807215 : "VI_ERROR_INV_MODE           ",#(_VI_ERROR+0x3FFF0091L) #/* BFFF0091, */
 -1073807204 : "VI_ERROR_SESN_NLOCKED       ",#(_VI_ERROR+0x3FFF009CL) #/* BFFF009C, */
 -1073807203 : "VI_ERROR_MEM_NSHARED        ",#(_VI_ERROR+0x3FFF009DL) #/* BFFF009D, */
 -1073807202 : "VI_ERROR_LIBRARY_NFOUND     ",#(_VI_ERROR+0x3FFF009EL) #/* BFFF009E, */
 -1073807201 : "VI_ERROR_NSUP_INTR          ",#(_VI_ERROR+0x3FFF009FL) #/* BFFF009F, */
 -1073807200 : "VI_ERROR_INV_LINE           ",#(_VI_ERROR+0x3FFF00A0L) #/* BFFF00A0, */
 -1073807199 : "VI_ERROR_FILE_ACCESS        ",#(_VI_ERROR+0x3FFF00A1L) #/* BFFF00A1, */
 -1073807198 : "VI_ERROR_FILE_IO            ",#(_VI_ERROR+0x3FFF00A2L) #/* BFFF00A2, */
 -1073807197 : "VI_ERROR_NSUP_LINE          ",#(_VI_ERROR+0x3FFF00A3L) #/* BFFF00A3, */
 -1073807196 : "VI_ERROR_NSUP_MECH          ",#(_VI_ERROR+0x3FFF00A4L) #/* BFFF00A4, */
 -1073807195 : "VI_ERROR_INTF_NUM_NCONFIG   ",#(_VI_ERROR+0x3FFF00A5L) #/* BFFF00A5, */
 -1073807194 : "VI_ERROR_CONN_LOST          ",#(_VI_ERROR+0x3FFF00A6L) #/* BFFF00A6, */
 -1073807193 : "VI_ERROR_MACHINE_NAVAIL     ",#(_VI_ERROR+0x3FFF00A7L) #/* BFFF00A7, */
 -1073807192 : "VI_ERROR_NPERMISSION        ",#(_VI_ERROR+0x3FFF00A8L) #/* B
 
#/*****************************************************************************/
#/*= Error constants   ivi.h                                             ========= */ 
#/*****************************************************************************/

ERROR_BASE.IVI_STATUS_CODE_BASE:"IVI_WARN_BASE                  ",         
ERROR_BASE.IVI_WARN_BASE + 0x1000:"IVI_CROSS_CLASS_WARN_BASE      ",         
ERROR_BASE.IVI_WARN_BASE + 0x2000:"IVI_CLASS_WARN_BASE            ",         
ERROR_BASE.IVI_WARN_BASE + 0x4000:"IVI_SPECIFIC_WARN_BASE         ",         
ERROR_BASE.IVI_WARN_BASE + 0x7FFF:"IVI_MAX_SPECIFIC_WARN_CODE     ",         
ERROR_BASE.IVI_WARN_BASE + 0x6000:"IVI_NI_WARN_BASE               ",         

ERROR_BASE._VI_ERROR + ERROR_BASE.IVI_STATUS_CODE_BASE	:"IVI_ERROR_BASE     ",         
ERROR_BASE.IVI_ERROR_BASE + 0x1000:"IVI_CROSS_CLASS_ERROR_BASE     ",         
ERROR_BASE.IVI_ERROR_BASE + 0x2000:"IVI_CLASS_ERROR_BASE           ",         
ERROR_BASE.IVI_ERROR_BASE + 0x4000:"IVI_SPECIFIC_ERROR_BASE        ",         
ERROR_BASE.IVI_ERROR_BASE + 0x7FFF:"IVI_MAX_SPECIFIC_ERROR_CODE    ",         
ERROR_BASE.IVI_ERROR_BASE + 0x6000:"IVI_NI_ERROR_BASE              ",         
ERROR_BASE.IVI_ERROR_BASE + 0x1000:"IVI_SHARED_COMPONENT_ERROR_BASE",         

    #/* IVI Foundation defined warnings */
ERROR_BASE.IVI_WARN_BASE + 0x65 : "IVI_WARN_NSUP_ID_QUERY    ",              
ERROR_BASE.IVI_WARN_BASE + 0x66 : "IVI_WARN_NSUP_RESET       ",              
ERROR_BASE.IVI_WARN_BASE + 0x67 : "IVI_WARN_NSUP_SELF_TEST   ",              
ERROR_BASE.IVI_WARN_BASE + 0x68 : "IVI_WARN_NSUP_ERROR_QUERY ",              
ERROR_BASE.IVI_WARN_BASE + 0x69 : "IVI_WARN_NSUP_REV_QUERY   ",              

    #/* IVI Foundation defined errors */
 ERROR_BASE.IVI_ERROR_BASE + 0x00 :"IVI_ERROR_CANNOT_RECOVER                ",
 ERROR_BASE.IVI_ERROR_BASE + 0x01 :"IVI_ERROR_INSTRUMENT_STATUS             ",
 ERROR_BASE.IVI_ERROR_BASE + 0x02 :"IVI_ERROR_CANNOT_OPEN_FILE              ",
 ERROR_BASE.IVI_ERROR_BASE + 0x03 :"IVI_ERROR_READING_FILE                  ",            
 ERROR_BASE.IVI_ERROR_BASE + 0x04 :"IVI_ERROR_WRITING_FILE                  ",            
 ERROR_BASE.IVI_ERROR_BASE + 0x0B :"IVI_ERROR_INVALID_PATHNAME              ",
 ERROR_BASE.IVI_ERROR_BASE + 0x0C :"IVI_ERROR_INVALID_ATTRIBUTE             ",
 ERROR_BASE.IVI_ERROR_BASE + 0x0D :"IVI_ERROR_IVI_ATTR_NOT_WRITABLE         ",
 ERROR_BASE.IVI_ERROR_BASE + 0x0E :"IVI_ERROR_IVI_ATTR_NOT_READABLE         ",
 ERROR_BASE.IVI_ERROR_BASE + 0x10 :"IVI_ERROR_INVALID_VALUE                 ",
 ERROR_BASE.IVI_ERROR_BASE + 0x11 :"IVI_ERROR_FUNCTION_NOT_SUPPORTED        ", 
 ERROR_BASE.IVI_ERROR_BASE + 0x12 :"IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED       ",
 ERROR_BASE.IVI_ERROR_BASE + 0x13 :"IVI_ERROR_VALUE_NOT_SUPPORTED           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x15 :"IVI_ERROR_TYPES_DO_NOT_MATCH            ",
 ERROR_BASE.IVI_ERROR_BASE + 0x1D :"IVI_ERROR_NOT_INITIALIZED               ",
 ERROR_BASE.IVI_ERROR_BASE + 0x20 :"IVI_ERROR_UNKNOWN_CHANNEL_NAME          ",
 ERROR_BASE.IVI_ERROR_BASE + 0x23 :"IVI_ERROR_TOO_MANY_OPEN_FILES           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x44 :"IVI_ERROR_CHANNEL_NAME_REQUIRED         ",
 ERROR_BASE.IVI_ERROR_BASE + 0x45 :"IVI_ERROR_CHANNEL_NAME_NOT_ALLOWED      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x49 :"IVI_ERROR_MISSING_OPTION_NAME           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x4A :"IVI_ERROR_MISSING_OPTION_VALUE          ",
 ERROR_BASE.IVI_ERROR_BASE + 0x4B :"IVI_ERROR_BAD_OPTION_NAME               ",
 ERROR_BASE.IVI_ERROR_BASE + 0x4C :"IVI_ERROR_BAD_OPTION_VALUE              ",
 ERROR_BASE.IVI_ERROR_BASE + 0x56 :"IVI_ERROR_OUT_OF_MEMORY                 ",
 ERROR_BASE.IVI_ERROR_BASE + 0x57 :"IVI_ERROR_OPERATION_PENDING             ",
 ERROR_BASE.IVI_ERROR_BASE + 0x58 :"IVI_ERROR_NULL_POINTER                  ",
 ERROR_BASE.IVI_ERROR_BASE + 0x59 :"IVI_ERROR_UNEXPECTED_RESPONSE           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x5B :"IVI_ERROR_FILE_NOT_FOUND                ",
 ERROR_BASE.IVI_ERROR_BASE + 0x5C :"IVI_ERROR_INVALID_FILE_FORMAT           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x5D :"IVI_ERROR_STATUS_NOT_AVAILABLE          ",
 ERROR_BASE.IVI_ERROR_BASE + 0x5E :"IVI_ERROR_ID_QUERY_FAILED               ",
 ERROR_BASE.IVI_ERROR_BASE + 0x5F :"IVI_ERROR_RESET_FAILED                  ",
 ERROR_BASE.IVI_ERROR_BASE + 0x60 :"IVI_ERROR_RESOURCE_UNKNOWN              ",
 ERROR_BASE.IVI_ERROR_BASE + 0x62 :"IVI_ERROR_CANNOT_CHANGE_SIMULATION_STATE",
 ERROR_BASE.IVI_ERROR_BASE + 0x63 :"IVI_ERROR_INVALID_NUMBER_OF_LEVELS_IN_SELECTOR",
 ERROR_BASE.IVI_ERROR_BASE + 0x64 :"IVI_ERROR_INVALID_RANGE_IN_SELECTOR",
 ERROR_BASE.IVI_ERROR_BASE + 0x65 :"IVI_ERROR_UNKOWN_NAME_IN_SELECTOR",
 ERROR_BASE.IVI_ERROR_BASE + 0x66 :"IVI_ERROR_BADLY_FORMED_SELECTOR",
 ERROR_BASE.IVI_ERROR_BASE + 0x67 :"IVI_ERROR_UNKNOWN_PHYSICAL_IDENTIFIER",

#/* IVI Foundation reserved (grandfathered) errors */
 ERROR_BASE.IVI_ERROR_BASE + 0x05 : "IVI_ERROR_DRIVER_MODULE_NOT_FOUND       ",
 ERROR_BASE.IVI_ERROR_BASE + 0x06 : "IVI_ERROR_CANNOT_OPEN_DRIVER_MODULE     ",            
 ERROR_BASE.IVI_ERROR_BASE + 0x07 : "IVI_ERROR_INVALID_DRIVER_MODULE         ",
 ERROR_BASE.IVI_ERROR_BASE + 0x08 : "IVI_ERROR_UNDEFINED_REFERENCES          ",
 ERROR_BASE.IVI_ERROR_BASE + 0x09 : "IVI_ERROR_FUNCTION_NOT_FOUND            ",
 ERROR_BASE.IVI_ERROR_BASE + 0x0A : "IVI_ERROR_LOADING_DRIVER_MODULE         ",
 ERROR_BASE.IVI_ERROR_BASE + 0x0F : "IVI_ERROR_INVALID_PARAMETER             ",
 ERROR_BASE.IVI_ERROR_BASE + 0x14 : "IVI_ERROR_INVALID_TYPE                  ",
 ERROR_BASE.IVI_ERROR_BASE + 0x16 : "IVI_ERROR_MULTIPLE_DEFERRED_SETTING     ",
 ERROR_BASE.IVI_ERROR_BASE + 0x17 : "IVI_ERROR_ITEM_ALREADY_EXISTS           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x18 : "IVI_ERROR_INVALID_CONFIGURATION         ",  
 ERROR_BASE.IVI_ERROR_BASE + 0x19 : "IVI_ERROR_VALUE_NOT_AVAILABLE           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x1A : "IVI_ERROR_ATTRIBUTE_VALUE_NOT_KNOWN     ", 
 ERROR_BASE.IVI_ERROR_BASE + 0x1B : "IVI_ERROR_NO_RANGE_TABLE                ",
 ERROR_BASE.IVI_ERROR_BASE + 0x1C : "IVI_ERROR_INVALID_RANGE_TABLE           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x1E : "IVI_ERROR_NON_INTERCHANGEABLE_BEHAVIOR  ",
 ERROR_BASE.IVI_ERROR_BASE + 0x1F : "IVI_ERROR_NO_CHANNEL_TABLE              ",
 ERROR_BASE.IVI_ERROR_BASE + 0x21 : "IVI_ERROR_SYS_RSRC_ALLOC                ",
 ERROR_BASE.IVI_ERROR_BASE + 0x22 : "IVI_ERROR_ACCESS_DENIED                 ",
 ERROR_BASE.IVI_ERROR_BASE + 0x24 : "IVI_ERROR_UNABLE_TO_CREATE_TEMP_FILE    ",
 ERROR_BASE.IVI_ERROR_BASE + 0x25 : "IVI_ERROR_NO_UNUSED_TEMP_FILENAMES      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x26 : "IVI_ERROR_DISK_FULL                     ",
 ERROR_BASE.IVI_ERROR_BASE + 0x27 : "IVI_ERROR_CONFIG_FILE_NOT_FOUND         ",
 ERROR_BASE.IVI_ERROR_BASE + 0x28 : "IVI_ERROR_CANNOT_OPEN_CONFIG_FILE       ",
 ERROR_BASE.IVI_ERROR_BASE + 0x29 : "IVI_ERROR_ERROR_READING_CONFIG_FILE     ",
 ERROR_BASE.IVI_ERROR_BASE + 0x2A : "IVI_ERROR_BAD_INTEGER_IN_CONFIG_FILE    ",
 ERROR_BASE.IVI_ERROR_BASE + 0x2B : "IVI_ERROR_BAD_DOUBLE_IN_CONFIG_FILE     ",
 ERROR_BASE.IVI_ERROR_BASE + 0x2C : "IVI_ERROR_BAD_BOOLEAN_IN_CONFIG_FILE    ",
 ERROR_BASE.IVI_ERROR_BASE + 0x2D : "IVI_ERROR_CONFIG_ENTRY_NOT_FOUND        ",
 ERROR_BASE.IVI_ERROR_BASE + 0x2E : "IVI_ERROR_DRIVER_DLL_INIT_FAILED        ",
 ERROR_BASE.IVI_ERROR_BASE + 0x2F : "IVI_ERROR_DRIVER_UNRESOLVED_SYMBOL      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x30 : "IVI_ERROR_CANNOT_FIND_CVI_RTE           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x31 : "IVI_ERROR_CANNOT_OPEN_CVI_RTE           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x32 : "IVI_ERROR_CVI_RTE_INVALID_FORMAT        ",
 ERROR_BASE.IVI_ERROR_BASE + 0x33 : "IVI_ERROR_CVI_RTE_MISSING_FUNCTION      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x34 : "IVI_ERROR_CVI_RTE_INIT_FAILED           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x35 : "IVI_ERROR_CVI_RTE_UNRESOLVED_SYMBOL     ",
 ERROR_BASE.IVI_ERROR_BASE + 0x36 : "IVI_ERROR_LOADING_CVI_RTE               ",
 ERROR_BASE.IVI_ERROR_BASE + 0x37 : "IVI_ERROR_CANNOT_OPEN_DLL_FOR_EXPORTS   ",
 ERROR_BASE.IVI_ERROR_BASE + 0x38 : "IVI_ERROR_DLL_CORRUPTED                 ",
 ERROR_BASE.IVI_ERROR_BASE + 0x39 : "IVI_ERROR_NO_DLL_EXPORT_TABLE           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x3A : "IVI_ERROR_UNKNOWN_DEFAULT_SETUP_ATTR    ",
 ERROR_BASE.IVI_ERROR_BASE + 0x3B : "IVI_ERROR_INVALID_DEFAULT_SETUP_VAL     ",
 ERROR_BASE.IVI_ERROR_BASE + 0x3C : "IVI_ERROR_UNKNOWN_MEMORY_PTR            ",
 ERROR_BASE.IVI_ERROR_BASE + 0x3D : "IVI_ERROR_EMPTY_CHANNEL_LIST            ",
 ERROR_BASE.IVI_ERROR_BASE + 0x3E : "IVI_ERROR_DUPLICATE_CHANNEL_STRING      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x3F : "IVI_ERROR_DUPLICATE_VIRT_CHAN_NAME      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x40 : "IVI_ERROR_MISSING_VIRT_CHAN_NAME        ",
 ERROR_BASE.IVI_ERROR_BASE + 0x41 : "IVI_ERROR_BAD_VIRT_CHAN_NAME            ",
 ERROR_BASE.IVI_ERROR_BASE + 0x42 : "IVI_ERROR_UNASSIGNED_VIRT_CHAN_NAME     ",
 ERROR_BASE.IVI_ERROR_BASE + 0x43 : "IVI_ERROR_BAD_VIRT_CHAN_ASSIGNMENT      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x46 : "IVI_ERROR_ATTR_NOT_VALID_FOR_CHANNEL    ",
 ERROR_BASE.IVI_ERROR_BASE + 0x47 : "IVI_ERROR_ATTR_MUST_BE_CHANNEL_BASED    ",
 ERROR_BASE.IVI_ERROR_BASE + 0x48 : "IVI_ERROR_CHANNEL_ALREADY_EXCLUDED      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x4D : "IVI_ERROR_NOT_CREATED_BY_CLASS          ",
 ERROR_BASE.IVI_ERROR_BASE + 0x4E : "IVI_ERROR_IVI_INI_IS_RESERVED           ",
 ERROR_BASE.IVI_ERROR_BASE + 0x4F : "IVI_ERROR_DUP_RUNTIME_CONFIG_ENTRY      ",
 ERROR_BASE.IVI_ERROR_BASE + 0x50 : "IVI_ERROR_INDEX_IS_ONE_BASED            ",
 ERROR_BASE.IVI_ERROR_BASE + 0x51 : "IVI_ERROR_INDEX_IS_TOO_HIGH             ",
 ERROR_BASE.IVI_ERROR_BASE + 0x52 : "IVI_ERROR_ATTR_NOT_CACHEABLE            ", 
 ERROR_BASE.IVI_ERROR_BASE + 0x53 : "IVI_ERROR_ADDR_ATTRS_MUST_BE_HIDDEN     ", 
 ERROR_BASE.IVI_ERROR_BASE + 0x54 : "IVI_ERROR_BAD_CHANNEL_NAME              ",
 ERROR_BASE.IVI_ERROR_BASE + 0x55 : "IVI_ERROR_BAD_PREFIX_IN_CONFIG_FILE     ",

#/* NI-Specific errors */
 ERROR_BASE.IVI_NI_ERROR_BASE + 0	: "IVI_ERROR_CANNOT_MODIFY_REPEATED_CAPABILITY_TABLE  ",
 ERROR_BASE.IVI_NI_ERROR_BASE + 1	: "IVI_ERROR_CANNOT_RESTRICT_ATTRIBUTE_TWICE          ",
 ERROR_BASE.IVI_NI_ERROR_BASE + 2	: "IVI_ERROR_REPEATED_CAPABILITY_ALREADY_EXISTS       ",
 ERROR_BASE.IVI_NI_ERROR_BASE + 3	: "IVI_ERROR_REPEATED_CAPABILITY_NOT_DEFINED          ",
 ERROR_BASE.IVI_NI_ERROR_BASE + 4	: "IVI_ERROR_INVALID_REPEATED_CAPABILITY_NAME         ",
 ERROR_BASE.IVI_NI_ERROR_BASE + 0xD : "IVI_ERROR_CONFIG_SERVER_NOT_PRESENT                ",

#/* NI-Specific renamed errors.  */
# IVI_ERROR_REPEATED_CAPABILITY_NAME_REQUIRED        IVI_ERROR_CHANNEL_NAME_REQUIRED
# IVI_ERROR_UNKNOWN_REPEATED_CAPABILITY_NAME         IVI_ERROR_UNKNOWN_CHANNEL_NAME
# IVI_ERROR_EMPTY_REPEATED_CAPABILITY_LIST           IVI_ERROR_EMPTY_CHANNEL_LIST
# IVI_ERROR_DUPLICATE_REPEATED_CAPABILITY_IDENTIFIER IVI_ERROR_DUPLICATE_CHANNEL_STRING
# IVI_ERROR_REPEATED_CAPABILITY_NAME_NOT_ALLOWED     IVI_ERROR_CHANNEL_NAME_NOT_ALLOWED
# IVI_ERROR_ATTR_NOT_VALID_FOR_REPEATED_CAPABILITY   IVI_ERROR_ATTR_NOT_VALID_FOR_CHANNEL
# IVI_ERROR_ATTR_MUST_BE_REPEATED_CAPABILITY_BASED   IVI_ERROR_ATTR_MUST_BE_CHANNEL_BASED
# IVI_ERROR_BAD_REPEATED_CAPABILITY_NAME             IVI_ERROR_BAD_CHANNEL_NAME
        
#/*  renamed errors. Do not use these identifiers in your drivers and applications. */
 ERROR_BASE.IVI_ERROR_BASE + 0x00 : "IVI_ERROR_CANNOT_LOAD_IVI_ENGINE",        
 ERROR_BASE.IVI_ERROR_BASE + 0x01 : "IVI_ERROR_INSTR_SPECIFIC        ",        
 ERROR_BASE.IVI_ERROR_BASE + 0x23 : "IVI_ERROR_TOO_MANY_FILES_OPEN   ",        

#/*  obsolete errors. Do not use these identifiers in your drivers and applications. */
 ERROR_BASE.IVI_ERROR_BASE + 0x61 : "IVI_ERROR_ALREADY_INITIALIZED   ",
#################################################################################### 
#vpptype.h
####################################################################################

ERROR_BASE._VI_ERROR+0x3FFC0001 : "LVI_ERROR_PARAMETER1   ",
ERROR_BASE._VI_ERROR+0x3FFC0002 : "LVI_ERROR_PARAMETER2   ",
ERROR_BASE._VI_ERROR+0x3FFC0003 : "LVI_ERROR_PARAMETER3   ",
ERROR_BASE._VI_ERROR+0x3FFC0004 : "LVI_ERROR_PARAMETER4   ",
ERROR_BASE._VI_ERROR+0x3FFC0005 : "LVI_ERROR_PARAMETER5   ",
ERROR_BASE._VI_ERROR+0x3FFC0006 : "LVI_ERROR_PARAMETER6   ",
ERROR_BASE._VI_ERROR+0x3FFC0007 : "LVI_ERROR_PARAMETER7   ",
ERROR_BASE._VI_ERROR+0x3FFC0008 : "LVI_ERROR_PARAMETER8   ",
ERROR_BASE._VI_ERROR+0x3FFC0011 : "LVI_ERROR_FAIL_ID_QUERY",
ERROR_BASE._VI_ERROR+0x3FFC0012 : "LVI_ERROR_INV_RESPONSE "
 
 
 }
 
WARNINGS = {
	1073676290 : "VI_SUCCESS_EVENT_EN         ",#          (0x3FFF0002L)
	1073676291 : "VI_SUCCESS_EVENT_DIS        ",#          (0x3FFF0003L)
	1073676292 : "VI_SUCCESS_QUEUE_EMPTY      ",#          (0x3FFF0004L)
	1073676293 : "VI_SUCCESS_TERM_CHAR        ",#          (0x3FFF0005L)
	1073676294 : "VI_SUCCESS_MAX_CNT          ",#          (0x3FFF0006L)
	1073676413 : "VI_SUCCESS_DEV_NPRESENT     ",#          (0x3FFF007DL)
	1073676414 : "VI_SUCCESS_TRIG_MAPPED      ",#          (0x3FFF007EL)
	1073676416 : "VI_SUCCESS_QUEUE_NEMPTY     ",#          (0x3FFF0080L)
	1073676440 : "VI_SUCCESS_NCHAIN           ",#          (0x3FFF0098L)
	1073676441 : "VI_SUCCESS_NESTED_SHARED    ",#          (0x3FFF0099L)
	1073676442 : "VI_SUCCESS_NESTED_EXCLUSIVE ",#          (0x3FFF009AL)
	1073676443 : "VI_SUCCESS_SYNC             ",#          (0x3FFF009BL)
	
	1073676300 : "VI_WARN_QUEUE_OVERFLOW      ",#          (0x3FFF000CL)
	1073676407 : "VI_WARN_CONFIG_NLOADED      ",#          (0x3FFF0077L)
	1073676418 : "VI_WARN_NULL_OBJECT         ",#          (0x3FFF0082L)
	1073676420 : "VI_WARN_NSUP_ATTR_STATE     ",#          (0x3FFF0084L)
	1073676421 : "VI_WARN_UNKNOWN_STATUS      ",#          (0x3FFF0085L)
	1073676424 : "VI_WARN_NSUP_BUF            ",#          (0x3FFF0088L)
	1073676457 : "VI_WARN_EXT_FUNC_NIMPL      ",#          (0x3FFF00A9L)

#################################################################################### 
#vpptype.h
####################################################################################
	0x3FFC0101 : "LVI_WARN_NSUP_ID_QUERY   ",
	0x3FFC0102 : "LVI_WARN_NSUP_RESET      ",
	0x3FFC0103 : "LVI_WARN_NSUP_SELF_TEST  ",
	0x3FFC0104 : "LVI_WARN_NSUP_ERROR_QUERY",
	0x3FFC0105 : "LVI_WARN_NSUP_REV_QUERY  "
}
