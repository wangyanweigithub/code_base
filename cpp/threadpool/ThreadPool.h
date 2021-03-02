#ifndef THREAD_POOL_H
#define THREAD_POOL_H

#include <vector>
#include <queue>
#include <memory>
#include <mutex>
#include <condition_vairble>
#include <future>
#include <stdexcept>

using namespace std;

class ThreadPool {
public:
	ThreadPool(size_t);
	template<class F, class... Args>
	auto enqueue(F&& f, Args... args) ->future<typename result_of<F(Args...)>::type>;
	~ThreadPool();
private:
	vector<thread> workers;
	queue<function<void()>> tasks;
	mutex queue_mutex;
	condition_variable condition;
	bool stop;
}

inline ThreadPool::ThreadPool(size_t threads): stop(false) {
	for(int i=0; i<threads; ++i) {
		workers.emplace_back([this]{
			for(;;) {
				unique_lock<mutex> lock(this->queue_mutex);
				this->condition.wait(lock, [this]{return this->stop || !this->tasks.empty();});
				if (this->stop && this->tasks.empty())
					return;
				auto task = std::move(this->tasks.front());
				this->tasks.pop();
				task();
			})
		}
	}
}	

#endif
