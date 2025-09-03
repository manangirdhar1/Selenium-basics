package com.example;

import com.epam.healenium.SelfHealingDriver;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.List;

public class AmazonWatchScraper {
    public static void main(String[] args) throws InterruptedException {
        // Setup ChromeDriver
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        options.addArguments("--disable-dev-shm-usage");
        options.addArguments("--no-sandbox");
        options.addArguments("--disable-gpu");
        options.addArguments("--start-maximized");

        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();

        try {
            driver.get("https://www.amazon.in/");
            driver.manage().window().maximize();

            // Search for watches
            WebElement searchBox = driver.findElement(By.id("twotabsearchtextbox"));
            searchBox.sendKeys("watches");
            driver.findElement(By.id("nav-search-submit-button")).click();

            Thread.sleep(3000); // wait for results to load

            // Locate first 10 watches
            List<WebElement> watchNames = driver.findElements(By.xpath("//div[@data-cy='title-recipe']"));
            List<WebElement> watchPrices = driver.findElements(By.xpath("//span[@class='a-price-whole']"));

            System.out.println("===== Top 10 Watches =====");
            for (int i = 0; i < 10 && i < watchNames.size() && i < watchPrices.size(); i++) {
                String name = watchNames.get(i).getText();
                String price = watchPrices.get(i).getText();
                System.out.println((i + 1) + ". " + name + " - ₹" + price);
            }
        } finally {
            driver.quit();
        }
    }
}
