
input_img_path=input('Path of the Image to be Predicted')
input_image=cv2.imread(input_img_path)
cv2_imshow(input_image)

input_image_resized= cv2.resize(input_image, (128,128))
input_image_scaled =input_image_resized/255
input_image_reshaped=np.reshape(input_image_scaled, [1,128,128,3])
input_prediction=model.predict(input_image_reshaped)
print(input_prediction)

input_pred_label=np.argmax(input_prediction)
print(input_pred_label)

if input_pred_label ==1:
  print("The person is wearing a Mask")

else:
  print("The person is nor wearing a Mask")