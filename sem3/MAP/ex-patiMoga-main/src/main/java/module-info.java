module com.example.aparate {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;
    requires java.sql;

    opens com.example.aparate to javafx.fxml;
    exports com.example.aparate;
}