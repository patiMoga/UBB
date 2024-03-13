package entity;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TortTest {

    @Test
    void getTip() {
        Tort tort = new Tort(1, "Chocolate");
        assertEquals("Chocolate", tort.getTip());
    }

    @Test
    void setTip() {
        Tort tort = new Tort(1, "Chocolate");
        tort.setTip("Vanilla");
        assertEquals("Vanilla", tort.getTip());
    }

    @Test
    void testToString() {
        Tort tort = new Tort(1, "Chocolate");
        String resultToString = tort.toString();

        assertEquals("Tort{id=1, tip='Chocolate'}", resultToString);
    }

    @Test
    void modify() {
        Tort tort = new Tort(1, "Chocolate");
        tort.modify("Vanilla");
        assertEquals(tort.getTip(), "Vanilla");

    }

}