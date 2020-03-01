#include <condition_variable>
#include <mutex>
#include <future>
#include <iostream>

bool readyFlag;
std::mutex readyMutex;
std::condition_variable readyCondVar;

void thread1() {
	std::cout << "<return>" << std::endl;
	std::cin.get();
	{
		std::lock_guard<std::mutex> lg(readyMutex);
		readyFlag = true;
	}
	readyCondVar.notify_one();
}

void thread2() {
	{
		std::unique_lock<std::mutex> ul(readyMutex);
		readyCondVar.wait(ul, [] { return readyFlag;  });
	}
}
