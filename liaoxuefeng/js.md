# js
## JavaScript简介
#### JavaScript历史 
1. 要了解JavaScript，我们首先要回顾一下JavaScript的诞生。

2. 在上个世纪的1995年，当时的网景公司正凭借其Navigator浏览器成为Web时代开启时最著名的第一代互联网公司。

3. 由于网景公司希望能在静态HTML页面上添加一些动态效果，于是叫Brendan Eich这哥们在两周之内设计出了JavaScript语言。你没看错，这哥们只用了10天时间。

4. 为什么起名叫JavaScript？原因是当时Java语言非常红火，所以网景公司希望借Java的名气来推广，但事实上JavaScript除了语法上有点像Java，其他部分基本上没啥关系。

#### ECMAScript 
1. 因为网景开发了JavaScript，一年后微软又模仿JavaScript开发了JScript，为了让JavaScript成为全球标准，几个公司联合ECMA（European Computer Manufacturers Association）组织定制了JavaScript语言的标准，被称为ECMAScript标准。

2. 所以简单说来就是，ECMAScript是一种语言标准，而JavaScript是网景公司对ECMAScript标准的一种实现。

3. 那为什么不直接把JavaScript定为标准呢？因为JavaScript是网景的注册商标。

4. 不过大多数时候，我们还是用JavaScript这个词。如果你遇到ECMAScript这个词，简单把它替换为JavaScript就行了。

#### JavaScript版本 
1. JavaScript语言是在10天时间内设计出来的，虽然语言的设计者水平非常NB，但谁也架不住“时间紧，任务重”，所以，JavaScript有很多设计缺陷，我们后面会慢慢讲到。

2. 此外，由于JavaScript的标准——ECMAScript在不断发展，最新版ECMAScript 6标准（简称ES6）已经在2015年6月正式发布了，所以，讲到JavaScript的版本，实际上就是说它实现了ECMAScript标准的哪个版本。

3. 由于浏览器在发布时就确定了JavaScript的版本，加上很多用户还在使用IE6这种古老的浏览器，这就导致你在写JavaScript的时候，要照顾一下老用户，不能一上来就用最新的ES6标准写，否则，老用户的浏览器是无法运行新版本的JavaScript代码的。

4. 不过，JavaScript的核心语法并没有多大变化。我们的教程会先讲JavaScript最核心的用法，然后，针对ES6讲解新增特性。

```
ECMAScript第一版标准发布于：
----
    1995年
    1996年
(x) 1997年
    1998年
    2015年
```
## 快速入门
1. JavaScript代码可以直接嵌在网页的任何地方，不过通常我们都把JavaScript代码放到<head>中：

```
<html>
<head>
  <script>
    alert('Hello, world');
  </script>
</head>
<body>
  ...
</body>
</html>
```
2. 由<script>...</script>包含的代码就是JavaScript代码，它将直接被浏览器执行。

3. 第二种方法是把JavaScript代码放到一个单独的.js文件，然后在HTML中通过<script src="..."></script>引入这个文件：

```
<html>
<head>
  <script src="/static/js/abc.js"></script>
</head>
<body>
  ...
</body>
</html>
```
4. 这样，/static/js/abc.js就会被浏览器执行。

5. 把JavaScript代码放入一个单独的.js文件中更利于维护代码，并且多个页面可以各自引用同一份.js文件。

6. 可以在同一个页面中引入多个.js文件，还可以在页面中多次编写<script> js代码... </script>，浏览器按照顺序依次执行。

7. 有些时候你会看到<script>标签还设置了一个type属性：

```
<script type="text/javascript">
  ...
</script>
```
8. 但这是没有必要的，因为默认的type就是JavaScript，所以不必显式地把type指定为JavaScript。

#### 如何编写JavaScript 
1. 可以用任何文本编辑器来编写JavaScript代码。这里我们推荐以下几种文本编辑器：

#### Visual Studio Code 
1. 微软出的Visual Studio Code，可以看做迷你版Visual Studio，免费！跨平台！内置JavaScript支持，强烈推荐使用！

#### Sublime Text 
1. Sublime Text是一个好用的文本编辑器，免费，但不注册会不定时弹出提示框。

#### Notepad++ 
1. Notepad++也是免费的文本编辑器，但仅限Windows下使用。

2. 注意：不可以用Word或写字板来编写JavaScript或HTML，因为带格式的文本保存后不是纯文本文件，无法被浏览器正常读取。也尽量不要用记事本编写，它会自作聪明地在保存UTF-8格式文本时添加BOM头。

#### 如何运行JavaScript 
1. 要让浏览器运行JavaScript，必须先有一个HTML页面，在HTML页面中引入JavaScript，然后，让浏览器加载该HTML页面，就可以执行JavaScript代码。

2. 你也许会想，直接在我的硬盘上创建好HTML和JavaScript文件，然后用浏览器打开，不就可以看到效果了吗？

3. 这种方式运行部分JavaScript代码没有问题，但由于浏览器的安全限制，以file://开头的地址无法执行如联网等JavaScript代码，最终，你还是需要架设一个Web服务器，然后以http://开头的地址来正常执行所有JavaScript代码。

4. 不过，开始学习阶段，你无须关心如何搭建开发环境的问题，我们提供在页面输入JavaScript代码并直接运行的功能，让你专注于JavaScript的学习。

5. 试试直接点击“Run”按钮执行下面的JavaScript代码：

```
// 以双斜杠开头直到行末的是注释，注释是给人看的，会被浏览器忽略
/* 在这中间的也是注释，将被浏览器忽略 */
// 第一个JavaScript代码:
----
alert('Hello, world'); // 观察执行效果
```
6. 浏览器将弹出一个对话框，显示“Hello, world”。你也可以修改两个单引号中间的内容，再试着运行。

#### 调试 
1. 俗话说得好，“工欲善其事，必先利其器。”，写JavaScript的时候，如果期望显示ABC，结果却显示XYZ，到底代码哪里出了问题？不要抓狂，也不要泄气，作为小白，要坚信：JavaScript本身没有问题，浏览器执行也没有问题，有问题的一定是我的代码。

2. 如何找出问题代码？这就需要调试。

3. 怎么在浏览器中调试JavaScript代码呢？

4. 首先，你需要安装Google Chrome浏览器，Chrome浏览器对开发者非常友好，可以让你方便地调试JavaScript代码。从这里下载Chrome浏览器。打开网页出问题的童鞋请移步国内镜像。

5. 安装后，随便打开一个网页，然后点击菜单“查看(View)”-“开发者(Developer)”-“开发者工具(Developer Tools)”，浏览器窗口就会一分为二，下方就是开发者工具：

6. 

7. 先点击“控制台(Console)“，在这个面板里可以直接输入JavaScript代码，按回车后执行。

8. 要查看一个变量的内容，在Console中输入console.log(a);，回车后显示的值就是变量的内容。

9. 关闭Console请点击右上角的“×”按钮。请熟练掌握Console的使用方法，在编写JavaScript代码时，经常需要在Console运行测试代码。

10. 如果你对自己还有更高的要求，可以研究开发者工具的“源码(Sources)”，掌握断点、单步执行等高级调试技巧。

#### 练习 
1. 打开新浪首页，然后查看页面源代码，找一找引入的JavaScript文件和直接编写在页面中的JavaScript代码。然后在Chrome中打开开发者工具，在控制台输入console.log('Hello');，回车查看JavaScript代码执行结果。

### 基本语法
#### 语法 
1. JavaScript的语法和Java语言类似，每个语句以;结束，语句块用{...}。但是，JavaScript并不强制要求在每个语句的结尾加;，浏览器中负责执行JavaScript代码的引擎会自动在每个语句的结尾补上;。

```
让JavaScript引擎自动加分号在某些情况下会改变程序的语义，导致运行结果与期望不一致。在本教程中，我们不会省略;，所有语句都会添加;。
```
2. 例如，下面的一行代码就是一个完整的赋值语句：

```
var x = 1;
```
3. 下面的一行代码是一个字符串，但仍然可以视为一个完整的语句：

```
'Hello, world';
```
4. 下面的一行代码包含两个语句，每个语句用;表示语句结束：

```
var x = 1; var y = 2; // 不建议一行写多个语句!
```
5. 语句块是一组语句的集合，例如，下面的代码先做了一个判断，如果判断成立，将执行{...}中的所有语句：

```
if (2 > 1) {
    x = 1;
    y = 2;
    z = 3;
}
```
6. 注意花括号{...}内的语句具有缩进，通常是4个空格。缩进不是JavaScript语法要求必须的，但缩进有助于我们理解代码的层次，所以编写代码时要遵守缩进规则。很多文本编辑器具有“自动缩进”的功能，可以帮助整理代码。

7. {...}还可以嵌套，形成层级结构：

```
if (2 > 1) {
    x = 1;
    y = 2;
    z = 3;
    if (x < y) {
        z = 4;
    }
    if (x > y) {
        z = 5;
    }
}
```
8. JavaScript本身对嵌套的层级没有限制，但是过多的嵌套无疑会大大增加看懂代码的难度。遇到这种情况，需要把部分代码抽出来，作为函数来调用，这样可以减少代码的复杂度。

#### 注释 
1. 以//开头直到行末的字符被视为行注释，注释是给开发人员看到，JavaScript引擎会自动忽略：

```
// 这是一行注释
alert('hello'); // 这也是注释
```
2. 另一种块注释是用/*...*/把多行字符包裹起来，把一大“块”视为一个注释：

```
/* 从这里开始是块注释
仍然是注释
仍然是注释
注释结束 */
```
3. 练习：

4. 分别利用行注释和块注释把下面的语句注释掉，使它不再执行：

```
// 请注释掉下面的语句:
----
alert('我不想执行');
alert('我也不想执行');
```
#### 大小写 
1. 请注意，JavaScript严格区分大小写，如果弄错了大小写，程序将报错或者运行不正常。

### 数据类型和变量
#### 数据类型 
1. 计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地可以处理各种数值。但是，计算机能处理的远不止数值，还可以处理文本、图形、音频、视频、网页等各种各样的数据，不同的数据，需要定义不同的数据类型。在JavaScript中定义了以下几种数据类型：

#### Number 
1. JavaScript不区分整数和浮点数，统一用Number表示，以下都是合法的Number类型：

```
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity
```
2. 计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等，它们和十进制表示的数值完全一样。

3. Number可以直接做四则运算，规则和数学一致：

```
1 + 2; // 3
(1 + 2) * 5 / 2; // 7.5
2 / 0; // Infinity
0 / 0; // NaN
10 % 3; // 1
10.5 % 3; // 1.5
```
4. 注意%是求余运算。

#### 字符串 
1. 字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。

#### 布尔值 
1. 布尔值和布尔代数的表示完全一致，一个布尔值只有true、false两种值，要么是true，要么是false，可以直接用true、false表示布尔值，也可以通过布尔运算计算出来：

```
true; // 这是一个true值
false; // 这是一个false值
2 > 1; // 这是一个true值
2 >= 3; // 这是一个false值
```
2. &&运算是与运算，只有所有都为true，&&运算结果才是true：

```
true && true; // 这个&&语句计算结果为true
true && false; // 这个&&语句计算结果为false
false && true && false; // 这个&&语句计算结果为false
```
3. ||运算是或运算，只要其中有一个为true，||运算结果就是true：

```
false || false; // 这个||语句计算结果为false
true || false; // 这个||语句计算结果为true
false || true || false; // 这个||语句计算结果为true
```
4. !运算是非运算，它是一个单目运算符，把true变成false，false变成true：

```
! true; // 结果为false
! false; // 结果为true
! (2 > 5); // 结果为true
```
5. 布尔值经常用在条件判断中，比如：

```
var age = 15;
if (age >= 18) {
    alert('adult');
} else {
    alert('teenager');
}
```
#### 比较运算符 
1. 当我们对Number做比较时，可以通过比较运算符得到一个布尔值：

```
2 > 5; // false
5 >= 2; // true
7 == 7; // true
```
2. 实际上，JavaScript允许对任意数据类型做比较：

```
false == 0; // true
false === 0; // false
```
3. 要特别注意相等运算符==。JavaScript在设计时，有两种比较运算符：

4. 第一种是==比较，它会自动转换数据类型再比较，很多时候，会得到非常诡异的结果；

5. 第二种是===比较，它不会自动转换数据类型，如果数据类型不一致，返回false，如果一致，再比较。

6. 由于JavaScript这个设计缺陷，不要使用==比较，始终坚持使用===比较。

7. 另一个例外是NaN这个特殊的Number与所有其他值都不相等，包括它自己：

```
NaN === NaN; // false
```
8. 唯一能判断NaN的方法是通过isNaN()函数：

```
isNaN(NaN); // true
```
9. 最后要注意浮点数的相等比较：

```
1 / 3 === (1 - 2 / 3); // false
```
10. 这不是JavaScript的设计缺陷。浮点数在运算过程中会产生误差，因为计算机无法精确表示无限循环小数。要比较两个浮点数是否相等，只能计算它们之差的绝对值，看是否小于某个阈值：

```
Math.abs(1 / 3 - (1 - 2 / 3)) < 0.0000001; // true
```
#### null和undefined 
1. null表示一个“空”的值，它和0以及空字符串''不同，0是一个数值，''表示长度为0的字符串，而null表示“空”。

2. 在其他语言中，也有类似JavaScript的null的表示，例如Java也用null，Swift用nil，Python用None表示。但是，在JavaScript中，还有一个和null类似的undefined，它表示“未定义”。

3. JavaScript的设计者希望用null表示一个空的值，而undefined表示值未定义。事实证明，这并没有什么卵用，区分两者的意义不大。大多数情况下，我们都应该用null。undefined仅仅在判断函数参数是否传递的情况下有用。

#### 数组 
1. 数组是一组按顺序排列的集合，集合的每个值称为元素。JavaScript的数组可以包括任意数据类型。例如：

```
[1, 2, 3.14, 'Hello', null, true];
```
2. 上述数组包含6个元素。数组用[]表示，元素之间用,分隔。

3. 另一种创建数组的方法是通过Array()函数实现：

```
new Array(1, 2, 3); // 创建了数组[1, 2, 3]
```
4. 然而，出于代码的可读性考虑，强烈建议直接使用[]。

5. 数组的元素可以通过索引来访问。请注意，索引的起始值为0：

```
var arr = [1, 2, 3.14, 'Hello', null, true];
arr[0]; // 返回索引为0的元素，即1
arr[5]; // 返回索引为5的元素，即true
arr[6]; // 索引超出了范围，返回undefined
```
#### 对象 
1. JavaScript的对象是一组由键-值组成的无序集合，例如：

```
var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    hasCar: true,
    zipcode: null
};
```
2. JavaScript对象的键都是字符串类型，值可以是任意数据类型。上述person对象一共定义了6个键值对，其中每个键又称为对象的属性，例如，person的name属性为'Bob'，zipcode属性为null。

3. 要获取一个对象的属性，我们用对象变量.属性名的方式：

```
person.name; // 'Bob'
person.zipcode; // null
```
#### 变量 
1. 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

2. 变量在JavaScript中就是用一个变量名表示，变量名是大小写英文、数字、$和_的组合，且不能用数字开头。变量名也不能是JavaScript的关键字，如if、while等。申明一个变量用var语句，比如：

```
var a; // 申明了变量a，此时a的值为undefined
var $b = 1; // 申明了变量$b，同时给$b赋值，此时$b的值为1
var s_007 = '007'; // s_007是一个字符串
var Answer = true; // Answer是一个布尔值true
var t = null; // t的值是null
```
3. 变量名也可以用中文，但是，请不要给自己找麻烦。

4. 在JavaScript中，使用等号=对变量进行赋值。可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，但是要注意只能用var申明一次，例如：

```
var a = 123; // a的值是整数123
a = 'ABC'; // a变为字符串
```
5. 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下：

```
int a = 123; // a是整数类型变量，类型用int申明
a = "ABC"; // 错误：不能把字符串赋给整型变量
```
6. 和静态语言相比，动态语言更灵活，就是这个原因。

7. 请不要把赋值语句的等号等同于数学的等号。比如下面的代码：

```
var x = 10;
x = x + 2;
```
8. 如果从数学上理解x = x + 2那无论如何是不成立的，在程序中，赋值语句先计算右侧的表达式x + 2，得到结果12，再赋给变量x。由于x之前的值是10，重新赋值后，x的值变成12。

9. 要显示变量的内容，可以用console.log(x)，打开Chrome的控制台就可以看到结果。

```
// 打印变量x
----
var x = 100;
console.log(x);
```
10. 使用console.log()代替alert()的好处是可以避免弹出烦人的对话框。

#### strict模式 
1. JavaScript在设计之初，为了方便初学者学习，并不强制要求用var申明变量。这个设计错误带来了严重的后果：如果一个变量没有通过var申明就被使用，那么该变量就自动被申明为全局变量：

```
i = 10; // i现在是全局变量
```
2. 在同一个页面的不同的JavaScript文件中，如果都不用var申明，恰好都使用了变量i，将造成变量i互相影响，产生难以调试的错误结果。

3. 使用var申明的变量则不是全局变量，它的范围被限制在该变量被申明的函数体内（函数的概念将稍后讲解），同名变量在不同的函数体内互不冲突。

4. 为了修补JavaScript这一严重设计缺陷，ECMA在后续规范中推出了strict模式，在strict模式下运行的JavaScript代码，强制通过var申明变量，未使用var申明变量就使用的，将导致运行错误。

5. 启用strict模式的方法是在JavaScript代码的第一行写上：

```
'use strict';
```
6. 这是一个字符串，不支持strict模式的浏览器会把它当做一个字符串语句执行，支持strict模式的浏览器将开启strict模式运行JavaScript。

7. 来测试一下你的浏览器是否能支持strict模式：

```
'use strict';
// 如果浏览器支持strict模式，
// 下面的代码将报ReferenceError错误:
----
abc = 'Hello, world';
console.log(abc);
```
8. 运行代码，如果浏览器报错，请修复后再运行。如果浏览器不报错，说明你的浏览器太古老了，需要尽快升级。

9. 不用var申明的变量会被视为全局变量，为了避免这一缺陷，所有的JavaScript代码都应该使用strict模式。我们在后面编写的JavaScript代码将全部采用strict模式。

### 字符串
1. JavaScript的字符串就是用''或""括起来的字符表示。

2. 如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。

3. 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：

```
'I\'m \"OK\"!';
```
4. 表示的字符串内容是：I'm "OK"!

5. 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\。

6. ASCII字符可以以\x##形式的十六进制表示，例如：

```
'\x41'; // 完全等同于 'A'
```
7. 还可以用\u####表示一个Unicode字符：

```
'\u4e2d\u6587'; // 完全等同于 '中文'
```
#### 多行字符串 
1. 由于多行字符串用\n写起来比较费事，所以最新的ES6标准新增了一种多行字符串的表示方法，用反引号 * ... * 表示：

```
`这是一个
多行
字符串`;
```
2. 注意：反引号在键盘的ESC下方，数字键1的左边：

```
┌─────┐ ┌─────┬─────┬─────┬─────┐
│ ESC │ │ F1  │ F2  │ F3  │ F4  │
│     │ │     │     │     │     │
└─────┘ └─────┴─────┴─────┴─────┘
┌─────┬─────┬─────┬─────┬─────┐
│  ~  │  !  │  @  │  #  │  $  │
│  `  │  1  │  2  │  3  │  4  │
├─────┴──┬──┴──┬──┴──┬──┴──┬──┘
│        │     │     │     │
│  tab   │  Q  │  W  │  E  │
├────────┴──┬──┴──┬──┴──┬──┘
│           │     │     │
│ caps lock │  A  │  S  │
└───────────┴─────┴─────┘
```
3. 练习：测试你的浏览器是否支持ES6标准，如果不支持，请把多行字符串用\n重新表示出来：

```
// 如果浏览器不支持ES6，将报SyntaxError错误:
----
console.log(`多行
字符串
测试`);
```
#### 模板字符串 
1. 要把多个字符串连接起来，可以用+号连接：

```
var name = '小明';
var age = 20;
var message = '你好, ' + name + ', 你今年' + age + '岁了!';
alert(message);
```
2. 如果有很多变量需要连接，用+号就比较麻烦。ES6新增了一种模板字符串，表示方法和上面的多行字符串一样，但是它会自动替换字符串中的变量：

```
var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`;
alert(message);
```
3. 练习：测试你的浏览器是否支持ES6模板字符串，如果不支持，请把模板字符串改为+连接的普通字符串：

```
'use strict';

// 如果浏览器支持模板字符串，将会替换字符串内部的变量:
var name = '小明';
var age = 20;
----
console.log(`你好, ${name}, 你今年${age}岁了!`);
```
#### 操作字符串 
1. 字符串常见的操作如下：

```
var s = 'Hello, world!';
s.length; // 13
```
2. 要获取字符串某个指定位置的字符，使用类似Array的下标操作，索引号从0开始：

```
var s = 'Hello, world!';

s[0]; // 'H'
s[6]; // ' '
s[7]; // 'w'
s[12]; // '!'
s[13]; // undefined 超出范围的索引不会报错，但一律返回undefined
```
3. 需要特别注意的是，字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果：

```
var s = 'Test';
s[0] = 'X';
alert(s); // s仍然为'Test'
```
4. JavaScript为字符串提供了一些常用方法，注意，调用这些方法本身不会改变原有字符串的内容，而是返回一个新字符串：

#### toUpperCase 
1. toUpperCase()把一个字符串全部变为大写：

```
var s = 'Hello';
s.toUpperCase(); // 返回'HELLO'
```
#### toLowerCase 
1. toLowerCase()把一个字符串全部变为小写：

```
var s = 'Hello';
var lower = s.toLowerCase(); // 返回'hello'并赋值给变量lower
lower; // 'hello'
```
#### indexOf 
1. indexOf()会搜索指定字符串出现的位置：

```
var s = 'hello, world';
s.indexOf('world'); // 返回7
s.indexOf('World'); // 没有找到指定的子串，返回-1
```
#### substring 
1. substring()返回指定索引区间的子串：

```
var s = 'hello, world'
s.substring(0, 5); // 从索引0开始到5（不包括5），返回'hello'
s.substring(7); // 从索引7开始到结束，返回'world'
```
### 数组
1. JavaScript的Array可以包含任意数据类型，并通过索引来访问每个元素。

2. 要取得Array的长度，直接访问length属性：

```
var arr = [1, 2, 3.14, 'Hello', null, true];
arr.length; // 6
```
3. 请注意，直接给Array的length赋一个新的值会导致Array大小的变化：

```
var arr = [1, 2, 3];
arr.length; // 3
arr.length = 6;
arr; // arr变为[1, 2, 3, undefined, undefined, undefined]
arr.length = 2;
arr; // arr变为[1, 2]
```
4. Array可以通过索引把对应的元素修改为新的值，因此，对Array的索引进行赋值会直接修改这个Array：

```
var arr = ['A', 'B', 'C'];
arr[1] = 99;
arr; // arr现在变为['A', 99, 'C']
```
5. 请注意，如果通过索引赋值时，索引超过了范围，同样会引起Array大小的变化：

```
var arr = [1, 2, 3];
arr[5] = 'x';
arr; // arr变为[1, 2, 3, undefined, undefined, 'x']
```
6. 大多数其他编程语言不允许直接改变数组的大小，越界访问索引会报错。然而，JavaScript的Array却不会有任何错误。在编写代码时，不建议直接修改Array的大小，访问索引时要确保索引不会越界。

#### indexOf 
1. 与String类似，Array也可以通过indexOf()来搜索一个指定的元素的位置：

```
var arr = [10, 20, '30', 'xyz'];
arr.indexOf(10); // 元素10的索引为0
arr.indexOf(20); // 元素20的索引为1
arr.indexOf(30); // 元素30没有找到，返回-1
arr.indexOf('30'); // 元素'30'的索引为2
```
2. 注意了，数字30和字符串'30'是不同的元素。

#### slice 
1. slice()就是对应String的substring()版本，它截取Array的部分元素，然后返回一个新的Array：

```
var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
arr.slice(0, 3); // 从索引0开始，到索引3结束，但不包括索引3: ['A', 'B', 'C']
arr.slice(3); // 从索引3开始到结束: ['D', 'E', 'F', 'G']
```
2. 注意到slice()的起止参数包括开始索引，不包括结束索引。

3. 如果不给slice()传递任何参数，它就会从头到尾截取所有元素。利用这一点，我们可以很容易地复制一个Array：

```
var arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
var aCopy = arr.slice();
aCopy; // ['A', 'B', 'C', 'D', 'E', 'F', 'G']
aCopy === arr; // false
```
#### push和pop 
1. push()向Array的末尾添加若干元素，pop()则把Array的最后一个元素删除掉：

```
var arr = [1, 2];
arr.push('A', 'B'); // 返回Array新的长度: 4
arr; // [1, 2, 'A', 'B']
arr.pop(); // pop()返回'B'
arr; // [1, 2, 'A']
arr.pop(); arr.pop(); arr.pop(); // 连续pop 3次
arr; // []
arr.pop(); // 空数组继续pop不会报错，而是返回undefined
arr; // []
```
#### unshift和shift 
1. 如果要往Array的头部添加若干元素，使用unshift()方法，shift()方法则把Array的第一个元素删掉：

```
var arr = [1, 2];
arr.unshift('A', 'B'); // 返回Array新的长度: 4
arr; // ['A', 'B', 1, 2]
arr.shift(); // 'A'
arr; // ['B', 1, 2]
arr.shift(); arr.shift(); arr.shift(); // 连续shift 3次
arr; // []
arr.shift(); // 空数组继续shift不会报错，而是返回undefined
arr; // []
```
#### sort 
1. sort()可以对当前Array进行排序，它会直接修改当前Array的元素位置，直接调用时，按照默认顺序排序：

```
var arr = ['B', 'C', 'A'];
arr.sort();
arr; // ['A', 'B', 'C']
```
2. 能否按照我们自己指定的顺序排序呢？完全可以，我们将在后面的函数中讲到。

#### reverse 
1. reverse()把整个Array的元素给掉个个，也就是反转：

```
var arr = ['one', 'two', 'three'];
arr.reverse(); 
arr; // ['three', 'two', 'one']
```
#### splice 
1. splice()方法是修改Array的“万能方法”，它可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素：

```
var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
// 从索引2开始删除3个元素,然后再添加两个元素:
arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
// 只删除,不添加:
arr.splice(2, 2); // ['Google', 'Facebook']
arr; // ['Microsoft', 'Apple', 'Oracle']
// 只添加,不删除:
arr.splice(2, 0, 'Google', 'Facebook'); // 返回[],因为没有删除任何元素
arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
```
#### concat 
1. concat()方法把当前的Array和另一个Array连接起来，并返回一个新的Array：

```
var arr = ['A', 'B', 'C'];
var added = arr.concat([1, 2, 3]);
added; // ['A', 'B', 'C', 1, 2, 3]
arr; // ['A', 'B', 'C']
```
2. 请注意，concat()方法并没有修改当前Array，而是返回了一个新的Array。

3. 实际上，concat()方法可以接收任意个元素和Array，并且自动把Array拆开，然后全部添加到新的Array里：

```
var arr = ['A', 'B', 'C'];
arr.concat(1, 2, [3, 4]); // ['A', 'B', 'C', 1, 2, 3, 4]
```
#### join 
1. join()方法是一个非常实用的方法，它把当前Array的每个元素都用指定的字符串连接起来，然后返回连接后的字符串：

```
var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'
```
2. 如果Array的元素不是字符串，将自动转换为字符串后再连接。

#### 多维数组 
1. 如果数组的某个元素又是一个Array，则可以形成多维数组，例如：

```
var arr = [[1, 2, 3], [400, 500, 600], '-'];
```
2. 上述Array包含3个元素，其中头两个元素本身也是Array。

3. 练习：如何通过索引取到500这个值：

```
'use strict';
var arr = [[1, 2, 3], [400, 500, 600], '-'];
----
var x = ??;
----
console.log(x); // x应该为500
```
#### 小结 
1. Array提供了一种顺序存储一组元素的功能，并可以按索引来读写。

2. 练习：在新生欢迎会上，你已经拿到了新同学的名单，请排序后显示：欢迎XXX，XXX，XXX和XXX同学！：

```
'use strict';
var arr = ['小明', '小红', '大军', '阿黄'];
----
console.log('???');
```
### 对象
1. JavaScript的对象是一种无序的集合数据类型，它由若干键值对组成。

2. JavaScript的对象用于描述现实世界中的某个对象。例如，为了描述“小明”这个淘气的小朋友，我们可以用若干键值对来描述他：

```
var xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};
```
3. JavaScript用一个{...}表示一个对象，键值对以xxx: xxx形式申明，用,隔开。注意，最后一个键值对不需要在末尾加,，如果加了，有的浏览器（如低版本的IE）将报错。

4. 上述对象申明了一个name属性，值是'小明'，birth属性，值是1990，以及其他一些属性。最后，把这个对象赋值给变量xiaoming后，就可以通过变量xiaoming来获取小明的属性了：

```
xiaoming.name; // '小明'
xiaoming.birth; // 1990
```
5. 访问属性是通过.操作符完成的，但这要求属性名必须是一个有效的变量名。如果属性名包含特殊字符，就必须用''括起来：

```
var xiaohong = {
    name: '小红',
    'middle-school': 'No.1 Middle School'
};
```
6. xiaohong的属性名middle-school不是一个有效的变量，就需要用''括起来。访问这个属性也无法使用.操作符，必须用['xxx']来访问：

```
xiaohong['middle-school']; // 'No.1 Middle School'
xiaohong['name']; // '小红'
xiaohong.name; // '小红'
```
7. 也可以用xiaohong['name']来访问xiaohong的name属性，不过xiaohong.name的写法更简洁。我们在编写JavaScript代码的时候，属性名尽量使用标准的变量名，这样就可以直接通过object.prop的形式访问一个属性了。

8. 实际上JavaScript对象的所有属性都是字符串，不过属性对应的值可以是任意数据类型。

9. 如果访问一个不存在的属性会返回什么呢？JavaScript规定，访问不存在的属性不报错，而是返回undefined：

```
'use strict';

var xiaoming = {
    name: '小明'
};
----
console.log(xiaoming.name);
console.log(xiaoming.age); // undefined
```
10. 由于JavaScript的对象是动态类型，你可以自由地给一个对象添加或删除属性：

```
var xiaoming = {
    name: '小明'
};
xiaoming.age; // undefined
xiaoming.age = 18; // 新增一个age属性
xiaoming.age; // 18
delete xiaoming.age; // 删除age属性
xiaoming.age; // undefined
delete xiaoming['name']; // 删除name属性
xiaoming.name; // undefined
delete xiaoming.school; // 删除一个不存在的school属性也不会报错
```
11. 如果我们要检测xiaoming是否拥有某一属性，可以用in操作符：

```
var xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};
'name' in xiaoming; // true
'grade' in xiaoming; // false
```
12. 不过要小心，如果in判断一个属性存在，这个属性不一定是xiaoming的，它可能是xiaoming继承得到的：

```
'toString' in xiaoming; // true
```
13. 因为toString定义在object对象中，而所有对象最终都会在原型链上指向object，所以xiaoming也拥有toString属性。

14. 要判断一个属性是否是xiaoming自身拥有的，而不是继承得到的，可以用hasOwnProperty()方法：

```
var xiaoming = {
    name: '小明'
};
xiaoming.hasOwnProperty('name'); // true
xiaoming.hasOwnProperty('toString'); // false
```
### 条件判断
1. JavaScript使用if () { ... } else { ... }来进行条件判断。例如，根据年龄显示不同内容，可以用if语句实现如下：

```
var age = 20;
if (age >= 18) { // 如果age >= 18为true，则执行if语句块
    alert('adult');
} else { // 否则执行else语句块
    alert('teenager');
}
```
2. 其中else语句是可选的。如果语句块只包含一条语句，那么可以省略{}：

```
var age = 20;
if (age >= 18)
    alert('adult');
else
    alert('teenager');
```
3. 省略{}的危险之处在于，如果后来想添加一些语句，却忘了写{}，就改变了if...else...的语义，例如：

```
var age = 20;
if (age >= 18)
    alert('adult');
else
    console.log('age < 18'); // 添加一行日志
    alert('teenager'); // <- 这行语句已经不在else的控制范围了
```
4. 上述代码的else子句实际上只负责执行console.log('age < 18');，原有的alert('teenager');已经不属于if...else...的控制范围了，它每次都会执行。

5. 相反地，有{}的语句就不会出错：

```
var age = 20;
if (age >= 18) {
    alert('adult');
} else {
    console.log('age < 18');
    alert('teenager');
}
```
6. 这就是为什么我们建议永远都要写上{}。

#### 多行条件判断 
1. 如果还要更细致地判断条件，可以使用多个if...else...的组合：

```
var age = 3;
if (age >= 18) {
    alert('adult');
} else if (age >= 6) {
    alert('teenager');
} else {
    alert('kid');
}
```
2. 上述多个if...else...的组合实际上相当于两层if...else...：

```
var age = 3;
if (age >= 18) {
    alert('adult');
} else {
    if (age >= 6) {
        alert('teenager');
    } else {
        alert('kid');
    }
}
```
3. 但是我们通常把else if连写在一起，来增加可读性。这里的else略掉了{}是没有问题的，因为它只包含一个if语句。注意最后一个单独的else不要略掉{}。

4. 请注意，if...else...语句的执行特点是二选一，在多个if...else...语句中，如果某个条件成立，则后续就不再继续判断了。

5. 试解释为什么下面的代码显示的是teenager：

