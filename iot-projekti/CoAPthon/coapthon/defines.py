import collections

__author__ = 'Giacomo Tanganelli'
__version__ = "3.0"

''' CoAP Parameters '''

ACK_TIMEOUT = 2  # standard 2

SEPARATE_TIMEOUT = ACK_TIMEOUT / 2

ACK_RANDOM_FACTOR = 1.5

MAX_RETRANSMIT = 4

MAX_TRANSMIT_SPAN = ACK_TIMEOUT * (pow(2, (MAX_RETRANSMIT + 1)) - 1) * ACK_RANDOM_FACTOR

MAX_LATENCY = 120  # 2 minutes

PROCESSING_DELAY = ACK_TIMEOUT

MAX_RTT = (2 * MAX_LATENCY) + PROCESSING_DELAY

EXCHANGE_LIFETIME = MAX_TRANSMIT_SPAN + (2 * MAX_LATENCY) + PROCESSING_DELAY

DISCOVERY_URL = "/.well-known/core"

ALL_COAP_NODES = "224.0.1.187"

MAX_PAYLOAD = 1024

MAX_NON_NOTIFICATIONS = 10

BLOCKWISE_SIZE = 1024

'''  Message Format '''

# number of bits used for the encoding of the CoAP version field.
VERSION_BITS = 2

# number of bits used for the encoding of the message type field.
TYPE_BITS = 2

# number of bits used for the encoding of the token length field.
TOKEN_LENGTH_BITS = 4

# number of bits used for the encoding of the request method/response code field.
CODE_BITS = 8

# number of bits used for the encoding of the message ID.
MESSAGE_ID_BITS = 16

# number of bits used for the encoding of the option delta field.
OPTION_DELTA_BITS = 4

# number of bits used for the encoding of the option delta field.
OPTION_LENGTH_BITS = 4

# One byte which indicates indicates the end of options and the start of the payload.
PAYLOAD_MARKER = 0xFF

# CoAP version supported by this Californium version.
VERSION = 1

# The lowest value of a request code.
REQUEST_CODE_LOWER_BOUND = 1

# The highest value of a request code.
REQUEST_CODE_UPPER_BOUND = 31

# The lowest value of a response code.
RESPONSE_CODE_LOWER_BOUND = 64

# The highest value of a response code.
RESPONSE_CODE_UPPER_BOUND = 191

corelinkformat = {
    'ct': 'content_type',
    'rt': 'resource_type',
    'if': 'interface_type',
    'sz': 'maximum_size_estimated'
}

# The integer.
INTEGER = 0
# The string.
STRING = 1
# The opaque.
OPAQUE = 2
# The unknown.
UNKNOWN = 3

OptionItem = collections.namedtuple('OptionItem', 'number name value_type repeatable default')


# (NAME, VALUE_TYPE, REPEATABLE, DEFAULT)
class OptionRegistry(object):

    def __init__(self):
        pass

    RESERVED = OptionItem(0, "Reserved", UNKNOWN, True, None)
    IF_MATCH = OptionItem(1, "If-Match", OPAQUE, True, None)
    URI_HOST = OptionItem(3, "Uri-Host", STRING, True, None)
    ETAG = OptionItem(4, "ETag", OPAQUE, True, None)
    IF_NONE_MATCH = OptionItem(5, "If-None-Match", INTEGER, False, None)
    OBSERVE = OptionItem(6, "Observe", INTEGER, False, 0)
    URI_PORT = OptionItem(7, "Uri-Port", INTEGER, False, 5683)
    LOCATION_PATH = OptionItem(8, "Location-Path", STRING, True, None)
    URI_PATH = OptionItem(11, "Uri-Path", STRING, True, None)
    CONTENT_TYPE = OptionItem(12, "Content-Type", INTEGER, False, 0)
    MAX_AGE = OptionItem(14, "Max-Age", INTEGER, False, 60)
    URI_QUERY = OptionItem(15, "Uri-Query", STRING, True, None)
    ACCEPT = OptionItem(17, "Accept", INTEGER, False, 0)
    LOCATION_QUERY = OptionItem(20, "Location-Query", STRING, True, None)
    BLOCK2 = OptionItem(23, "Block2", INTEGER, False, None)
    BLOCK1 = OptionItem(27, "Block1", INTEGER, False, None)
    PROXY_URI = OptionItem(35, "Proxy-Uri", STRING, False, None)
    PROXY_SCHEME = OptionItem(39, "Proxy-Schema", STRING, False, None)
    SIZE1 = OptionItem(60, "Size1", INTEGER, False, None)

    LIST = {
        0: RESERVED,
        1: IF_MATCH,
        3: URI_HOST,
        4: ETAG,
        5: IF_MATCH,
        6: OBSERVE,
        7: URI_PORT,
        8: LOCATION_PATH,
        11: URI_PATH,
        12: CONTENT_TYPE,
        14: MAX_AGE,
        15: URI_QUERY,
        17: ACCEPT,
        20: LOCATION_QUERY,
        23: BLOCK2,
        27: BLOCK1,
        35: PROXY_URI,
        39: PROXY_SCHEME,
        60: SIZE1

    }


