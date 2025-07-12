interface Greeting {
    void greet();

    static void hello() {
        System.out.println("hello ji!!");
    }
}


class TestClass implements Greeting {
    @Override
    public void greet() {
        System.out.println("Greetings from TestClass!");
    }

}

public class AbstractionViaInterface {
    public static void main(String[] args) {
        TestClass obj = new TestClass();
        obj.greet();
        Greeting.hello();
    }
}