```
'use strict';
var age = 20;
----
if (age >= 6) {
    console.log('teenager');
} else if (age >= 18) {
    console.log('adult');
} else {
    console.log('kid');
}
```
6. 由于age的值为20，它实际上同时满足条件age >= 6和age >= 18，这说明条件判断的顺序非常重要。请修复后让其显示adult。

7. 如果if的条件判断语句结果不是true或false怎么办？例如：

```
var s = '123';
if (s.length) { // 条件计算结果为3
    //
}
```
8. JavaScript把null、undefined、0、NaN和空字符串''视为false，其他值一概视为true，因此上述代码条件判断的结果是true。

#### 练习 
1. 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

2. 
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖


3. 用if...else...判断并显示结果：

```
'use strict';

var height = parseFloat(prompt('请输入身高(m):'));
var weight = parseFloat(prompt('请输入体重(kg):'));
----
var bmi = ???;
if ...
```
### 循环
#### 循环 
1. 要计算1+2+3，我们可以直接写表达式：

```
1 + 2 + 3; // 6
```
2. 要计算1+2+3+...+10，勉强也能写出来。

3. 但是，要计算1+2+3+...+10000，直接写表达式就不可能了。

4. 为了让计算机能计算成千上万次的重复运算，我们就需要循环语句。

5. JavaScript的循环有两种，一种是for循环，通过初始条件、结束条件和递增条件来循环执行语句块：

```
var x = 0;
var i;
for (i=1; i<=10000; i++) {
    x = x + i;
}
x; // 50005000
```
6. 让我们来分析一下for循环的控制条件：

7. 
i=1 这是初始条件，将变量i置为1；
i<=10000 这是判断条件，满足时就继续循环，不满足就退出循环；
i++ 这是每次循环后的递增条件，由于每次循环后变量i都会加1，因此它终将在若干次循环后不满足判断条件i<=10000而退出循环。


#### 练习 
1. 利用for循环计算1 * 2 * 3 * ... * 10的结果：

```
'use strict';
----
var x = ?;
var i;
for ...
----
if (x === 3628800) {
    console.log('1 x 2 x 3 x ... x 10 = ' + x);
}
else {
    console.log('计算错误');
}
```
2. for循环最常用的地方是利用索引来遍历数组：

```
var arr = ['Apple', 'Google', 'Microsoft'];
var i, x;
for (i=0; i<arr.length; i++) {
    x = arr[i];
    console.log(x);
}
```
3. for循环的3个条件都是可以省略的，如果没有退出循环的判断条件，就必须使用break语句退出循环，否则就是死循环：

```
var x = 0;
for (;;) { // 将无限循环下去
    if (x > 100) {
        break; // 通过if判断来退出循环
    }
    x ++;
}
```
#### for ... in 
1. for循环的一个变体是for ... in循环，它可以把一个对象的所有属性依次循环出来：

```
var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    console.log(key); // 'name', 'age', 'city'
}
```
2. 要过滤掉对象继承的属性，用hasOwnProperty()来实现：

```
var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    if (o.hasOwnProperty(key)) {
        console.log(key); // 'name', 'age', 'city'
    }
}
```
3. 由于Array也是对象，而它的每个元素的索引被视为对象的属性，因此，for ... in循环可以直接循环出Array的索引：

```
var a = ['A', 'B', 'C'];
for (var i in a) {
    console.log(i); // '0', '1', '2'
    console.log(a[i]); // 'A', 'B', 'C'
}
```
4. 请注意，for ... in对Array的循环得到的是String而不是Number。

#### while 
1. for循环在已知循环的初始和结束条件时非常有用。而上述忽略了条件的for循环容易让人看不清循环的逻辑，此时用while循环更佳。

2. while循环只有一个判断条件，条件满足，就不断循环，条件不满足时则退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：

```
var x = 0;
var n = 99;
while (n > 0) {
    x = x + n;
    n = n - 2;
}
x; // 2500
```
3. 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。

#### do ... while 
1. 最后一种循环是do { ... } while()循环，它和while循环的唯一区别在于，不是在每次循环开始的时候判断条件，而是在每次循环完成的时候判断条件：

```
var n = 0;
do {
    n = n + 1;
} while (n < 100);
n; // 100
```
2. 用do { ... } while()循环要小心，循环体会至少执行1次，而for和while循环则可能一次都不执行。

#### 练习 
1. 请利用循环遍历数组中的每个名字，并显示Hello, xxx!：

```
'use strict';
var arr = ['Bart', 'Lisa', 'Adam'];
----
for ...
```
2. 请尝试for循环和while循环，并以正序、倒序两种方式遍历。

#### 小结 
1. 循环是让计算机做重复任务的有效的方法，有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。JavaScript的死循环会让浏览器无法正常显示或执行当前页面的逻辑，有的浏览器会直接挂掉，有的浏览器会在一段时间后提示你强行终止JavaScript的执行，因此，要特别注意死循环的问题。

2. 在编写循环代码时，务必小心编写初始条件和判断条件，尤其是边界值。特别注意i < 100和i <= 100是不同的判断逻辑。

### Map和Set
1. JavaScript的默认对象表示方式{}可以视为其他语言中的Map或Dictionary的数据结构，即一组键值对。

2. 但是JavaScript的对象有个小问题，就是键必须是字符串。但实际上Number或者其他数据类型作为键也是非常合理的。

3. 为了解决这个问题，最新的ES6规范引入了新的数据类型Map。要测试你的浏览器是否支持ES6规范，请执行以下代码，如果浏览器报ReferenceError错误，那么你需要换一个支持ES6的浏览器：

```
'use strict';
var m = new Map();
var s = new Set();
console.log('你的浏览器支持Map和Set！');
----
// 直接运行测试
```
#### Map 
1. Map是一组键值对的结构，具有极快的查找速度。

2. 举个例子，假设要根据同学的名字查找对应的成绩，如果用Array实现，需要两个Array：

```
var names = ['Michael', 'Bob', 'Tracy'];
var scores = [95, 75, 85];
```
3. 给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，Array越长，耗时越长。

4. 如果用Map实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用JavaScript写一个Map如下：

```
var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael'); // 95
```
5. **初始化Map需要一个二维数组，或者直接初始化一个空Map。Map具有以下方法：**

```
var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined
```
6. 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

```
var m = new Map();
m.set('Adam', 67);
m.set('Adam', 88);
m.get('Adam'); // 88
```
#### Set 
1. Set和Map类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key。

2. 要创建一个Set，需要提供一个Array作为输入，或者直接创建一个空Set：

```
var s1 = new Set(); // 空Set
var s2 = new Set([1, 2, 3]); // 含1, 2, 3
```
3. 重复元素在Set中自动被过滤：

```
var s = new Set([1, 2, 3, 3, '3']);
s; // Set {1, 2, 3, "3"}
```
4. 注意数字3和字符串'3'是不同的元素。

5. 通过add(key)方法可以添加元素到Set中，可以重复添加，但不会有效果：

```
s.add(4);
s; // Set {1, 2, 3, 4}
s.add(4);
s; // 仍然是 Set {1, 2, 3, 4}
```
6. 通过delete(key)方法可以删除元素：

```
var s = new Set([1, 2, 3]);
s; // Set {1, 2, 3}
s.delete(3);
s; // Set {1, 2}
```
#### 小结 
1. Map和Set是ES6标准新增的数据类型，请根据浏览器的支持情况决定是否要使用。

### iterable
1. 遍历Array可以采用下标循环，遍历Map和Set就无法使用下标。为了统一集合类型，ES6标准引入了新的iterable类型，Array、Map和Set都属于iterable类型。

2. 具有iterable类型的集合可以通过新的for ... of循环来遍历。

3. for ... of循环是ES6引入的新的语法，请测试你的浏览器是否支持：

```
'use strict';
var a = [1, 2, 3];
for (var x of a) {
}
console.log('你的浏览器支持for ... of');
----
// 请直接运行测试
```
4. 用for ... of循环遍历集合，用法如下：

```
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
    console.log(x);
}
for (var x of s) { // 遍历Set
    console.log(x);
}
for (var x of m) { // 遍历Map
    console.log(x[0] + '=' + x[1]);
}
```
5. 你可能会有疑问，**for ... of循环和for ... in循环有何区别？**

	1. for ... in循环由于历史遗留问题，它遍历的实际上是对象的属性名称。一个Array数组实际上也是一个对象，
	它的每个元素的索引被视为一个属性。

	2. 当我们手动给Array对象添加了额外的属性后，for ... in循环将带来意想不到的意外效果：

	```
	var a = ['A', 'B', 'C'];
	a.name = 'Hello';
	for (var x in a) {
		console.log(x); // '0', '1', '2', 'name'
	}
	```
	3. for ... in循环将把name包括在内，但Array的length属性却不包括在内。


6. for ... of循环则完全修复了这些问题，它只循环集合本身的元素：

```
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x of a) {
    console.log(x); // 'A', 'B', 'C'
}
```

7. 这就是为什么要引入新的for ... of循环。

8. 然而，更好的方式是直接使用iterable内置的forEach方法，它接收一个函数，每次迭代就自动回调该函数。以Array为例：

```
'use strict';
var a = ['A', 'B', 'C'];
----
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    console.log(element + ', index = ' + index);
});
```
9. 注意，forEach()方法是ES5.1标准引入的，你需要测试浏览器是否支持。

10. Set与Array类似，但Set没有索引，因此回调函数的前两个参数都是元素本身：

```
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    console.log(element);
});
```
14. Map的回调函数参数依次为value、key和map本身：

```
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    console.log(value);
});
```
15. 如果对某些参数不感兴趣，由于JavaScript的函数调用不要求参数必须一致，因此可以忽略它们。例如，只需要获得Array的element：

```
var a = ['A', 'B', 'C'];
a.forEach(function (element) {
    console.log(element);
});
```
## 函数
1. 我们知道圆的面积计算公式为：

```
\mathrm{πr}^2
```
2. 当我们知道半径r的值时，就可以根据公式计算出面积。假设我们需要计算3个不同大小的圆的面积：

```
var r1 = 12.34;
var r2 = 9.08;
var r3 = 73.1;
var s1 = 3.14 * r1 * r1;
var s2 = 3.14 * r2 * r2;
var s3 = 3.14 * r3 * r3;
```
3. 当代码出现有规律的重复的时候，你就需要当心了，每次写3.14 * x * x不仅很麻烦，而且，如果要把3.14改成3.14159265359的时候，得全部替换。

4. 有了函数，我们就不再每次写s = 3.14 * x * x，而是写成更有意义的函数调用s = area_of_circle(x)，而函数area_of_circle本身只需要写一次，就可以多次调用。

5. 基本上所有的高级语言都支持函数，JavaScript也不例外。JavaScript的函数不但是“头等公民”，而且可以像变量一样使用，具有非常强大的抽象能力。

#### 抽象 
1. 抽象是数学中非常常见的概念。举个例子：

2. 计算数列的和，比如：1 + 2 + 3 + ... + 100，写起来十分不方便，于是数学家发明了求和符号∑，可以把1 + 2 + 3 + ... + 100记作：

```
\sum_{n=1}^{100}n
```
3. 这种抽象记法非常强大，因为我们看到 ∑ 就可以理解成求和，而不是还原成低级的加法运算。

4. 而且，这种抽象记法是可扩展的，比如：

```
\sum_{n=1}^{100}n^2+1
```
5. 还原成加法运算就变成了：

```
(1\times1+1)+(2\times2+1)+(3\times3+1)+\dots+(100\times100+1)
```
6. 可见，借助抽象，我们才能不关心底层的具体计算过程，而直接在更高的层次上思考问题。

7. 写计算机程序也是一样，函数就是最基本的一种代码抽象的方式。

### 函数定义和调用
#### 定义函数 
1. 在JavaScript中，定义函数的方式如下：

```
function abs(x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
```
2. 上述abs()函数的定义如下：

3. 
function指出这是一个函数定义；
abs是函数的名称；
(x)括号内列出函数的参数，多个参数以,分隔；
{ ... }之间的代码是函数体，可以包含若干语句，甚至可以没有任何语句。


4. 请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

5. 如果没有return语句，函数执行完毕后也会返回结果，只是结果为undefined。

6. 由于JavaScript的函数也是一个对象，上述定义的abs()函数实际上是一个函数对象，而函数名abs可以视为指向该函数的变量。

7. 因此，第二种定义函数的方式如下：

```
var abs = function (x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
};
```
8. 在这种方式下，function (x) { ... }是一个匿名函数，它没有函数名。但是，这个匿名函数赋值给了变量abs，所以，通过变量abs就可以调用该函数。

9. 上述两种定义完全等价，注意第二种方式按照完整语法需要在函数体末尾加一个;，表示赋值语句结束。

#### 调用函数 
1. 调用函数时，按顺序传入参数即可：

```
abs(10); // 返回10
abs(-9); // 返回9
```
2. 由于JavaScript允许传入任意个参数而不影响调用，因此传入的参数比定义的参数多也没有问题，虽然函数内部并不需要这些参数：

```
abs(10, 'blablabla'); // 返回10
abs(-9, 'haha', 'hehe', null); // 返回9
```
3. 传入的参数比定义的少也没有问题：

```
abs(); // 返回NaN
```
4. 此时abs(x)函数的参数x将收到undefined，计算结果为NaN。

5. 要避免收到undefined，可以对参数进行检查：

```
function abs(x) {
    if (typeof x !== 'number') {
        throw 'Not a number';
    }
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
```
#### arguments 
1. JavaScript还有一个免费赠送的关键字arguments，它只在函数内部起作用，并且永远指向当前函数的调用者传入的所有参数。arguments类似Array但它不是一个Array：

```
'use strict'
----
function foo(x) {
    console.log('x = ' + x); // 10
    for (var i=0; i<arguments.length; i++) {
        console.log('arg ' + i + ' = ' + arguments[i]); // 10, 20, 30
    }
}
foo(10, 20, 30);
```
2. 利用arguments，你可以获得调用者传入的所有参数。也就是说，即使函数不定义任何参数，还是可以拿到参数的值：

```
function abs() {
    if (arguments.length === 0) {
        return 0;
    }
    var x = arguments[0];
    return x >= 0 ? x : -x;
}

abs(); // 0
abs(10); // 10
abs(-9); // 9
```
3. 实际上arguments最常用于判断传入参数的个数。你可能会看到这样的写法：

```
// foo(a[, b], c)
// 接收2~3个参数，b是可选参数，如果只传2个参数，b默认为null：
function foo(a, b, c) {
    if (arguments.length === 2) {
        // 实际拿到的参数是a和b，c为undefined
        c = b; // 把b赋给c
        b = null; // b变为默认值
    }
    // ...
}
```
4. 要把中间的参数b变为“可选”参数，就只能通过arguments判断，然后重新调整参数并赋值。

#### rest参数 
1. 由于JavaScript函数允许接收任意个参数，于是我们就不得不用arguments来获取所有参数：

```
function foo(a, b) {
    var i, rest = [];
    if (arguments.length > 2) {
        for (i = 2; i<arguments.length; i++) {
            rest.push(arguments[i]);
        }
    }
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
}
```
2. 为了获取除了已定义参数a、b之外的参数，我们不得不用arguments，并且循环要从索引2开始以便排除前两个参数，这种写法很别扭，只是为了获得额外的rest参数，有没有更好的方法？

3. ES6标准引入了rest参数，上面的函数可以改写为：

```
function foo(a, b, ...rest) {
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
}

foo(1, 2, 3, 4, 5);
// 结果:
// a = 1
// b = 2
// Array [ 3, 4, 5 ]

foo(1);
// 结果:
// a = 1
// b = undefined
// Array []
```
4. rest参数只能写在最后，前面用...标识，从运行结果可知，传入的参数先绑定a、b，多余的参数以数组形式交给变量rest，所以，不再需要arguments我们就获取了全部参数。

5. 如果传入的参数连正常定义的参数都没填满，也不要紧，rest参数会接收一个空数组（注意不是undefined）。

6. 因为rest参数是ES6新标准，所以你需要测试一下浏览器是否支持。请用rest参数编写一个sum()函数，接收任意个参数并返回它们的和：

```
'use strict';
----
function sum(...rest) {
   ???
}
----
// 测试:
var i, args = [];
for (i=1; i<=100; i++) {
    args.push(i);
}
if (sum() !== 0) {
    console.log('测试失败: sum() = ' + sum());
} else if (sum(1) !== 1) {
    console.log('测试失败: sum(1) = ' + sum(1));
} else if (sum(2, 3) !== 5) {
    console.log('测试失败: sum(2, 3) = ' + sum(2, 3));
} else if (sum.apply(null, args) !== 5050) {
    console.log('测试失败: sum(1, 2, 3, ..., 100) = ' + sum.apply(null, args));
} else {
    console.log('测试通过!');
}
```
#### 小心你的return语句 
1. 前面我们讲到了JavaScript引擎有一个在行末自动添加分号的机制，这可能让你栽到return语句的一个大坑：

```
function foo() {
    return { name: 'foo' };
}

foo(); // { name: 'foo' }
```
2. 如果把return语句拆成两行：

```
function foo() {
    return
        { name: 'foo' };
}

foo(); // undefined
```
3. 要小心了，由于JavaScript引擎在行末自动添加分号的机制，上面的代码实际上变成了：

```
function foo() {
    return; // 自动添加了分号，相当于return undefined;
        { name: 'foo' }; // 这行语句已经没法执行到了
}
```
4. 所以正确的多行写法是：

```
function foo() {
    return { // 这里不会自动加分号，因为{表示语句尚未结束
        name: 'foo'
    };
}
```
#### 练习 
1. 定义一个计算圆面积的函数area_of_circle()，它有两个参数：

2. 
r: 表示圆的半径；
pi: 表示π的值，如果不传，则默认3.14


```
'use strict';

function area_of_circle(r, pi) {
----
    return 0;
----
}
// 测试:
if (area_of_circle(2) === 12.56 && area_of_circle(2, 3.1416) === 12.5664) {
    console.log('测试通过');
} else {
    console.log('测试失败');
}
```
3. 小明是一个JavaScript新手，他写了一个max()函数，返回两个数中较大的那个：

```
'use strict';

function max(a, b) {
----
    if (a > b) {
        return
                a;
    } else {
        return
                b;
    }
----
}
console.log(max(15, 20));
```
4. 但是小明抱怨他的浏览器出问题了，无论传入什么数，max()函数总是返回undefined。请帮他指出问题并修复。

### 变量作用域与解构赋值
1. 在JavaScript中，用var申明的变量实际上是有作用域的。

2. 如果一个变量在函数体内部申明，则该变量的作用域为整个函数体，在函数体外不可引用该变量：

```
'use strict';

function foo() {
    var x = 1;
    x = x + 1;
}

x = x + 2; // ReferenceError! 无法在函数体外引用变量x
```
3. 如果两个不同的函数各自申明了同一个变量，那么该变量只在各自的函数体内起作用。换句话说，不同函数内部的同名变量互相独立，互不影响：

```
'use strict';

function foo() {
    var x = 1;
    x = x + 1;
}

function bar() {
    var x = 'A';
    x = x + 'B';
}
```
4. 由于JavaScript的函数可以嵌套，此时，内部函数可以访问外部函数定义的变量，反过来则不行：

```
'use strict';

function foo() {
    var x = 1;
    function bar() {
        var y = x + 1; // bar可以访问foo的变量x!
    }
    var z = y + 1; // ReferenceError! foo不可以访问bar的变量y!
}
```
5. 如果内部函数和外部函数的变量名重名怎么办？来测试一下：

```
'use strict';
----
function foo() {
    var x = 1;
    function bar() {
        var x = 'A';
        console.log('x in bar() = ' + x); // 'A'
    }
    console.log('x in foo() = ' + x); // 1
    bar();
}

foo();
```
6. 这说明JavaScript的函数在查找变量时从自身函数定义开始，从“内”向“外”查找。如果内部函数定义了与外部函数重名的变量，则内部函数的变量将“屏蔽”外部函数的变量。

#### 变量提升 
1. JavaScript的函数定义有个特点，它会先扫描整个函数体的语句，把所有申明的变量“提升”到函数顶部：

```
'use strict';

function foo() {
    var x = 'Hello, ' + y;
    console.log(x);
    var y = 'Bob';
}

foo();
```
2. 虽然是strict模式，但语句var x = 'Hello, ' + y;并不报错，原因是变量y在稍后申明了。但是console.log显示Hello, undefined，说明变量y的值为undefined。这正是因为JavaScript引擎自动提升了变量y的声明，但不会提升变量y的赋值。

3. 对于上述foo()函数，JavaScript引擎看到的代码相当于：

```
function foo() {
    var y; // 提升变量y的申明，此时y为undefined
    var x = 'Hello, ' + y;
    console.log(x);
    y = 'Bob';
}
```
4. 由于JavaScript的这一怪异的“特性”，我们在函数内部定义变量时，请严格遵守“在函数内部首先申明所有变量”这一规则。最常见的做法是用一个var申明函数内部用到的所有变量：

```
function foo() {
    var
        x = 1, // x初始化为1
        y = x + 1, // y初始化为2
        z, i; // z和i为undefined
    // 其他语句:
    for (i=0; i<100; i++) {
        ...
    }
}
```
#### 全局作用域 
1. 不在任何函数内定义的变量就具有全局作用域。实际上，JavaScript默认有一个全局对象window，全局作用域的变量实际上被绑定到window的一个属性：

```
'use strict';

var course = 'Learn JavaScript';
alert(course); // 'Learn JavaScript'
alert(window.course); // 'Learn JavaScript'
```
2. 因此，直接访问全局变量course和访问window.course是完全一样的。

3. 你可能猜到了，由于函数定义有两种方式，以变量方式var foo = function () {}定义的函数实际上也是一个全局变量，因此，顶层函数的定义也被视为一个全局变量，并绑定到window对象：

```
'use strict';

function foo() {
    alert('foo');
}

foo(); // 直接调用foo()
window.foo(); // 通过window.foo()调用
```
4. 进一步大胆地猜测，我们每次直接调用的alert()函数其实也是window的一个变量：

```
'use strict';

window.alert('调用window.alert()');
// 把alert保存到另一个变量:
var old_alert = window.alert;
// 给alert赋一个新函数:
window.alert = function () {}
----
alert('无法用alert()显示了!');
----
// 恢复alert:
window.alert = old_alert;
alert('又可以用alert()了!');
```
5. 这说明JavaScript实际上只有一个全局作用域。任何变量（函数也视为变量），如果没有在当前函数作用域中找到，就会继续往上查找，最后如果在全局作用域中也没有找到，则报ReferenceError错误。

#### 名字空间 
1. 全局变量会绑定到window上，不同的JavaScript文件如果使用了相同的全局变量，或者定义了相同名字的顶层函数，都会造成命名冲突，并且很难被发现。

2. 减少冲突的一个方法是把自己的所有变量和函数全部绑定到一个全局变量中。例如：

```
// 唯一的全局变量MYAPP:
var MYAPP = {};

// 其他变量:
MYAPP.name = 'myapp';
MYAPP.version = 1.0;

// 其他函数:
MYAPP.foo = function () {
    return 'foo';
};
```
3. 把自己的代码全部放入唯一的名字空间MYAPP中，会大大减少全局变量冲突的可能。

4. 许多著名的JavaScript库都是这么干的：jQuery，YUI，underscore等等。

#### 局部作用域 
1. 由于JavaScript的变量作用域实际上是函数内部，我们在for循环等语句块中是无法定义具有局部作用域的变量的：

```
'use strict';

function foo() {
    for (var i=0; i<100; i++) {
        //
    }
    i += 100; // 仍然可以引用变量i
}
```
2. 为了解决块级作用域，ES6引入了新的关键字let，用let替代var可以申明一个块级作用域的变量：

```
'use strict';

function foo() {
    var sum = 0;
    for (let i=0; i<100; i++) {
        sum += i;
    }
    // SyntaxError:
    i += 1;
}
```
#### 常量 
1. 由于var和let申明的是变量，如果要申明一个常量，在ES6之前是不行的，我们通常用全部大写的变量来表示“这是一个常量，不要修改它的值”：

```
var PI = 3.14;
```
2. ES6标准引入了新的关键字const来定义常量，const与let都具有块级作用域：

```
'use strict';

const PI = 3.14;
PI = 3; // 某些浏览器不报错，但是无效果！
PI; // 3.14
```
#### 解构赋值 
1. 从ES6开始，JavaScript引入了解构赋值，可以同时对一组变量进行赋值。

2. 什么是解构赋值？我们先看看传统的做法，如何把一个数组的元素分别赋值给几个变量：

```
var array = ['hello', 'JavaScript', 'ES6'];
var x = array[0];
var y = array[1];
var z = array[2];
```
3. 现在，在ES6中，可以使用解构赋值，直接对多个变量同时赋值：

```
'use strict';

// 如果浏览器支持解构赋值就不会报错:
var [x, y, z] = ['hello', 'JavaScript', 'ES6'];
----
// x, y, z分别被赋值为数组对应元素:
console.log('x = ' + x + ', y = ' + y + ', z = ' + z);
```
4. 注意，对数组元素进行解构赋值时，多个变量要用[...]括起来。

5. 如果数组本身还有嵌套，也可以通过下面的形式进行解构赋值，注意嵌套层次和位置要保持一致：

```
let [x, [y, z]] = ['hello', ['JavaScript', 'ES6']];
x; // 'hello'
y; // 'JavaScript'
z; // 'ES6'
```
6. 解构赋值还可以忽略某些元素：

```
let [, , z] = ['hello', 'JavaScript', 'ES6']; // 忽略前两个元素，只对z赋值第三个元素
z; // 'ES6'
```
7. 如果需要从一个对象中取出若干属性，也可以使用解构赋值，便于快速获取对象的指定属性：

```
'use strict';

var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school'
};
var {name, age, passport} = person;
----
// name, age, passport分别被赋值为对应属性:
console.log('name = ' + name + ', age = ' + age + ', passport = ' + passport);
```
8. 对一个对象进行解构赋值时，同样可以直接对嵌套的对象属性进行赋值，只要保证对应的层次是一致的：

```
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school',
    address: {
        city: 'Beijing',
        street: 'No.1 Road',
        zipcode: '100001'
    }
};
var {name, address: {city, zip}} = person;
name; // '小明'
city; // 'Beijing'
zip; // undefined, 因为属性名是zipcode而不是zip
// 注意: address不是变量，而是为了让city和zip获得嵌套的address对象的属性:
address; // Uncaught ReferenceError: address is not defined
```
9. 使用解构赋值对对象属性进行赋值时，如果对应的属性不存在，变量将被赋值为undefined，这和引用一个不存在的属性获得undefined是一致的。如果要使用的变量名和属性名不一致，可以用下面的语法获取：

```
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school'
};

// 把passport属性赋值给变量id:
let {name, passport:id} = person;
name; // '小明'
id; // 'G-12345678'
// 注意: passport不是变量，而是为了让变量id获得passport属性:
passport; // Uncaught ReferenceError: passport is not defined
```
10. 解构赋值还可以使用默认值，这样就避免了不存在的属性返回undefined的问题：

```
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678'
};

// 如果person对象没有single属性，默认赋值为true:
var {name, single=true} = person;
name; // '小明'
single; // true
```
11. 有些时候，如果变量已经被声明了，再次赋值的时候，正确的写法也会报语法错误：

