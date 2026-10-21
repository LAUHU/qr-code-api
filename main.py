import io
import qrcode
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/v1/qr/generate")
def generate_qr(text: str):
  # Genera l'immagine del QR Code in memoria
  img = qrcode.make(text)
  buf = io.BytesIO()
  img.save(buf, format="PNG")
  buf.seek(0)
  return StreamingResponse(buf, media_type="image/png")