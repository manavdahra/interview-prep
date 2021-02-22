package threading;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Task {

    public static void main(String[] args) throws InterruptedException {
        Foo foo = new Foo();
        List<Thread> threads = new ArrayList<>();
        final Random random = new Random();
        final int[] sleeps = new int[3];
        sleeps[0] = random.nextInt(100);
        sleeps[1] = random.nextInt(100);
        sleeps[2] = random.nextInt(100);

        threads.add(new Thread(() -> {
            try {
                Thread.sleep(sleeps[0]);
                foo.first(() -> System.out.println("first"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }));
        threads.add(new Thread(() -> {
            try {
                Thread.sleep(sleeps[1]);
                foo.second(() -> System.out.println("second"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }));
        threads.add(new Thread(() -> {
            try {
                Thread.sleep(sleeps[2]);
                foo.third(() -> System.out.println("third"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }));

        for (Thread thread : threads) {
            thread.start();
        }

        for (Thread thread : threads) {
            thread.join();
        }
    }

}