Types = {
    'CON': 0,
    'NON': 1,
    'ACK': 2,
    'RST': 3,
    'None': None
}

CodeItem = collections.namedtuple('CodeItem', 'number name')


class Codes(object):
    ERROR_LOWER_BOUND = 128

    EMPTY = CodeItem(0, 'EMPTY')
    GET = CodeItem(1, 'GET')
    POST = CodeItem(2, 'POST')
    PUT = CodeItem(3, 'PUT')
    DELETE = CodeItem(4, 'DELETE')

    CREATED = CodeItem(65, 'CREATED')
    DELETED = CodeItem(66, 'DELETED')
    VALID = CodeItem(67, 'VALID')
    CHANGED = CodeItem(68, 'CHANGED')
    CONTENT = CodeItem(69, 'CONTENT')
    CONTINUE = CodeItem(95, 'CONTINUE')

    BAD_REQUEST = CodeItem(128, 'BAD_REQUEST')
    FORBIDDEN = CodeItem(131, 'FORBIDDEN')
    NOT_FOUND = CodeItem(132, 'NOT_FOUND')
    METHOD_NOT_ALLOWED = CodeItem(133, 'METHOD_NOT_ALLOWED')
    NOT_ACCEPTABLE = CodeItem(134, 'NOT_ACCEPTABLE')
    REQUEST_ENTITY_INCOMPLETE = CodeItem(136, 'REQUEST_ENTITY_INCOMPLETE')
    PRECONDITION_FAILED = CodeItem(140, 'PRECONDITION_FAILED')
    REQUEST_ENTITY_TOO_LARGE = CodeItem(141, 'REQUEST_ENTITY_TOO_LARGE')
    UNSUPPORTED_CONTENT_FORMAT = CodeItem(143, 'UNSUPPORTED_CONTENT_FORMAT')

    INTERNAL_SERVER_ERROR = CodeItem(160, 'INTERNAL_SERVER_ERROR')
    NOT_IMPLEMENTED = CodeItem(161, 'NOT_IMPLEMENTED')
    BAD_GATEWAY = CodeItem(162, 'BAD_GATEWAY')
    SERVICE_UNAVAILABLE = CodeItem(163, 'SERVICE_UNAVAILABLE')
    GATEWAY_TIMEOUT = CodeItem(164, 'GATEWAY_TIMEOUT')
    PROXY_NOT_SUPPORTED = CodeItem(165, 'PROXY_NOT_SUPPORTED')

    LIST = {
        0: EMPTY,
        1: GET,
        2: POST,
        3: PUT,
        4: DELETE,

        65: CREATED,
        66: DELETE,
        67: VALID,
        68: CHANGED,
        69: CONTENT,
        95: CONTINUE,

        128: BAD_REQUEST,
        131: FORBIDDEN,
        132: NOT_FOUND,
        133: METHOD_NOT_ALLOWED,
        134: NOT_ACCEPTABLE,
        136: REQUEST_ENTITY_INCOMPLETE,
        140: PRECONDITION_FAILED,
        141: REQUEST_ENTITY_TOO_LARGE,
        143: UNSUPPORTED_CONTENT_FORMAT,

        160: INTERNAL_SERVER_ERROR,
        161: NOT_IMPLEMENTED,
        162: BAD_GATEWAY,
        163:SERVICE_UNAVAILABLE,
        164: GATEWAY_TIMEOUT,
        165: PROXY_NOT_SUPPORTED

    }


Content_types = {
    "text/plain": 0,
    "application/link-format": 40,
    "application/xml": 41,
    "application/octet-stream": 42,
    "application/exi": 47,
    "application/json": 50
}
