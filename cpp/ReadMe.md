### report.cpp
BM 算法的cpp实现

### riterator_error.cpp
> c++中，rverse_iterator和iterator指向同一个位置时返回的结果不用。
1. iterator的返回值是指针所指位置的值
2. 反向迭代器返回的值是指针所指的位置加一所指向的值。因为区间范围是前闭后开，包括第一个不包括最后一个，而反向迭代器尾指针指向的是容器最后一个元素的后面，所以第一个是无用指针，而最后一个反而是有值的位置。

3. 所以反向迭代器返回的值是指针位置加一返回的值。

### 内存泄露检查器c++实现
> leakdetector
1. 实现原理和步骤: leakDetector/Readme.md
