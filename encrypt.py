class Cipher():
    # Python3 code to implement Hill Cipher

    def __init__(self):

        self.keyMatrix = [[0] * 3 for i in range(3)]

    # Generate vector for the message
        self.messageVector = [[0] for i in range(3)]

    # Generate vector for the cipher
        self.cipherMatrix = [[0] for i in range(3)]

    # Following function generates the
    # key matrix for the key string
    def getKeyMatrix(self,key):
        k = 0
        for i in range(3):
            for j in range(3):
                self.keyMatrix[i][j] = ord(key[k]) % 65
                k += 1

    # Following function encrypts the message
    def encrypt(self,messageVector):
        for i in range(3):
            for j in range(1):
                self.cipherMatrix[i][j] = 0
                for x in range(3):
                    self.cipherMatrix[i][j] += (self.keyMatrix[i][x] *
                                        self.messageVector[x][j])
                self.cipherMatrix[i][j] = self.cipherMatrix[i][j] % 26

    def HillCipher(self,message, key):

        # Get key matrix from the key string
        self.getKeyMatrix(key)

        # Generate vector for the message
        for i in range(3):
            self.messageVector[i][0] = ord(message[i]) % 65

        # Following function generates
        # the encrypted vector
        self.encrypt(self.messageVector)

        # Generate the encrypted text
        # from the encrypted vector
        CipherText = []
        for i in range(3):
            CipherText.append(chr(self.cipherMatrix[i][0] + 65))

        # Finally print the ciphertext
        return CipherText
