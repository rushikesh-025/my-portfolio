import qrcode

# Portfolio URL
portfolio_url = "https://its-rushi.netlify.app/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(portfolio_url)
qr.make(fit=True)

# Create QR image
img = qr.make_image(fill_color="black", back_color="white")

# Save it
img.save("portfolio_qr.png")

print("✅ Clean QR code generated successfully! (Saved as portfolio_qr.png)")