```
// 声明变量:
var x, y;
// 解构赋值:
{x, y} = { name: '小明', x: 100, y: 200};
// 语法错误: Uncaught SyntaxError: Unexpected token =
```
12. 这是因为JavaScript引擎把{开头的语句当作了块处理，于是=不再合法。解决方法是用小括号括起来：

```
({x, y} = { name: '小明', x: 100, y: 200});
```
#### 使用场景 
1. 解构赋值在很多时候可以大大简化代码。例如，交换两个变量x和y的值，可以这么写，不再需要临时变量：

```
var x=1, y=2;
[x, y] = [y, x]
```
2. 快速获取当前页面的域名和路径：

```
var {hostname:domain, pathname:path} = location;
```
3. 如果一个函数接收一个对象作为参数，那么，可以使用解构直接把对象的属性绑定到变量中。例如，下面的函数可以快速创建一个Date对象：

```
function buildDate({year, month, day, hour=0, minute=0, second=0}) {
    return new Date(year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second);
}
```
4. 它的方便之处在于传入的对象只需要year、month和day这三个属性：

```
buildDate({ year: 2017, month: 1, day: 1 });
// Sun Jan 01 2017 00:00:00 GMT+0800 (CST)
```
5. 也可以传入hour、minute和second属性：

```
buildDate({ year: 2017, month: 1, day: 1, hour: 20, minute: 15 });
// Sun Jan 01 2017 20:15:00 GMT+0800 (CST)
```
6. 使用解构赋值可以减少代码量，但是，需要在支持ES6解构赋值特性的现代浏览器中才能正常运行。目前支持解构赋值的浏览器包括Chrome，Firefox，Edge等。

### 方法
1. 在一个对象中绑定函数，称为这个对象的方法。

2. 在JavaScript中，对象的定义是这样的：

```
var xiaoming = {
    name: '小明',
    birth: 1990
};
```
3. 但是，如果我们给xiaoming绑定一个函数，就可以做更多的事情。比如，写个age()方法，返回xiaoming的年龄：

```
var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var y = new Date().getFullYear();
        return y - this.birth;
    }
};

xiaoming.age; // function xiaoming.age()
xiaoming.age(); // 今年调用是25,明年调用就变成26了
```
4. 绑定到对象上的函数称为方法，和普通函数也没啥区别，但是它在内部使用了一个this关键字，这个东东是什么？

5. 在一个方法内部，this是一个特殊变量，它始终指向当前对象，也就是xiaoming这个变量。所以，this.birth可以拿到xiaoming的birth属性。

6. 让我们拆开写：

```
function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth;
}

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: getAge
};

xiaoming.age(); // 25, 正常结果
getAge(); // NaN
```
7. 单独调用函数getAge()怎么返回了NaN？请注意，我们已经进入到了JavaScript的一个大坑里。

8. JavaScript的函数内部如果调用了this，那么这个this到底指向谁？

9. 答案是，视情况而定！

10. 如果以对象的方法形式调用，比如xiaoming.age()，该函数的this指向被调用的对象，也就是xiaoming，这是符合我们预期的。

11. 如果单独调用函数，比如getAge()，此时，该函数的this指向全局对象，也就是window。

12. 坑爹啊！

13. 更坑爹的是，如果这么写：

```
var fn = xiaoming.age; // 先拿到xiaoming的age函数
fn(); // NaN
```
14. 也是不行的！要保证this指向正确，必须用obj.xxx()的形式调用！

15. 由于这是一个巨大的设计错误，要想纠正可没那么简单。ECMA决定，在strict模式下让函数的this指向undefined，因此，在strict模式下，你会得到一个错误：

```
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var y = new Date().getFullYear();
        return y - this.birth;
    }
};

var fn = xiaoming.age;
fn(); // Uncaught TypeError: Cannot read property 'birth' of undefined
```
16. 这个决定只是让错误及时暴露出来，并没有解决this应该指向的正确位置。

17. 有些时候，喜欢重构的你把方法重构了一下：

```
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - this.birth;
        }
        return getAgeFromBirth();
    }
};

xiaoming.age(); // Uncaught TypeError: Cannot read property 'birth' of undefined
```
18. 结果又报错了！原因是this指针只在age方法的函数内指向xiaoming，在函数内部定义的函数，this又指向undefined了！（在非strict模式下，它重新指向全局对象window！）

19. 修复的办法也不是没有，我们用一个that变量首先捕获this：

```
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var that = this; // 在方法内部一开始就捕获this
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - that.birth; // 用that而不是this
        }
        return getAgeFromBirth();
    }
};

xiaoming.age(); // 25
```
20. 用var that = this;，你就可以放心地在方法内部定义其他函数，而不是把所有语句都堆到一个方法中。

#### apply 
1. 虽然在一个独立的函数调用中，根据是否是strict模式，this指向undefined或window，不过，我们还是可以控制this的指向的！

2. 要指定函数的this指向哪个对象，可以用函数本身的apply方法，它接收两个参数，第一个参数就是需要绑定的this变量，第二个参数是Array，表示函数本身的参数。

3. 用apply修复getAge()调用：

```
function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth;
}

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: getAge
};

xiaoming.age(); // 25
getAge.apply(xiaoming, []); // 25, this指向xiaoming, 参数为空
```
4. 另一个与apply()类似的方法是call()，唯一区别是：

5. 

apply()把参数打包成Array再传入；


call()把参数按顺序传入。



6. 比如调用Math.max(3, 5, 4)，分别用apply()和call()实现如下：

```
Math.max.apply(null, [3, 5, 4]); // 5
Math.max.call(null, 3, 5, 4); // 5
```
7. 对普通函数调用，我们通常把this绑定为null。

#### 装饰器 
1. 利用apply()，我们还可以动态改变函数的行为。

2. JavaScript的所有对象都是动态的，即使内置的函数，我们也可以重新指向新的函数。

3. 现在假定我们想统计一下代码一共调用了多少次parseInt()，可以把所有的调用都找出来，然后手动加上count += 1，不过这样做太傻了。最佳方案是用我们自己的函数替换掉默认的parseInt()：

```
'use strict';

var count = 0;
var oldParseInt = parseInt; // 保存原函数

window.parseInt = function () {
    count += 1;
    return oldParseInt.apply(null, arguments); // 调用原函数
};
----
// 测试:
parseInt('10');
parseInt('20');
parseInt('30');
console.log('count = ' + count); // 3
```
### 高阶函数
1. 高阶函数英文叫Higher-order function。那么什么是高阶函数？

2. JavaScript的函数其实都指向某个变量。既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

3. 一个最简单的高阶函数：

```
function add(x, y, f) {
    return f(x) + f(y);
}
```
4. 当我们调用add(-5, 6, Math.abs)时，参数x，y和f分别接收-5，6和函数Math.abs，根据函数定义，我们可以推导计算过程为：

```
x = -5;
y = 6;
f = Math.abs;
f(x) + f(y) ==> Math.abs(-5) + Math.abs(6) ==> 11;
return 11;
```
5. 用代码验证一下：

```
'use strict';

function add(x, y, f) {
    return f(x) + f(y);
}
----
var x = add(-5, 6, Math.abs); // 11
console.log(x);
```
6. 编写高阶函数，就是让函数的参数能够接收别的函数。

### 闭包
#### 函数作为返回值 
1. 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

2. 我们来实现一个对Array的求和。通常情况下，求和的函数是这样定义的：

```
function sum(arr) {
    return arr.reduce(function (x, y) {
        return x + y;
    });
}

sum([1, 2, 3, 4, 5]); // 15
```
3. 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数！

```
function lazy_sum(arr) {
    var sum = function () {
        return arr.reduce(function (x, y) {
            return x + y;
        });
    }
    return sum;
}
```
4. 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：

```
var f = lazy_sum([1, 2, 3, 4, 5]); // function sum()
```
5. 调用函数f时，才真正计算求和的结果：

```
f(); // 15
```
6. 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

7. 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

```
var f1 = lazy_sum([1, 2, 3, 4, 5]);
var f2 = lazy_sum([1, 2, 3, 4, 5]);
f1 === f2; // false
```
8. f1()和f2()的调用结果互不影响。

#### 闭包 
1. 注意到返回的函数在其定义内部引用了局部变量arr，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

2. 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：

```
function count() {
    var arr = [];
    for (var i=1; i<=3; i++) {
        arr.push(function () {
            return i * i;
        });
    }
    return arr;
}

var results = count();
var f1 = results[0];
var f2 = results[1];
var f3 = results[2];
```
3. 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都添加到一个Array中返回了。

4. 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：

```
f1(); // 16
f2(); // 16
f3(); // 16
```
5. 全部都是16！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了4，因此最终结果为16。

6. 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

7. 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

```
function count() {
    var arr = [];
    for (var i=1; i<=3; i++) {
        arr.push((function (n) {
            return function () {
                return n * n;
            }
        })(i));
    }
    return arr;
}

var results = count();
var f1 = results[0];
var f2 = results[1];
var f3 = results[2];

f1(); // 1
f2(); // 4
f3(); // 9
```
8. 注意这里用了一个“创建一个匿名函数并立刻执行”的语法：

```
(function (x) {
    return x * x;
})(3); // 9
```
9. 理论上讲，创建一个匿名函数并立刻执行可以这么写：

```
function (x) { return x * x } (3);
```
10. 但是由于JavaScript语法解析的问题，会报SyntaxError错误，因此需要用括号把整个函数定义括起来：

```
(function (x) { return x * x }) (3);
```
11. 通常，一个立即执行的匿名函数可以把函数体拆开，一般这么写：

```
(function (x) {
    return x * x;
})(3);
```
12. 说了这么多，难道闭包就是为了返回一个函数然后延迟执行吗？

13. 当然不是！闭包有非常强大的功能。举个栗子：

14. 在面向对象的程序设计语言里，比如Java和C++，要在对象内部封装一个私有变量，可以用private修饰一个成员变量。

15. 在没有class机制，只有函数的语言里，借助闭包，同样可以封装一个私有变量。我们用JavaScript创建一个计数器：

```
'use strict';

function create_counter(initial) {
    var x = initial || 0;
    return {
        inc: function () {
            x += 1;
            return x;
        }
    }
}
```
16. 它用起来像这样：

```
var c1 = create_counter();
c1.inc(); // 1
c1.inc(); // 2
c1.inc(); // 3

var c2 = create_counter(10);
c2.inc(); // 11
c2.inc(); // 12
c2.inc(); // 13
```
17. 在返回的对象中，实现了一个闭包，该闭包携带了局部变量x，并且，从外部代码根本无法访问到变量x。换句话说，闭包就是携带状态的函数，并且它的状态可以完全对外隐藏起来。

18. 闭包还可以把多参数的函数变成单参数的函数。例如，要计算xy可以用Math.pow(x, y)函数，不过考虑到经常计算x2或x3，我们可以利用闭包创建新的函数pow2和pow3：

```
'use strict';

function make_pow(n) {
    return function (x) {
        return Math.pow(x, n);
    }
}
----
// 创建两个新函数:
var pow2 = make_pow(2);
var pow3 = make_pow(3);

console.log(pow2(5)); // 25
console.log(pow3(7)); // 343
```
#### 脑洞大开 
1. 很久很久以前，有个叫阿隆佐·邱奇的帅哥，发现只需要用函数，就可以用计算机实现运算，而不需要0、1、2、3这些数字和+、-、*、/这些符号。

2. JavaScript支持函数，所以可以用JavaScript用函数来写这些计算。来试试：

```
'use strict';

// 定义数字0:
var zero = function (f) {
    return function (x) {
        return x;
    }
};

// 定义数字1:
var one = function (f) {
    return function (x) {
        return f(x);
    }
};

// 定义加法:
function add(n, m) {
    return function (f) {
        return function (x) {
            return m(f)(n(f)(x));
        }
    }
}
----
// 计算数字2 = 1 + 1:
var two = add(one, one);

// 计算数字3 = 1 + 2:
var three = add(one, two);

// 计算数字5 = 2 + 3:
var five = add(two, three);

// 你说它是3就是3，你说它是5就是5，你怎么证明？

// 呵呵，看这里:

// 给3传一个函数,会打印3次:
(three(function () {
    console.log('print 3 times');
}))();

// 给5传一个函数,会打印5次:
(five(function () {
    console.log('print 5 times');
}))();

// 继续接着玩一会...
```
### 箭头函数
1. ES6标准新增了一种新的函数：Arrow Function（箭头函数）。

2. 为什么叫Arrow Function？因为它的定义用的就是一个箭头：

```
x => x * x
```
3. 上面的箭头函数相当于：

```
function (x) {
    return x * x;
}
```
4. 在继续学习箭头函数之前，请测试你的浏览器是否支持ES6的Arrow Function：

```
'use strict';
----
var fn = x => x * x;
----
console.log('你的浏览器支持ES6的Arrow Function!');
```
5. 箭头函数相当于匿名函数，并且简化了函数定义。箭头函数有两种格式，一种像上面的，只包含一个表达式，连{ ... }和return都省略掉了。还有一种可以包含多条语句，这时候就不能省略{ ... }和return：

```
x => {
    if (x > 0) {
        return x * x;
    }
    else {
        return - x * x;
    }
}
```
6. 如果参数不是一个，就需要用括号()括起来：

```
// 两个参数:
(x, y) => x * x + y * y

// 无参数:
() => 3.14

// 可变参数:
(x, y, ...rest) => {
    var i, sum = x + y;
    for (i=0; i<rest.length; i++) {
        sum += rest[i];
    }
    return sum;
}
```
7. 如果要返回一个对象，就要注意，如果是单表达式，这么写的话会报错：

```
// SyntaxError:
x => { foo: x }
```
8. 因为和函数体的{ ... }有语法冲突，所以要改为：

```
// ok:
x => ({ foo: x })
```
#### this 
1. 箭头函数看上去是匿名函数的一种简写，但实际上，箭头函数和匿名函数有个明显的区别：箭头函数内部的this是词法作用域，由上下文确定。

2. 回顾前面的例子，由于JavaScript函数对this绑定的错误处理，下面的例子无法得到预期结果：

```
var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = function () {
            return new Date().getFullYear() - this.birth; // this指向window或undefined
        };
        return fn();
    }
};
```
3. 现在，箭头函数完全修复了this的指向，this总是指向词法作用域，也就是外层调用者obj：

```
var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = () => new Date().getFullYear() - this.birth; // this指向obj对象
        return fn();
    }
};
obj.getAge(); // 25
```
4. 如果使用箭头函数，以前的那种hack写法：

```
var that = this;
```
5. 就不再需要了。

6. 由于this在箭头函数中已经按照词法作用域绑定了，所以，用call()或者apply()调用箭头函数时，无法对this进行绑定，即传入的第一个参数被忽略：

```
var obj = {
    birth: 1990,
    getAge: function (year) {
        var b = this.birth; // 1990
        var fn = (y) => y - this.birth; // this.birth仍是1990
        return fn.call({birth:2000}, year);
    }
};
obj.getAge(2015); // 25
```
#### 练习 
1. 请使用箭头函数简化排序时传入的函数：

```
'use strict'
var arr = [10, 20, 1, 2];
----
arr.sort((x, y) => {
    ???
});
console.log(arr); // [1, 2, 10, 20]
```
### generator
1. generator（生成器）是ES6标准引入的新的数据类型。一个generator看上去像一个函数，但可以返回多次。

2. ES6定义generator标准的哥们借鉴了Python的generator的概念和语法，如果你对Python的generator很熟悉，那么ES6的generator就是小菜一碟了。如果你对Python还不熟，赶快恶补Python教程！。

3. 我们先复习函数的概念。一个函数是一段完整的代码，调用一个函数就是传入参数，然后返回结果：

```
function foo(x) {
    return x + x;
}

var r = foo(1); // 调用foo函数
```
4. 函数在执行过程中，如果没有遇到return语句（函数末尾如果没有return，就是隐含的return undefined;），控制权无法交回被调用的代码。

5. generator跟函数很像，定义如下：

```
function* foo(x) {
    yield x + 1;
    yield x + 2;
    return x + 3;
}
```
6. generator和函数不同的是，generator由function*定义（注意多出的*号），并且，除了return语句，还可以用yield返回多次。

7. 大多数同学立刻就晕了，generator就是能够返回多次的“函数”？返回多次有啥用？

8. 还是举个栗子吧。

9. 我们以一个著名的斐波那契数列为例，它由0，1开头：

```
0 1 1 2 3 5 8 13 21 34 ...
```
10. 要编写一个产生斐波那契数列的函数，可以这么写：

```
function fib(max) {
    var
        t,
        a = 0,
        b = 1,
        arr = [0, 1];
    while (arr.length < max) {
        [a, b] = [b, a + b];
        arr.push(b);
    }
    return arr;
}

// 测试:
fib(5); // [0, 1, 1, 2, 3]
fib(10); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
11. 函数只能返回一次，所以必须返回一个Array。但是，如果换成generator，就可以一次返回一个数，不断返回多次。用generator改写如下：

```
function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 0;
    while (n < max) {
        yield a;
        [a, b] = [b, a + b];
        n ++;
    }
    return;
}
```
12. 直接调用试试：

```
fib(5); // fib {[[GeneratorStatus]]: "suspended", [[GeneratorReceiver]]: Window}
```
13. 直接调用一个generator和调用函数不一样，fib(5)仅仅是创建了一个generator对象，还没有去执行它。

14. 调用generator对象有两个方法，一是不断地调用generator对象的next()方法：

```
var f = fib(5);
f.next(); // {value: 0, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 2, done: false}
f.next(); // {value: 3, done: false}
f.next(); // {value: undefined, done: true}
```
15. next()方法会执行generator的代码，然后，每次遇到yield x;就返回一个对象{value: x, done: true/false}，然后“暂停”。返回的value就是yield的返回值，done表示这个generator是否已经执行结束了。如果done为true，则value就是return的返回值。

16. 当执行到done为true时，这个generator对象就已经全部执行完毕，不要再继续调用next()了。

17. 第二个方法是直接用for ... of循环迭代generator对象，这种方式不需要我们自己判断done：

```
'use strict'

function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 0;
    while (n < max) {
        yield a;
        [a, b] = [b, a + b];
        n ++;
    }
    return;
}
----
for (var x of fib(10)) {
    console.log(x); // 依次输出0, 1, 1, 2, 3, ...
}
```
18. generator和普通函数相比，有什么用？

19. 因为generator可以在执行过程中多次返回，所以它看上去就像一个可以记住执行状态的函数，利用这一点，写一个generator就可以实现需要用面向对象才能实现的功能。例如，用一个对象来保存状态，得这么写：

```
var fib = {
    a: 0,
    b: 1,
    n: 0,
    max: 5,
    next: function () {
        var
            r = this.a,
            t = this.a + this.b;
        this.a = this.b;
        this.b = t;
        if (this.n < this.max) {
            this.n ++;
            return r;
        } else {
            return undefined;
        }
    }
};
```
20. 用对象的属性来保存状态，相当繁琐。

21. generator还有另一个巨大的好处，就是把异步回调代码变成“同步”代码。这个好处要等到后面学了AJAX以后才能体会到。

22. 没有generator之前的黑暗时代，用AJAX时需要这么写代码：

```
ajax('http://url-1', data1, function (err, result) {
    if (err) {
        return handle(err);
    }
    ajax('http://url-2', data2, function (err, result) {
        if (err) {
            return handle(err);
        }
        ajax('http://url-3', data3, function (err, result) {
            if (err) {
                return handle(err);
            }
            return success(result);
        });
    });
});
```
23. 回调越多，代码越难看。

24. 有了generator的美好时代，用AJAX时可以这么写：

```
try {
    r1 = yield ajax('http://url-1', data1);
    r2 = yield ajax('http://url-2', data2);
    r3 = yield ajax('http://url-3', data3);
    success(r3);
}
catch (err) {
    handle(err);
}
```
25. 看上去是同步的代码，实际执行是异步的。

#### 练习 
1. 要生成一个自增的ID，可以编写一个next_id()函数：

```
var current_id = 0;

function next_id() {
    current_id ++;
    return current_id;
}
```
2. 由于函数无法保存状态，故需要一个全局变量current_id来保存数字。

3. 不用闭包，试用generator改写：

```
'use strict';
function* next_id() {
----
    ???
----
}

// 测试:
var
    x,
    pass = true,
    g = next_id();
for (x = 1; x < 100; x ++) {
    if (g.next().value !== x) {
        pass = false;
        console.log('测试失败!');
        break;
    }
}
if (pass) {
    console.log('测试通过!');
}
```
## 标准对象
1. 在JavaScript的世界里，一切都是对象。

2. 但是某些对象还是和其他对象不太一样。为了区分对象的类型，我们用typeof操作符获取对象的类型，它总是返回一个字符串：

```
typeof 123; // 'number'
typeof NaN; // 'number'
typeof 'str'; // 'string'
typeof true; // 'boolean'
typeof undefined; // 'undefined'
typeof Math.abs; // 'function'
typeof null; // 'object'
typeof []; // 'object'
typeof {}; // 'object'
```
3. 可见，number、string、boolean、function和undefined有别于其他类型。特别注意null的类型是object，Array的类型也是object，如果我们用typeof将无法区分出null、Array和通常意义上的object——{}。

#### 包装对象 
1. 除了这些类型外，JavaScript还提供了包装对象，熟悉Java的小伙伴肯定很清楚int和Integer这种暧昧关系。

2. number、boolean和string都有包装对象。没错，在JavaScript中，字符串也区分string类型和它的包装类型。包装对象用new创建：

```
var n = new Number(123); // 123,生成了新的包装类型
var b = new Boolean(true); // true,生成了新的包装类型
var s = new String('str'); // 'str',生成了新的包装类型
```
3. 虽然包装对象看上去和原来的值一模一样，显示出来也是一模一样，但他们的类型已经变为object了！所以，包装对象和原始值用===比较会返回false：

```
typeof new Number(123); // 'object'
new Number(123) === 123; // false

typeof new Boolean(true); // 'object'
new Boolean(true) === true; // false

typeof new String('str'); // 'object'
new String('str') === 'str'; // false
```
4. 所以闲的蛋疼也不要使用包装对象！尤其是针对string类型！！！

5. 如果我们在使用Number、Boolean和String时，没有写new会发生什么情况？

6. 此时，Number()、Boolean和String()被当做普通函数，把任何类型的数据转换为number、boolean和string类型（注意不是其包装类型）：

```
var n = Number('123'); // 123，相当于parseInt()或parseFloat()
typeof n; // 'number'

var b = Boolean('true'); // true
typeof b; // 'boolean'

var b2 = Boolean('false'); // true! 'false'字符串转换结果为true！因为它是非空字符串！
var b3 = Boolean(''); // false

var s = String(123.45); // '123.45'
typeof s; // 'string'
```
7. 是不是感觉头大了？这就是JavaScript特有的催眠魅力！

8. 总结一下，有这么几条规则需要遵守：

9. 

不要使用new Number()、new Boolean()、new String()创建包装对象；


用parseInt()或parseFloat()来转换任意类型到number；


用String()来转换任意类型到string，或者直接调用某个对象的toString()方法；


通常不必把任意类型转换为boolean再判断，因为可以直接写if (myVar) {...}；


typeof操作符可以判断出number、boolean、string、function和undefined；


判断Array要使用Array.isArray(arr)；


判断null请使用myVar === null；


判断某个全局变量是否存在用typeof window.myVar === 'undefined'；


函数内部判断某个变量是否存在用typeof myVar === 'undefined'。



10. 最后有细心的同学指出，任何对象都有toString()方法吗？null和undefined就没有！确实如此，这两个特殊值要除外，虽然null还伪装成了object类型。

11. 更细心的同学指出，number对象调用toString()报SyntaxError：

```
123.toString(); // SyntaxError
```
12. 遇到这种情况，要特殊处理一下：

```
123..toString(); // '123', 注意是两个点！
(123).toString(); // '123'
```
13. 不要问为什么，这就是JavaScript代码的乐趣！

### Date
1. 在JavaScript中，Date对象用来表示日期和时间。

2. 要获取系统当前时间，用：

```
var now = new Date();
now; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
now.getFullYear(); // 2015, 年份
now.getMonth(); // 5, 月份，注意月份范围是0~11，5表示六月
now.getDate(); // 24, 表示24号
now.getDay(); // 3, 表示星期三
now.getHours(); // 19, 24小时制
now.getMinutes(); // 49, 分钟
now.getSeconds(); // 22, 秒
now.getMilliseconds(); // 875, 毫秒数
now.getTime(); // 1435146562875, 以number形式表示的时间戳
```
3. 注意，当前时间是浏览器从本机操作系统获取的时间，所以不一定准确，因为用户可以把当前时间设定为任何值。

4. 如果要创建一个指定日期和时间的Date对象，可以用：

```
var d = new Date(2015, 5, 19, 20, 15, 30, 123);
d; // Fri Jun 19 2015 20:15:30 GMT+0800 (CST)
```
5. 你可能观察到了一个非常非常坑爹的地方，就是JavaScript的月份范围用整数表示是0~11，0表示一月，1表示二月……，所以要表示6月，我们传入的是5！这绝对是JavaScript的设计者当时脑抽了一下，但是现在要修复已经不可能了。

```
JavaScript的Date对象月份值从0开始，牢记0=1月，1=2月，2=3月，……，11=12月。
```
6. 第二种创建一个指定日期和时间的方法是解析一个符合ISO 8601格式的字符串：

```
var d = Date.parse('2015-06-24T19:49:22.875+08:00');
d; // 1435146562875
```
7. 但它返回的不是Date对象，而是一个时间戳。不过有时间戳就可以很容易地把它转换为一个Date：

```
var d = new Date(1435146562875);
d; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
d.getMonth(); // 5
```
```
使用Date.parse()时传入的字符串使用实际月份01~12，转换为Date对象后getMonth()获取的月份值为0~11。
```
#### 时区 
1. Date对象表示的时间总是按浏览器所在时区显示的，不过我们既可以显示本地时间，也可以显示调整后的UTC时间：

```
var d = new Date(1435146562875);
d.toLocaleString(); // '2015/6/24 下午7:49:22'，本地时间（北京时区+8:00），显示的字符串与操作系统设定的格式有关
d.toUTCString(); // 'Wed, 24 Jun 2015 11:49:22 GMT'，UTC时间，与本地时间相差8小时
```
2. 那么在JavaScript中如何进行时区转换呢？实际上，只要我们传递的是一个number类型的时间戳，我们就不用关心时区转换。任何浏览器都可以把一个时间戳正确转换为本地时间。

3. 时间戳是个什么东西？时间戳是一个自增的整数，它表示从1970年1月1日零时整的GMT时区开始的那一刻，到现在的毫秒数。假设浏览器所在电脑的时间是准确的，那么世界上无论哪个时区的电脑，它们此刻产生的时间戳数字都是一样的，所以，时间戳可以精确地表示一个时刻，并且与时区无关。

4. 所以，我们只需要传递时间戳，或者把时间戳从数据库里读出来，再让JavaScript自动转换为当地时间就可以了。

5. 要获取当前时间戳，可以用：

```
'use strict';
----
if (Date.now) {
    console.log(Date.now()); // 老版本IE没有now()方法
} else {
    console.log(new Date().getTime());
}
```
#### 练习 
1. 小明为了和女友庆祝情人节，特意制作了网页，并提前预定了法式餐厅。小明打算用JavaScript给女友一个惊喜留言：

```
'use strict';
----
var today = new Date();
if (today.getMonth() === 2 && today.getDate() === 14) {
    alert('亲爱的，我预定了晚餐，晚上6点在餐厅见！');
}
```
2. 结果女友并未出现。小明非常郁闷，请你帮忙分析他的JavaScript代码有何问题。

3. 

### RegExp
1. 字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。比如判断一个字符串是否是合法的Email地址，虽然可以编程提取@前后的子串，再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用。

2. 正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

3. 所以我们判断一个字符串是否是合法的Email的方法是：

4. 

创建一个匹配Email的正则表达式；


用该正则表达式去匹配用户的输入来判断是否合法。



5. 因为正则表达式也是用字符串表示的，所以，我们要首先了解如何用字符来描述字符。

6. 在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：

7. 

'00\d'可以匹配'007'，但无法匹配'00A'；


'\d\d\d'可以匹配'010'；


'\w\w'可以匹配'js'；



8. .可以匹配任意字符，所以：

9. 
'js.'可以匹配'jsp'、'jss'、'js!'等等。


10. 要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：

11. 来看一个复杂的例子：\d{3}\s+\d{3,8}。

12. 我们来从左到右解读一下：

13. 

\d{3}表示匹配3个数字，例如'010'；


\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，'\t\t'等；


\d{3,8}表示3-8个数字，例如'1234567'。



14. 综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。

15. 如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。

16. 但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。

#### 进阶 
1. 要做更精确地匹配，可以用[]表示范围，比如：

2. 

[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；


[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'js2015'等等；


[a-zA-Z\_\$][0-9a-zA-Z\_\$]*可以匹配由字母或下划线、$开头，后接任意个由一个数字、字母或者下划线、$组成的字符串，也就是JavaScript允许的变量名；


[a-zA-Z\_\$][0-9a-zA-Z\_\$]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。



3. A|B可以匹配A或B，所以(J|j)ava(S|s)cript可以匹配'JavaScript'、'Javascript'、'javaScript'或者'javascript'。

4. ^表示行的开头，^\d表示必须以数字开头。

5. $表示行的结束，\d$表示必须以数字结束。

6. 你可能注意到了，js也可以匹配'jsp'，但是加上^js$就变成了整行匹配，就只能匹配'js'了。

#### RegExp 
1. 有了准备知识，我们就可以在JavaScript中使用正则表达式了。

2. JavaScript有两种方式创建一个正则表达式：

3. 第一种方式是直接通过/正则表达式/写出来，第二种方式是通过new RegExp('正则表达式')创建一个RegExp对象。

4. 两种写法是一样的：

```
var re1 = /ABC\-001/;
var re2 = new RegExp('ABC\\-001');

re1; // /ABC\-001/
re2; // /ABC\-001/
```
5. 注意，如果使用第二种写法，因为字符串的转义问题，字符串的两个\\实际上是一个\。

6. 先看看如何判断正则表达式是否匹配：

```
var re = /^\d{3}\-\d{3,8}$/;
re.test('010-12345'); // true
re.test('010-1234x'); // false
re.test('010 12345'); // false
```
7. RegExp对象的test()方法用于测试给定的字符串是否符合条件。

#### 切分字符串 
1. 用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码：

```
'a b   c'.split(' '); // ['a', 'b', '', '', 'c']
```
2. 嗯，无法识别连续的空格，用正则表达式试试：

```
'a b   c'.split(/\s+/); // ['a', 'b', 'c']
```
3. 无论多少个空格都可以正常分割。加入,试试：

```
'a,b, c  d'.split(/[\s\,]+/); // ['a', 'b', 'c', 'd']
```
4. 再加入;试试：

```
'a,b;; c  d'.split(/[\s\,\;]+/); // ['a', 'b', 'c', 'd']
```
5. 如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组。

#### 分组 
1. 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：

2. ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：

```
var re = /^(\d{3})-(\d{3,8})$/;
re.exec('010-12345'); // ['010-12345', '010', '12345']
re.exec('010 12345'); // null
```
3. 如果正则表达式中定义了组，就可以在RegExp对象上用exec()方法提取出子串来。

4. exec()方法在匹配成功后，会返回一个Array，第一个元素是正则表达式匹配到的整个字符串，后面的字符串表示匹配成功的子串。

5. exec()方法在匹配失败时返回null。

6. 提取子串非常有用。来看一个更凶残的例子：

```
var re = /^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$/;
re.exec('19:05:30'); // ['19:05:30', '19', '05', '30']
```
7. 这个正则表达式可以直接识别合法的时间。但是有些时候，用正则表达式也无法做到完全验证，比如识别日期：

```
var re = /^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$/;
```
8. 对于'2-30'，'4-31'这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。

#### 贪婪匹配 
1. 需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：

```
var re = /^(\d+)(0*)$/;
re.exec('102300'); // ['102300', '102300', '']
```
2. 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。

3. 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：

```
var re = /^(\d+?)(0*)$/;
re.exec('102300'); // ['102300', '1023', '00']
```
#### 全局搜索 
1. JavaScript的正则表达式还有几个特殊的标志，最常用的是g，表示全局匹配：

```
var r1 = /test/g;
// 等价于:
var r2 = new RegExp('test', 'g');
```
2. 全局匹配可以多次执行exec()方法来搜索一个匹配的字符串。当我们指定g标志后，每次运行exec()，正则表达式本身会更新lastIndex属性，表示上次匹配到的最后索引：

```
var s = 'JavaScript, VBScript, JScript and ECMAScript';
var re=/[a-zA-Z]+Script/g;

// 使用全局匹配:
re.exec(s); // ['JavaScript']
re.lastIndex; // 10

re.exec(s); // ['VBScript']
re.lastIndex; // 20

re.exec(s); // ['JScript']
re.lastIndex; // 29

re.exec(s); // ['ECMAScript']
re.lastIndex; // 44

re.exec(s); // null，直到结束仍没有匹配到
```
3. 全局匹配类似搜索，因此不能使用/^...$/，那样只会最多匹配一次。

4. 正则表达式还可以指定i标志，表示忽略大小写，m标志，表示执行多行匹配。

#### 小结 
1. 正则表达式非常强大，要在短短的一节里讲完是不可能的。要讲清楚正则的所有内容，可以写一本厚厚的书了。如果你经常遇到正则表达式的问题，你可能需要一本正则表达式的参考书。

#### 练习 
1. 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

```
'use strict';
----
var re = /^$/;
----
// 测试:
var
    i,
    success = true,
    should_pass = ['someone@gmail.com', 'bill.gates@microsoft.com', 'tom@voyager.org', 'bob2015@163.com'],
    should_fail = ['test#gmail.com', 'bill@microsoft', 'bill%gates@ms.com', '@voyager.org'];
for (i = 0; i < should_pass.length; i++) {
    if (!re.test(should_pass[i])) {
        console.log('测试失败: ' + should_pass[i]);
        success = false;
        break;
    }
}
for (i = 0; i < should_fail.length; i++) {
    if (re.test(should_fail[i])) {
        console.log('测试失败: ' + should_fail[i]);
        success = false;
        break;
    }
}
if (success) {
    console.log('测试通过!');
}
```
2. 版本二可以验证并提取出带名字的Email地址：

```
'use strict';
----
var re = /^$/;
----
// 测试:
var r = re.exec('<Tom Paris> tom@voyager.org');
if (r === null || r.toString() !== ['<Tom Paris> tom@voyager.org', 'Tom Paris', 'tom@voyager.org'].toString()) {
    console.log('测试失败!');
}
else {
    console.log('测试成功!');
}
```
### JSON
1. JSON是JavaScript Object Notation的缩写，它是一种数据交换格式。

2. 在JSON出现之前，大家一直用XML来传递数据。因为XML是一种纯文本格式，所以它适合在网络上交换数据。XML本身不算复杂，但是，加上DTD、XSD、XPath、XSLT等一大堆复杂的规范以后，任何正常的软件开发人员碰到XML都会感觉头大了，最后大家发现，即使你努力钻研几个月，也未必搞得清楚XML的规范。

3. 终于，在2002年的一天，道格拉斯·克罗克福特（Douglas Crockford）同学为了拯救深陷水深火热同时又被某几个巨型软件企业长期愚弄的软件工程师，发明了JSON这种超轻量级的数据交换格式。

4. 道格拉斯同学长期担任雅虎的高级架构师，自然钟情于JavaScript。他设计的JSON实际上是JavaScript的一个子集。在JSON中，一共就这么几种数据类型：

5. 
number：和JavaScript的number完全一致；
boolean：就是JavaScript的true或false；
string：就是JavaScript的string；
null：就是JavaScript的null；
array：就是JavaScript的Array表示方式——[]；
object：就是JavaScript的{ ... }表示方式。


6. 以及上面的任意组合。

7. 并且，JSON还定死了字符集必须是UTF-8，表示多语言就没有问题了。为了统一解析，JSON的字符串规定必须用双引号""，Object的键也必须用双引号""。

8. 由于JSON非常简单，很快就风靡Web世界，并且成为ECMA标准。几乎所有编程语言都有解析JSON的库，而在JavaScript中，我们可以直接使用JSON，因为JavaScript内置了JSON的解析。

9. 把任何JavaScript对象变成JSON，就是把这个对象序列化成一个JSON格式的字符串，这样才能够通过网络传递给其他计算机。

10. 如果我们收到一个JSON格式的字符串，只需要把它反序列化成一个JavaScript对象，就可以在JavaScript中直接使用这个对象了。

#### 序列化 
1. 让我们先把小明这个对象序列化成JSON格式的字符串：

```
'use strict';

var xiaoming = {
    name: '小明',
    age: 14,
    gender: true,
    height: 1.65,
    grade: null,
    'middle-school': '\"W3C\" Middle School',
    skills: ['JavaScript', 'Java', 'Python', 'Lisp']
};
----
var s = JSON.stringify(xiaoming);
console.log(s);
```
2. 要输出得好看一些，可以加上参数，按缩进输出：

```
JSON.stringify(xiaoming, null, '  ');
```
3. 结果：

```
{
  "name": "小明",
  "age": 14,
  "gender": true,
  "height": 1.65,
  "grade": null,
  "middle-school": "\"W3C\" Middle School",
  "skills": [
    "JavaScript",
    "Java",
    "Python",
    "Lisp"
  ]
}
```
4. 第二个参数用于控制如何筛选对象的键值，如果我们只想输出指定的属性，可以传入Array：

```
JSON.stringify(xiaoming, ['name', 'skills'], '  ');
```
5. 结果：

```
{
  "name": "小明",
  "skills": [
    "JavaScript",
    "Java",
    "Python",
    "Lisp"
  ]
}
```
6. 还可以传入一个函数，这样对象的每个键值对都会被函数先处理：

```
function convert(key, value) {
    if (typeof value === 'string') {
        return value.toUpperCase();
    }
    return value;
}

JSON.stringify(xiaoming, convert, '  ');
```
7. 上面的代码把所有属性值都变成大写：

```
{
  "name": "小明",
  "age": 14,
  "gender": true,
  "height": 1.65,
  "grade": null,
  "middle-school": "\"W3C\" MIDDLE SCHOOL",
  "skills": [
    "JAVASCRIPT",
    "JAVA",
    "PYTHON",
    "LISP"
  ]
}
```
8. 如果我们还想要精确控制如何序列化小明，可以给xiaoming定义一个toJSON()的方法，直接返回JSON应该序列化的数据：

```
var xiaoming = {
    name: '小明',
    age: 14,
    gender: true,
    height: 1.65,
    grade: null,
    'middle-school': '\"W3C\" Middle School',
    skills: ['JavaScript', 'Java', 'Python', 'Lisp'],
    toJSON: function () {
        return { // 只输出name和age，并且改变了key：
            'Name': this.name,
            'Age': this.age
        };
    }
};

JSON.stringify(xiaoming); // '{"Name":"小明","Age":14}'
```
#### 反序列化 
1. 拿到一个JSON格式的字符串，我们直接用JSON.parse()把它变成一个JavaScript对象：

```
JSON.parse('[1,2,3,true]'); // [1, 2, 3, true]
JSON.parse('{"name":"小明","age":14}'); // Object {name: '小明', age: 14}
JSON.parse('true'); // true
JSON.parse('123.45'); // 123.45
```
2. JSON.parse()还可以接收一个函数，用来转换解析出的属性：

```
'use strict';
----
var obj = JSON.parse('{"name":"小明","age":14}', function (key, value) {
    if (key === 'name') {
        return value + '同学';
    }
    return value;
});
console.log(JSON.stringify(obj)); // {name: '小明同学', age: 14}
```
3. 在JavaScript中使用JSON，就是这么简单！

#### 练习 
1. 用浏览器访问OpenWeatherMap的天气API，查看返回的JSON数据，然后返回城市、天气预报等信息：

```
'use strict'

