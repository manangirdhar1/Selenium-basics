import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import java.util.List;

// page_url = about:blank?wi_0
public class Page {
    public Page(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }
}