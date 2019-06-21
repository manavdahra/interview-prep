package algo;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class FileSystem {

    public static void main(String[] args) {
        List<File> allFiles = new ArrayList<>();
        allFiles("/Users/manav/interview-prep", allFiles);
        allFiles.sort(new Comparator<File>() {
            @Override
            public int compare(File o1, File o2) {
                if (o1.length() > o2.length()) {
                    return -1;
                } else if (o1.length() < o2.length()) {
                    return 1;
                } else {
                    return 0;
                }
            }
        });

        for (int i = 0; i < 5; i++) {
            System.out.println(allFiles.get(i).getAbsolutePath() + " " + allFiles.get(i).length());
        }
    }

    private static List<File> ls(String path) {
        File file = new File(path);
        File[] fs = file.listFiles();
        return (fs != null) ? Arrays.asList(fs) : null;
    }

    private static boolean isFile(File f) {
        return f.isFile();
    }

    private static void allFiles(String path, List<File> allFiles) {
        List<File> paths = ls(path);
        if (paths == null) {
            return;
        }
        for (File p: paths) {
            if (isFile(p)) {
                allFiles.add(p);
                continue;
            }

            allFiles(p.getPath(), allFiles);
        }
    }
}