var url = 'https://api.openweathermap.org/data/2.5/forecast?q=Beijing,cn&appid=800f49846586c3ba6e7052cfc89af16c';
$.getJSON(url, function (data) {
----
    var info = {
        city: data.city.name,
        weather: data.list[0].weather[0].main,
        time: data.list[0].dt_txt
    };
    alert(JSON.stringify(info, null, '  '));
----
});
```
## 面向对象编程
1. JavaScript的所有数据都可以看成对象，那是不是我们已经在使用面向对象编程了呢？

2. 当然不是。如果我们只使用Number、Array、string以及基本的{...}定义的对象，还无法发挥出面向对象编程的威力。

3. JavaScript的面向对象编程和大多数其他语言如Java、C#的面向对象编程都不太一样。如果你熟悉Java或C#，很好，你一定明白面向对象的两个基本概念：

4. 

类：类是对象的类型模板，例如，定义Student类来表示学生，类本身是一种类型，Student表示学生类型，但不表示任何具体的某个学生；


实例：实例是根据类创建的对象，例如，根据Student类可以创建出xiaoming、xiaohong、xiaojun等多个实例，每个实例表示一个具体的学生，他们全都属于Student类型。



5. 所以，类和实例是大多数面向对象编程语言的基本概念。

6. 不过，在JavaScript中，这个概念需要改一改。JavaScript不区分类和实例的概念，而是通过原型（prototype）来实现面向对象编程。

7. 原型是指当我们想要创建xiaoming这个具体的学生时，我们并没有一个Student类型可用。那怎么办？恰好有这么一个现成的对象：

```
var robot = {
    name: 'Robot',
    height: 1.6,
    run: function () {
        console.log(this.name + ' is running...');
    }
};
```
8. 我们看这个robot对象有名字，有身高，还会跑，有点像小明，干脆就根据它来“创建”小明得了！

9. 于是我们把它改名为Student，然后创建出xiaoming：

```
var Student = {
    name: 'Robot',
    height: 1.2,
    run: function () {
        console.log(this.name + ' is running...');
    }
};

var xiaoming = {
    name: '小明'
};

xiaoming.__proto__ = Student;
```
10. 注意最后一行代码把xiaoming的原型指向了对象Student，看上去xiaoming仿佛是从Student继承下来的：

```
xiaoming.name; // '小明'
xiaoming.run(); // 小明 is running...
```
11. xiaoming有自己的name属性，但并没有定义run()方法。不过，由于小明是从Student继承而来，只要Student有run()方法，xiaoming也可以调用：

12. 

13. JavaScript的原型链和Java的Class区别就在，它没有“Class”的概念，所有对象都是实例，所谓继承关系不过是把一个对象的原型指向另一个对象而已。

14. 如果你把xiaoming的原型指向其他对象：

```
var Bird = {
    fly: function () {
        console.log(this.name + ' is flying...');
    }
};

xiaoming.__proto__ = Bird;
```
15. 现在xiaoming已经无法run()了，他已经变成了一只鸟：

```
xiaoming.fly(); // 小明 is flying...
```
16. 在JavaScrip代码运行时期，你可以把xiaoming从Student变成Bird，或者变成任何对象。

17. 请注意，上述代码仅用于演示目的。在编写JavaScript代码时，不要直接用obj.__proto__去改变一个对象的原型，并且，低版本的IE也无法使用__proto__。Object.create()方法可以传入一个原型对象，并创建一个基于该原型的新对象，但是新对象什么属性都没有，因此，我们可以编写一个函数来创建xiaoming：

```
// 原型对象:
var Student = {
    name: 'Robot',
    height: 1.2,
    run: function () {
        console.log(this.name + ' is running...');
    }
};

function createStudent(name) {
    // 基于Student原型创建一个新对象:
    var s = Object.create(Student);
    // 初始化新对象:
    s.name = name;
    return s;
}

var xiaoming = createStudent('小明');
xiaoming.run(); // 小明 is running...
xiaoming.__proto__ === Student; // true
```
18. 这是创建原型继承的一种方法，JavaScript还有其他方法来创建对象，我们在后面会一一讲到。

### 创建对象
1. JavaScript对每个创建的对象都会设置一个原型，指向它的原型对象。

2. 当我们用obj.xxx访问一个对象的属性时，JavaScript引擎先在当前对象上查找该属性，如果没有找到，就到其原型对象上找，如果还没有找到，就一直上溯到Object.prototype对象，最后，如果还没有找到，就只能返回undefined。

3. 例如，创建一个Array对象：

```
var arr = [1, 2, 3];
```
4. 其原型链是：

```
arr ----> Array.prototype ----> Object.prototype ----> null
```
5. Array.prototype定义了indexOf()、shift()等方法，因此你可以在所有的Array对象上直接调用这些方法。

6. 当我们创建一个函数时：

```
function foo() {
    return 0;
}
```
7. 函数也是一个对象，它的原型链是：

```
foo ----> Function.prototype ----> Object.prototype ----> null
```
8. 由于Function.prototype定义了apply()等方法，因此，所有函数都可以调用apply()方法。

9. 很容易想到，如果原型链很长，那么访问一个对象的属性就会因为花更多的时间查找而变得更慢，因此要注意不要把原型链搞得太长。

#### 构造函数 
1. 除了直接用{ ... }创建一个对象外，JavaScript还可以用一种构造函数的方法来创建对象。它的用法是，先定义一个构造函数：

```
function Student(name) {
    this.name = name;
    this.hello = function () {
        alert('Hello, ' + this.name + '!');
    }
}
```
2. 你会问，咦，这不是一个普通函数吗？

3. 这确实是一个普通函数，但是在JavaScript中，可以用关键字new来调用这个函数，并返回一个对象：

```
var xiaoming = new Student('小明');
xiaoming.name; // '小明'
xiaoming.hello(); // Hello, 小明!
```
4. 注意，如果不写new，这就是一个普通函数，它返回undefined。但是，如果写了new，它就变成了一个构造函数，它绑定的this指向新创建的对象，并默认返回this，也就是说，不需要在最后写return this;。

5. 新创建的xiaoming的原型链是：

```
xiaoming ----> Student.prototype ----> Object.prototype ----> null
```
6. 也就是说，xiaoming的原型指向函数Student的原型。如果你又创建了xiaohong、xiaojun，那么这些对象的原型与xiaoming是一样的：

```
xiaoming ↘
xiaohong -→ Student.prototype ----> Object.prototype ----> null
xiaojun  ↗
```
7. 用new Student()创建的对象还从原型上获得了一个constructor属性，它指向函数Student本身：

```
xiaoming.constructor === Student.prototype.constructor; // true
Student.prototype.constructor === Student; // true

Object.getPrototypeOf(xiaoming) === Student.prototype; // true

xiaoming instanceof Student; // true
```
8. 看晕了吧？用一张图来表示这些乱七八糟的关系就是：

9. 

10. 红色箭头是原型链。注意，Student.prototype指向的对象就是xiaoming、xiaohong的原型对象，这个原型对象自己还有个属性constructor，指向Student函数本身。

11. 另外，函数Student恰好有个属性prototype指向xiaoming、xiaohong的原型对象，但是xiaoming、xiaohong这些对象可没有prototype这个属性，不过可以用__proto__这个非标准用法来查看。

12. 现在我们就认为xiaoming、xiaohong这些对象“继承”自Student。

13. 不过还有一个小问题，注意观察：

```
xiaoming.name; // '小明'
xiaohong.name; // '小红'
xiaoming.hello; // function: Student.hello()
xiaohong.hello; // function: Student.hello()
xiaoming.hello === xiaohong.hello; // false
```
14. xiaoming和xiaohong各自的name不同，这是对的，否则我们无法区分谁是谁了。

15. xiaoming和xiaohong各自的hello是一个函数，但它们是两个不同的函数，虽然函数名称和代码都是相同的！

16. 如果我们通过new Student()创建了很多对象，这些对象的hello函数实际上只需要共享同一个函数就可以了，这样可以节省很多内存。

17. 要让创建的对象共享一个hello函数，根据对象的属性查找原则，我们只要把hello函数移动到xiaoming、xiaohong这些对象共同的原型上就可以了，也就是Student.prototype：

18. 

19. 修改代码如下：

```
function Student(name) {
    this.name = name;
}

Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
};
```
20. 用new创建基于原型的JavaScript的对象就是这么简单！

#### 忘记写new怎么办 
1. 如果一个函数被定义为用于创建对象的构造函数，但是调用时忘记了写new怎么办？

2. 在strict模式下，this.name = name将报错，因为this绑定为undefined，在非strict模式下，this.name = name不报错，因为this绑定为window，于是无意间创建了全局变量name，并且返回undefined，这个结果更糟糕。

3. 所以，调用构造函数千万不要忘记写new。为了区分普通函数和构造函数，按照约定，构造函数首字母应当大写，而普通函数首字母应当小写，这样，一些语法检查工具如jslint将可以帮你检测到漏写的new。

4. 最后，我们还可以编写一个createStudent()函数，在内部封装所有的new操作。一个常用的编程模式像这样：

```
function Student(props) {
    this.name = props.name || '匿名'; // 默认值为'匿名'
    this.grade = props.grade || 1; // 默认值为1
}

Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
};

function createStudent(props) {
    return new Student(props || {})
}
```
5. 这个createStudent()函数有几个巨大的优点：一是不需要new来调用，二是参数非常灵活，可以不传，也可以这么传：

```
var xiaoming = createStudent({
    name: '小明'
});

xiaoming.grade; // 1
```
6. 如果创建的对象有很多属性，我们只需要传递需要的某些属性，剩下的属性可以用默认值。由于参数是一个Object，我们无需记忆参数的顺序。如果恰好从JSON拿到了一个对象，就可以直接创建出xiaoming。

#### 练习 
1. 请利用构造函数定义Cat，并让所有的Cat对象有一个name属性，并共享一个方法say()，返回字符串'Hello, xxx!'：

```
'use strict';
----
function Cat(name) {
    //
}
----
// 测试:
var kitty = new Cat('Kitty');
var doraemon = new Cat('哆啦A梦');
if (kitty && kitty.name === 'Kitty'
    && kitty.say
    && typeof kitty.say === 'function'
    && kitty.say() === 'Hello, Kitty!'
    && kitty.say === doraemon.say
) {
    console.log('测试通过!');
} else {
    console.log('测试失败!');
}
```
### 原型继承
1. 在传统的基于Class的语言如Java、C++中，继承的本质是扩展一个已有的Class，并生成新的Subclass。

2. 由于这类语言严格区分类和实例，继承实际上是类型的扩展。但是，JavaScript由于采用原型继承，我们无法直接扩展一个Class，因为根本不存在Class这种类型。

3. 但是办法还是有的。我们先回顾Student构造函数：

```
function Student(props) {
    this.name = props.name || 'Unnamed';
}

Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
}
```
4. 以及Student的原型链：

5. 

6. 现在，我们要基于Student扩展出PrimaryStudent，可以先定义出PrimaryStudent：

```
function PrimaryStudent(props) {
    // 调用Student构造函数，绑定this变量:
    Student.call(this, props);
    this.grade = props.grade || 1;
}
```
7. 但是，调用了Student构造函数不等于继承了Student，PrimaryStudent创建的对象的原型是：

```
new PrimaryStudent() ----> PrimaryStudent.prototype ----> Object.prototype ----> null
```
8. 必须想办法把原型链修改为：

```
new PrimaryStudent() ----> PrimaryStudent.prototype ----> Student.prototype ----> Object.prototype ----> null
```
9. 这样，原型链对了，继承关系就对了。新的基于PrimaryStudent创建的对象不但能调用PrimaryStudent.prototype定义的方法，也可以调用Student.prototype定义的方法。

10. 如果你想用最简单粗暴的方法这么干：

```
PrimaryStudent.prototype = Student.prototype;
```
11. 是不行的！如果这样的话，PrimaryStudent和Student共享一个原型对象，那还要定义PrimaryStudent干啥？

12. 我们必须借助一个中间对象来实现正确的原型链，这个中间对象的原型要指向Student.prototype。为了实现这一点，参考道爷（就是发明JSON的那个道格拉斯）的代码，中间对象可以用一个空函数F来实现：

```
// PrimaryStudent构造函数:
function PrimaryStudent(props) {
    Student.call(this, props);
    this.grade = props.grade || 1;
}

// 空函数F:
function F() {
}

// 把F的原型指向Student.prototype:
F.prototype = Student.prototype;

// 把PrimaryStudent的原型指向一个新的F对象，F对象的原型正好指向Student.prototype:
PrimaryStudent.prototype = new F();

// 把PrimaryStudent原型的构造函数修复为PrimaryStudent:
PrimaryStudent.prototype.constructor = PrimaryStudent;

// 继续在PrimaryStudent原型（就是new F()对象）上定义方法：
PrimaryStudent.prototype.getGrade = function () {
    return this.grade;
};

// 创建xiaoming:
var xiaoming = new PrimaryStudent({
    name: '小明',
    grade: 2
});
xiaoming.name; // '小明'
xiaoming.grade; // 2

// 验证原型:
xiaoming.__proto__ === PrimaryStudent.prototype; // true
xiaoming.__proto__.__proto__ === Student.prototype; // true

// 验证继承关系:
xiaoming instanceof PrimaryStudent; // true
xiaoming instanceof Student; // true
```
13. 用一张图来表示新的原型链：

14. 

15. 注意，函数F仅用于桥接，我们仅创建了一个new F()实例，而且，没有改变原有的Student定义的原型链。

16. 如果把继承这个动作用一个inherits()函数封装起来，还可以隐藏F的定义，并简化代码：

```
function inherits(Child, Parent) {
    var F = function () {};
    F.prototype = Parent.prototype;
    Child.prototype = new F();
    Child.prototype.constructor = Child;
}
```
17. 这个inherits()函数可以复用：

```
function Student(props) {
    this.name = props.name || 'Unnamed';
}

Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
}

function PrimaryStudent(props) {
    Student.call(this, props);
    this.grade = props.grade || 1;
}

// 实现原型继承链:
inherits(PrimaryStudent, Student);

// 绑定其他方法到PrimaryStudent原型:
PrimaryStudent.prototype.getGrade = function () {
    return this.grade;
};
```
#### 小结 
1. JavaScript的原型继承实现方式就是：

2. 

定义新的构造函数，并在内部用call()调用希望“继承”的构造函数，并绑定this；


借助中间函数F实现原型链继承，最好通过封装的inherits函数完成；


继续在新的构造函数的原型上定义新方法。



### class继承
1. 在上面的章节中我们看到了JavaScript的对象模型是基于原型实现的，特点是简单，缺点是理解起来比传统的类－实例模型要困难，最大的缺点是继承的实现需要编写大量代码，并且需要正确实现原型链。

2. 有没有更简单的写法？有！

3. 新的关键字class从ES6开始正式被引入到JavaScript中。class的目的就是让定义类更简单。

4. 我们先回顾用函数实现Student的方法：

```
function Student(name) {
    this.name = name;
}

Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
}
```
5. 如果用新的class关键字来编写Student，可以这样写：

```
class Student {
    constructor(name) {
        this.name = name;
    }

    hello() {
        alert('Hello, ' + this.name + '!');
    }
}
```
6. 比较一下就可以发现，class的定义包含了构造函数constructor和定义在原型对象上的函数hello()（注意没有function关键字），这样就避免了Student.prototype.hello = function () {...}这样分散的代码。

7. 最后，创建一个Student对象代码和前面章节完全一样：

```
var xiaoming = new Student('小明');
xiaoming.hello();
```
#### class继承 
1. 用class定义对象的另一个巨大的好处是继承更方便了。想一想我们从Student派生一个PrimaryStudent需要编写的代码量。现在，原型继承的中间对象，原型对象的构造函数等等都不需要考虑了，直接通过extends来实现：

```
class PrimaryStudent extends Student {
    constructor(name, grade) {
        super(name); // 记得用super调用父类的构造方法!
        this.grade = grade;
    }

    myGrade() {
        alert('I am at grade ' + this.grade);
    }
}

```
2. 注意PrimaryStudent的定义也是class关键字实现的，而extends则表示原型链对象来自Student。子类的构造函数可能会与父类不太相同，例如，PrimaryStudent需要name和grade两个参数，并且需要通过super(name)来调用父类的构造函数，否则父类的name属性无法正常初始化。

3. PrimaryStudent已经自动获得了父类Student的hello方法，我们又在子类中定义了新的myGrade方法。

4. ES6引入的class和原有的JavaScript原型继承有什么区别呢？实际上它们没有任何区别，class的作用就是让JavaScript引擎去实现原来需要我们自己编写的原型链代码。简而言之，用class的好处就是极大地简化了原型链代码。

5. 你一定会问，class这么好用，能不能现在就用上？

6. 现在用还早了点，因为不是所有的主流浏览器都支持ES6的class。如果一定要现在就用上，就需要一个工具把class代码转换为传统的prototype代码，可以试试Babel这个工具。

#### 练习 
1. 请利用class重新定义Cat，并让它从已有的Animal继承，然后新增一个方法say()，返回字符串'Hello, xxx!'：

```
'use strict';

class Animal {
    constructor(name) {
        this.name = name;
    }
}
----
class Cat ???
----
// 测试:
var kitty = new Cat('Kitty');
var doraemon = new Cat('哆啦A梦');
if ((new Cat('x') instanceof Animal)
    && kitty 
    && kitty.name === 'Kitty'
    && kitty.say
    && typeof kitty.say === 'function'
    && kitty.say() === 'Hello, Kitty!'
    && kitty.say === doraemon.say)
{
    console.log('测试通过!');
} else {
    console.log('测试失败!');
}
```
2. 这个练习需要浏览器支持ES6的class，如果遇到SyntaxError，则说明浏览器不支持class语法，请换一个最新的浏览器试试。

## 浏览器
1. 由于JavaScript的出现就是为了能在浏览器中运行，所以，浏览器自然是JavaScript开发者必须要关注的。

2. 目前主流的浏览器分这么几种：

3. 

IE 6~11：国内用得最多的IE浏览器，历来对W3C标准支持差。从IE10开始支持ES6标准；


Chrome：Google出品的基于Webkit内核浏览器，内置了非常强悍的JavaScript引擎——V8。由于Chrome一经安装就时刻保持自升级，所以不用管它的版本，最新版早就支持ES6了；


Safari：Apple的Mac系统自带的基于Webkit内核的浏览器，从OS X 10.7 Lion自带的6.1版本开始支持ES6，目前最新的OS X 10.11 El Capitan自带的Safari版本是9.x，早已支持ES6；


Firefox：Mozilla自己研制的Gecko内核和JavaScript引擎OdinMonkey。早期的Firefox按版本发布，后来终于聪明地学习Chrome的做法进行自升级，时刻保持最新；


移动设备上目前iOS和Android两大阵营分别主要使用Apple的Safari和Google的Chrome，由于两者都是Webkit核心，结果HTML5首先在手机上全面普及（桌面绝对是Microsoft拖了后腿），对JavaScript的标准支持也很好，最新版本均支持ES6。



4. 其他浏览器如Opera等由于市场份额太小就被自动忽略了。

5. 另外还要注意识别各种国产浏览器，如某某安全浏览器，某某旋风浏览器，它们只是做了一个壳，其核心调用的是IE，也有号称同时支持IE和Webkit的“双核”浏览器。

6. 不同的浏览器对JavaScript支持的差异主要是，有些API的接口不一样，比如AJAX，File接口。对于ES6标准，不同的浏览器对各个特性支持也不一样。

7. 在编写JavaScript的时候，就要充分考虑到浏览器的差异，尽量让同一份JavaScript代码能运行在不同的浏览器中。

### 浏览器对象
1. JavaScript可以获取浏览器提供的很多对象，并进行操作。

#### window 
1. window对象不但充当全局作用域，而且表示浏览器窗口。

2. window对象有innerWidth和innerHeight属性，可以获取浏览器窗口的内部宽度和高度。内部宽高是指除去菜单栏、工具栏、边框等占位元素后，用于显示网页的净宽高。

3. 兼容性：IE<=8不支持。

```
'use strict';
----
// 可以调整浏览器窗口大小试试:
console.log('window inner size: ' + window.innerWidth + ' x ' + window.innerHeight);
```
4. 对应的，还有一个outerWidth和outerHeight属性，可以获取浏览器窗口的整个宽高。

#### navigator 
1. navigator对象表示浏览器的信息，最常用的属性包括：

2. 
navigator.appName：浏览器名称；
navigator.appVersion：浏览器版本；
navigator.language：浏览器设置的语言；
navigator.platform：操作系统类型；
navigator.userAgent：浏览器设定的User-Agent字符串。


```
'use strict';
----
console.log('appName = ' + navigator.appName);
console.log('appVersion = ' + navigator.appVersion);
console.log('language = ' + navigator.language);
console.log('platform = ' + navigator.platform);
console.log('userAgent = ' + navigator.userAgent);
```
3. 请注意，navigator的信息可以很容易地被用户修改，所以JavaScript读取的值不一定是正确的。很多初学者为了针对不同浏览器编写不同的代码，喜欢用if判断浏览器版本，例如：

```
var width;
if (getIEVersion(navigator.userAgent) < 9) {
    width = document.body.clientWidth;
} else {
    width = window.innerWidth;
}
```
4. 但这样既可能判断不准确，也很难维护代码。正确的方法是充分利用JavaScript对不存在属性返回undefined的特性，直接用短路运算符||计算：

```
var width = window.innerWidth || document.body.clientWidth;
```
#### screen 
1. screen对象表示屏幕的信息，常用的属性有：

2. 
screen.width：屏幕宽度，以像素为单位；
screen.height：屏幕高度，以像素为单位；
screen.colorDepth：返回颜色位数，如8、16、24。


```
'use strict';
----
console.log('Screen size = ' + screen.width + ' x ' + screen.height);
```
#### location 
1. location对象表示当前页面的URL信息。例如，一个完整的URL：

```
http://www.example.com:8080/path/index.html?a=1&b=2#TOP
```
2. 可以用location.href获取。要获得URL各个部分的值，可以这么写：

```
location.protocol; // 'http'
location.host; // 'www.example.com'
location.port; // '8080'
location.pathname; // '/path/index.html'
location.search; // '?a=1&b=2'
location.hash; // 'TOP'
```
3. 要加载一个新页面，可以调用location.assign()。如果要重新加载当前页面，调用location.reload()方法非常方便。

```
'use strict';
----
if (confirm('重新加载当前页' + location.href + '?')) {
    location.reload();
} else {
    location.assign('/'); // 设置一个新的URL地址
}
```
#### document 
1. document对象表示当前页面。由于HTML在浏览器中以DOM形式表示为树形结构，document对象就是整个DOM树的根节点。

2. document的title属性是从HTML文档中的<title>xxx</title>读取的，但是可以动态改变：

```
'use strict';
----
document.title = '努力学习JavaScript!';
```
3. 请观察浏览器窗口标题的变化。

4. 要查找DOM树的某个节点，需要从document对象开始查找。最常用的查找是根据ID和Tag Name。

5. 我们先准备HTML数据：

```
<dl id="drink-menu" style="border:solid 1px #ccc;padding:6px;">
    <dt>摩卡</dt>
    <dd>热摩卡咖啡</dd>
    <dt>酸奶</dt>
    <dd>北京老酸奶</dd>
    <dt>果汁</dt>
    <dd>鲜榨苹果汁</dd>
</dl>
```
6. 用document对象提供的getElementById()和getElementsByTagName()可以按ID获得一个DOM节点和按Tag名称获得一组DOM节点：

```
'use strict';
----
var menu = document.getElementById('drink-menu');
var drinks = document.getElementsByTagName('dt');
var i, s;

s = '提供的饮料有:';
for (i=0; i<drinks.length; i++) {
    s = s + drinks[i].innerHTML + ',';
}
console.log(s);
```
7. 
    摩卡
    热摩卡咖啡
    酸奶
    北京老酸奶
    果汁
    鲜榨苹果汁


8. document对象还有一个cookie属性，可以获取当前页面的Cookie。

9. Cookie是由服务器发送的key-value标示符。因为HTTP协议是无状态的，但是服务器要区分到底是哪个用户发过来的请求，就可以用Cookie来区分。当一个用户成功登录后，服务器发送一个Cookie给浏览器，例如user=ABC123XYZ(加密的字符串)...，此后，浏览器访问该网站时，会在请求头附上这个Cookie，服务器根据Cookie即可区分出用户。

10. Cookie还可以存储网站的一些设置，例如，页面显示的语言等等。

11. JavaScript可以通过document.cookie读取到当前页面的Cookie：

```
document.cookie; // 'v=123; remember=true; prefer=zh'
```
12. 由于JavaScript能读取到页面的Cookie，而用户的登录信息通常也存在Cookie中，这就造成了巨大的安全隐患，这是因为在HTML页面中引入第三方的JavaScript代码是允许的：

```
<!-- 当前页面在wwwexample.com -->
<html>
    <head>
        <script src="http://www.foo.com/jquery.js"></script>
    </head>
    ...
</html>
```
13. 如果引入的第三方的JavaScript中存在恶意代码，则www.foo.com网站将直接获取到www.example.com网站的用户登录信息。

14. 为了解决这个问题，服务器在设置Cookie时可以使用httpOnly，设定了httpOnly的Cookie将不能被JavaScript读取。这个行为由浏览器实现，主流浏览器均支持httpOnly选项，IE从IE6 SP1开始支持。

15. 为了确保安全，服务器端在设置Cookie时，应该始终坚持使用httpOnly。

#### history 
1. history对象保存了浏览器的历史记录，JavaScript可以调用history对象的back()或forward ()，相当于用户点击了浏览器的“后退”或“前进”按钮。

2. 这个对象属于历史遗留对象，对于现代Web页面来说，由于大量使用AJAX和页面交互，简单粗暴地调用history.back()可能会让用户感到非常愤怒。

3. 新手开始设计Web页面时喜欢在登录页登录成功时调用history.back()，试图回到登录前的页面。这是一种错误的方法。

4. 任何情况，你都不应该使用history这个对象了。

### 操作DOM
1. 由于HTML文档被浏览器解析后就是一棵DOM树，要改变HTML的结构，就需要通过JavaScript来操作DOM。

2. 始终记住DOM是一个树形结构。操作一个DOM节点实际上就是这么几个操作：

3. 

更新：更新该DOM节点的内容，相当于更新了该DOM节点表示的HTML的内容；


遍历：遍历该DOM节点下的子节点，以便进行进一步操作；


添加：在该DOM节点下新增一个子节点，相当于动态增加了一个HTML节点；


删除：将该节点从HTML中删除，相当于删掉了该DOM节点的内容以及它包含的所有子节点。



4. 在操作一个DOM节点前，我们需要通过各种方式先拿到这个DOM节点。最常用的方法是document.getElementById()和document.getElementsByTagName()，以及CSS选择器document.getElementsByClassName()。

5. 由于ID在HTML文档中是唯一的，所以document.getElementById()可以直接定位唯一的一个DOM节点。document.getElementsByTagName()和document.getElementsByClassName()总是返回一组DOM节点。要精确地选择DOM，可以先定位父节点，再从父节点开始选择，以缩小范围。

6. 例如：

```
// 返回ID为'test'的节点：
var test = document.getElementById('test');

// 先定位ID为'test-table'的节点，再返回其内部所有tr节点：
var trs = document.getElementById('test-table').getElementsByTagName('tr');

// 先定位ID为'test-div'的节点，再返回其内部所有class包含red的节点：
var reds = document.getElementById('test-div').getElementsByClassName('red');

// 获取节点test下的所有直属子节点:
var cs = test.children;

// 获取节点test下第一个、最后一个子节点：
var first = test.firstElementChild;
var last = test.lastElementChild;
```
7. 第二种方法是使用querySelector()和querySelectorAll()，需要了解selector语法，然后使用条件来获取节点，更加方便：

```
// 通过querySelector获取ID为q1的节点：
var q1 = document.querySelector('#q1');

// 通过querySelectorAll获取q1节点内的符合条件的所有节点：
var ps = q1.querySelectorAll('div.highlighted > p');
```
8. 注意：低版本的IE<8不支持querySelector和querySelectorAll。IE8仅有限支持。

9. 严格地讲，我们这里的DOM节点是指Element，但是DOM节点实际上是Node，在HTML中，Node包括Element、Comment、CDATA_SECTION等很多种，以及根节点Document类型，但是，绝大多数时候我们只关心Element，也就是实际控制页面结构的Node，其他类型的Node忽略即可。根节点Document已经自动绑定为全局变量document。

#### 练习 
1. 如下的HTML结构：

2. 
  
    JavaScript
    Java
  
  
    Python
    Ruby
    Swift
  
  
    Scheme
    Haskell
  


```
<!-- HTML结构 -->
<div id="test-div">
<div class="c-red">
    <p id="test-p">JavaScript</p>
    <p>Java</p>
  </div>
  <div class="c-red c-green">
    <p>Python</p>
    <p>Ruby</p>
    <p>Swift</p>
  </div>
  <div class="c-green">
    <p>Scheme</p>
    <p>Haskell</p>
  </div>
</div>
```
3. 请选择出指定条件的节点：

```
'use strict';
----
// 选择<p>JavaScript</p>:
var js = ???;

// 选择<p>Python</p>,<p>Ruby</p>,<p>Swift</p>:
var arr = ???;

// 选择<p>Haskell</p>:
var haskell = ???;
----
// 测试:
if (!js || js.innerText !== 'JavaScript') {
    alert('选择JavaScript失败!');
} else if (!arr || arr.length !== 3 || !arr[0] || !arr[1] || !arr[2] || arr[0].innerText !== 'Python' || arr[1].innerText !== 'Ruby' || arr[2].innerText !== 'Swift') {
    console.log('选择Python,Ruby,Swift失败!');
} else if (!haskell || haskell.innerText !== 'Haskell') {
    console.log('选择Haskell失败!');
} else {
    console.log('测试通过!');
}
```
### 操作表单
1. 用JavaScript操作表单和操作DOM是类似的，因为表单本身也是DOM树。

2. 不过表单的输入框、下拉框等可以接收用户输入，所以用JavaScript来操作表单，可以获得用户输入的内容，或者对一个输入框设置新的内容。

3. HTML表单的输入控件主要有以下几种：

4. 

文本框，对应的<input type="text">，用于输入文本；


口令框，对应的<input type="password">，用于输入口令；


单选框，对应的<input type="radio">，用于选择一项；


复选框，对应的<input type="checkbox">，用于选择多项；


下拉框，对应的<select>，用于选择一项；


隐藏文本，对应的<input type="hidden">，用户不可见，但表单提交时会把隐藏文本发送到服务器。



#### 获取值 
1. 如果我们获得了一个<input>节点的引用，就可以直接调用value获得对应的用户输入值：

```
// <input type="text" id="email">
var input = document.getElementById('email');
input.value; // '用户输入的值'
```
2. 这种方式可以应用于text、password、hidden以及select。但是，对于单选框和复选框，value属性返回的永远是HTML预设的值，而我们需要获得的实际是用户是否“勾上了”选项，所以应该用checked判断：

```
// <label><input type="radio" name="weekday" id="monday" value="1"> Monday</label>
// <label><input type="radio" name="weekday" id="tuesday" value="2"> Tuesday</label>
var mon = document.getElementById('monday');
var tue = document.getElementById('tuesday');
mon.value; // '1'
tue.value; // '2'
mon.checked; // true或者false
tue.checked; // true或者false
```
#### 设置值 
1. 设置值和获取值类似，对于text、password、hidden以及select，直接设置value就可以：

```
// <input type="text" id="email">
var input = document.getElementById('email');
input.value = 'test@example.com'; // 文本框的内容已更新
```
2. 对于单选框和复选框，设置checked为true或false即可。

#### HTML5控件 
1. HTML5新增了大量标准控件，常用的包括date、datetime、datetime-local、color等，它们都使用<input>标签：

```
<input type="date" value="2015-07-01">
```
2. 

```
<input type="datetime-local" value="2015-07-01T02:03:04">
```
3. 

```
<input type="color" value="#ff0000">
```
4. 

5. 不支持HTML5的浏览器无法识别新的控件，会把它们当做type="text"来显示。支持HTML5的浏览器将获得格式化的字符串。例如，type="date"类型的input的value将保证是一个有效的YYYY-MM-DD格式的日期，或者空字符串。

#### 提交表单 
1. 最后，JavaScript可以以两种方式来处理表单的提交（AJAX方式在后面章节介绍）。

2. 方式一是通过<form>元素的submit()方法提交一个表单，例如，响应一个<button>的click事件，在JavaScript代码中提交表单：

```
<!-- HTML -->
<form id="test-form">
    <input type="text" name="test">
    <button type="button" onclick="doSubmitForm()">Submit</button>
</form>

