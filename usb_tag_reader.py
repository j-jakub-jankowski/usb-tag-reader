from ctypes import *

class Reader:
    #
    def __init__(self):
        self.mydll = windll.LoadLibrary('C:/Users/jjaku/Desktop/USB_UHFReader.dll')

    def open_reader(self):
        open_ = self.mydll.API_OpenUsb()
        if open_ != 1:
            print('Waiting for tag')
        else:
            print('Reconnect')

    def close_reader(self):
        close_ = self.mydll.API_CloseUsb()
        if close_ != 1:
            print('Reader was closed')
        else:
            print('Closing was failed')

    @property
    def read_tag(self):
        uLen = c_ubyte()
        uReadData = bytes(10)
        assert isinstance(self.mydll.API_InventoryOnce, object)
        read_tag_hex = self.mydll.API_InventoryOnce
        tag_int = None
        read_ = read_tag_hex(uReadData, byref(uLen))
        if read_ == 0:
            tag_hex = uReadData.hex()
            a = int.from_bytes(uLen, byteorder='big') * 2
            tag_int = int(tag_hex[a - 4:a], 16)
        return tag_int



