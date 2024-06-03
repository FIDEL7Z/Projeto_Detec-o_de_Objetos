import cv2
import time

COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]

class_names = []
with open("coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

cap = cv2.VideoCapture("VIdeoteste.mp4")

net = cv2.dnn.readNetFromDarknet("yolov4-tiny.cfg", "yolov4-tiny.weights")

model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    start = time.time()

    
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)

    end = time.time()

    for (classid, score, box) in zip(classes, scores, boxes):
        
        color = COLORS[int(classid) % len(COLORS)]

    
        label = f"{class_names[classid]}: {int(score * 100)}%"
       
        cv2.rectangle(frame, box, color, 2)
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                    
    fps_label = f"FPS: {round((1.0 / (end - start)), 1)}"

    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Projeto - Detecção de Objetos", frame)

  
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
