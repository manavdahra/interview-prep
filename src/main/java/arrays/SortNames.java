package arrays;

import java.util.*;

public class SortNames {

    public static void main(String[] args) {
        List<String> names = Arrays.asList("Luis", "Hector", "Selena", "Emmanuel", "Amish");

        Map<Character, String> map = new HashMap<>();
        for (String name: names) {
            map.put(name.charAt(0), name);
        }

        List<String> seq = null;
        for (String name: map.values()) {
            seq = new ArrayList<>();
            String s = name;
            seq.add(s);
            while ((s = map.getOrDefault(Character.toUpperCase(s.charAt(s.length() - 1)), null)) != null) {
                seq.add(s);
            }
            if (seq.size() == names.size()) {
                break;
            }
        }
        System.out.println(seq);
    }
}
