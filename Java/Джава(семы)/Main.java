package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

            Scanner scan = new Scanner(System.in);
            System.out.println("Введите а:");
            double a = scan.nextDouble();
            System.out.println("Введите b:");
            double b = scan.nextDouble();
            System.out.println("Введите ha:");
            double ha = scan.nextDouble();
            Trapezia l1 = new Trapezia();

            double t1 = l1.Trap(a, b, ha);
            System.out.println("Ответ " + t1);
            more();

        }

    public static void more() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("do u want again? If NO print 'exit' ");
        String input = scanner.nextLine();
        if (input.equals("exit")) {
        } else {
            main();
        }
    }

        private static void main(){
            Scanner scan = new Scanner(System.in);
            System.out.println("Введите а:");
            double a = scan.nextDouble();
            System.out.println("Введите b:");
            double b = scan.nextDouble();
            System.out.println("Введите ha:");
            double ha = scan.nextDouble();
            Trapezia l1 = new Trapezia();

            double t1 = l1.Trap(a, b, ha);
            System.out.println("Ответ " + t1);
            more();
        }


    }
class Trapezia {


    //      {Функция, площадь которой нужно вычислить}
    public double f(double x) {
        double F=x*x+(Math.sin(2*x))+x-3;
        return F;
    }


    public double Trap(double a,double b, double h){
        double result=0;
        int n = (int)((b-a)/h);
        result += (f(a)+f(b))/2;
        for(int i = 1; i < n; i++)
            result += f(a + h*i );
        return h*result;
    }
    }