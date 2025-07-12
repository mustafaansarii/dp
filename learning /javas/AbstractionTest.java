abstract class Test {
    abstract void testMethod();

    static void testStaticMethod() {
        System.out.println("Static method in abstract class");
    }
}

class TestImplementation extends Test {
    @Override
    void testMethod() {
        System.out.println("Implementation of abstract method");
    }

    public static void main(String[] args) {
        Test test = new TestImplementation();
        test.testMethod();
        Test.testStaticMethod();

    }

    public class AbstractionTest {
        public static void main(String[] args) {
            TestImplementation testImpl = new TestImplementation();
            testImpl.testMethod();
            Test.testStaticMethod();
        }
    }}