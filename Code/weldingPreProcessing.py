def process(content):
    import io
    from PIL import Image
    import numpy as np
    
    im = Image.open(io.BytesIO(content)).convert('RGB')       
    x = np.array(im)
    x = x.astype(np.float32)
    x = x/255.
    x = np.expand_dims(x, axis=(0))
    return {"input":x}
