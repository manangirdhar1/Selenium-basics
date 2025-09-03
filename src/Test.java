//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Test {
    public static void main(String[] args) {
        String s1 = "abcdefgh";
        System.out.println(goodInteger("12223334567"));
    }

                public static String goodInteger(String num) {
                    String[] numbers = {"999","888","777","666","555","444","333","222","111","000"};
                    for (String s : numbers) {
                        if (num.contains(s)) {
                            return s;
                        }
                    }
                    return "";
                }
            }
            