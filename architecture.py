import numpy as np

# REGESTERS

registerA = 0
registerB = 0
registerC = 0
registerD = 0
registerE = 0
registerH = 0
registerL = 0

# Program Counter

PC = 0

# flags

sign = False
zero = False
aux_carry = False
parity = False
carry = False

# Memory

memory = np.empty((256,256))

