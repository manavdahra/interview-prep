package algo;

import java.util.*;
import java.util.stream.Collectors;

public class HotelReviews {

    public static void main(String[] args) {
        Set<String> query = new HashSet<>(Arrays.asList("good", "shit"));
        Map<String, List<String>> reviews = new HashMap();
        reviews.put("1", new ArrayList(Arrays.asList("good", "great", "awesome", "good")));
        reviews.put("2", new ArrayList(Arrays.asList("nasty", "shit", "disgusting")));
        reviews.put("3", new ArrayList(Arrays.asList("moderate", "good", "shit")));

        List<Rating> ratings = sortHotelRatings(reviews, query);

        System.out.println(ratings);
    }

    /**
     * Filtered reviews based on words we are looking for
     * @param reviews
     * @return
     */
    private static List<Rating> sortHotelRatings(Map<String, List<String>> reviews, Set<String> words) {
        List<Rating> sortedHotels = new ArrayList<>();
        for (Map.Entry<String, List<String>> review: reviews.entrySet()) {
            List<String> foundWords = review.getValue().stream().filter(words::contains).collect(Collectors.toList());
            sortedHotels.add(new Rating(review.getKey(), foundWords.size()));
        }
        sortedHotels.sort(new Comparator<Rating>() {
            @Override
            public int compare(Rating o1, Rating o2) {
                if (o1.reviewCount > o2.reviewCount) {
                    return -1;
                } else if (o1.reviewCount < o2.reviewCount) {
                    return 1;
                } else {
                    return o1.key.compareTo(o2.key);
                }
            }
        });

        System.out.println(sortedHotels);
        return sortedHotels;
    }

    private static class Rating {
        String key;
        Integer reviewCount;

        public Rating(String key, Integer reviewCount) {
            this.key = key;
            this.reviewCount = reviewCount;
        }

        @Override
        public String toString() {
            return "Rating{" +
                    "key='" + key + '\'' +
                    ", reviewCount=" + reviewCount +
                    '}';
        }
    }
}
