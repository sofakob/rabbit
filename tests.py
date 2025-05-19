import unittest 
from laba import chitaem_z, inisialisation_for_key, next

class Test_Z(unittest.TestCase):
    def test_z_1(self):
        keys="00000000000000000000000000000000"
        vec="0000000000000000"
        z=[]
        z=chitaem_z(keys, vec, z)
        z_str=""
        for i in range(len(z)):
            z_str+=str(hex(z[i])[2:].zfill(4))
        z_test="EDB70567375DCD7CD89554F85E27A7C68D4ADC7032298F7BD4EFF504ACA6295F668FBF478ADB2BE51E6CDE292B82DE2AB48D2AC6565979220EC909A7E7576098"
        self.assertEqual(z_str.upper(), z_test)

    def test_z_2(self):
        keys="00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
        vec="00 01 02 03 04 05 06 07"
        keys="".join(keys.split())
        vec="".join(vec.split())
        z=[]
        z=chitaem_z(keys, vec, z)
        z_str=""
        for i in range(len(z)):
            z_str+=str(hex(z[i])[2:].zfill(4))
        z_test=" 98 71 C7 BA 4E A3 08 07 CD AA 49 64 66 39 2D 2F 4A FF 43 55 EF 90 69 56 10 9B 96 65 97 8D AC ED9B 7C 6F 7F C8 2C 67 D2 73 22 CB DE 9D B0 16 45 8C 38 2C 9C 7D 30 44 E6 52 0B B9 2A 1353 C0 FF"
        z_test=''.join(z_test.split())
        self.assertEqual(z_str.upper(), z_test)
    def test_z_3(self):
        keys="00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F"
        vec=" 00 00 00 00 00 00 00 00"
        keys="".join(keys.split())
        vec="".join(vec.split())
        z=[]
        z=chitaem_z(keys, vec, z)
        z_str=""
        for i in range(len(z)):
            z_str+=str(hex(z[i])[2:].zfill(4))
        z_test="A8 F7 E6 9B 69 40 A7 8D 13 6A 5C 15 4A 15 79 52 A6 E4 23 58 59 E3 02 20 EA 68 64 36 BB 38 EF 539C 29 40 55 6B 09 EC D7 FE A2 B0 AC 83 07 F1 69 62 65 A3 D6 44 28 1C 39 C9 CD 5E 1E 2F 9B E4 D0"
        z_test=''.join(z_test.split())
        self.assertEqual(z_str.upper(), z_test)
    def test_z_4(self):
        keys="00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F "
        vec="00 01 02 03 04 05 06 07"
        keys="".join(keys.split())
        vec="".join(vec.split())
        z=[]
        z=chitaem_z(keys, vec, z)
        z_str=""
        for i in range(len(z)):
            z_str+=str(hex(z[i])[2:].zfill(4))
        z_test=" F2 89 19 DD A1 28 F8 F9 0A 30 34 6E 97 94 D2 B7 4C 69 A2 D9 91 37 27 BC 5A 30 18 E6 33 2A F7 F3BE 3A C3 EF B3 68 F4 3A 4C B8 58 67 B8 1C 91 F9 24 29 0C 81 6B 8B 57 88 98 C5 7F B4 C0 BA 05 BD"
        z_test=''.join(z_test.split())
        self.assertEqual(z_str.upper(), z_test)
    def test_z_5_minus_9(self):
        keys="00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F "
        vec="00 01 02 03 04 05 06 07"
        keys="".join(keys.split())
        vec="".join(vec.split())
        key=inisialisation_for_key(keys)
        x=[0]*8
        c=[0]*8
        for j in range(8):
            if j%2==0:
                x[j]=key[(j+1)%8]+key[(j)%8]
                c[j]=key[(j+4)%8]+key[(j+5)%8]
            else:
                x[j]=key[(j+5)%8]+key[(j+4)%8]
                c[j]=key[j]+key[(j+1)%8]
        for i in range(8):
            x[i]=int(x[i], 16)
            c[i]=int(c[i], 16)
        test=[x, c]
        test_data=[[0x03020100, 0x0D0C0B0A, 0x07060504, 0x01000F0E, 0x0B0A0908, 0x05040302, 0x0F0E0D0C, 0x09080706], [0x09080B0A, 0x03020504, 0x0D0C0F0E, 0x07060908,  0x01000302,  0x0B0A0D0C,  0x05040706, 0x0F0E0100]]
        self.assertEqual(test, test_data)
    def test_z_5_minus_8(self):
        keys="00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F "
        vec="00 01 02 03 04 05 06 07"
        keys="".join(keys.split())
        vec="".join(vec.split())
        key=inisialisation_for_key(keys)
        x=[0]*8
        c=[0]*8
        for j in range(8):
            if j%2==0:
                x[j]=key[(j+1)%8]+key[(j)%8]
                c[j]=key[(j+4)%8]+key[(j+5)%8]
            else:
                x[j]=key[(j+5)%8]+key[(j+4)%8]
                c[j]=key[j]+key[(j+1)%8]
        for i in range(8):
            x[i]=int(x[i], 16)
            c[i]=int(c[i], 16)
        b=0
        b, x, c=next(b, x, c)
        test=[x, c]
        test_data=[[0x05783933, 0x162113C0, 0xB38F168E, 0xF08A919E, 0x7F2CDA94, 0xACBEB878, 0x0D5257A9, 0x4FF46B46], [0x563CDE57, 0xD64F39D7, 0x41DF5C42, 0x543ADC55,  0xD44D37D5,  0x3FDD5A40,  0x5238DA53, 0xE25B35D3]]
        self.assertEqual(test, test_data)
    def test_z_5_minus_7(self):
        keys="00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F "
        vec="00 01 02 03 04 05 06 07"
        keys="".join(keys.split())
        vec="".join(vec.split())
        key=inisialisation_for_key(keys)
        x=[0]*8
        c=[0]*8
        for j in range(8):
            if j%2==0:
                x[j]=key[(j+1)%8]+key[(j)%8]
                c[j]=key[(j+4)%8]+key[(j+5)%8]
            else:
                x[j]=key[(j+5)%8]+key[(j+4)%8]
                c[j]=key[j]+key[(j+1)%8]
        for i in range(8):
            x[i]=int(x[i], 16)
            c[i]=int(c[i], 16)
        b=0
        for i in range(2):
            b, x, c=next(b, x, c)
        test=[x, c]
        test_data=[[0x798C2CEC, 0xCC05FFD4, 0x50D68324, 0x2C306745, 0xAD519559, 0x81595E7A, 0x29A589E2, 0x15212B97], [0xA371B1A4, 0xA99C6EAA, 0x76B2A977, 0xA16FAFA2,  0xA79A6CA8,  0x74B0A775,  0x9F6DADA0, 0xB5A86AA6]]
        self.assertEqual(test, test_data)



if __name__ == "__main__":
    unittest.main()