<script>
function doSubmitForm() {
    var form = document.getElementById('test-form');
    // 可以在此修改form的input...
    // 提交form:
    form.submit();
}
</script>
```
3. 这种方式的缺点是扰乱了浏览器对form的正常提交。浏览器默认点击<button type="submit">时提交表单，或者用户在最后一个输入框按回车键。因此，第二种方式是响应<form>本身的onsubmit事件，在提交form时作修改：

```
<!-- HTML -->
<form id="test-form" onsubmit="return checkForm()">
    <input type="text" name="test">
    <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
    var form = document.getElementById('test-form');
    // 可以在此修改form的input...
    // 继续下一步:
    return true;
}
</script>
```
4. 注意要return true来告诉浏览器继续提交，如果return false，浏览器将不会继续提交form，这种情况通常对应用户输入有误，提示用户错误信息后终止提交form。

5. 在检查和修改<input>时，要充分利用<input type="hidden">来传递数据。

6. 例如，很多登录表单希望用户输入用户名和口令，但是，安全考虑，提交表单时不传输明文口令，而是口令的MD5。普通JavaScript开发人员会直接修改<input>：

```
<!-- HTML -->
<form id="login-form" method="post" onsubmit="return checkForm()">
    <input type="text" id="username" name="username">
    <input type="password" id="password" name="password">
    <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
    var pwd = document.getElementById('password');
    // 把用户输入的明文变为MD5:
    pwd.value = toMD5(pwd.value);
    // 继续下一步:
    return true;
}
</script>
```
7. 这个做法看上去没啥问题，但用户输入了口令提交时，口令框的显示会突然从几个*变成32个*（因为MD5有32个字符）。

8. 要想不改变用户的输入，可以利用<input type="hidden">实现：

```
<!-- HTML -->
<form id="login-form" method="post" onsubmit="return checkForm()">
    <input type="text" id="username" name="username">
    <input type="password" id="input-password">
    <input type="hidden" id="md5-password" name="password">
    <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
    var input_pwd = document.getElementById('input-password');
    var md5_pwd = document.getElementById('md5-password');
    // 把用户输入的明文变为MD5:
    md5_pwd.value = toMD5(input_pwd.value);
    // 继续下一步:
    return true;
}
</script>
```
9. 注意到id为md5-password的<input>标记了name="password"，而用户输入的id为input-password的<input>没有name属性。没有name属性的<input>的数据不会被提交。

#### 练习 
1. 利用JavaScript检查用户注册信息是否正确，在以下情况不满足时报错并阻止提交表单：

2. 

用户名必须是3-10位英文字母或数字；


口令必须是6-20位；


两次输入口令必须一致。



```
<!-- HTML结构 -->
<form id="test-register" action="#" target="_blank" onsubmit="return checkRegisterForm()">
    <p id="test-error" style="color:red"></p>
    <p>
        用户名: <input type="text" id="username" name="username">
    </p>
    <p>
        口令: <input type="password" id="password" name="password">
    </p>
    <p>
        重复口令: <input type="password" id="password-2">
    </p>
    <p>
        <button type="submit">提交</button> <button type="reset">重置</button>
    </p>
</form>
```
3. 
    
    
        用户名: 
    
    
        口令: 
    
    
        重复口令: 
    
    
        提交 重置
    


4. 
window.testFormHandler = function () {
    return false;
}

function checkForm() {
    var r = window.testFormHandler();
    if (r === false) {
        console.log('checkRegisterForm() return false!');
    } else {
        alert('Form可以正常提交！');
    }
    return r;
}


```
'use strict';
var checkRegisterForm = function () {
----
    // TODO:
    return false;
}
----
// 测试:
;(function () {
    window.testFormHandler = checkRegisterForm;
    var form = document.getElementById('test-register');
    if (form.dispatchEvent) {
        var event = new Event('submit', {
    		bubbles: true,
    		cancelable: true
  		});
        form.dispatchEvent(event);
    } else {
        form.fireEvent('onsubmit');
    }
})();
```
### 操作文件
1. 在HTML表单中，可以上传文件的唯一控件就是<input type="file">。

2. 注意：当一个表单包含<input type="file">时，表单的enctype必须指定为multipart/form-data，method必须指定为post，浏览器才能正确编码并以multipart/form-data格式发送表单的数据。

3. 出于安全考虑，浏览器只允许用户点击<input type="file">来选择本地文件，用JavaScript对<input type="file">的value赋值是没有任何效果的。当用户选择了上传某个文件后，JavaScript也无法获得该文件的真实路径：


6. 通常，上传的文件都由后台服务器处理，JavaScript可以在提交表单时对文件扩展名做检查，以便防止用户上传无效格式的文件：

```
var f = document.getElementById('test-file-upload');
var filename = f.value; // 'C:\fakepath\test.png'
if (!filename || !(filename.endsWith('.jpg') || filename.endsWith('.png') || filename.endsWith('.gif'))) {
    alert('Can only upload image file.');
    return false;
}
```
#### File API 
1. 由于JavaScript对用户上传的文件操作非常有限，尤其是无法读取文件内容，使得很多需要操作文件的网页不得不用Flash这样的第三方插件来实现。

2. 随着HTML5的普及，新增的File API允许JavaScript读取文件内容，获得更多的文件信息。

3. HTML5的File API提供了File和FileReader两个主要对象，可以获得文件信息并读取文件。

4. 下面的例子演示了如何读取用户选取的图片文件，并在一个<div>中预览图像：

5. 
$(function() {
    var fileInput = document.getElementById('test-image-file');
    var info = document.getElementById('test-file-info');
    var preview = document.getElementById('test-image-preview');
    fileInput.addEventListener('change', function () {
        preview.style.backgroundImage = '';
        if (!fileInput.value) {
            info.innerHTML = '没有选择文件';
            return;
        }
        var file = fileInput.files[0];
        info.innerHTML = '文件: ' + file.name + '<br>' +
                         '大小: ' + file.size + '<br>' +
                         '修改: ' + file.lastModifiedDate;
        if (file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif') {
            alert('不是有效的图片文件!');
            return;
        }
        var reader = new FileReader();
        reader.onload = function(e) {
            var
                data = e.target.result;
                index = data.indexOf(';base64,');
            preview.style.backgroundImage = 'url(' + data + ')';
        };
        reader.readAsDataURL(file);
    });
});


6. 
```
var
    fileInput = document.getElementById('test-image-file'),
    info = document.getElementById('test-file-info'),
    preview = document.getElementById('test-image-preview');
// 监听change事件:
fileInput.addEventListener('change', function () {
    // 清除背景图片:
    preview.style.backgroundImage = '';
    // 检查文件是否选择:
    if (!fileInput.value) {
        info.innerHTML = '没有选择文件';
        return;
    }
    // 获取File引用:
    var file = fileInput.files[0];
    // 获取File信息:
    info.innerHTML = '文件: ' + file.name + '<br>' +
                     '大小: ' + file.size + '<br>' +
                     '修改: ' + file.lastModifiedDate;
    if (file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/gif') {
        alert('不是有效的图片文件!');
        return;
    }
    // 读取文件:
    var reader = new FileReader();
    reader.onload = function(e) {
        var
            data = e.target.result; // 'data:image/jpeg;base64,/9j/4AAQSk...(base64编码)...'            
        preview.style.backgroundImage = 'url(' + data + ')';
    };
    // 以DataURL的形式读取文件:
    reader.readAsDataURL(file);
});
```
7. 上面的代码演示了如何通过HTML5的File API读取文件内容。以DataURL的形式读取到的文件是一个字符串，类似于data:image/jpeg;base64,/9j/4AAQSk...(base64编码)...，常用于设置图像。如果需要服务器端处理，把字符串base64,后面的字符发送给服务器并用Base64解码就可以得到原始文件的二进制内容。

#### 回调 
1. 上面的代码还演示了JavaScript的一个重要的特性就是单线程执行模式。在JavaScript中，浏览器的JavaScript执行引擎在执行JavaScript代码时，总是以单线程模式执行，也就是说，任何时候，JavaScript代码都不可能同时有多于1个线程在执行。

2. 你可能会问，单线程模式执行的JavaScript，如何处理多任务？

3. 在JavaScript中，执行多任务实际上都是异步调用，比如上面的代码：

```
reader.readAsDataURL(file);
```
4. 就会发起一个异步操作来读取文件内容。因为是异步操作，所以我们在JavaScript代码中就不知道什么时候操作结束，因此需要先设置一个回调函数：

```
reader.onload = function(e) {
    // 当文件读取完成后，自动调用此函数:
};
```
5. 当文件读取完成后，JavaScript引擎将自动调用我们设置的回调函数。执行回调函数时，文件已经读取完毕，所以我们可以在回调函数内部安全地获得文件内容。

### AJAX
1. AJAX不是JavaScript的规范，它只是一个哥们“发明”的缩写：Asynchronous JavaScript and XML，意思就是用JavaScript执行异步网络请求。

2. 如果仔细观察一个Form的提交，你就会发现，一旦用户点击“Submit”按钮，表单开始提交，浏览器就会刷新页面，然后在新页面里告诉你操作是成功了还是失败了。如果不幸由于网络太慢或者其他原因，就会得到一个404页面。

3. 这就是Web的运作原理：一次HTTP请求对应一个页面。

4. 如果要让用户留在当前页面中，同时发出新的HTTP请求，就必须用JavaScript发送这个新请求，接收到数据后，再用JavaScript更新页面，这样一来，用户就感觉自己仍然停留在当前页面，但是数据却可以不断地更新。

5. 最早大规模使用AJAX的就是Gmail，Gmail的页面在首次加载后，剩下的所有数据都依赖于AJAX来更新。

6. 用JavaScript写一个完整的AJAX代码并不复杂，但是需要注意：AJAX请求是异步执行的，也就是说，要通过回调函数获得响应。

7. 在现代浏览器上写AJAX主要依靠XMLHttpRequest对象：

```
'use strict';
----
function success(text) {
    var textarea = document.getElementById('test-response-text');
    textarea.value = text;
}

function fail(code) {
    var textarea = document.getElementById('test-response-text');
    textarea.value = 'Error code: ' + code;
}

var request = new XMLHttpRequest(); // 新建XMLHttpRequest对象

request.onreadystatechange = function () { // 状态发生变化时，函数被回调
    if (request.readyState === 4) { // 成功完成
        // 判断响应结果:
        if (request.status === 200) {
            // 成功，通过responseText拿到响应的文本:
            return success(request.responseText);
        } else {
            // 失败，根据响应码判断失败原因:
            return fail(request.status);
        }
    } else {
        // HTTP请求还在继续...
    }
}

// 发送请求:
request.open('GET', '/api/categories');
request.send();

alert('请求已发送，请等待响应...');
```
8. 
响应结果：


9. 对于低版本的IE，需要换一个ActiveXObject对象：

```
'use strict';
----
function success(text) {
    var textarea = document.getElementById('test-ie-response-text');
    textarea.value = text;
}

function fail(code) {
    var textarea = document.getElementById('test-ie-response-text');
    textarea.value = 'Error code: ' + code;
}

var request = new ActiveXObject('Microsoft.XMLHTTP'); // 新建Microsoft.XMLHTTP对象

request.onreadystatechange = function () { // 状态发生变化时，函数被回调
    if (request.readyState === 4) { // 成功完成
        // 判断响应结果:
        if (request.status === 200) {
            // 成功，通过responseText拿到响应的文本:
            return success(request.responseText);
        } else {
            // 失败，根据响应码判断失败原因:
            return fail(request.status);
        }
    } else {
        // HTTP请求还在继续...
    }
}

// 发送请求:
request.open('GET', '/api/categories');
request.send();

alert('请求已发送，请等待响应...');
```
10. 
IE响应结果：


11. 如果你想把标准写法和IE写法混在一起，可以这么写：

```
var request;
if (window.XMLHttpRequest) {
    request = new XMLHttpRequest();
} else {
    request = new ActiveXObject('Microsoft.XMLHTTP');
}
```
12. 通过检测window对象是否有XMLHttpRequest属性来确定浏览器是否支持标准的XMLHttpRequest。注意，不要根据浏览器的navigator.userAgent来检测浏览器是否支持某个JavaScript特性，一是因为这个字符串本身可以伪造，二是通过IE版本判断JavaScript特性将非常复杂。

13. 当创建了XMLHttpRequest对象后，要先设置onreadystatechange的回调函数。在回调函数中，通常我们只需通过readyState === 4判断请求是否完成，如果已完成，再根据status === 200判断是否是一个成功的响应。

14. XMLHttpRequest对象的open()方法有3个参数，第一个参数指定是GET还是POST，第二个参数指定URL地址，第三个参数指定是否使用异步，默认是true，所以不用写。

15. 注意，千万不要把第三个参数指定为false，否则浏览器将停止响应，直到AJAX请求完成。如果这个请求耗时10秒，那么10秒内你会发现浏览器处于“假死”状态。

16. 最后调用send()方法才真正发送请求。GET请求不需要参数，POST请求需要把body部分以字符串或者FormData对象传进去。

#### 安全限制 
1. 上面代码的URL使用的是相对路径。如果你把它改为'http://www.sina.com.cn/'，再运行，肯定报错。在Chrome的控制台里，还可以看到错误信息。

2. 这是因为浏览器的同源策略导致的。默认情况下，JavaScript在发送AJAX请求时，URL的域名必须和当前页面完全一致。

3. 完全一致的意思是，域名要相同（www.example.com和example.com不同），协议要相同（http和https不同），端口号要相同（默认是:80端口，它和:8080就不同）。有的浏览器口子松一点，允许端口不同，大多数浏览器都会严格遵守这个限制。

4. 那是不是用JavaScript无法请求外域（就是其他网站）的URL了呢？方法还是有的，大概有这么几种：

5. 一是通过Flash插件发送HTTP请求，这种方式可以绕过浏览器的安全限制，但必须安装Flash，并且跟Flash交互。不过Flash用起来麻烦，而且现在用得也越来越少了。

6. 二是通过在同源域名下架设一个代理服务器来转发，JavaScript负责把请求发送到代理服务器：

```
'/proxy?url=http://www.sina.com.cn'
```
7. 代理服务器再把结果返回，这样就遵守了浏览器的同源策略。这种方式麻烦之处在于需要服务器端额外做开发。

8. 第三种方式称为JSONP，它有个限制，只能用GET请求，并且要求返回JavaScript。这种方式跨域实际上是利用了浏览器允许跨域引用JavaScript资源：

```
<html>
<head>
    <script src="http://example.com/abc.js"></script>
    ...
</head>
<body>
...
</body>
</html>
```
9. JSONP通常以函数调用的形式返回，例如，返回JavaScript内容如下：

```
foo('data');
```
10. 这样一来，我们如果在页面中先准备好foo()函数，然后给页面动态加一个`<script>`节点，相当于动态读取外域的JavaScript资源，最后就等着接收回调了。

11. 以163的股票查询URL为例，对于URL：http://api.money.126.net/data/feed/0000001,1399001?callback=refreshPrice，你将得到如下返回：

```
refreshPrice({"0000001":{"code": "0000001", ... });
```
12. 因此我们需要首先在页面中准备好回调函数：

13. 
```
function getPrice() {
    var
        js = document.createElement('script'),
        head = document.getElementsByTagName('head')[0];
    js.src = 'http://api.money.126.net/data/feed/0000001,1399001?callback=refreshPrice';
    head.appendChild(js);
}

function refreshPrice(data) {
    var p = document.getElementById('test-jsonp');
    p.innerHTML = '当前价格：' +
        data['0000001'].name +': ' + 
        data['0000001'].price + '；' +
        data['1399001'].name + ': ' +
        data['1399001'].price;
}
```
14. 
    当前价格：
    刷新


15. 最后用getPrice()函数触发：

```
function getPrice() {
    var
        js = document.createElement('script'),
        head = document.getElementsByTagName('head')[0];
    js.src = 'http://api.money.126.net/data/feed/0000001,1399001?callback=refreshPrice';
    head.appendChild(js);
}
```
16. 就完成了跨域加载数据。

#### CORS 
1. 如果浏览器支持HTML5，那么就可以一劳永逸地使用新的跨域策略：CORS了。

2. CORS全称Cross-Origin Resource Sharing，是HTML5规范定义的如何跨域访问资源。

3. 了解CORS前，我们先搞明白概念：

4. Origin表示本域，也就是浏览器当前页面的域。当JavaScript向外域（如sina.com）发起请求后，浏览器收到响应后，首先检查Access-Control-Allow-Origin是否包含本域，如果是，则此次跨域请求成功，如果不是，则请求失败，JavaScript将无法获取到响应的任何数据。

5. 用一个图来表示就是：

6. 

7. 假设本域是my.com，外域是sina.com，只要响应头Access-Control-Allow-Origin为http://my.com，或者是*，本次请求就可以成功。

8. 可见，跨域能否成功，取决于对方服务器是否愿意给你设置一个正确的Access-Control-Allow-Origin，决定权始终在对方手中。

9. 上面这种跨域请求，称之为“简单请求”。简单请求包括GET、HEAD和POST（POST的Content-Type类型
仅限application/x-www-form-urlencoded、multipart/form-data和text/plain），并且不能出现任何自定义头（例如，X-Custom: 12345），通常能满足90%的需求。

10. 无论你是否需要用JavaScript通过CORS跨域请求资源，你都要了解CORS的原理。最新的浏览器全面支持HTML5。在引用外域资源时，除了JavaScript和CSS外，都要验证CORS。例如，当你引用了某个第三方CDN上的字体文件时：

```
/* CSS */
@font-face {
  font-family: 'FontAwesome';
  src: url('http://cdn.com/fonts/fontawesome.ttf') format('truetype');
}
```
11. 如果该CDN服务商未正确设置Access-Control-Allow-Origin，那么浏览器无法加载字体资源。

12. 对于PUT、DELETE以及其他类型如application/json的POST请求，在发送AJAX请求之前，浏览器会先发送一个OPTIONS请求（称为preflighted请求）到这个URL上，询问目标服务器是否接受：

```
OPTIONS /path/to/resource HTTP/1.1
Host: bar.com
Origin: http://my.com
Access-Control-Request-Method: POST
```
13. 服务器必须响应并明确指出允许的Method：

```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: http://my.com
Access-Control-Allow-Methods: POST, GET, PUT, OPTIONS
Access-Control-Max-Age: 86400
```
14. 浏览器确认服务器响应的Access-Control-Allow-Methods头确实包含将要发送的AJAX请求的Method，才会继续发送AJAX，否则，抛出一个错误。

15. 由于以POST、PUT方式传送JSON格式的数据在REST中很常见，所以要跨域正确处理POST和PUT请求，服务器端必须正确响应OPTIONS请求。

16. 需要深入了解CORS的童鞋请移步W3C文档。

### Promise
1. 在JavaScript的世界中，所有代码都是单线程执行的。

2. 由于这个“缺陷”，导致JavaScript的所有网络操作，浏览器事件，都必须是异步执行。异步执行可以用回调函数实现：

```
function callback() {
    console.log('Done');
}
console.log('before setTimeout()');
setTimeout(callback, 1000); // 1秒钟后调用callback函数
console.log('after setTimeout()');
```
3. 观察上述代码执行，在Chrome的控制台输出可以看到：

```
before setTimeout()
after setTimeout()
(等待1秒后)
Done
```
4. 可见，异步操作会在将来的某个时间点触发一个函数调用。

5. AJAX就是典型的异步操作。以上一节的代码为例：

```
request.onreadystatechange = function () {
    if (request.readyState === 4) {
        if (request.status === 200) {
            return success(request.responseText);
        } else {
            return fail(request.status);
        }
    }
}
```
6. 把回调函数success(request.responseText)和fail(request.status)写到一个AJAX操作里很正常，但是不好看，而且不利于代码复用。

7. 有没有更好的写法？比如写成这样：

```
var ajax = ajaxGet('http://...');
ajax.ifSuccess(success)
    .ifFail(fail);
```
8. 这种链式写法的好处在于，先统一执行AJAX逻辑，不关心如何处理结果，然后，根据结果是成功还是失败，在将来的某个时候调用success函数或fail函数。

9. 古人云：“君子一诺千金”，这种“承诺将来会执行”的对象在JavaScript中称为Promise对象。

10. Promise有各种开源实现，在ES6中被统一规范，由浏览器直接支持。先测试一下你的浏览器是否支持Promise：

```
'use strict';

new Promise(function () {});
----
// 直接运行测试:
console.log('支持Promise!');
```
11. 我们先看一个最简单的Promise例子：生成一个0-2之间的随机数，如果小于1，则等待一段时间后返回成功，否则返回失败：

```
function test(resolve, reject) {
    var timeOut = Math.random() * 2;
    log('set timeout to: ' + timeOut + ' seconds.');
    setTimeout(function () {
        if (timeOut < 1) {
            log('call resolve()...');
            resolve('200 OK');
        }
        else {
            log('call reject()...');
            reject('timeout in ' + timeOut + ' seconds.');
        }
    }, timeOut * 1000);
}
```
12. 这个test()函数有两个参数，这两个参数都是函数，如果执行成功，我们将调用resolve('200 OK')，如果执行失败，我们将调用reject('timeout in ' + timeOut + ' seconds.')。可以看出，test()函数只关心自身的逻辑，并不关心具体的resolve和reject将如何处理结果。

13. 有了执行函数，我们就可以用一个Promise对象来执行它，并在将来某个时刻获得成功或失败的结果：

```
var p1 = new Promise(test);
var p2 = p1.then(function (result) {
    console.log('成功：' + result);
});
var p3 = p2.catch(function (reason) {
    console.log('失败：' + reason);
});
```
14. 变量p1是一个Promise对象，它负责执行test函数。由于test函数在内部是异步执行的，当test函数执行成功时，我们告诉Promise对象：

```
// 如果成功，执行这个函数：
p1.then(function (result) {
    console.log('成功：' + result);
});
```
15. 当test函数执行失败时，我们告诉Promise对象：

```
p2.catch(function (reason) {
    console.log('失败：' + reason);
});
```
16. Promise对象可以串联起来，所以上述代码可以简化为：

```
new Promise(test).then(function (result) {
    console.log('成功：' + result);
}).catch(function (reason) {
    console.log('失败：' + reason);
});
```
17. 实际测试一下，看看Promise是如何异步执行的：

```
'use strict';

// 清除log:
var logging = document.getElementById('test-promise-log');
while (logging.children.length > 1) {
    logging.removeChild(logging.children[logging.children.length - 1]);
}

// 输出log到页面:
function log(s) {
    var p = document.createElement('p');
    p.innerHTML = s;
    logging.appendChild(p);
}

----
new Promise(function (resolve, reject) {
    log('start new Promise...');
    var timeOut = Math.random() * 2;
    log('set timeout to: ' + timeOut + ' seconds.');
    setTimeout(function () {
        if (timeOut < 1) {
            log('call resolve()...');
            resolve('200 OK');
        }
        else {
            log('call reject()...');
            reject('timeout in ' + timeOut + ' seconds.');
        }
    }, timeOut * 1000);
}).then(function (r) {
    log('Done: ' + r);
}).catch(function (reason) {
    log('Failed: ' + reason);
});
```

19. 可见Promise最大的好处是在异步执行的流程中，把执行代码和处理结果的代码清晰地分离了：

21. Promise还可以做更多的事情，比如，有若干个异步任务，需要先做任务1，如果成功后再做任务2，任何任务失败则不再继续并执行错误处理函数。

22. 要串行执行这样的异步任务，不用Promise需要写一层一层的嵌套代码。有了Promise，我们只需要简单地写：

```
job1.then(job2).then(job3).catch(handleError);
```
23. 其中，job1、job2和job3都是Promise对象。

24. 下面的例子演示了如何串行执行一系列需要异步计算获得结果的任务：

```
'use strict';

var logging = document.getElementById('test-promise2-log');
while (logging.children.length > 1) {
    logging.removeChild(logging.children[logging.children.length - 1]);
}

function log(s) {
    var p = document.createElement('p');
    p.innerHTML = s;
    logging.appendChild(p);
}

----
// 0.5秒后返回input*input的计算结果:
function multiply(input) {
    return new Promise(function (resolve, reject) {
        log('calculating ' + input + ' x ' + input + '...');
        setTimeout(resolve, 500, input * input);
    });
}

// 0.5秒后返回input+input的计算结果:
function add(input) {
    return new Promise(function (resolve, reject) {
        log('calculating ' + input + ' + ' + input + '...');
        setTimeout(resolve, 500, input + input);
    });
}

var p = new Promise(function (resolve, reject) {
    log('start new Promise...');
    resolve(123);
});

p.then(multiply)
 .then(add)
 .then(multiply)
 .then(add)
 .then(function (result) {
    log('Got value: ' + result);
});
```
25. 
    Log:


26. setTimeout可以看成一个模拟网络等异步执行的函数。现在，我们把上一节的AJAX异步执行函数转换为Promise对象，看看用Promise如何简化异步处理：

```
'use strict';

// ajax函数将返回Promise对象:
function ajax(method, url, data) {
    var request = new XMLHttpRequest();
    return new Promise(function (resolve, reject) {
        request.onreadystatechange = function () {
            if (request.readyState === 4) {
                if (request.status === 200) {
                    resolve(request.responseText);
                } else {
                    reject(request.status);
                }
            }
        };
        request.open(method, url);
        request.send(data);
    });
}
----
var log = document.getElementById('test-promise-ajax-result');
var p = ajax('GET', '/api/categories');
p.then(function (text) { // 如果AJAX成功，获得响应内容
    log.innerText = text;
}).catch(function (status) { // 如果AJAX失败，获得响应代码
    log.innerText = 'ERROR: ' + status;
});
```
27. 
    Result:


28. 除了串行执行若干异步任务外，Promise还可以并行执行异步任务。

29. 试想一个页面聊天系统，我们需要从两个不同的URL分别获得用户的个人信息和好友列表，这两个任务是可以并行执行的，用Promise.all()实现如下：

```
var p1 = new Promise(function (resolve, reject) {
    setTimeout(resolve, 500, 'P1');
});
var p2 = new Promise(function (resolve, reject) {
    setTimeout(resolve, 600, 'P2');
});
// 同时执行p1和p2，并在它们都完成后执行then:
Promise.all([p1, p2]).then(function (results) {
    console.log(results); // 获得一个Array: ['P1', 'P2']
});
```
30. 有些时候，多个异步任务是为了容错。比如，同时向两个URL读取用户的个人信息，只需要获得先返回的结果即可。这种情况下，用Promise.race()实现：

```
var p1 = new Promise(function (resolve, reject) {
    setTimeout(resolve, 500, 'P1');
});
var p2 = new Promise(function (resolve, reject) {
    setTimeout(resolve, 600, 'P2');
});
Promise.race([p1, p2]).then(function (result) {
    console.log(result); // 'P1'
});
```
31. 由于p1执行较快，Promise的then()将获得结果'P1'。p2仍在继续执行，但执行结果将被丢弃。

32. 如果我们组合使用Promise，就可以把很多异步任务以并行和串行的方式组合起来执行。

### Canvas
1. Canvas是HTML5新增的组件，它就像一块幕布，可以用JavaScript在上面绘制各种图表、动画等。

2. 没有Canvas的年代，绘图只能借助Flash插件实现，页面不得不用JavaScript和Flash进行交互。有了Canvas，我们就再也不需要Flash了，直接使用JavaScript完成绘制。

3. 一个Canvas定义了一个指定尺寸的矩形框，在这个范围内我们可以随意绘制：

```
<canvas id="test-canvas" width="300" height="200"></canvas>
```
4. 由于浏览器对HTML5标准支持不一致，所以，通常在<canvas>内部添加一些说明性HTML代码，如果浏览器支持Canvas，它将忽略<canvas>内部的HTML，如果浏览器不支持Canvas，它将显示<canvas>内部的HTML：

```
<canvas id="test-stock" width="300" height="200">
    <p>Current Price: 25.51</p>
</canvas>
```
5. 在使用Canvas前，用canvas.getContext来测试浏览器是否支持Canvas：

```
<!-- HTML代码 -->
<canvas id="test-canvas" width="200" heigth="100">
    <p>你的浏览器不支持Canvas</p>
</canvas>
```
6. 
    你的浏览器不支持Canvas


```
'use strict';
----
var canvas = document.getElementById('test-canvas');
if (canvas.getContext) {
    console.log('你的浏览器支持Canvas!');
} else {
    console.log('你的浏览器不支持Canvas!');
}
```
7. getContext('2d')方法让我们拿到一个CanvasRenderingContext2D对象，所有的绘图操作都需要通过这个对象完成。

```
var ctx = canvas.getContext('2d');
```
8. 如果需要绘制3D怎么办？HTML5还有一个WebGL规范，允许在Canvas中绘制3D图形：

```
gl = canvas.getContext("webgl");
```
9. 本节我们只专注于绘制2D图形。

#### 绘制形状 
1. 我们可以在Canvas上绘制各种形状。在绘制前，我们需要先了解一下Canvas的坐标系统：

2. 

3. Canvas的坐标以左上角为原点，水平向右为X轴，垂直向下为Y轴，以像素为单位，所以每个点都是非负整数。

4. CanvasRenderingContext2D对象有若干方法来绘制图形：

```
'use strict';

var
    canvas = document.getElementById('test-shape-canvas'),
    ctx = canvas.getContext('2d');
----
ctx.clearRect(0, 0, 200, 200); // 擦除(0,0)位置大小为200x200的矩形，擦除的意思是把该区域变为透明
ctx.fillStyle = '#dddddd'; // 设置颜色
ctx.fillRect(10, 10, 130, 130); // 把(10,10)位置大小为130x130的矩形涂色
// 利用Path绘制复杂路径:
var path=new Path2D();
path.arc(75, 75, 50, 0, Math.PI*2, true);
path.moveTo(110,75);
path.arc(75, 75, 35, 0, Math.PI, false);
path.moveTo(65, 65);
path.arc(60, 65, 5, 0, Math.PI*2, true);
path.moveTo(95, 65);
path.arc(90, 65, 5, 0, Math.PI*2, true);
ctx.strokeStyle = '#0000ff';
ctx.stroke(path);
```
5. 


#### 绘制文本 
1. 绘制文本就是在指定的位置输出文本，可以设置文本的字体、样式、阴影等，与CSS完全一致：

```
'use strict';

var
    canvas = document.getElementById('test-text-canvas'),
    ctx = canvas.getContext('2d');
----
ctx.clearRect(0, 0, canvas.width, canvas.height);
ctx.shadowOffsetX = 2;
ctx.shadowOffsetY = 2;
ctx.shadowBlur = 2;
ctx.shadowColor = '#666666';
ctx.font = '24px Arial';
ctx.fillStyle = '#333333';
ctx.fillText('带阴影的文字', 20, 40);
```
2. 


3. Canvas除了能绘制基本的形状和文本，还可以实现动画、缩放、各种滤镜和像素转换等高级操作。如果要实现非常复杂的操作，考虑以下优化方案：

4. 

通过创建一个不可见的Canvas来绘图，然后将最终绘制结果复制到页面的可见Canvas中；


尽量使用整数坐标而不是浮点数；


可以创建多个重叠的Canvas绘制不同的层，而不是在一个Canvas中绘制非常复杂的图；


背景图片如果不变可以直接用<img>标签并放到最底层。



#### 练习 
1. 请根据从163获取的JSON数据绘制最近30个交易日的K线图，数据已处理为包含一组对象的数组：

2. 
function downloadStockImage() {
    var
        canvas = document.getElementById('stock-canvas'),
        data = canvas.toDataURL();
    window.open(data.replace('image/png', 'image/octet-stream'));
}


```
```
```
'use strict';

window.loadStockData = function (r) {
    var
        NUMS = 30,
        data = r.data;
    if (data.length > NUMS) {
        data = data.slice(data.length - NUMS);
    }
    data = data.map(function (x) {
        return {
            date: x[0],
            open: x[1],
            close: x[2],
            high: x[3],
            low: x[4],
            vol: x[5],
            change: x[6]
        };
    });
    window.drawStock(data);
}

window.drawStock = function (data) {
----
    var
        canvas = document.getElementById('stock-canvas'),
        width = canvas.width,
        height = canvas.height,
        ctx = canvas.getContext('2d');
    console.log(JSON.stringify(data[0])); // {"date":"20150602","open":4844.7,"close":4910.53,"high":4911.57,"low":4797.55,"vol":62374809900,"change":1.69}
    ctx.clearRect(0, 0, width, height);
    ctx.fillText('Test Canvas', 10, 10);
----
};

// 加载最近30个交易日的K线图数据:
var js = document.createElement('script');
js.src = 'http://img1.money.126.net/data/hs/kline/day/history/2015/0000001.json?callback=loadStockData&t=' + Date.now();
document.getElementsByTagName('head')[0].appendChild(js);
```

## jQuery
1. 你可能听说过jQuery，它名字起得很土，但却是JavaScript世界中使用最广泛的一个库。

2. 江湖传言，全世界大约有80~90%的网站直接或间接地使用了jQuery。鉴于它如此流行，又如此好用，所以每一个入门JavaScript的前端工程师都应该了解和学习它。

3. jQuery这么流行，肯定是因为它解决了一些很重要的问题。实际上，jQuery能帮我们干这些事情：

4. 

消除浏览器差异：你不需要自己写冗长的代码来针对不同的浏览器来绑定事件，编写AJAX等代码；


简洁的操作DOM的方法：写$('#test')肯定比document.getElementById('test')来得简洁；


轻松实现动画、修改CSS等各种操作。



5. jQuery的理念“Write Less, Do More“，让你写更少的代码，完成更多的工作！

#### jQuery版本 
1. 目前jQuery有1.x和2.x两个主要版本，区别在于2.x移除了对古老的IE 6、7、8的支持，因此2.x的代码更精简。选择哪个版本主要取决于你是否想支持IE 6~8。

2. 从jQuery官网可以下载最新版本。jQuery只是一个jquery-xxx.js文件，但你会看到有compressed（已压缩）和uncompressed（未压缩）两种版本，使用时完全一样，但如果你想深入研究jQuery源码，那就用uncompressed版本。

#### 使用jQuery 
1. 使用jQuery只需要在页面的<head>引入jQuery文件即可：

```
<html>
<head>
    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
	...
</head>
<body>
    ...
</body>
</html>
```
2. 好消息是，当你在学习这个教程时，由于网站本身已经引用了jQuery，所以你可以直接使用：

```
'use strict';
----
console.log('jQuery版本：' + $.fn.jquery);
```
#### $符号 
1. $是著名的jQuery符号。实际上，jQuery把所有功能全部封装在一个全局变量jQuery中，而$也是一个合法的变量名，它是变量jQuery的别名：

```
window.jQuery; // jQuery(selector, context)
window.$; // jQuery(selector, context)
$ === jQuery; // true
typeof($); // 'function'
```
2. $本质上就是一个函数，但是函数也是对象，于是$除了可以直接调用外，也可以有很多其他属性。

3. 注意，你看到的$函数名可能不是jQuery(selector, context)，因为很多JavaScript压缩工具可以对函数名和参数改名，所以压缩过的jQuery源码$函数可能变成a(b, c)。

4. 绝大多数时候，我们都直接用$（因为写起来更简单嘛）。但是，如果$这个变量不幸地被占用了，而且还不能改，那我们就只能让jQuery把$变量交出来，然后就只能使用jQuery这个变量：

```
$; // jQuery(selector, context)
jQuery.noConflict();
$; // undefined
jQuery; // jQuery(selector, context)
```
5. 这种黑魔法的原理是jQuery在占用$之前，先在内部保存了原来的$,调用jQuery.noConflict()时会把原来保存的变量还原。

### 选择器
1. 选择器是jQuery的核心。一个选择器写出来类似$('#dom-id')。

2. 为什么jQuery要发明选择器？回顾一下DOM操作中我们经常使用的代码：

```
// 按ID查找：
var a = document.getElementById('dom-id');

// 按tag查找：
var divs = document.getElementsByTagName('div');

// 查找<p class="red">：
var ps = document.getElementsByTagName('p');
// 过滤出class="red":
// TODO:

// 查找<table class="green">里面的所有<tr>：
var table = ...
for (var i=0; i<table.children; i++) {
    // TODO: 过滤出<tr>
}
```
3. 这些代码实在太繁琐了，并且，在层级关系中，例如，查找<table class="green">里面的所有<tr>，一层循环实际上是错的，因为<table>的标准写法是：

```
<table>
    <tbody>
        <tr>...</tr>
        <tr>...</tr>
    </tbody>
</table>
```
4. 很多时候，需要递归查找所有子节点。

5. jQuery的选择器就是帮助我们快速定位到一个或多个DOM节点。

#### 按ID查找 
1. 如果某个DOM节点有id属性，利用jQuery查找如下：

```
// 查找<div id="abc">:
var div = $('#abc');
```
2. 注意，#abc以#开头。返回的对象是jQuery对象。

3. 什么是jQuery对象？jQuery对象类似数组，它的每个元素都是一个引用了DOM节点的对象。

4. 以上面的查找为例，如果id为abc的<div>存在，返回的jQuery对象如下：

```
[<div id="abc">...</div>]
```
5. 如果id为abc的<div>不存在，返回的jQuery对象如下：

```
[]
```
6. 总之jQuery的选择器不会返回undefined或者null，这样的好处是你不必在下一行判断if (div === undefined)。

7. jQuery对象和DOM对象之间可以互相转化：

```
var div = $('#abc'); // jQuery对象
var divDom = div.get(0); // 假设存在div，获取第1个DOM元素
var another = $(divDom); // 重新把DOM包装为jQuery对象
```
8. 通常情况下你不需要获取DOM对象，直接使用jQuery对象更加方便。如果你拿到了一个DOM对象，那可以简单地调用$(aDomObject)把它变成jQuery对象，这样就可以方便地使用jQuery的API了。

#### 按tag查找 
1. 按tag查找只需要写上tag名称就可以了：

```
var ps = $('p'); // 返回所有<p>节点
ps.length; // 数一数页面有多少个<p>节点
```
#### 按class查找 
1. 按class查找注意在class名称前加一个.：

```
var a = $('.red'); // 所有节点包含`class="red"`都将返回
// 例如:
// <div class="red">...</div>
// <p class="green red">...</p>
```
2. 通常很多节点有多个class，我们可以查找同时包含red和green的节点：

```
var a = $('.red.green'); // 注意没有空格！
// 符合条件的节点：
// <div class="red green">...</div>
// <div class="blue green red">...</div>
```
#### 按属性查找 
1. 一个DOM节点除了id和class外还可以有很多属性，很多时候按属性查找会非常方便，比如在一个表单中按属性来查找：

```
var email = $('[name=email]'); // 找出<??? name="email">
var passwordInput = $('[type=password]'); // 找出<??? type="password">
var a = $('[items="A B"]'); // 找出<??? items="A B">
```
2. 当属性的值包含空格等特殊字符时，需要用双引号括起来。

3. 按属性查找还可以使用前缀查找或者后缀查找：

```
var icons = $('[name^=icon]'); // 找出所有name属性值以icon开头的DOM
// 例如: name="icon-1", name="icon-2"
var names = $('[name$=with]'); // 找出所有name属性值以with结尾的DOM
// 例如: name="startswith", name="endswith"
```
4. 这个方法尤其适合通过class属性查找，且不受class包含多个名称的影响：

```
var icons = $('[class^="icon-"]'); // 找出所有class包含至少一个以`icon-`开头的DOM
// 例如: class="icon-clock", class="abc icon-home"
```
#### 组合查找 
1. 组合查找就是把上述简单选择器组合起来使用。如果我们查找$('[name=email]')，很可能把表单外的<div name="email">也找出来，但我们只希望查找<input>，就可以这么写：

```
var emailInput = $('input[name=email]'); // 不会找出<div name="email">
```
2. 同样的，根据tag和class来组合查找也很常见：

```
var tr = $('tr.red'); // 找出<tr class="red ...">...</tr>
```
#### 多项选择器 
1. 多项选择器就是把多个选择器用,组合起来一块选：

```
$('p,div'); // 把<p>和<div>都选出来
$('p.red,p.green'); // 把<p class="red">和<p class="green">都选出来
```
2. 要注意的是，选出来的元素是按照它们在HTML中出现的顺序排列的，而且不会有重复元素。例如，<p class="red green">不会被上面的$('p.red,p.green')选择两次。

### 操作DOM
1. jQuery的选择器很强大，用起来又简单又灵活，但是搞了这么久，我拿到了jQuery对象，到底要干什么？

2. 答案当然是操作对应的DOM节点啦！

3. 回顾一下修改DOM的CSS、文本、设置HTML有多么麻烦，而且有的浏览器只有innerHTML，有的浏览器支持innerText，有了jQuery对象，不需要考虑浏览器差异了，全部统一操作！

#### 修改Text和HTML 
1. jQuery对象的text()和html()方法分别获取节点的文本和原始HTML文本，例如，如下的HTML结构：

```
<!-- HTML结构 -->
<ul id="test-ul">
    <li class="js">JavaScript</li>
    <li name="book">Java &amp; JavaScript</li>
</ul>
```
2. 分别获取文本和HTML：

```
$('#test-ul li[name=book]').text(); // 'Java & JavaScript'
$('#test-ul li[name=book]').html(); // 'Java &amp; JavaScript'
```
3. 如何设置文本或HTML？jQuery的API设计非常巧妙：无参数调用text()是获取文本，传入参数就变成设置文本，HTML也是类似操作，自己动手试试：

```
'use strict';
var j1 = $('#test-ul li.js');
var j2 = $('#test-ul li[name=book]');
----
j1.html('<span style="color: red">JavaScript</span>');
j2.text('JavaScript & ECMAScript');
```
4. 
    JavaScript
    Java & JavaScript


5. 一个jQuery对象可以包含0个或任意个DOM对象，它的方法实际上会作用在对应的每个DOM节点上。在上面的例子中试试：

```
$('#test-ul li').text('JS'); // 是不是两个节点都变成了JS？
```
6. 所以jQuery对象的另一个好处是我们可以执行一个操作，作用在对应的一组DOM节点上。即使选择器没有返回任何DOM节点，调用jQuery对象的方法仍然不会报错：

```
// 如果不存在id为not-exist的节点：
$('#not-exist').text('Hello'); // 代码不报错，没有节点被设置为'Hello'
```
7. 这意味着jQuery帮你免去了许多if语句。

#### 修改CSS 
1. jQuery对象有“批量操作”的特点，这用于修改CSS实在是太方便了。考虑下面的HTML结构：

```
<!-- HTML结构 -->
<ul id="test-css">
    <li class="lang dy"><span>JavaScript</span></li>
    <li class="lang"><span>Java</span></li>
    <li class="lang dy"><span>Python</span></li>
    <li class="lang"><span>Swift</span></li>
    <li class="lang dy"><span>Scheme</span></li>
</ul>
```
2. 要高亮显示动态语言，调用jQuery对象的css('name', 'value')方法，我们用一行语句实现：

```
'use strict';
----
$('#test-css li.dy>span').css('background-color', '#ffd351').css('color', 'red');
```
3. 
    JavaScript
    Java
    Python
    Swift
    Scheme


4. 注意，jQuery对象的所有方法都返回一个jQuery对象（可能是新的也可能是自身），这样我们可以进行链式调用，非常方便。

5. jQuery对象的css()方法可以这么用：

```
var div = $('#test-div');
div.css('color'); // '#000033', 获取CSS属性
div.css('color', '#336699'); // 设置CSS属性
div.css('color', ''); // 清除CSS属性
```
6. 为了和JavaScript保持一致，CSS属性可以用'background-color'和'backgroundColor'两种格式。

7. css()方法将作用于DOM节点的style属性，具有最高优先级。如果要修改class属性，可以用jQuery提供的下列方法：

```
var div = $('#test-div');
div.hasClass('highlight'); // false， class是否包含highlight
div.addClass('highlight'); // 添加highlight这个class
div.removeClass('highlight'); // 删除highlight这个class
```
8. 练习：分别用css()方法和addClass()方法高亮显示JavaScript：

```
<!-- HTML结构 -->
<style>
.highlight {
    color: #dd1144;
    background-color: #ffd351;
}
</style>

<div id="test-highlight-css">
    <ul>
        <li class="py"><span>Python</span></li>
        <li class="js"><span>JavaScript</span></li>
        <li class="sw"><span>Swift</span></li>
        <li class="hk"><span>Haskell</span></li>
    </ul>
</div>
```
```
'use strict';
----
var div = $('#test-highlight-css');
// TODO:
```
9. 
.highlight {
    color: #dd1144;
    background-color: #ffd351;
}


10. 
    
        Python
        JavaScript
        Swift
        Haskell
    


#### 显示和隐藏DOM 
1. 要隐藏一个DOM，我们可以设置CSS的display属性为none，利用css()方法就可以实现。不过，要显示这个DOM就需要恢复原有的display属性，这就得先记下来原有的display属性到底是block还是inline还是别的值。

2. 考虑到显示和隐藏DOM元素使用非常普遍，jQuery直接提供show()和hide()方法，我们不用关心它是如何修改display属性的，总之它能正常工作：

```
var a = $('a[target=_blank]');
a.hide(); // 隐藏
a.show(); // 显示
```
3. 注意，隐藏DOM节点并未改变DOM树的结构，它只影响DOM节点的显示。这和删除DOM节点是不同的。

#### 获取DOM信息 
1. 利用jQuery对象的若干方法，我们直接可以获取DOM的高宽等信息，而无需针对不同浏览器编写特定代码：

```
// 浏览器可视窗口大小:
$(window).width(); // 800
$(window).height(); // 600

// HTML文档大小:
$(document).width(); // 800
$(document).height(); // 3500

// 某个div的大小:
var div = $('#test-div');
div.width(); // 600
div.height(); // 300
div.width(400); // 设置CSS属性 width: 400px，是否生效要看CSS是否有效
div.height('200px'); // 设置CSS属性 height: 200px，是否生效要看CSS是否有效
```
2. attr()和removeAttr()方法用于操作DOM节点的属性：

```
// <div id="test-div" name="Test" start="1">...</div>
var div = $('#test-div');
div.attr('data'); // undefined, 属性不存在
div.attr('name'); // 'Test'
div.attr('name', 'Hello'); // div的name属性变为'Hello'
div.removeAttr('name'); // 删除name属性
div.attr('name'); // undefined
```
3. prop()方法和attr()类似，但是HTML5规定有一种属性在DOM节点中可以没有值，只有出现与不出现两种，例如：

```
<input id="test-radio" type="radio" name="test" checked value="1">
```
4. 等价于：

```
<input id="test-radio" type="radio" name="test" checked="checked" value="1">
```
5. attr()和prop()对于属性checked处理有所不同：

```
var radio = $('#test-radio');
radio.attr('checked'); // 'checked'
radio.prop('checked'); // true
```
6. prop()返回值更合理一些。不过，用is()方法判断更好：

```
var radio = $('#test-radio');
radio.is(':checked'); // true
```
7. 类似的属性还有selected，处理时最好用is(':selected')。

#### 操作表单 
1. 对于表单元素，jQuery对象统一提供val()方法获取和设置对应的value属性：

```
/*
    <input id="test-input" name="email" value="">
    <select id="test-select" name="city">
        <option value="BJ" selected>Beijing</option>
        <option value="SH">Shanghai</option>
        <option value="SZ">Shenzhen</option>
    </select>
    <textarea id="test-textarea">Hello</textarea>
*/
var
    input = $('#test-input'),
    select = $('#test-select'),
    textarea = $('#test-textarea');

input.val(); // 'test'
input.val('abc@example.com'); // 文本框的内容已变为abc@example.com

select.val(); // 'BJ'
select.val('SH'); // 选择框已变为Shanghai

textarea.val(); // 'Hello'
textarea.val('Hi'); // 文本区域已更新为'Hi'
```
2. 可见，一个val()就统一了各种输入框的取值和赋值的问题。

### 事件
1. 因为JavaScript在浏览器中以单线程模式运行，页面加载后，一旦页面上所有的JavaScript代码被执行完后，就只能依赖触发事件来执行JavaScript代码。

2. 浏览器在接收到用户的鼠标或键盘输入后，会自动在对应的DOM节点上触发相应的事件。如果该节点已经绑定了对应的JavaScript处理函数，该函数就会自动调用。

3. 由于不同的浏览器绑定事件的代码都不太一样，所以用jQuery来写代码，就屏蔽了不同浏览器的差异，我们总是编写相同的代码。

4. 举个例子，假设要在用户点击了超链接时弹出提示框，我们用jQuery这样绑定一个click事件：

5. 
$(function () {
    $('#test-link').click(function () {
        alert('Hello!');
    });
});


```
/* HTML:
 *
 * <a id="test-link" href="#0">点我试试</a>
 *
 */

// 获取超链接的jQuery对象:
var a = $('#test-link');
a.on('click', function () {
    alert('Hello!');
});
```
6. 实测：点我试试

7. on方法用来绑定一个事件，我们需要传入事件名称和对应的处理函数。

8. 另一种更简化的写法是直接调用click()方法：

```
a.click(function () {
    alert('Hello!');
});
```
9. 两者完全等价。我们通常用后面的写法。

10. jQuery能够绑定的事件主要包括：

#### 鼠标事件 
1. 
click: 鼠标单击时触发；
dblclick：鼠标双击时触发；
mouseenter：鼠标进入时触发；
mouseleave：鼠标移出时触发；
mousemove：鼠标在DOM内部移动时触发；
hover：鼠标进入和退出时触发两个函数，相当于mouseenter加上mouseleave。


#### 键盘事件 
1. 键盘事件仅作用在当前焦点的DOM上，通常是<input>和<textarea>。

2. 
keydown：键盘按下时触发；
keyup：键盘松开时触发；
keypress：按一次键后触发。


#### 其他事件 
1. 
focus：当DOM获得焦点时触发；
blur：当DOM失去焦点时触发；
change：当<input>、<select>或<textarea>的内容改变时触发；
submit：当<form>提交时触发；
ready：当页面被载入并且DOM树完成初始化后触发。


2. 其中，ready仅作用于document对象。由于ready事件在DOM完成初始化后触发，且只触发一次，所以非常适合用来写其他的初始化代码。假设我们想给一个<form>表单绑定submit事件，下面的代码没有预期的效果：

```
<html>
<head>
    <script>
        // 代码有误:
        $('#testForm).on('submit', function () {
            alert('submit!');
        });
    </script>
