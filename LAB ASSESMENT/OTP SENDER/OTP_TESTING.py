from OTP import otp_sender
import unittest

class TestingOTPSender(unittest.TestCase):
    def assertBetween(self, x, low, hi):
        if not (low <= x <= hi):
            raise AssertionError(
                'Length of OTP should be in between %r and %r' % (low, hi))

    def test_generateOTP(self):
        OTP = otp_sender()
        OTP.size = 5

        self.assertBetween(OTP.size, 4, 8)

        OTP.generateOTP()
        self.assertEqual(len(OTP.Otp), OTP.size, 'OTP length does not match')

    def test_verifyOTP(self):
        OTP = otp_sender()
        OTP.size = 5

        OTP.generateOTP()

        self.assertTrue(OTP.verifyOTP(OTP.Otp), "OTP does not match")
        self.assertFalse(OTP.verifyOTP('abcd'),
                        "OTP should not have matched")

    def test_validateEmail(self):
        receiver_email = 'username@domain.in'

        self.assertIn('@', receiver_email, "Email is not valid")
        self.assertIn('.in', receiver_email, "Email is not valid")

    def test_validateEmail2(self):
        receiver_email = 'username@domain.com'

        self.assertIn('@', receiver_email, "Email is not valid")
        self.assertIn('.com', receiver_email, "Email is not valid")

    def test_sendOTP(self):
        OTP = otp_sender()

        OTP.size = 5
        self.assertBetween(OTP.size, 4, 8)

        OTP.generateOTP()
        self.assertIsNotNone(OTP.Otp, "OTP is null")

        OTP.receiver_email = 'rohitgendsolapur@gmail.com'
        self.assertIn('@', OTP.receiver_email, "Email is not valid")
        self.assertIn('.in', OTP.receiver_email, "Email is not valid")

        OTP.sendOTP()


if __name__ == '__main__':
    unittest.main()