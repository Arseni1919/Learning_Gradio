import gradio as gr
import numpy as np
import random

# def greet(name):
#     return "Hello " + name + "!!"
# ------------------------------------------------------------------------ #
# iface = gr.Interface(
#     fn=greet,
#     inputs="text",
#     outputs="text"
# )
# ------------------------------------------------------------------------ #
# iface = gr.Interface(
#   fn=greet,
#   inputs=gr.inputs.Textbox(lines=20, placeholder="Name Here..."),
#   outputs="text")
# ------------------------------------------------------------------------ #
# def greet(name, is_morning, temperature):
#   salutation = "Good morning" if is_morning else "Good evening"
#   greeting = "%s %s. It is %s degrees today" % (
#     salutation, name, temperature)
#   celsius = (temperature - 32) * 5 / 9
#   return greeting, round(celsius, 2)
#
# iface = gr.Interface(
#   fn=greet,
#   inputs=["text", "checkbox", gr.inputs.Slider(0, 100)],
#   outputs=["text", "number"])
# ------------------------------------------------------------------------ #
# def sepia(img):
#   sepia_filter = np.array([[.393, .769, .189],
#                            [.349, .686, .168],
#                            [.272, .534, .131]])
#   sepia_img = img.dot(sepia_filter.T)
#   sepia_img /= sepia_img.max()
#   return sepia_img
#
# iface = gr.Interface(sepia, gr.inputs.Image(shape=(200, 200)), "image")
# Additionally, our Image input interface comes with an 'edit' button
# which opens tools for cropping, flipping, rotating, drawing over,
# and applying filters to images.
# We've found that manipulating images in this way will often reveal
# hidden flaws in a model.
# ------------------------------------------------------------------------ #
def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2

iface = gr.Interface(calculator,
    ["number", gr.inputs.Radio(["add", "subtract", "multiply", "divide"]), "number"],
    "number",
    examples=[
        [5, "add", 3],
        [4, "divide", 2],
        [-4, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
)
# ------------------------------------------------------------------------ #
male_words, female_words = ["he", "his", "him"], ["she", "her"]
def gender_of_sentence(sentence):
  male_count = len([word for word in sentence.split() if word.lower() in male_words])
  female_count = len([word for word in sentence.split() if word.lower() in female_words])
  total = max(male_count + female_count, 1)
  return {"male": male_count / total, "female": female_count / total}

iface = gr.Interface(
  fn=gender_of_sentence, inputs=gr.inputs.Textbox(default="She went to his house to get her keys."),
  outputs="label", interpretation="default")
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
iface.launch()
# iface.launch(share=True)
