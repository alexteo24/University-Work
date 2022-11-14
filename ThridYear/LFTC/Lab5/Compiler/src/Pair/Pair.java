package Pair;

public class Pair<K extends Comparable<K>, V> implements Comparable<Pair<K, V>> {
    private final K key;
    private final V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    @Override
    public int compareTo(Pair<K, V> o) {
        return this.key.compareTo(o.key);
    }

    @Override
    public String toString() {
        return "Pair.Pair{" +
                "key=" + key +
                ", value=" + value +
                '}';
    }

    public V getValue() {
        return value;
    }
}
