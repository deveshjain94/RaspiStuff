#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv/opencv.h>

using namespace std;
using namespace cv;

int main(){
Mat img1,img2;
VideoCapture capture0(0);
VideoCapture capture1(1);
capture0.set(CV_CAP_PROP_FRAME_WIDTH,1280); 	//set resolution of image
capture0.set(CV_CAP_PROP_FRAME_HEIGHT,960);

capture1.set(CV_CAP_PROP_FRAME_WIDTH,1280); 	//set resolution of image
capture1.set(CV_CAP_PROP_FRAME_HEIGHT,960);

while(1){
capture0>>img1;
capture1>>img2;

namedWindow("Cam1",1);
imshow("Cam1",img1);
namedWindow("Cam2",1);
imshow("Cam2",img2);

}
}