</head>
<body>
    <form id="testForm">
        ...
    </form>
</body>
```
3. 因为JavaScript在此执行的时候，<form>尚未载入浏览器，所以$('#testForm)返回[]，并没有绑定事件到任何DOM上。

4. 所以我们自己的初始化代码必须放到document对象的ready事件中，保证DOM已完成初始化：

```
<html>
<head>
    <script>
        $(document).on('ready', function () {
            $('#testForm).on('submit', function () {
                alert('submit!');
            });
        });
    </script>
</head>
<body>
    <form id="testForm">
        ...
    </form>
</body>
```
5. 这样写就没有问题了。因为相关代码会在DOM树初始化后再执行。

6. 由于ready事件使用非常普遍，所以可以这样简化：

```
$(document).ready(function () {
    // on('submit', function)也可以简化:
    $('#testForm).submit(function () {
        alert('submit!');
    });
});
```
7. 甚至还可以再简化为：

```
$(function () {
    // init...
});
```
8. 上面的这种写法最为常见。如果你遇到$(function () {...})的形式，牢记这是document对象的ready事件处理函数。

9. 完全可以反复绑定事件处理函数，它们会依次执行：

```
$(function () {
    console.log('init A...');
});
$(function () {
    console.log('init B...');
});
$(function () {
    console.log('init C...');
});
```
#### 事件参数 
1. 有些事件，如mousemove和keypress，我们需要获取鼠标位置和按键的值，否则监听这些事件就没什么意义了。所有事件都会传入Event对象作为参数，可以从Event对象上获取到更多的信息：

```
$(function () {
    $('#testMouseMoveDiv').mousemove(function (e) {
        $('#testMouseMoveSpan').text('pageX = ' + e.pageX + ', pageY = ' + e.pageY);
    });
});
```
2. 
$(function () {
    $('#testMouseMoveDiv').mousemove(function (e) {
        $('#testMouseMoveSpan').text('pageX = ' + e.pageX + ', pageY = ' + e.pageY);
    });
});


3. 效果实测：

4. mousemove: 

5. 在此区域移动鼠标试试

#### 取消绑定 
1. 一个已被绑定的事件可以解除绑定，通过off('click', function)实现：

```
function hello() {
    alert('hello!');
}

a.click(hello); // 绑定事件

// 10秒钟后解除绑定:
setTimeout(function () {
    a.off('click', hello);
}, 10000);
```
2. 需要特别注意的是，下面这种写法是无效的：

```
// 绑定事件:
a.click(function () {
    alert('hello!');
});

// 解除绑定:
a.off('click', function () {
    alert('hello!');
});
```
3. 这是因为两个匿名函数虽然长得一模一样，但是它们是两个不同的函数对象，off('click', function () {...})无法移除已绑定的第一个匿名函数。

4. 为了实现移除效果，可以使用off('click')一次性移除已绑定的click事件的所有处理函数。

5. 同理，无参数调用off()一次性移除已绑定的所有类型的事件处理函数。

#### 事件触发条件 
1. 一个需要注意的问题是，事件的触发总是由用户操作引发的。例如，我们监控文本框的内容改动：

```
var input = $('#test-input');
input.change(function () {
    console.log('changed...');
});
```
2. 当用户在文本框中输入时，就会触发change事件。但是，如果用JavaScript代码去改动文本框的值，将不会触发change事件：

```
var input = $('#test-input');
input.val('change it!'); // 无法触发change事件
```
3. 有些时候，我们希望用代码触发change事件，可以直接调用无参数的change()方法来触发该事件：

```
var input = $('#test-input');
input.val('change it!');
input.change(); // 触发change事件
```
4. input.change()相当于input.trigger('change')，它是trigger()方法的简写。

5. 为什么我们希望手动触发一个事件呢？如果不这么做，很多时候，我们就得写两份一模一样的代码。

#### 浏览器安全限制 
1. 在浏览器中，有些JavaScript代码只有在用户触发下才能执行，例如，window.open()函数：

```
// 无法弹出新窗口，将被浏览器屏蔽:
$(function () {
    window.open('/');
});
```
2. 这些“敏感代码”只能由用户操作来触发：

```
var button1 = $('#testPopupButton1');
var button2 = $('#testPopupButton2');

function popupTestWindow() {
    window.open('/');
}

button1.click(function () {
    popupTestWindow();
});

button2.click(function () {
    // 不立刻执行popupTestWindow()，3秒后执行:
    setTimeout(popupTestWindow, 3000);
});
```
3. 当用户点击button1时，click事件被触发，由于popupTestWindow()在click事件处理函数内执行，这是浏览器允许的，而button2的click事件并未立刻执行popupTestWindow()，延迟执行的popupTestWindow()将被浏览器拦截。

4. 
$(function () {
    var button1 = $('#testPopupButton1');
    var button2 = $('#testPopupButton2');

    function popupTestWindow() {
        window.open('?t=' + new Date().getTime(), 'popupWindow', 'width=400&height=300');
    }

    button1.click(function () {
        popupTestWindow();
    });

    button2.click(function () {
        setTimeout(popupTestWindow, 3000);
    });
});


5. 效果实测：

6. Button 1   Button 2

#### 练习 
1. 对如下的Form表单：

```
<!-- HTML结构 -->
<form id="test-form" action="test">
    <legend>请选择想要学习的编程语言：</legend>
    <fieldset>
        <p><label class="selectAll"><input type="checkbox"> <span class="selectAll">全选</span><span class="deselectAll">全不选</span></label> <a href="#0" class="invertSelect">反选</a></p>
        <p><label><input type="checkbox" name="lang" value="javascript"> JavaScript</label></p>
        <p><label><input type="checkbox" name="lang" value="python"> Python</label></p>
        <p><label><input type="checkbox" name="lang" value="ruby"> Ruby</label></p>
        <p><label><input type="checkbox" name="lang" value="haskell"> Haskell</label></p>
        <p><label><input type="checkbox" name="lang" value="scheme"> Scheme</label></p>
		<p><button type="submit">Submit</button></p>
    </fieldset>
</form>
```
2. 绑定合适的事件处理函数，实现以下逻辑：

3. 当用户勾上“全选”时，自动选中所有语言，并把“全选”变成“全不选”；

4. 当用户去掉“全不选”时，自动不选中所有语言；

5. 当用户点击“反选”时，自动把所有语言状态反转（选中的变为未选，未选的变为选中）；

6. 当用户把所有语言都手动勾上时，“全选”被自动勾上，并变为“全不选”；

7. 当用户手动去掉选中至少一种语言时，“全不选”自动被去掉选中，并变为“全选”。

```
'use strict';

var
    form = $('#test-form'),
    langs = form.find('[name=lang]'),
    selectAll = form.find('label.selectAll :checkbox'),
    selectAllLabel = form.find('label.selectAll span.selectAll'),
    deselectAllLabel = form.find('label.selectAll span.deselectAll'),
    invertSelect = form.find('a.invertSelect');

// 重置初始化状态:
form.find('*').show().off();
form.find(':checkbox').prop('checked', false).off();
deselectAllLabel.hide();
// 拦截form提交事件:
form.off().submit(function (e) {
    e.preventDefault();
    alert(form.serialize());
});
----
// TODO:绑定事件
----
// 测试:
console.log('请测试功能是否正常。');
```
8. 
    请选择想要学习的编程语言：
    
         全选全不选 反选
         JavaScript
         Python
         Ruby
         Haskell
         Scheme
		Submit
    


### 动画
1. 用JavaScript实现动画，原理非常简单：我们只需要以固定的时间间隔（例如，0.1秒），每次把DOM元素的CSS样式修改一点（例如，高宽各增加10%），看起来就像动画了。

2. 但是要用JavaScript手动实现动画效果，需要编写非常复杂的代码。如果想要把动画效果用函数封装起来便于复用，那考虑的事情就更多了。

3. 使用jQuery实现动画，代码已经简单得不能再简化了：只需要一行代码！

4. 让我们先来看看jQuery内置的几种动画样式：

#### show / hide 
1. 直接以无参数形式调用show()和hide()，会显示和隐藏DOM元素。但是，只要传递一个时间参数进去，就变成了动画：

```
var div = $('#test-show-hide');
div.hide(3000); // 在3秒钟内逐渐消失
```
2. 时间以毫秒为单位，但也可以是'slow'，'fast'这些字符串：

```
var div = $('#test-show-hide');
div.show('slow'); // 在0.6秒钟内逐渐显示
```
3. toggle()方法则根据当前状态决定是show()还是hide()。

4. 效果实测：

5. 
    
        hide('slow')
        show('slow')
        toggle('slow')
    
    
        
    


#### slideUp / slideDown 
1. 你可能已经看出来了，show()和hide()是从左上角逐渐展开或收缩的，而slideUp()和slideDown()则是在垂直方向逐渐展开或收缩的。

2. slideUp()把一个可见的DOM元素收起来，效果跟拉上窗帘似的，slideDown()相反，而slideToggle()则根据元素是否可见来决定下一步动作：

```
var div = $('#test-slide');
div.slideUp(3000); // 在3秒钟内逐渐向上消失
```
3. 效果实测：

4. 
    
        slideUp('slow')
        slideDown('slow')
        slideToggle('slow')
    
    
        
    


#### fadeIn / fadeOut 
1. fadeIn()和fadeOut()的动画效果是淡入淡出，也就是通过不断设置DOM元素的opacity属性来实现，而fadeToggle()则根据元素是否可见来决定下一步动作：

```
var div = $('#test-fade');
div.fadeOut('slow'); // 在0.6秒内淡出
```
2. 
    
        fadeOut('slow')
        fadeIn('slow')
        fadeToggle('slow')
    
    
        
    


#### 自定义动画 
1. 如果上述动画效果还不能满足你的要求，那就祭出最后大招：animate()，它可以实现任意动画效果，我们需要传入的参数就是DOM元素最终的CSS状态和时间，jQuery在时间段内不断调整CSS直到达到我们设定的值：

```
var div = $('#test-animate');
div.animate({
    opacity: 0.25,
    width: '256px',
    height: '256px'
}, 3000); // 在3秒钟内CSS过渡到设定值
```
2. animate()还可以再传入一个函数，当动画结束时，该函数将被调用：

```
var div = $('#test-animate');
div.animate({
    opacity: 0.25,
    width: '256px',
    height: '256px'
}, 3000, function () {
    console.log('动画已结束');
    // 恢复至初始状态:
    $(this).css('opacity', '1.0').css('width', '128px').css('height', '128px');
});
```
3. 实际上这个回调函数参数对于基本动画也是适用的。

4. 有了animate()，你就可以实现各种自定义动画效果了：

5. 
function customAnimate() {
    $('#test-animate').animate({
        opacity: 0.25,
        width: '256px',
        height: '256px'
    }, 3000, function() {
        $(this).css('opacity', '1.0').css('width', '128px').css('height', '128px');
    });
}


6. 
    
        animate()
    
    
        
    


#### 串行动画 
1. jQuery的动画效果还可以串行执行，通过delay()方法还可以实现暂停，这样，我们可以实现更复杂的动画效果，而代码却相当简单：

```
var div = $('#test-animates');
// 动画效果：slideDown - 暂停 - 放大 - 暂停 - 缩小
div.slideDown(2000)
   .delay(1000)
   .animate({
       width: '256px',
       height: '256px'
   }, 2000)
   .delay(1000)
   .animate({
       width: '128px',
       height: '128px'
   }, 2000);
}
</script>
```
2. 因为动画需要执行一段时间，所以jQuery必须不断返回新的Promise对象才能后续执行操作。简单地把动画封装在函数中是不够的。

3. 效果实测：

4. 
function animates() {
    $('#test-animates')
        .hide()
        .slideDown(2000)
        .delay(1000)
        .animate({
            width: '256px',
            height: '256px'
        }, 2000)
        .delay(1000)
        .animate({
            width: '128px',
            height: '128px'
        }, 2000);
}


5. 
    
        animate
    
    
        
    


#### 为什么有的动画没有效果 
1. 你可能会遇到，有的动画如slideUp()根本没有效果。这是因为jQuery动画的原理是逐渐改变CSS的值，如height从100px逐渐变为0。但是很多不是block性质的DOM元素，对它们设置height根本就不起作用，所以动画也就没有效果。

2. 此外，jQuery也没有实现对background-color的动画效果，用animate()设置background-color也没有效果。这种情况下可以使用CSS3的transition实现动画效果。

#### 练习 
1. 在执行删除操作时，给用户显示一个动画比直接调用remove()要更好。请在表格删除一行的时候添加一个淡出的动画效果：

```
'use strict';

function deleteFirstTR() {
    var tr = $('#test-table>tbody>tr:visible').first();
----
----
}

deleteFirstTR();
```
2. 
$(function () {
    var trs = [['Bart Simpson', 'bart.s@primary.school', 'Springfield', 'Active'],
               ['Michael Scofield', 'm.scofield@escape.org', 'Fox River', 'Locked'],
               ['Optimus Prime', 'prime@cybertron.org', 'Cybertron', 'Active'],
               ['Peter Parker', 'spider@movie.org', 'New York', 'Active'],
               ['Thor Odinson', 'thor@asgard.org', 'Asgard', 'Active']];
    var tbody = $('#test-table>tbody');
    var i;
    for (i=0; i < trs.length; i++) {
        tbody.append('<tr><td>' + trs[i].join('</td><td>') + '</td></tr>');
    }
    i = 0;
    $('#test-add-button').click(function () {
        if (i>=trs.length) {
            i = 0;
        }
        tbody.append('<tr><td>' + trs[i].join('</td><td>') + '</td></tr>');
        i ++;
    });
});


3. 
    
        
            Name
            Email
            Address
            Status
        
    
    
    


4.  Add

### AJAX
1. 用JavaScript写AJAX前面已经介绍过了，主要问题就是不同浏览器需要写不同代码，并且状态和错误处理写起来很麻烦。

2. 用jQuery的相关对象来处理AJAX，不但不需要考虑浏览器问题，代码也能大大简化。

#### ajax 
1. jQuery在全局对象jQuery（也就是$）绑定了ajax()函数，可以处理AJAX请求。ajax(url, settings)函数需要接收一个URL和一个可选的settings对象，常用的选项如下：

2. 

async：是否异步执行AJAX请求，默认为true，千万不要指定为false；


method：发送的Method，缺省为'GET'，可指定为'POST'、'PUT'等；


contentType：发送POST请求的格式，默认值为'application/x-www-form-urlencoded; charset=UTF-8'，也可以指定为text/plain、application/json；


data：发送的数据，可以是字符串、数组或object。如果是GET请求，data将被转换成query附加到URL上，如果是POST请求，根据contentType把data序列化成合适的格式；


headers：发送的额外的HTTP头，必须是一个object；


dataType：接收的数据格式，可以指定为'html'、'xml'、'json'、'text'等，缺省情况下根据响应的Content-Type猜测。



3. 下面的例子发送一个GET请求，并返回一个JSON格式的数据：

```
var jqxhr = $.ajax('/api/categories', {
    dataType: 'json'
});
// 请求已经发送了
```
4. 不过，如何用回调函数处理返回的数据和出错时的响应呢？

5. 还记得Promise对象吗？jQuery的jqXHR对象类似一个Promise对象，我们可以用链式写法来处理各种回调：

```
'use strict';

function ajaxLog(s) {
    var txt = $('#test-response-text');
    txt.val(txt.val() + '\n' + s);
}

$('#test-response-text').val('');
----
var jqxhr = $.ajax('/api/categories', {
    dataType: 'json'
}).done(function (data) {
    ajaxLog('成功, 收到的数据: ' + JSON.stringify(data));
}).fail(function (xhr, status) {
    ajaxLog('失败: ' + xhr.status + ', 原因: ' + status);
}).always(function () {
    ajaxLog('请求完成: 无论成功或失败都会调用');
});
```
6. 
响应结果：


#### get 
1. 对常用的AJAX操作，jQuery提供了一些辅助方法。由于GET请求最常见，所以jQuery提供了get()方法，可以这么写：

```
var jqxhr = $.get('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
});
```
2. 第二个参数如果是object，jQuery自动把它变成query string然后加到URL后面，实际的URL是：

```
/path/to/resource?name=Bob%20Lee&check=1
```
3. 这样我们就不用关心如何用URL编码并构造一个query string了。

#### post 
1. post()和get()类似，但是传入的第二个参数默认被序列化为application/x-www-form-urlencoded：

```
var jqxhr = $.post('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
});
```
2. 实际构造的数据name=Bob%20Lee&check=1作为POST的body被发送。

#### getJSON 
1. 由于JSON用得越来越普遍，所以jQuery也提供了getJSON()方法来快速通过GET获取一个JSON对象：

```
var jqxhr = $.getJSON('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
}).done(function (data) {
    // data已经被解析为JSON对象了
});
```
#### 安全限制 
1. jQuery的AJAX完全封装的是JavaScript的AJAX操作，所以它的安全限制和前面讲的用JavaScript写AJAX完全一样。

2. 如果需要使用JSONP，可以在ajax()中设置jsonp: 'callback'，让jQuery实现JSONP跨域加载数据。

3. 关于跨域的设置请参考浏览器 - AJAX一节中CORS的设置。

### 扩展
1. 当我们使用jQuery对象的方法时，由于jQuery对象可以操作一组DOM，而且支持链式操作，所以用起来非常方便。

2. 但是jQuery内置的方法永远不可能满足所有的需求。比如，我们想要高亮显示某些DOM元素，用jQuery可以这么实现：

```
$('span.hl').css('backgroundColor', '#fffceb').css('color', '#d85030');

