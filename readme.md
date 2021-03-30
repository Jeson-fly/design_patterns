# 设计模式

### 一、创建型模式（5种）
    1-0. 简单工厂模式
    1-1. 工厂方法模式
    2. 抽象工厂模式
    3. 建造者模式
    4. 单例模式
    5. 原型模式（了解）  


### 二、结构型模型（7种）
    1. 适配器模式 
    2. 桥模式
    3. 组合模式
    4. 外观模式
    5. 代理模式  
    6. 装饰模式(了解)
    7. 享元模式(了解)
    
### 三、行为型模型（11种）
    1. 责任链模式
    2. 观察者模式（发布订阅）
    3. 策略模式
    4. 模板方法模式
    5. 解释器模式(了解)
    6. 命令模式（了解）
    7. 迭代器模式（了解）
    8. 中介者模式（了解）
    9. 备忘录模式（了解）
    10. 状态模式（了解）
    11. 访问者模式（了解）
    
___

#### 一 、 简单工厂模式

> 1 内容
> > 不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责产品类的实例

> 2 角色
> > 工厂角色（creater）
> > 抽象产品角色（product）
> > 具体产品角色（concrete product）

> 3 优点
> > 隐藏对象创建的细节；
> > 客户端不需要修改代码。

> 4 缺点
> > 违反了单一原则，将创建逻辑集中到一个工厂类中；
> > 当添加新产品时，需要修改工厂类代码，违反了开闭原则。

> 5 示例代码
>```python
> from abc import ABCMeta, abstractmethod
> # 抽象产品
> class Payment(metaclass=ABCMeta):
>     @abstractmethod    
>     def pay(self,money):
>         """"""
>
> # 具体产品
> class AliaPayment(Payment):
>     def pay(self,money):
>         print("支付宝支付：%s元"%money)
>
> class WechatPay(Payment):
>     def pay(self, money):
>         print("微信支付:%s元")
>
> # 工厂角色
> class PaymentFactory(object):
>     def creat_payment(self, method):
>         if method == "alia":
>             return AliaPayment()
>         elif method == "wechat":
>             return WechatPay()
>         else:
>             raise TypeError("No such payment name %s" % method)
> # 客户端
> p = 
>
>```
![简单工厂](./images/class_simple_factory.png)
![简单工厂](./images/simple_factory.png)

#### 二、工厂方法模式

> 1 角色
> > 抽象工厂角色；具体工厂角色；抽象产品角色、具体产品角色

> 5 示例代码
> ```python
> from abc import ABCMeta, abstractmethod
> # 抽象产品接口
> class Payment(metaclass=ABCMeta):
>    @abstractmethod
>    def pay(self, money):
>        """"""
>
> # 具体产品1
> class AliPay(Payment):
>    def pay(self, money):
>        print("支付宝支付：%s元" % money)
>
> # 具体产品2
> class WechatPay(Payment):
>    def pay(self, money):
>        print("微信支付：%s元"%money)
>
> #抽象工厂（接口）
> class PayFactory(metaclass=ABCMeta):
>    @abstractmethod
>    def creat_payment(self):
>        """"""
>
> # 具体工厂1
> class AliFactory(PayFactory):
>   def creat_payment(self):
>        return AliPay()
>
> # 具体工厂2
> class WechatFactory(PayFactory):
>    def creat_payment(self):
>        return WechatPay()
> 
> # 客户端
> p = AliFactory()
> p.creat_payment()
> t.pay()
>```
![工厂方法模式](images/class_factory.png)
![工厂方法模式](./images/factory.png)


#### 三、 抽象工厂模式


![抽象工厂](images/class_abstract.png)
![抽象工厂模式](abstract_factory.py)
#### 四、 建造者模式
1. 主要用于构建一些复杂的对象，这些对象内部构造顺序通常是稳定的，但对象内部的构建往往则是复杂多变的。
2. 角色
    - 抽象建造者（builder）
    - 具体建造者（concrete builder）
    - 指挥者（director）
    - 产品
3. 优点：
    - 客户端不必知道产品内部细节，产品的产生和产品的构建过程解耦，相同的构建过程可以创建不同种类的对象；
    - 客户端想要修改产品类别，只需要修改具体的产品建造者；
    - 增加新的具体构造者无需修改现有代码，扩展方便，符合“开闭原则”。
    
4. 缺点：
    - 使用范围有限制：使用建造者模式中，产品组成成分和构造过程相似，产品之间差别太大则不适合建造者模式
    - 如果产品内部变化比较负责，需要很多具体建造者来适应这种变化，导致建造类继承关系臃肿。
    
5. 适用场景
    - 需要生成的产品对象有复杂的内部结构，这些产品对象通常包含多个成员属性。
    - 需要生成的产品对象的属性相互依赖，需要指定其生成顺序。
    - 隔离复杂对象的创建和使用，并使得相同的创建过程可以创建不同的产品。
    
6. 应用实例 
    - 换装游戏中，给人物选择不同的帽子，上衣，裤子，鞋子，包包等
![建造者模式](./images/build.png)
      

#### 五、 单例模式
1. 保证一个类仅有一个实例，并提供一个访问它的全局访问点
2. 优点
    - 由于全局只有唯一实例，因此单例模式可以严格控制客户端的访问；
    - 由于系统内存中只存在一个对象，节省系统资源；对于频繁创建和销毁的对象，单例模式无疑可以提高系统性能。
    - 单例模式可以进一步进化为创建固定数目的实例（多例模式）。
3. 缺点：
    - 单例模式没有抽象层，扩展很困难（享元模式=多例模式+抽象层）
    - 单例类的职责过”重“，既当工厂类（提供工厂方法）有充当产品角色（提供产品的功能方法）
    - 注意线程安全

![单例模式](./images/singleton.png)


#### 六、 适配器模式
1. 特点

2. 优点：
   - 为复用现有的类与方法，通过引入Adapter将适配者与目标接口兼容，而不需要修改原有代码；
   - 增加适配者类的透明性，适配者类被封装在适配器类中，对客户端而言是透明的。
   - 灵活性和拓展性好，可以在不改变原有代码基础上增加新的适配器类，符合开闭原则。
3. 缺点：
   - 对于Java、C#等不支持多重继承的语言，一次最多只能适配一个适配者类 
     
4. 适用场景
   - 系统需要使用现有的类，而这些类的接口不符合系统的需要。
   - 在系统设计之初，需要使用第三方组件的地方可以使用适配器模式（该组件与系统的接口是不同的，而系统没有必要为了迎合它而改动自己的接口）

![适配器模式](./images/class_adapter.png)
![适配器模式](./images/adapter_model.png)
#### 七、 桥模式

![桥模式](./images/brigge_model.png)
#### 八、 组合模式
![组合模式](./images/class_compute.png)
![组合模式](./images/composite_mode.png)
#### 九、 外观模式
    1. 内容
       - 为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得子系统更加容易使用。
    2. 角色
       - 外观（facade）
       - 子系统类
![外观模式](./images/observe.png)
#### 十、 代理模式

![代理模式](./images/proxy_model.png)
#### 十一、责任链模式


![责任链模式](./images/responsibility_model.png)
#### 十二、 观察者模式

![观察者模式](./images/observe.png)
#### 十三、 策略模式

![策略模式](./images/strategy_model.png)

#### 十四、 模版方法模式


![模版方法](./images/template_model.png)