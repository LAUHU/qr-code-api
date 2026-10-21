from fastapi import FastAPI, Response
import qrcode
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Benvenuto nella QR Code API! Usa /v1/generate?text=tuo_testo"}

@app.get("/v1/generate")
def generate_qr(text: str = "https://rapidapi.com"):
    img = qrcode.make(text)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return Response(content=buf.getvalue(), media_type="image/png")
