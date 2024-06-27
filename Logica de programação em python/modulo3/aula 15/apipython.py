import google.generativeai as genai
import PIL.Image

# Configure the API key diretamente
genai.configure(api_key="AIzaSyDSPnyubixbAbJk8bM9l9fXUIZUhmQF6Hs")

def analyze_image(image_path):
    # Open the image
    img = PIL.Image.open(image_path)

    # Initialize the model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Generate the content using the image object
    response = model.generate_content(["O que tem na foto? Responda em português", img])

    return response.text

if __name__ == "__main__":
    # Use o caminho correto para a imagem carregada
    image_path = 'C:/Users/62129532024.1/Downloads/AulasProgramacao/aulas/Logica de programação em python/modulo3/aula 15/imagem.png'  # Caminho para a imagem carregada
    analysis_result = analyze_image(image_path)
    print("Resultado da análise:", analysis_result)