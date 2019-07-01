
# [HillCypher](https://hillcipher.herokuapp.com)

Hill cipher is a polygraphic substitution ciper.Each letter is represented by a number modulo 26

A=0,B=1,...Z=25
## Encryption
Each block of letters(considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26.

## Decryption
Each block is multiplied by the inverse of the matrix used for encryption.
