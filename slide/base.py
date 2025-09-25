import base64

# 画像をbase64に変換する関数
def image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def image_to_data_uri(image_path: str, mime_type: str = "image/png") -> str:
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded_string}"

# 例：使い方
if __name__ == "__main__":
    data_uri = image_to_data_uri("2025-09-26-01-36-41.png")
    with open("image_md.txt", "w") as f:
        f.write(f"![説明文]({data_uri})")
