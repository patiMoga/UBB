package configurations;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

public class ConfigReader {
    private static final String CONFIG_FILE = "C:\\Users\\Andrei2\\Desktop\\GIT\\sem3\\MAP\\ex-patiMoga-main\\src\\main\\java\\configurations\\settings.properties";
    private Properties properties = new Properties();

    public Map<String, String> config() {
        Map<String, String> elements = new HashMap<>();
        try (FileInputStream input = new FileInputStream(CONFIG_FILE)) {
            properties.load(input);

            String repositoryType = properties.getProperty("Repository");
            String patientsFile = properties.getProperty("Produs");

            elements.put("Repository", repositoryType);
            elements.put("Produs", patientsFile);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return elements;
    }
}
