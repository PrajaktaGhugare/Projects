import java.util.Scanner;

class machine {

    public static int water = 400;
    public static int milk = 540;
    public static int beans = 120;
    public static int money = 550;
    public static int cup = 9;

    public machine() {
    }

    public static int getWater() {
        return water;
    }

    public static void setWater(int water) {
        machine.water = water;
    }

    public static int getMilk() {
        return milk;
    }

    public static void setMilk(int milk) {
        machine.milk = milk;
    }

    public static int getBeans() {
        return beans;
    }

    public static void setBeans(int beans) {
        machine.beans = beans;
    }

    public static int getMoney() {
        return money;
    }

    public static void setMoney(int money) {
        machine.money = money;
    }

    public static int getCup() {
        return cup;
    }

    public static void setCup(int cup) {
        machine.cup = cup;
    }
}

class coffee {

    public int water, milk, beans, cost;


    public coffee(int water, int milk, int beans, int cost) {
        this.water = water;
        this.milk = milk;
        this.beans = beans;
        this.cost = cost;
    }

    public int getWater() {
        return water;
    }

    public void setWater(int water) {
        this.water = water;
    }

    public int getMilk() {
        return milk;
    }

    public void setMilk(int milk) {
        this.milk = milk;
    }

    public int getBeans() {
        return beans;
    }

    public void setBeans(int beans) {
        this.beans = beans;
    }

    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }
}

public class CoffeeMachine {

    public static boolean status = true;
    public static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        new machine();

        while (status == true){

            System.out.println("Write action (buy, fill, take, remaining, exit):");
            String action = scanner.nextLine();

            switch (action){
                case "buy":
                    coffee_buy();
                    break;
                case "fill":
                    coffee_fill();
                    break;
                case "take":
                    take_money();
                    break;
                case "remaining":
                    coffee_remaining();
                    break;
                case "exit":
                    status = false;
                    break;
                default:
                    System.out.println("Wrong action!");
                    break;

            }
        }
    }

    private static void take_money() {
        machine.setMoney(0);
    }

    private static void coffee_fill() {
        System.out.println("Write how many ml of water you want to add:");
        int add_water = scanner.nextInt();
        machine.setWater(machine.getWater()+add_water);

        System.out.println("Write how many ml of milk you want to add:");
        int add_milk = scanner.nextInt();
        machine.setMilk(machine.getMilk()+add_milk);

        System.out.println("Write how many grams of coffee beans you want to add:");
        int add_beans = scanner.nextInt();
        machine.setBeans(machine.getBeans()+add_beans);

        System.out.println("Write how many disposable cups you want to add:");
        int add_cup = scanner.nextInt();
        machine.setCup(machine.getCup()+add_cup);
    }

    private static void coffee_remaining() {

        System.out.println("The coffee machine has:\n" +
                machine.getWater() + " ml of water\n" +
                machine.getMilk() + " ml of milk\n" +
                machine.getBeans() + " g of coffee beans\n" +
                machine.getCup() + " disposable cups\n" + "$" +
                machine.getMoney() + " of money\n");

    }

    private static void coffee_buy() {
        System.out.println("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:");

        String coffee_input = scanner.nextLine();
        coffee select_coffee = null;

        switch (coffee_input){
            case "1":
                select_coffee = new coffee(250,0,16,4);
                break;
            case "2":
                select_coffee = new coffee(350,75,20,7);
                break;
            case "3":
                select_coffee = new coffee(200,100,12,6);
                break;
            case "back":
                break;
            default:
                System.out.println("Wrong Input!");
                break;
        }

        if (select_coffee != null){
            check_coffee_remaining(select_coffee);
        }
    }

    private static void check_coffee_remaining(coffee selectCoffee) {
        if (machine.getWater() < selectCoffee.water){
            System.out.println("Sorry, not enough water!");
        } else if (machine.getMilk() < selectCoffee.milk){
            System.out.println("Sorry, not enough milk!");
        } else if (machine.getBeans() < selectCoffee.beans){
            System.out.println("Sorry, not enough coffee beans!");
        } else if (machine.getCup() < 1){
            System.out.println("Sorry, not enough cups!");
        } else {
            System.out.println("I have enough resources, making you a coffee!");
            machine.setWater(machine.getWater()-selectCoffee.water);
            machine.setMilk(machine.getMilk()-selectCoffee.milk);
            machine.setBeans(machine.getBeans()-selectCoffee.beans);
            machine.setCup(machine.getCup()-1);
            machine.setMoney(machine.getMoney()+selectCoffee.cost);
        }
    }
}