$('p a.hl').css('backgroundColor', '#fffceb').css('color', '#d85030');
```
3. 总是写重复代码可不好，万一以后还要修改字体就更麻烦了，能不能统一起来，写个highlight()方法？

```
$('span.hl').highlight();

$('p a.hl').highlight();
```
4. 答案是肯定的。我们可以扩展jQuery来实现自定义方法。将来如果要修改高亮的逻辑，只需修改一处扩展代码。这种方式也称为编写jQuery插件。

#### 编写jQuery插件 
1. 给jQuery对象绑定一个新方法是通过扩展$.fn对象实现的。让我们来编写第一个扩展——highlight1()：

2. 
$.fn.highlight1 = function () {
    this.css('backgroundColor', '#fffceb').css('color', '#d85030');
    return this;
}


```
$.fn.highlight1 = function () {
    // this已绑定为当前jQuery对象:
    this.css('backgroundColor', '#fffceb').css('color', '#d85030');
    return this;
}
```
3. 注意到函数内部的this在调用时被绑定为jQuery对象，所以函数内部代码可以正常调用所有jQuery对象的方法。

4. 对于如下的HTML结构：

```
<!-- HTML结构 -->
<div id="test-highlight1">
    <p>什么是<span>jQuery</span></p>
    <p><span>jQuery</span>是目前最流行的<span>JavaScript</span>库。</p>
</div>
```
5. 来测试一下highlight1()的效果：

```
'use strict';
----
$('#test-highlight1 span').highlight1();
```
6. 
    什么是jQuery
    jQuery是目前最流行的JavaScript库。


7. 细心的童鞋可能发现了，为什么最后要return this;？因为jQuery对象支持链式操作，我们自己写的扩展方法也要能继续链式下去：

```
$('span.hl').highlight1().slideDown();
```
8. 不然，用户调用的时候，就不得不把上面的代码拆成两行。

9. 但是这个版本并不完美。有的用户希望高亮的颜色能自己来指定，怎么办？

10. 我们可以给方法加个参数，让用户自己把参数用对象传进去。于是我们有了第二个版本的highlight2()：

11. 
$.fn.highlight2 = function (options) {
    var bgcolor = options && options.backgroundColor || '#fffceb';
    var color = options && options.color || '#d85030';
    this.css('backgroundColor', bgcolor).css('color', color);
    return this;
}


```
$.fn.highlight2 = function (options) {
    // 要考虑到各种情况:
    // options为undefined
    // options只有部分key
    var bgcolor = options && options.backgroundColor || '#fffceb';
    var color = options && options.color || '#d85030';
    this.css('backgroundColor', bgcolor).css('color', color);
    return this;
}
```
12. 对于如下HTML结构：

```
<!-- HTML结构 -->
<div id="test-highlight2">
    <p>什么是<span>jQuery</span> <span>Plugin</span></p>
    <p>编写<span>jQuery</span> <span>Plugin</span>可以用来扩展<span>jQuery</span>的功能。</p>
</div>
```
13. 来实测一下带参数的highlight2()：

```
'use strict';
----
$('#test-highlight2 span').highlight2({
    backgroundColor: '#00a8e6',
    color: '#ffffff'
});
```
14. 
    什么是jQuery Plugin
    编写jQuery Plugin可以用来扩展jQuery的功能。


15. 对于默认值的处理，我们用了一个简单的&&和||短路操作符，总能得到一个有效的值。

16. 另一种方法是使用jQuery提供的辅助方法$.extend(target, obj1, obj2, ...)，它把多个object对象的属性合并到第一个target对象中，遇到同名属性，总是使用靠后的对象的值，也就是越往后优先级越高：

```
// 把默认值和用户传入的options合并到对象{}中并返回:
var opts = $.extend({}, {
    backgroundColor: '#00a8e6',
    color: '#ffffff'
}, options);
```
17. 紧接着用户对highlight2()提出了意见：每次调用都需要传入自定义的设置，能不能让我自己设定一个缺省值，以后的调用统一使用无参数的highlight2()？

18. 也就是说，我们设定的默认值应该能允许用户修改。

19. 那默认值放哪比较合适？放全局变量肯定不合适，最佳地点是$.fn.highlight2这个函数对象本身。

20. 于是最终版的highlight()终于诞生了：

21. 
$.fn.highlight = function (options) {
    var opts = $.extend({}, $.fn.highlight.defaults, options);
    this.css('backgroundColor', opts.backgroundColor).css('color', opts.color);
    return this;
}

$.fn.highlight.defaults = {
    color: '#d85030',
    backgroundColor: '#fff8de'
}


```
$.fn.highlight = function (options) {
    // 合并默认值和用户设定值:
    var opts = $.extend({}, $.fn.highlight.defaults, options);
    this.css('backgroundColor', opts.backgroundColor).css('color', opts.color);
    return this;
}

// 设定默认值:
$.fn.highlight.defaults = {
    color: '#d85030',
    backgroundColor: '#fff8de'
}
```
22. 这次用户终于满意了。用户使用时，只需一次性设定默认值：

```
$.fn.highlight.defaults.color = '#fff';
$.fn.highlight.defaults.backgroundColor = '#000';
```
23. 然后就可以非常简单地调用highlight()了。

24. 对如下的HTML结构：

```
<!-- HTML结构 -->
<div id="test-highlight">
    <p>如何编写<span>jQuery</span> <span>Plugin</span></p>
    <p>编写<span>jQuery</span> <span>Plugin</span>，要设置<span>默认值</span>，并允许用户修改<span>默认值</span>，或者运行时传入<span>其他值</span>。</p>
</div>
```
25. 实测一下修改默认值的效果：

```
'use strict';
----
$.fn.highlight.defaults.color = '#659f13';
$.fn.highlight.defaults.backgroundColor = '#f2fae3';

$('#test-highlight p:first-child span').highlight();

$('#test-highlight p:last-child span').highlight({
    color: '#dd1144'
});
```
26. 
    如何编写jQuery Plugin
    编写jQuery Plugin，要设置默认值，并允许用户修改默认值，或者运行时传入其他值。


27. 最终，我们得出编写一个jQuery插件的原则：

28. 
给$.fn绑定函数，实现插件的代码逻辑；
插件函数最后要return this;以支持链式调用；
插件函数要有默认值，绑定在$.fn.<pluginName>.defaults上；
用户在调用时可传入设定值以便覆盖默认值。


#### 针对特定元素的扩展 
1. 我们知道jQuery对象的有些方法只能作用在特定DOM元素上，比如submit()方法只能针对form。如果我们编写的扩展只能针对某些类型的DOM元素，应该怎么写？

2. 还记得jQuery的选择器支持filter()方法来过滤吗？我们可以借助这个方法来实现针对特定元素的扩展。

3. 举个例子，现在我们要给所有指向外链的超链接加上跳转提示，怎么做？

4. 先写出用户调用的代码：

```
$('#main a').external();
```
5. 然后按照上面的方法编写一个external扩展：

6. 
$.fn.external = function () {
    return this.filter('a').each(function () {
        var a = $(this);
        var url = a.attr('href');
        if (url && (url.indexOf('http://')===0 || url.indexOf('https://')===0)) {
            a.attr('href', '#0')
             .removeAttr('target')
             .append(' <i class="uk-icon-external-link"></i>')
             .click(function () {
                if(confirm('你确定要前往' + url + '？')) {
                    window.open(url);
                }
            });
        }
    });
}


```
$.fn.external = function () {
    // return返回的each()返回结果，支持链式调用:
    return this.filter('a').each(function () {
        // 注意: each()内部的回调函数的this绑定为DOM本身!
        var a = $(this);
        var url = a.attr('href');
        if (url && (url.indexOf('http://')===0 || url.indexOf('https://')===0)) {
            a.attr('href', '#0')
             .removeAttr('target')
             .append(' <i class="uk-icon-external-link"></i>')
             .click(function () {
                if(confirm('你确定要前往' + url + '？')) {
                    window.open(url);
                }
            });
        }
    });
}
```
7. 对如下的HTML结构：

```
<!-- HTML结构 -->
<div id="test-external">
    <p>如何学习<a href="http://jquery.com">jQuery</a>？</p>
    <p>首先，你要学习<a href="/wiki/1022910821149312">JavaScript</a>，并了解基本的<a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>。</p>
</div>
```
8. 实测外链效果：

```
'use strict';
----
$('#test-external a').external();
```
9. 
如何学习jQuery？
    首先，你要学习JavaScript，并了解基本的HTML。


#### 小结 
1. 扩展jQuery对象的功能十分简单，但是我们要遵循jQuery的原则，编写的扩展方法能支持链式调用、具备默认值和过滤特定元素，使得扩展方法看上去和jQuery本身的方法没有什么区别。

## 错误处理
1. 在执行JavaScript代码的时候，有些情况下会发生错误。

2. 错误分两种，一种是程序写的逻辑不对，导致代码执行异常。例如：

```
var s = null;
var len = s.length; // TypeError：null变量没有length属性
```
3. 对于这种错误，要修复程序。

4. 一种是执行过程中，程序可能遇到无法预测的异常情况而报错，例如，网络连接中断，读取不存在的文件，没有操作权限等。

5. 对于这种错误，我们需要处理它，并可能需要给用户反馈。

6. 错误处理是程序设计时必须要考虑的问题。对于C这样贴近系统底层的语言，错误是通过错误码返回的：

```
int fd = open("/path/to/file", O_RDONLY);
if (fd == -1) {
    printf("Error when open file!");
} else {
    // TODO
}
```
7. 通过错误码返回错误，就需要约定什么是正确的返回值，什么是错误的返回值。上面的open()函数约定返回-1表示错误。

8. 显然，这种用错误码表示错误在编写程序时十分不便。

9. 因此，高级语言通常都提供了更抽象的错误处理逻辑try ... catch ... finally，JavaScript也不例外。

#### try ... catch ... finally 
1. 使用try ... catch ... finally处理错误时，我们编写的代码如下：

```
'use strict';
----
var r1, r2, s = null;
try {
    r1 = s.length; // 此处应产生错误
    r2 = 100; // 该语句不会执行
} catch (e) {
    console.log('出错了：' + e);
} finally {
    console.log('finally');
}
console.log('r1 = ' + r1); // r1应为undefined
console.log('r2 = ' + r2); // r2应为undefined
----
// 直接运行
```
2. 运行后可以发现，输出提示类似“出错了：TypeError: Cannot read property 'length' of null”。

3. 我们来分析一下使用try ... catch ... finally的执行流程。

4. 当代码块被try { ... }包裹的时候，就表示这部分代码执行过程中可能会发生错误，一旦发生错误，就不再继续执行后续代码，转而跳到catch块。catch (e) { ... }包裹的代码就是错误处理代码，变量e表示捕获到的错误。最后，无论有没有错误，finally一定会被执行。

5. 所以，有错误发生时，执行流程像这样：

6. 
先执行try { ... }的代码；
执行到出错的语句时，后续语句不再继续执行，转而执行catch (e) { ... }代码；
最后执行finally { ... }代码。


7. 而没有错误发生时，执行流程像这样：

8. 
先执行try { ... }的代码；
因为没有出错，catch (e) { ... }代码不会被执行；
最后执行finally { ... }代码。


9. 最后请注意，catch和finally可以不必都出现。也就是说，try语句一共有三种形式：

10. 完整的try ... catch ... finally：

```
try {
    ...
} catch (e) {
    ...
} finally {
    ...
}
```
11. 只有try ... catch，没有finally：

```
try {
    ...
} catch (e) {
    ...
}
```
12. 只有try ... finally，没有catch：

```
try {
    ...
} finally {
    ...
}
```
#### 错误类型 
1. JavaScript有一个标准的Error对象表示错误，还有从Error派生的TypeError、ReferenceError等错误对象。我们在处理错误时，可以通过catch(e)捕获的变量e访问错误对象：

```
try {
    ...
} catch (e) {
    if (e instanceof TypeError) {
        alert('Type error!');
    } else if (e instanceof Error) {
        alert(e.message);
    } else {
        alert('Error: ' + e);
    }
}
```
2. 使用变量e是一个习惯用法，也可以以其他变量名命名，如catch(ex)。

#### 抛出错误 
1. 程序也可以主动抛出一个错误，让执行流程直接跳转到catch块。抛出错误使用throw语句。

2. 例如，下面的代码让用户输入一个数字，程序接收到的实际上是一个字符串，然后用parseInt()转换为整数。当用户输入不合法的时候，我们就抛出错误：

```
'use strict';
----
var r, n, s;
try {
    s = prompt('请输入一个数字');
    n = parseInt(s);
    if (isNaN(n)) {
        throw new Error('输入错误');
    }
    // 计算平方:
    r = n * n;
    console.log(n + ' * ' + n + ' = ' + r);
} catch (e) {
    console.log('出错了：' + e);
}
----
// 直接运行
```
3. 实际上，JavaScript允许抛出任意对象，包括数字、字符串。但是，最好还是抛出一个Error对象。

4. 最后，当我们用catch捕获错误时，一定要编写错误处理语句：

```
var n = 0, s;
try {
    n = s.length;
} catch (e) {
    console.log(e);
}
console.log(n);
```
5. 哪怕仅仅把错误打印出来，也不要什么也不干：

```
var n = 0, s;
try {
    n = s.length;
} catch (e) {
}
console.log(n);
```
6. 因为catch到错误却什么都不执行，就不知道程序执行过程中到底有没有发生错误。

7. 处理错误时，请不要简单粗暴地用alert()把错误显示给用户。教程的代码使用alert()是为了便于演示。

### 错误传播
1. 如果代码发生了错误，又没有被try ... catch捕获，那么，程序执行流程会跳转到哪呢？

```
function getLength(s) {
    return s.length;
}

function printLength() {
    console.log(getLength('abc')); // 3
    console.log(getLength(null)); // Error!
}

printLength();
```
2. 如果在一个函数内部发生了错误，它自身没有捕获，错误就会被抛到外层调用函数，如果外层函数也没有捕获，该错误会一直沿着函数调用链向上抛出，直到被JavaScript引擎捕获，代码终止执行。

3. 所以，我们不必在每一个函数内部捕获错误，只需要在合适的地方来个统一捕获，一网打尽：

```
'use strict';
----
function main(s) {
    console.log('BEGIN main()');
    try {
        foo(s);
    } catch (e) {
        console.log('出错了：' + e);
    }
    console.log('END main()');
}

function foo(s) {
    console.log('BEGIN foo()');
    bar(s);
    console.log('END foo()');
}

function bar(s) {
    console.log('BEGIN bar()');
    console.log('length = ' + s.length);
    console.log('END bar()');
}

main(null);
----
// 直接运行，观察控制台输出
```
4. 当bar()函数传入参数null时，代码会报错，错误会向上抛给调用方foo()函数，foo()函数没有try ... catch语句，所以错误继续向上抛给调用方main()函数，main()函数有try ... catch语句，所以错误最终在main()函数被处理了。

5. 至于在哪些地方捕获错误比较合适，需要视情况而定。

### 异步错误处理
1. 编写JavaScript代码时，我们要时刻牢记，JavaScript引擎是一个事件驱动的执行引擎，代码总是以单线程执行，而回调函数的执行需要等到下一个满足条件的事件出现后，才会被执行。

2. 例如，setTimeout()函数可以传入回调函数，并在指定若干毫秒后执行：

```
function printTime() {
    console.log('It is time!');
}

setTimeout(printTime, 1000);
console.log('done');
```
3. 上面的代码会先打印done，1秒后才会打印It is time!。

4. 如果printTime()函数内部发生了错误，我们试图用try包裹setTimeout()是无效的：

```
'use strict';
----
function printTime() {
    throw new Error();
}

try {
    setTimeout(printTime, 1000);
    console.log('done');
} catch (e) {
    console.log('error');
}
----
// 直接运行，看是否会alert
```
5. 原因就在于调用setTimeout()函数时，传入的printTime函数并未立刻执行！紧接着，JavaScript引擎会继续执行console.log('done');语句，而此时并没有错误发生。直到1秒钟后，执行printTime函数时才发生错误，但此时除了在printTime函数内部捕获错误外，外层代码并无法捕获。

6. 所以，涉及到异步代码，无法在调用时捕获，原因就是在捕获的当时，回调函数并未执行。

7. 类似的，当我们处理一个事件时，在绑定事件的代码处，无法捕获事件处理函数的错误。

8. 例如，针对以下的表单：

```
<form>
    <input id="x"> + <input id="y">
    <button id="calc" type="button">计算</button>
</form>
```
9. 
     + 
    计算


10. 我们用下面的代码给button绑定click事件：

```
'use strict';

var $btn = $('#calc');

// 取消已绑定的事件:
$btn.off('click');
----
try {
    $btn.click(function () {
        var
            x = parseFloat($('#x').val()),
            y = parseFloat($('#y').val()),
            r;
        if (isNaN(x) || isNaN(y)) {
            throw new Error('输入有误');
        }
        r = x + y;
        alert('计算结果：' + r);
    });
} catch (e) {
    alert('输入有误！');
}
```
11. 但是，用户输入错误时，处理函数并未捕获到错误。请修复错误处理代码。

## underscore
1. 前面我们已经讲过了，JavaScript是函数式编程语言，支持高阶函数和闭包。函数式编程非常强大，可以写出非常简洁的代码。例如Array的map()和filter()方法：

```
'use strict';
var a1 = [1, 4, 9, 16];
var a2 = a1.map(Math.sqrt); // [1, 2, 3, 4]
var a3 = a2.filter((x) => { return x % 2 === 0; }); // [2, 4]
```
2. 现在问题来了，Array有map()和filter()方法，可是Object没有这些方法。此外，低版本的浏览器例如IE6～8也没有这些方法，怎么办？

3. 方法一，自己把这些方法添加到Array.prototype中，然后给Object.prototype也加上mapObject()等类似的方法。

4. 方法二，直接找一个成熟可靠的第三方开源库，使用统一的函数来实现map()、filter()这些操作。

5. 我们采用方法二，选择的第三方库就是underscore。

6. 正如jQuery统一了不同浏览器之间的DOM操作的差异，让我们可以简单地对DOM进行操作，underscore则提供了一套完善的函数式编程的接口，让我们更方便地在JavaScript中实现函数式编程。

7. jQuery在加载时，会把自身绑定到唯一的全局变量$上，underscore与其类似，会把自身绑定到唯一的全局变量_上，这也是为啥它的名字叫underscore的原因。

8. 用underscore实现map()操作如下：

```
'use strict';
_.map([1, 2, 3], (x) => x * x); // [1, 4, 9]
```
9. 咋一看比直接用Array.map()要麻烦一点，可是underscore的map()还可以作用于Object：

```
'use strict';
_.map({ a: 1, b: 2, c: 3 }, (v, k) => k + '=' + v); // ['a=1', 'b=2', 'c=3']
```
10. 后面我们会详细介绍underscore提供了一系列函数式接口。

### Collections
1. underscore为集合类对象提供了一致的接口。集合类是指Array和Object，暂不支持Map和Set。

#### map/filter 
1. 和Array的map()与filter()类似，但是underscore的map()和filter()可以作用于Object。当作用于Object时，传入的函数为function (value, key)，第一个参数接收value，第二个参数接收key：

```
'use strict';

var obj = {
    name: 'bob',
    school: 'No.1 middle school',
    address: 'xueyuan road'
};
----
var upper = _.map(obj, function (value, key) {
    return ???;
});
----
console.log(JSON.stringify(upper));
```
2. 你也许会想，为啥对Object作map()操作的返回结果是Array？应该是Object才合理啊！把_.map换成_.mapObject再试试。

#### every / some 
1. 当集合的所有元素都满足条件时，_.every()函数返回true，当集合的至少一个元素满足条件时，_.some()函数返回true：

```
'use strict';
// 所有元素都大于0？
_.every([1, 4, 7, -3, -9], (x) => x > 0); // false
// 至少一个元素大于0？
_.some([1, 4, 7, -3, -9], (x) => x > 0); // true
```
2. 当集合是Object时，我们可以同时获得value和key：

```
'use strict';
var obj = {
    name: 'bob',
    school: 'No.1 middle school',
    address: 'xueyuan road'
};
// 判断key和value是否全部是小写：
----
var r1 = _.every(obj, function (value, key) {
    return ???;
});
var r2 = _.some(obj, function (value, key) {
    return ???;
});
----
console.log('every key-value are lowercase: ' + r1 + '\nsome key-value are lowercase: ' + r2);
```
#### max / min 
1. 这两个函数直接返回集合中最大和最小的数：

```
'use strict';
var arr = [3, 5, 7, 9];
_.max(arr); // 9
_.min(arr); // 3

// 空集合会返回-Infinity和Infinity，所以要先判断集合不为空：
_.max([])
-Infinity
_.min([])
Infinity
```
2. 注意，如果集合是Object，max()和min()只作用于value，忽略掉key：

```
'use strict';
_.max({ a: 1, b: 2, c: 3 }); // 3
```
#### groupBy 
1. groupBy()把集合的元素按照key归类，key由传入的函数返回：

```
'use strict';

var scores = [20, 81, 75, 40, 91, 59, 77, 66, 72, 88, 99];
var groups = _.groupBy(scores, function (x) {
    if (x < 60) {
        return 'C';
    } else if (x < 80) {
        return 'B';
    } else {
        return 'A';
    }
});
// 结果:
// {
//   A: [81, 91, 88, 99],
//   B: [75, 77, 66, 72],
//   C: [20, 40, 59]
// }
```
2. 可见groupBy()用来分组是非常方便的。

#### shuffle / sample 
1. shuffle()用洗牌算法随机打乱一个集合：

```
'use strict';
// 注意每次结果都不一样：
_.shuffle([1, 2, 3, 4, 5, 6]); // [3, 5, 4, 6, 2, 1]
```
2. sample()则是随机选择一个或多个元素：

```
'use strict';
// 注意每次结果都不一样：
// 随机选1个：
_.sample([1, 2, 3, 4, 5, 6]); // 2
// 随机选3个：
_.sample([1, 2, 3, 4, 5, 6], 3); // [6, 1, 4]
```
3. 更多完整的函数请参考underscore的文档：http://underscorejs.org/#collections

### Arrays
1. underscore为Array提供了许多工具类方法，可以更方便快捷地操作Array。

#### first / last 
1. 顾名思义，这两个函数分别取第一个和最后一个元素：

```
'use strict';
var arr = [2, 4, 6, 8];
_.first(arr); // 2
_.last(arr); // 8
```
#### flatten 
1. flatten()接收一个Array，无论这个Array里面嵌套了多少个Array，flatten()最后都把它们变成一个一维数组：

```
'use strict';

_.flatten([1, [2], [3, [[4], [5]]]]); // [1, 2, 3, 4, 5]
```
#### zip / unzip 
1. zip()把两个或多个数组的所有元素按索引对齐，然后按索引合并成新数组。例如，你有一个Array保存了名字，另一个Array保存了分数，现在，要把名字和分数给对上，用zip()轻松实现：

```
'use strict';

var names = ['Adam', 'Lisa', 'Bart'];
var scores = [85, 92, 59];
_.zip(names, scores);
// [['Adam', 85], ['Lisa', 92], ['Bart', 59]]
```
2. unzip()则是反过来：

```
'use strict';
var namesAndScores = [['Adam', 85], ['Lisa', 92], ['Bart', 59]];
_.unzip(namesAndScores);
// [['Adam', 'Lisa', 'Bart'], [85, 92, 59]]
```
#### object 
1. 有时候你会想，与其用zip()，为啥不把名字和分数直接对应成Object呢？别急，object()函数就是干这个的：

```
'use strict';

var names = ['Adam', 'Lisa', 'Bart'];
var scores = [85, 92, 59];
_.object(names, scores);
// {Adam: 85, Lisa: 92, Bart: 59}
```
2. 注意_.object()是一个函数，不是JavaScript的Object对象。

#### range 
1. range()让你快速生成一个序列，不再需要用for循环实现了：

```
'use strict';

// 从0开始小于10:
_.range(10); // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

// 从1开始小于11：
_.range(1, 11); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// 从0开始小于30，步长5:
_.range(0, 30, 5); // [0, 5, 10, 15, 20, 25]

// 从0开始大于-10，步长-1:
_.range(0, -10, -1); // [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```
2. 更多完整的函数请参考underscore的文档：http://underscorejs.org/#arrays

#### 练习 
1. 请根据underscore官方文档，使用_.uniq对数组元素进行不区分大小写去重：

```
'use strict';

var arr = ['Apple', 'orange', 'banana', 'ORANGE', 'apple', 'PEAR'];
----
var result = ???
----
// 测试
if (result.toString() === ["Apple", "orange", "banana", "PEAR"].toString()) {
    console.log('测试成功!');
} else {
    console.log('测试失败!');
}
```
### Functions
1. 因为underscore本来就是为了充分发挥JavaScript的函数式编程特性，所以也提供了大量JavaScript本身没有的高阶函数。

#### bind 
1. bind()有什么用？我们先看一个常见的错误用法：

```
'use strict';

var s = ' Hello  ';
s.trim();
// 输出'Hello'

var fn = s.trim;
fn();
// Uncaught TypeError: String.prototype.trim called on null or undefined
```
2. 如果你想用fn()取代s.trim()，按照上面的做法是不行的，因为直接调用fn()传入的this指针是undefined，必须这么用：

```
'use strict';

var s = ' Hello  ';
var fn = s.trim;
// 调用call并传入s对象作为this:
fn.call(s)
// 输出Hello
```
3. 这样搞多麻烦！还不如直接用s.trim()。但是，bind()可以帮我们把s对象直接绑定在fn()的this指针上，以后调用fn()就可以直接正常调用了：

```
'use strict';

var s = ' Hello  ';
var fn = _.bind(s.trim, s);
fn();
// 输出Hello
```
4. 结论：当用一个变量fn指向一个对象的方法时，直接调用fn()是不行的，因为丢失了this对象的引用。用bind可以修复这个问题。

#### partial 
1. partial()就是为一个函数创建偏函数。偏函数是什么东东？看例子：

2. 假设我们要计算xy，这时只需要调用Math.pow(x, y)就可以了。

3. 假设我们经常计算2y，每次都写Math.pow(2, y)就比较麻烦，如果创建一个新的函数能直接这样写pow2N(y)就好了，这个新函数pow2N(y)就是根据Math.pow(x, y)创建出来的偏函数，它固定住了原函数的第一个参数（始终为2）：

```
'use strict';

var pow2N = _.partial(Math.pow, 2);
pow2N(3); // 8
pow2N(5); // 32
pow2N(10); // 1024
```
4. 如果我们不想固定第一个参数，想固定第二个参数怎么办？比如，希望创建一个偏函数cube(x)，计算x3，可以用_作占位符，固定住第二个参数：

```
'use strict';

var cube = _.partial(Math.pow, _, 3);
cube(3); // 27
cube(5); // 125
cube(10); // 1000
```
5. 可见，创建偏函数的目的是将原函数的某些参数固定住，可以降低新函数调用的难度。

#### memoize 
1. 如果一个函数调用开销很大，我们就可能希望能把结果缓存下来，以便后续调用时直接获得结果。举个例子，计算阶乘就比较耗时：

```
'use strict';

function factorial(n) {
    console.log('start calculate ' + n + '!...');
    var s = 1, i = n;
    while (i > 1) {
        s = s * i;
        i --;
    }
    console.log(n + '! = ' + s);
    return s;
}

factorial(10); // 3628800
// 注意控制台输出:
// start calculate 10!...
// 10! = 3628800
```
2. 用memoize()就可以自动缓存函数计算的结果：

```
'use strict';

var factorial = _.memoize(function(n) {
    console.log('start calculate ' + n + '!...');
    var s = 1, i = n;
    while (i > 1) {
        s = s * i;
        i --;
    }
    console.log(n + '! = ' + s);
    return s;
});

// 第一次调用:
factorial(10); // 3628800
// 注意控制台输出:
// start calculate 10!...
// 10! = 3628800

// 第二次调用:
factorial(10); // 3628800
// 控制台没有输出
```
3. 对于相同的调用，比如连续两次调用factorial(10)，第二次调用并没有计算，而是直接返回上次计算后缓存的结果。不过，当你计算factorial(9)的时候，仍然会重新计算。

4. 可以对factorial()进行改进，让其递归调用：

```
'use strict';

var factorial = _.memoize(function(n) {
    console.log('start calculate ' + n + '!...');
    if (n < 2) {
        return 1;
    }
    return n * factorial(n - 1);
});

factorial(10); // 3628800
// 输出结果说明factorial(1)~factorial(10)都已经缓存了:
// start calculate 10!...
// start calculate 9!...
// start calculate 8!...
// start calculate 7!...
// start calculate 6!...
// start calculate 5!...
// start calculate 4!...
// start calculate 3!...
// start calculate 2!...
// start calculate 1!...

factorial(9); // 362880
// console无输出
```
#### once 
1. 顾名思义，once()保证某个函数执行且仅执行一次。如果你有一个方法叫register()，用户在页面上点两个按钮的任何一个都可以执行的话，就可以用once()保证函数仅调用一次，无论用户点击多少次：

```
'use strict';
----
var register = _.once(function () {
    alert('Register ok!');
});
----
// 测试效果:
register();
register();
register();
```
#### delay 
1. delay()可以让一个函数延迟执行，效果和setTimeout()是一样的，但是代码明显简单了：

```
'use strict';

// 2秒后调用alert():
_.delay(alert, 2000);
```
2. 如果要延迟调用的函数有参数，把参数也传进去：

```
'use strict';

var log = _.bind(console.log, console);
_.delay(log, 2000, 'Hello,', 'world!');
// 2秒后打印'Hello, world!':
```
3. 更多完整的函数请参考underscore的文档：http://underscorejs.org/#functions

### Objects
1. 和Array类似，underscore也提供了大量针对Object的函数。

#### keys / allKeys 
1. keys()可以非常方便地返回一个object自身所有的key，但不包含从原型链继承下来的：

```
'use strict';

function Student(name, age) {
    this.name = name;
    this.age = age;
}

var xiaoming = new Student('小明', 20);
_.keys(xiaoming); // ['name', 'age']
```
2. allKeys()除了object自身的key，还包含从原型链继承下来的：

```
'use strict';

function Student(name, age) {
    this.name = name;
    this.age = age;
}
Student.prototype.school = 'No.1 Middle School';
var xiaoming = new Student('小明', 20);
_.allKeys(xiaoming); // ['name', 'age', 'school']
```
#### values 
1. 和keys()类似，values()返回object自身但不包含原型链继承的所有值：

```
'use strict';

var obj = {
    name: '小明',
    age: 20
};

_.values(obj); // ['小明', 20]
```
2. 注意，没有allValues()，原因我也不知道。

#### mapObject 
1. mapObject()就是针对object的map版本：

```
'use strict';

var obj = { a: 1, b: 2, c: 3 };
// 注意传入的函数签名，value在前，key在后:
_.mapObject(obj, (v, k) => 100 + v); // { a: 101, b: 102, c: 103 }
```
#### invert 
1. invert()把object的每个key-value来个交换，key变成value，value变成key：

```
'use strict';

var obj = {
    Adam: 90,
    Lisa: 85,
    Bart: 59
};
_.invert(obj); // { '59': 'Bart', '85': 'Lisa', '90': 'Adam' }
```
#### extend / extendOwn 
1. extend()把多个object的key-value合并到第一个object并返回：

```
'use strict';

var a = {name: 'Bob', age: 20};
_.extend(a, {age: 15}, {age: 88, city: 'Beijing'}); // {name: 'Bob', age: 88, city: 'Beijing'}
// 变量a的内容也改变了：
a; // {name: 'Bob', age: 88, city: 'Beijing'}
```
2. 注意：如果有相同的key，后面的object的value将覆盖前面的object的value。

3. extendOwn()和extend()类似，但获取属性时忽略从原型链继承下来的属性。

#### clone 
1. 如果我们要复制一个object对象，就可以用clone()方法，它会把原有对象的所有属性都复制到新的对象中：

```
'use strict';
var source = {
    name: '小明',
    age: 20,
    skills: ['JavaScript', 'CSS', 'HTML']
};
----
var copied = _.clone(source);
----
console.log(JSON.stringify(copied, null, '  '));
```
2. 注意，clone()是“浅复制”。所谓“浅复制”就是说，两个对象相同的key所引用的value其实是同一对象：

```
source.skills === copied.skills; // true
```
3. 也就是说，修改source.skills会影响copied.skills。

#### isEqual 
1. isEqual()对两个object进行深度比较，如果内容完全相同，则返回true：

```
'use strict';

var o1 = { name: 'Bob', skills: { Java: 90, JavaScript: 99 }};
var o2 = { name: 'Bob', skills: { JavaScript: 99, Java: 90 }};

o1 === o2; // false
_.isEqual(o1, o2); // true
```
2. isEqual()其实对Array也可以比较：

```
'use strict';

var o1 = ['Bob', { skills: ['Java', 'JavaScript'] }];
var o2 = ['Bob', { skills: ['Java', 'JavaScript'] }];

o1 === o2; // false
_.isEqual(o1, o2); // true
```
3. 更多完整的函数请参考underscore的文档：http://underscorejs.org/#objects

### Chaining
1. 还记得jQuery支持链式调用吗？

