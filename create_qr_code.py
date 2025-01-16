import qrcode  # qrcode 모듈을 가져옵니다.

# QRCode 생성기 초기화
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# QR코드에 데이터 추가
qr.add_data("https://byebye-mu.vercel.app/")  # 여기에 배포된 URL을 입력하세요.
qr.make(fit=True)

# QR 코드 이미지 생성
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")  # qrcode.png 파일로 저장
