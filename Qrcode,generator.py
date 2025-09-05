import qrcode

#taking upi id as input
upi_id = input("enter your upi id =")

#upi://pay?pa=upi_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#defining the payment based on upi id and the payment app
#you can modify these url based on the payment apps you want to support

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code for each payment app
phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save qr code to image file
phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#dispaly the qr code ( install pillow library before display)
phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()