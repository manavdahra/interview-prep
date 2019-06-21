package algo;

import java.util.*;

public class Hotels {

    public static void main(String[] args) {
        Map<String, List<String>> freq = new HashMap<>();
        updateFreq("u1", Arrays.asList("h2", "h3", "h1"), freq);
        updateFreq("u2", Arrays.asList("h2", "h5", "h3"), freq);
        updateFreq("u3", Arrays.asList("h7", "h3", "h1"), freq);

        System.out.println(freq);

        String mostVisited = null;
        int max = Integer.MIN_VALUE;
        for (Map.Entry<String, List<String>> e: freq.entrySet()) {
            if (max < e.getValue().size()) {
                max = e.getValue().size();
                mostVisited = e.getKey();
            }
        }
        System.out.println(mostVisited);
    }

    private static void updateFreq(String userId, List<String> hotels, Map<String, List<String>> freq) {
        for (String hotel: hotels) {
            List<String> userIds = freq.getOrDefault(hotel, new ArrayList<>());
            userIds.add(userId);
            freq.put(hotel, userIds);
        }
    }
}