```
$('a').attr('target', '_blank')
      .append(' <i class="uk-icon-external-link"></i>')
      .click(function () {});
```
2. 如果我们有一组操作，用underscore提供的函数，写出来像这样：

```
_.filter(_.map([1, 4, 9, 16, 25], Math.sqrt), x => x % 2 === 1);
// [1, 3, 5]
```
3. 能不能写成链式调用？

4. 能！

5. underscore提供了把对象包装成能进行链式调用的方法，就是chain()函数：

```
----
var r = _.chain([1, 4, 9, 16, 25])
         .map(Math.sqrt)
         .filter(x => x % 2 === 1)
         .value();
----
console.log(r); // [1, 3, 5]
```
6. 因为每一步返回的都是包装对象，所以最后一步的结果需要调用value()获得最终结果。

#### 小结 
1. 通过学习underscore，是不是对JavaScript的函数式编程又有了进一步的认识？

## Node.js
1. 从本章开始，我们就正式开启JavaScript的后端开发之旅。

2. Node.js是目前非常火热的技术，但是它的诞生经历却很奇特。

3. 众所周知，在Netscape设计出JavaScript后的短短几个月，JavaScript事实上已经是前端开发的唯一标准。

4. 后来，微软通过IE击败了Netscape后一统桌面，结果几年时间，浏览器毫无进步。（2001年推出的古老的IE 6到今天仍然有人在使用！）

5. 没有竞争就没有发展。微软认为IE6浏览器已经非常完善，几乎没有可改进之处，然后解散了IE6开发团队！而Google却认为支持现代Web应用的新一代浏览器才刚刚起步，尤其是浏览器负责运行JavaScript的引擎性能还可提升10倍。

6. 先是Mozilla借助已壮烈牺牲的Netscape遗产在2002年推出了Firefox浏览器，紧接着Apple于2003年在开源的KHTML浏览器的基础上推出了WebKit内核的Safari浏览器，不过仅限于Mac平台。

7. 随后，Google也开始创建自家的浏览器。他们也看中了WebKit内核，于是基于WebKit内核推出了Chrome浏览器。

8. Chrome浏览器是跨Windows和Mac平台的，并且，Google认为要运行现代Web应用，浏览器必须有一个性能非常强劲的JavaScript引擎，于是Google自己开发了一个高性能JavaScript引擎，名字叫V8，以BSD许可证开源。

9. 现代浏览器大战让微软的IE浏览器远远地落后了，因为他们解散了最有经验、战斗力最强的浏览器团队！回过头再追赶却发现，支持HTML5的WebKit已经成为手机端的标准了，IE浏览器从此与主流移动端设备绝缘。

10. 浏览器大战和Node有何关系？

11. 话说有个叫Ryan Dahl的歪果仁，他的工作是用C/C++写高性能Web服务。对于高性能，异步IO、事件驱动是基本原则，但是用C/C++写就太痛苦了。于是这位仁兄开始设想用高级语言开发Web服务。他评估了很多种高级语言，发现很多语言虽然同时提供了同步IO和异步IO，但是开发人员一旦用了同步IO，他们就再也懒得写异步IO了，所以，最终，Ryan瞄向了JavaScript。

12. 因为JavaScript是单线程执行，根本不能进行同步IO操作，所以，JavaScript的这一“缺陷”导致了它只能使用异步IO。

13. 选定了开发语言，还要有运行时引擎。这位仁兄曾考虑过自己写一个，不过明智地放弃了，因为V8就是开源的JavaScript引擎。让Google投资去优化V8，咱只负责改造一下拿来用，还不用付钱，这个买卖很划算。

14. 于是在2009年，Ryan正式推出了基于JavaScript语言和V8引擎的开源Web服务器项目，命名为Node.js。虽然名字很土，但是，Node第一次把JavaScript带入到后端服务器开发，加上世界上已经有无数的JavaScript开发人员，所以Node一下子就火了起来。

15. 在Node上运行的JavaScript相比其他后端开发语言有何优势？

16. 最大的优势是借助JavaScript天生的事件驱动机制加V8高性能引擎，使编写高性能Web服务轻而易举。

17. 其次，JavaScript语言本身是完善的函数式语言，在前端开发时，开发人员往往写得比较随意，让人感觉JavaScript就是个“玩具语言”。但是，在Node环境下，通过模块化的JavaScript代码，加上函数式编程，并且无需考虑浏览器兼容性问题，直接使用最新的ECMAScript 6标准，可以完全满足工程上的需求。

18. 
我还听说过io.js，这又是什么鬼？


19. 因为Node.js是开源项目，虽然由社区推动，但幕后一直由Joyent公司资助。由于一群开发者对Joyent公司的策略不满，于2014年从Node.js项目fork出了io.js项目，决定单独发展，但两者实际上是兼容的。

20. 然而中国有句古话，叫做“分久必合，合久必分”。分家后没多久，Joyent公司表示要和解，于是，io.js项目又决定回归Node.js。

21. 具体做法是将来io.js将首先添加新的特性，如果大家测试用得爽，就把新特性加入Node.js。io.js是“尝鲜版”，而Node.js是线上稳定版，相当于Fedora Linux和RHEL的关系。

22. 本章教程的所有代码都在Node.js上调试通过。如果你要尝试io.js也是可以的，不过两者如果遇到一些区别请自行查看io.js的文档。

### 安装Node.js和npm
1. 由于Node.js平台是在后端运行JavaScript代码，所以，必须首先在本机安装Node环境。

#### 安装Node.js 
1. 目前Node.js的最新版本是7.6.x。首先，从Node.js官网下载对应平台的安装程序，网速慢的童鞋请移步国内镜像。

2. 在Windows上安装时务必选择全部组件，包括勾选Add to Path。

3. 安装完成后，在Windows环境下，请打开命令提示符，然后输入node -v，如果安装正常，你应该看到v7.6.0这样的输出：

```
C:\Users\IEUser>node -v
v7.6.0
```
4. 继续在命令提示符输入node，此刻你将进入Node.js的交互环境。在交互环境下，你可以输入任意JavaScript语句，例如100+200，回车后将得到输出结果。

5. 要退出Node.js环境，连按两次Ctrl+C。

6. 




7. 在Mac或Linux环境下，请打开终端，然后输入node -v，你应该看到如下输出：

```
$ node -v
v7.6.0
```
8. 如果版本号小于v7.6.0，说明Node.js版本不对，后面章节的代码不保证能正常运行，请重新安装最新版本。

#### npm 
1. 在正式开始Node.js学习之前，我们先认识一下npm。

2. npm是什么东东？npm其实是Node.js的包管理工具（package manager）。

3. 为啥我们需要一个包管理工具呢？因为我们在Node.js上开发时，会用到很多别人写的JavaScript代码。如果我们要使用别人写的某个包，每次都根据名称搜索一下官方网站，下载代码，解压，再使用，非常繁琐。于是一个集中管理的工具应运而生：大家都把自己开发的模块打包后放到npm官网上，如果要使用，直接通过npm安装就可以直接用，不用管代码存在哪，应该从哪下载。

4. 更重要的是，如果我们要使用模块A，而模块A又依赖于模块B，模块B又依赖于模块X和模块Y，npm可以根据依赖关系，把所有依赖的包都下载下来并管理起来。否则，靠我们自己手动管理，肯定既麻烦又容易出错。

5. 讲了这么多，npm究竟在哪？

6. 其实npm已经在Node.js安装的时候顺带装好了。我们在命令提示符或者终端输入npm -v，应该看到类似的输出：

```
C:\>npm -v
4.1.2
```
7. 如果直接输入npm，你会看到类似下面的输出：

```
C:\> npm

Usage: npm <command>

where <command> is one of:
    ...
```
8. 上面的一大堆文字告诉你，npm需要跟上命令。现在我们不用关心这些命令，后面会一一讲到。目前，你只需要确保npm正确安装了，能运行就行。

#### 小结 
1. 请在本机安装Node.js环境，并确保node和npm能正常运行。

### 第一个Node程序
1. 在前面的所有章节中，我们编写的JavaScript代码都是在浏览器中运行的，因此，我们可以直接在浏览器中敲代码，然后直接运行。

2. 从本章开始，我们编写的JavaScript代码将不能在浏览器环境中执行了，而是在Node环境中执行，因此，JavaScript代码将直接在你的计算机上以命令行的方式运行，所以，我们要先选择一个文本编辑器来编写JavaScript代码，并且把它保存到本地硬盘的某个目录，才能够执行。

3. 那么问题来了：文本编辑器到底哪家强？

4. 首先，请注意，绝对不能用Word和写字板。Word和写字板保存的不是纯文本文件。如果我们要用记事本来编写JavaScript代码，要务必注意，记事本以UTF-8格式保存文件时，会自作聪明地在文件开始的地方加上几个特殊字符（UTF-8 BOM），结果经常会导致程序运行出现莫名其妙的错误。

5. 所以，用记事本写代码时请注意，保存文件时使用ANSI编码，并且暂时不要输入中文。

6. 如果你的电脑上已经安装了Sublime Text，或者Notepad++，也可以用来编写JavaScript代码，注意用UTF-8格式保存。

7. 输入以下代码：

```
'use strict';

console.log('Hello, world.');
```
8. 第一行总是写上'use strict';是因为我们总是以严格模式运行JavaScript代码，避免各种潜在陷阱。

9. 然后，选择一个目录，例如C:\Workspace，把文件保存为hello.js，就可以打开命令行窗口，把当前目录切换到hello.js所在目录，然后输入以下命令运行这个程序了：

```
C:\Workspace>node hello.js
Hello, world.
```
10. 也可以保存为别的名字，比如first.js，但是必须要以.js结尾。此外，文件名只能是英文字母、数字和下划线的组合。

11. 如果当前目录下没有hello.js这个文件，运行node hello.js就会报错：

```
C:\Workspace>node hello.js
module.js:338
    throw err;
          ^
Error: Cannot find module 'C:\Workspace\hello.js'
    at Function.Module._resolveFilename
    at Function.Module._load
    at Function.Module.runMain
    at startup
    at node.js
```
12. 报错的意思就是，没有找到hello.js这个文件，因为文件不存在。这个时候，就要检查一下当前目录下是否有这个文件了。

#### 命令行模式和Node交互模式 
1. 请注意区分命令行模式和Node交互模式。

2. 看到类似C:\>是在Windows提供的命令行模式：

3. 

4. 在命令行模式下，可以执行node进入Node交互式环境，也可以执行node hello.js运行一个.js文件。

5. 看到>是在Node交互式环境下：

6. 

7. 在Node交互式环境下，我们可以输入JavaScript代码并立刻执行。

8. 此外，在命令行模式运行.js文件和在Node交互式环境下直接运行JavaScript代码有所不同。Node交互式环境会把每一行JavaScript代码的结果自动打印出来，但是，直接运行JavaScript文件却不会。

9. 例如，在Node交互式环境下，输入：

```
> 100 + 200 + 300;
600
```
10. 直接可以看到结果600。

11. 但是，写一个calc.js的文件，内容如下：

```
100 + 200 + 300;
```
12. 然后在命令行模式下执行：

```
C:\Workspace>node calc.js
```
13. 发现什么输出都没有。

14. 这是正常的。想要输出结果，必须自己用console.log()打印出来。把calc.js改造一下：

```
console.log(100 + 200 + 300);
```
15. 再执行，就可以看到结果：

```
C:\Workspace>node calc.js
600
```
#### 使用严格模式 
1. 如果在JavaScript文件开头写上'use strict';，那么Node在执行该JavaScript时将使用严格模式。但是，在服务器环境下，如果有很多JavaScript文件，每个文件都写上'use strict';很麻烦。我们可以给Nodejs传递一个参数，让Node直接为所有js文件开启严格模式：

```
node --use_strict calc.js
```
2. 后续代码，如无特殊说明，我们都会直接给Node传递--use_strict参数来开启严格模式。

#### 小结 
1. 用文本编辑器写JavaScript程序，然后保存为后缀为.js的文件，就可以用node直接运行这个程序了。

2. Node的交互模式和直接运行.js文件有什么区别呢？

3. 直接输入node进入交互模式，相当于启动了Node解释器，但是等待你一行一行地输入源代码，每输入一行就执行一行。

4. 直接运行node hello.js文件相当于启动了Node解释器，然后一次性把hello.js文件的源代码给执行了，你是没有机会以交互的方式输入源代码的。

5. 在编写JavaScript代码的时候，完全可以一边在文本编辑器里写代码，一边开一个Node交互式命令窗口，在写代码的过程中，把部分代码粘到命令行去验证，事半功倍！前提是得有个27'的超大显示器！

#### 参考源码 
1. hello.js和calc.js

### 搭建Node开发环境
1. 使用文本编辑器来开发Node程序，最大的缺点是效率太低，运行Node程序还需要在命令行单独敲命令。如果还需要调试程序，就更加麻烦了。

2. 所以我们需要一个IDE集成开发环境，让我们能在一个环境里编码、运行、调试，这样就可以大大提升开发效率。

3. Java的集成开发环境有Eclipse，Intellij idea等，C#的集成开发环境有Visual Studio，那么问题又来了：Node.js的集成开发环境到底哪家强？

4. 考察Node.js的集成开发环境，重点放在启动速度快，执行简单，调试方便这三点上。当然，免费使用是一个加分项。

5. 综合考察后，我们隆重向大家推荐Node.js集成开发环境：

#### Visual Studio Code 
1. Visual Studio Code由微软出品，但它不是那个大块头的Visual Studio，它是一个精简版的迷你Visual Studio，并且，Visual Studio Code可以跨！平！台！Windows、Mac和Linux通用。

#### 安装Visual Studio Code 
1. 可以从Visual Studio Code的官方网站下载并安装最新的版本。

2. 安装过程中，请务必钩上以下选项：

3. 

4.  将“通过Code打开”操作添加到Windows资源管理器目录上下文菜单

5. 这将大大提升将来的操作快捷度。

6. 在Mac系统上，Finder选中一个目录，右键菜单并没有“通过Code打开”这个操作。不过我们可以通过Automator自己添加这个操作。

7. 先运行Automator，选择“服务”：

8. 

9. 然后，执行以下操作：

10. 

11. 
在右侧面板选择“服务”收到选定的“文件夹”，位于“Finder.app“，该选项是为了从Finder中接收一个文件夹；
在左侧面板选择”实用工具“，然后找到”运行Shell脚本“，把它拽到右侧面板里；
在右侧”运行Shell脚本“的面板里，选择Shell”/bin/bash“，传递输入“作为自变量”，然后修改Shell脚本如下：


```
for f in "$@"
do
    open -a "Visual Studio Code" "$f"
done
```
12. 保存为“Open With VSCode”后，打开Finder，选中一个文件夹，点击右键，“服务”，就可以看到“Open With VSCode”菜单：

13. 

#### 运行和调试JavaScript 
1. 在VS Code中，我们可以非常方便地运行JavaScript文件。

2. VS Code以文件夹作为工程目录（Workspace Dir），所有的JavaScript文件都存放在该目录下。此外，VS Code在工程目录下还需要一个.vscode的配置目录，里面存放里VS Code需要的配置文件。

3. 假设我们在C:\Work\目录下创建了一个hello目录作为工程目录，并编写了一个hello.js文件，则该工程目录的结构如下：

```
hello/ <-- workspace dir
|
+- hello.js <-- JavaScript file
|
+- .vscode/  <-- VS Code config
   |
   +- launch.json <-- VS Code config file for JavaScript
```
4. 可以用VS Code快速创建launch.json，然后修改如下：

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run hello.js",
            "type": "node",
            "request": "launch",
            "program": "${workspaceRoot}/hello.js",
            "stopOnEntry": false,
            "args": [],
            "cwd": "${workspaceRoot}",
            "preLaunchTask": null,
            "runtimeExecutable": null,
            "runtimeArgs": [
                "--nolazy"
            ],
            "env": {
                "NODE_ENV": "development"
            },
            "externalConsole": false,
            "sourceMaps": false,
            "outDir": null
        }
    ]
}
```
5. 有了配置文件，即可使用VS Code调试JavaScript。

6. 视频演示：

7. 

#### 参考源码 
1. hello.js

### 模块
1. 在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。

2. 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Node环境中，一个.js文件就称之为一个模块（module）。

3. 使用模块有什么好处？

4. 最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。我们在编写程序的时候，也经常引用其他模块，包括Node内置的模块和来自第三方的模块。

5. 使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。

6. 在上一节，我们编写了一个hello.js文件，这个hello.js文件就是一个模块，模块的名字就是文件名（去掉.js后缀），所以hello.js文件就是名为hello的模块。

7. 我们把hello.js改造一下，创建一个函数，这样我们就可以在其他地方调用这个函数：

```
'use strict';

var s = 'Hello';

function greet(name) {
    console.log(s + ', ' + name + '!');
}

module.exports = greet;
```
8. 函数greet()是我们在hello模块中定义的，你可能注意到最后一行是一个奇怪的赋值语句，它的意思是，把函数greet作为模块的输出暴露出去，这样其他模块就可以使用greet函数了。

9. 问题是其他模块怎么使用hello模块的这个greet函数呢？我们再编写一个main.js文件，调用hello模块的greet函数：

```
'use strict';

// 引入hello模块:
var greet = require('./hello');

var s = 'Michael';

greet(s); // Hello, Michael!
```
10. 注意到引入hello模块用Node提供的require函数：

```
var greet = require('./hello');
```
11. 引入的模块作为变量保存在greet变量中，那greet变量到底是什么东西？其实变量greet就是在hello.js中我们用module.exports = greet;输出的greet函数。所以，main.js就成功地引用了hello.js模块中定义的greet()函数，接下来就可以直接使用它了。

12. 在使用require()引入模块的时候，请注意模块的相对路径。因为main.js和hello.js位于同一个目录，所以我们用了当前目录.：

```
var greet = require('./hello'); // 不要忘了写相对目录!
```
13. 如果只写模块名：

```
var greet = require('hello');
```
14. 则Node会依次在内置模块、全局模块和当前模块下查找hello.js，你很可能会得到一个错误：

```
module.js
    throw err;
          ^
Error: Cannot find module 'hello'
    at Function.Module._resolveFilename
    at Function.Module._load
    ...
    at Function.Module._load
    at Function.Module.runMain
```
15. 遇到这个错误，你要检查：

16. 
模块名是否写对了；
模块文件是否存在；
相对路径是否写对了。


#### CommonJS规范 
1. 这种模块加载机制被称为CommonJS规范。在这个规范下，每个.js文件都是一个模块，它们内部各自使用的变量名和函数名都互不冲突，例如，hello.js和main.js都申明了全局变量var s = 'xxx'，但互不影响。

2. 一个模块想要对外暴露变量（函数也是变量），可以用module.exports = variable;，一个模块要引用其他模块暴露的变量，用var ref = require('module_name');就拿到了引用模块的变量。

#### 结论 
1. 要在模块中对外输出变量，用：

```
module.exports = variable;
```
2. 输出的变量可以是任意对象、函数、数组等等。

3. 要引入其他模块输出的对象，用：

```
var foo = require('other_module');
```
4. 引入的对象具体是什么，取决于引入模块输出的对象。

#### 深入了解模块原理 
1. 如果你想详细地了解CommonJS的模块实现原理，请继续往下阅读。如果不想了解，请直接跳到最后做练习。

2. 当我们编写JavaScript代码时，我们可以申明全局变量：

```
var s = 'global';
```
3. 在浏览器中，大量使用全局变量可不好。如果你在a.js中使用了全局变量s，那么，在b.js中也使用全局变量s，将造成冲突，b.js中对s赋值会改变a.js的运行逻辑。

4. 也就是说，JavaScript语言本身并没有一种模块机制来保证不同模块可以使用相同的变量名。

5. 那Node.js是如何实现这一点的？

6. 其实要实现“模块”这个功能，并不需要语法层面的支持。Node.js也并不会增加任何JavaScript语法。实现“模块”功能的奥妙就在于JavaScript是一种函数式编程语言，它支持闭包。如果我们把一段JavaScript代码用一个函数包装起来，这段代码的所有“全局”变量就变成了函数内部的局部变量。

7. 请注意我们编写的hello.js代码是这样的：

```
var s = 'Hello';
var name = 'world';

console.log(s + ' ' + name + '!');
```
8. Node.js加载了hello.js后，它可以把代码包装一下，变成这样执行：

```
(function () {
    // 读取的hello.js代码:
    var s = 'Hello';
    var name = 'world';

    console.log(s + ' ' + name + '!');
    // hello.js代码结束
})();
```
9. 这样一来，原来的全局变量s现在变成了匿名函数内部的局部变量。如果Node.js继续加载其他模块，这些模块中定义的“全局”变量s也互不干扰。

10. 所以，Node利用JavaScript的函数式编程的特性，轻而易举地实现了模块的隔离。

11. 但是，模块的输出module.exports怎么实现？

12. 这个也很容易实现，Node可以先准备一个对象module：

```
// 准备module对象:
var module = {
    id: 'hello',
    exports: {}
};
var load = function (module) {
    // 读取的hello.js代码:
    function greet(name) {
        console.log('Hello, ' + name + '!');
    }
    
    module.exports = greet;
    // hello.js代码结束
    return module.exports;
};
var exported = load(module);
// 保存module:
save(module, exported);
```
13. 可见，变量module是Node在加载js文件前准备的一个变量，并将其传入加载函数，我们在hello.js中可以直接使用变量module原因就在于它实际上是函数的一个参数：

```
module.exports = greet;
```
14. 通过把参数module传递给load()函数，hello.js就顺利地把一个变量传递给了Node执行环境，Node会把module变量保存到某个地方。

15. 由于Node保存了所有导入的module，当我们用require()获取module时，Node找到对应的module，把这个module的exports变量返回，这样，另一个模块就顺利拿到了模块的输出：

```
var greet = require('./hello');
```
16. 以上是Node实现JavaScript模块的一个简单的原理介绍。

#### module.exports vs exports 
1. 很多时候，你会看到，在Node环境中，有两种方法可以在一个模块中输出变量：

2. 方法一：对module.exports赋值：

```
// hello.js

function hello() {
    console.log('Hello, world!');
}

function greet(name) {
    console.log('Hello, ' + name + '!');
}

module.exports = {
    hello: hello,
    greet: greet
};
```
3. 方法二：直接使用exports：

```
// hello.js

function hello() {
    console.log('Hello, world!');
}

function greet(name) {
    console.log('Hello, ' + name + '!');
}

function hello() {
    console.log('Hello, world!');
}

exports.hello = hello;
exports.greet = greet;
```
4. 但是你不可以直接对exports赋值：

```
// 代码可以执行，但是模块并没有输出任何变量:
exports = {
    hello: hello,
    greet: greet
};
```
5. 如果你对上面的写法感到十分困惑，不要着急，我们来分析Node的加载机制：

6. 首先，Node会把整个待加载的hello.js文件放入一个包装函数load中执行。在执行这个load()函数前，Node准备好了module变量：

```
var module = {
    id: 'hello',
    exports: {}
};
```
7. load()函数最终返回module.exports：

```
var load = function (exports, module) {
    // hello.js的文件内容
    ...
    // load函数返回:
    return module.exports;
};

var exported = load(module.exports, module);
```
8. 也就是说，默认情况下，Node准备的exports变量和module.exports变量实际上是同一个变量，并且初始化为空对象{}，于是，我们可以写：

```
exports.foo = function () { return 'foo'; };
exports.bar = function () { return 'bar'; };
```
9. 也可以写：

```
module.exports.foo = function () { return 'foo'; };
module.exports.bar = function () { return 'bar'; };
```
10. 换句话说，Node默认给你准备了一个空对象{}，这样你可以直接往里面加东西。

11. 但是，如果我们要输出的是一个函数或数组，那么，只能给module.exports赋值：

```
module.exports = function () { return 'foo'; };
```
12. 给exports赋值是无效的，因为赋值后，module.exports仍然是空对象{}。

#### 结论 
1. 如果要输出一个键值对象{}，可以利用exports这个已存在的空对象{}，并继续在上面添加新的键值；

2. 如果要输出一个函数或数组，必须直接对module.exports对象赋值。

3. 所以我们可以得出结论：直接对module.exports赋值，可以应对任何情况：

```
module.exports = {
    foo: function () { return 'foo'; }
};
```
4. 或者：

```
module.exports = function () { return 'foo'; };
```
5. 最终，我们强烈建议使用module.exports = xxx的方式来输出模块变量，这样，你只需要记忆一种方法。

#### 练习 
1. 编写hello.js，输出一个或多个函数；

2. 编写main.js，引入hello模块，调用其函数。

#### 参考源码 
1. module

### 基本模块
1. 因为Node.js是运行在服务区端的JavaScript环境，服务器程序和浏览器程序相比，最大的特点是没有浏览器的安全限制了，而且，服务器程序必须能接收网络请求，读写文件，处理二进制内容，所以，Node.js内置的常用模块就是为了实现基本的服务器功能。这些模块在浏览器环境中是无法被执行的，因为它们的底层代码是用C/C++在Node.js运行环境中实现的。

#### global 
1. 在前面的JavaScript课程中，我们已经知道，JavaScript有且仅有一个全局对象，在浏览器中，叫window对象。而在Node.js环境中，也有唯一的全局对象，但不叫window，而叫global，这个对象的属性和方法也和浏览器环境的window不同。进入Node.js交互环境，可以直接输入：

```
> global.console
Console {
  log: [Function: bound ],
  info: [Function: bound ],
  warn: [Function: bound ],
  error: [Function: bound ],
  dir: [Function: bound ],
  time: [Function: bound ],
  timeEnd: [Function: bound ],
  trace: [Function: bound trace],
  assert: [Function: bound ],
  Console: [Function: Console] }
```
#### process 
1. process也是Node.js提供的一个对象，它代表当前Node.js进程。通过process对象可以拿到许多有用信息：

```
> process === global.process;
true
> process.version;
'v5.2.0'
> process.platform;
'darwin'
> process.arch;
'x64'
> process.cwd(); //返回当前工作目录
'/Users/michael'
> process.chdir('/private/tmp'); // 切换当前工作目录
undefined
> process.cwd();
'/private/tmp'
```
2. JavaScript程序是由事件驱动执行的单线程模型，Node.js也不例外。Node.js不断执行响应事件的JavaScript函数，直到没有任何响应事件的函数可以执行时，Node.js就退出了。

3. 如果我们想要在下一次事件响应中执行代码，可以调用process.nextTick()：

```
// test.js

// process.nextTick()将在下一轮事件循环中调用:
process.nextTick(function () {
    console.log('nextTick callback!');
});
console.log('nextTick was set!');
```
4. 用Node执行上面的代码node test.js，你会看到，打印输出是：

```
nextTick was set!
nextTick callback!
```
5. 这说明传入process.nextTick()的函数不是立刻执行，而是要等到下一次事件循环。

6. Node.js进程本身的事件就由process对象来处理。如果我们响应exit事件，就可以在程序即将退出时执行某个回调函数：

```
// 程序即将退出时的回调函数:
process.on('exit', function (code) {
    console.log('about to exit with code: ' + code);
});
```
#### 判断JavaScript执行环境 
1. 有很多JavaScript代码既能在浏览器中执行，也能在Node环境执行，但有些时候，程序本身需要判断自己到底是在什么环境下执行的，常用的方式就是根据浏览器和Node环境提供的全局变量名称来判断：

```
if (typeof(window) === 'undefined') {
    console.log('node.js');
} else {
    console.log('browser');
}
```
2. 后面，我们将介绍Node.js的常用内置模块。

#### 参考源码 
1. gl.js

### Web开发
1. 最早的软件都是运行在大型机上的，软件使用者通过“哑终端”登陆到大型机上去运行软件。后来随着PC机的兴起，软件开始主要运行在桌面上，而数据库这样的软件运行在服务器端，这种Client/Server模式简称CS架构。

2. 随着互联网的兴起，人们发现，CS架构不适合Web，最大的原因是Web应用程序的修改和升级非常迅速，而CS架构需要每个客户端逐个升级桌面App，因此，Browser/Server模式开始流行，简称BS架构。

3. 在BS架构下，客户端只需要浏览器，应用程序的逻辑和数据都存储在服务器端。浏览器只需要请求服务器，获取Web页面，并把Web页面展示给用户即可。

4. 当然，Web页面也具有极强的交互性。由于Web页面是用HTML编写的，而HTML具备超强的表现力，并且，服务器端升级后，客户端无需任何部署就可以使用到新的版本，因此，BS架构迅速流行起来。

5. 今天，除了重量级的软件如Office，Photoshop等，大部分软件都以Web形式提供。比如，新浪提供的新闻、博客、微博等服务，均是Web应用。

6. Web应用开发可以说是目前软件开发中最重要的部分。Web开发也经历了好几个阶段：

7. 静态Web页面：由文本编辑器直接编辑并生成静态的HTML页面，如果要修改Web页面的内容，就需要再次编辑HTML源文件，早期的互联网Web页面就是静态的；

8. CGI：由于静态Web页面无法与用户交互，比如用户填写了一个注册表单，静态Web页面就无法处理。要处理用户发送的动态数据，出现了Common Gateway Interface，简称CGI，用C/C++编写。

9. ASP/JSP/PHP：由于Web应用特点是修改频繁，用C/C++这样的低级语言非常不适合Web开发，而脚本语言由于开发效率高，与HTML结合紧密，因此，迅速取代了CGI模式。ASP是微软推出的用VBScript脚本编程的Web开发技术，而JSP用Java来编写脚本，PHP本身则是开源的脚本语言。

10. MVC：为了解决直接用脚本语言嵌入HTML导致的可维护性差的问题，Web应用也引入了Model-View-Controller的模式，来简化Web开发。ASP发展为ASP.Net，JSP和PHP也有一大堆MVC框架。

11. 目前，Web开发技术仍在快速发展中，异步开发、新的MVVM前端技术层出不穷。

12. 由于Node.js把JavaScript引入了服务器端，因此，原来必须使用PHP/Java/C#/Python/Ruby等其他语言来开发服务器端程序，现在可以使用Node.js开发了！

13. 用Node.js开发Web服务器端，有几个显著的优势：

14. 一是后端语言也是JavaScript，以前掌握了前端JavaScript的开发人员，现在可以同时编写后端代码；

15. 二是前后端统一使用JavaScript，就没有切换语言的障碍了；

16. 三是速度快，非常快！这得益于Node.js天生是异步的。

17. 在Node.js诞生后的短短几年里，出现了无数种Web框架、ORM框架、模版引擎、测试框架、自动化构建工具，数量之多，即使是JavaScript老司机，也不免眼花缭乱。

18. 常见的Web框架包括：Express，Sails.js，koa，Meteor，DerbyJS，Total.js，restify……

19. ORM框架比Web框架要少一些：Sequelize，ORM2，Bookshelf.js，Objection.js……

20. 模版引擎PK：Jade，EJS，Swig，Nunjucks，doT.js……

21. 测试框架包括：Mocha，Expresso，Unit.js，Karma……

22. 构建工具有：Grunt，Gulp，Webpack……

23. 目前，在npm上已发布的开源Node.js模块数量超过了30万个。

24. 有选择恐惧症的朋友，看到这里可以洗洗睡了。

25. 好消息是这个教程已经帮你选好了，你只需要跟着教程一条道走到黑就可以了。

### 自动化工具
1. 即将推出，请耐心等待。等待不耐烦的，请关注微博@廖雪峰

2. 
window.hurry = true;


## React
1. 即将推出，请耐心等待。等待不耐烦的，请关注微博@廖雪峰

2. 
window.hurry = true;


### 第一个React应用
1. New wiki page content

```
<!-- learn react -->
----
<html>
<head>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
</head>
<body>
    <div id="root"></div>
<script type="text/babel">

ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
);

</script>
</body>
</html>
```
### 元素渲染
1. New wiki page content

```
<!-- learn react -->
----
<html>
<head>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
</head>
<body>
    <div id="root"></div>
<script type="text/babel">

const clock = (
    // 一个React DOM元素只能有一个根元素，因此
    // <h1>和<p>必须用一个根元素包起来：
    <div>
        <h1>Clock</h1>
        <p>It is { new Date().toLocaleString() }</p>
    </div>
);

ReactDOM.render(
    clock,
    document.getElementById('root')
);

</script>
</body>
</html>
```
### 组件
1. New wiki page content

```
<!-- learn react -->
----
<html>
<head>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
</head>
<body>
    <div id="root"></div>
<script type="text/babel">

function Welcome(props) {
    return <h1>Hello, {props.name}</h1>
}

function App() {
    return (
        <div>
            <Welcome name="Bob"/>
            <Welcome name="Alice"/>
            <Welcome name="Tom"/>
        </div>
    )
}

ReactDOM.render(
    <App/>,
    document.getElementById('root')
);

</script>
</body>
</html>
```
### 组件和状态
1. New wiki page content

```
<!-- learn react -->
----
<html>
<head>
    <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
</head>
<body>
    <div id="root"></div>
<script type="text/babel">

class Welcome extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            date: new Date()
        }
    }

    render() {
        const
            hour = this.state.date.getHours(),
            hello = hour < 12 ? "Good morning" : (hour > 18 ? "Good afternoon" : "Good evening"),
            time = this.state.date.toLocaleTimeString();
        return (
            <div>
                <h1>{hello}, {this.props.name}</h1>
                <h2>It is {time}</h2>
            </div>
        );
    }
}

ReactDOM.render(
    <Welcome name="Bob"/>,
    document.getElementById('root')
);

</script>
</body>
</html>
```
## 期末总结
1. 即将推出，请耐心等待。等待不耐烦的，请关注微博@廖雪峰

2. 
window.hurry = true;
