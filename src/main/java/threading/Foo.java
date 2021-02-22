package threading;

public class Foo {

    private boolean firstDone;
    private boolean secondDone;
    private final Object lock = new Object();
    public Foo() {
        this.firstDone = false;
        this.secondDone = false;
    }

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        synchronized (this.lock) {
            this.firstDone = true;
            this.lock.notifyAll();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        synchronized (this.lock) {
            while (!this.firstDone) {
                this.lock.wait();
            }
            // printSecond.run() outputs "second". Do not change or remove this line.
            printSecond.run();
            this.secondDone = true;
            this.lock.notifyAll();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        synchronized (this.lock) {
            while (!this.firstDone || !this.secondDone) {
                this.lock.wait();
            }
            // printThird.run() outputs "third". Do not change or remove this line.
            printThird.run();
        }
    }
}
