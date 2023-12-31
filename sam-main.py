
from segment_anything import SamPredictor, sam_model_registry

# Specify the model type and the path to the checkpoint
model_type = "deeplabv3_resnet50"
checkpoint_path = "./sam_vit_b_01ec64.pth"

# Instantiate a segmentation model using the specified model type and checkpoint
#sam = sam_model_registry[model_type](checkpoint=checkpoint_path)

sam = sam_model_registry["default"](checkpoint="./sam_vit_b_01ec64.pth")


# Create a predictor using the segmentation model
predictor = SamPredictor(sam)

# Set an image for prediction
your_image = "./1234.jpg"
predictor.set_image(your_image)

# Specify input prompts for segmentation
input_prompts = "a person standing in front of a building"

# Make a prediction to obtain segmentation masks
masks, _, _ = predictor.predict(input_prompts)

# The 'masks' variable now contains the segmentation masks predicted by the model
