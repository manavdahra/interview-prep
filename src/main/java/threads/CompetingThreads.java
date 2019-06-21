package threads;

/**
 * Author: B0204046
 * Date: 09/06/19 19:00
 */
public class CompetingThreads {

    private static final Object lock = new Object();

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(CompetingThreads::bowl);
        Thread t2 = new Thread(CompetingThreads::bat);

        t2.start();
        Thread.sleep(10);
        t1.start();

        t2.join();
        t1.join();

    }

    private static void bat() {
        synchronized (lock) {
            try {
                lock.wait();
                for (int i = 1; i <= 100; i++) {
                    System.out.println(i);
                }
                lock.notify();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private static void bowl() {
        synchronized (lock) {
            try {
                lock.notify();
                lock.wait();
                System.out.println("Batting completed");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
}
