#include <string>
#include <iostream>
#include <vector>
#include "opencv2/opencv.hpp"

using namespace std;

int main(int argc, char** argv) {
	vector<string> files;
	string filepath = argv[1];
	cv::glob(filepath, files, false);
	size_t count = files.size();

	cv::namedWindow("image", CV_WINDOW_AUTOSIZE);
	for (int i = 0; i < count; i++) {
		cout << "name is :" << files[i] << endl;
		cv::Mat mat = cv::imread(files[i]);
		cv::imshow("image", mat);
		cv::waitKey(5000);
	}
}

