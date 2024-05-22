import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;
import java.io.*;
import java.nio.file.*;


public class shiyan {
    double a;
    double b;
    double c;

    public shiyan(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public void print_shiyan() {
        System.out.println(this.a);
        System.out.println(this.b);
        System.out.println(this.c);
    }

    public double zhouchang() {
        return this.a + this.b + this.c;
    }

    public double mianji() {
        double p = this.zhouchang() / 2.0;
        return Math.sqrt(p * (p - this.a) * (p - this.b) * (p - this.c));
    }

    public boolean is_sanjiaoxing() {
        double max1 = Math.max(this.a, this.b);
        max1 = Math.max(max1, this.c);
        double duan = this.zhouchang() - max1;
        return duan > max1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        shiyan shiyan1 = new shiyan(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());
        shiyan1.print_shiyan();
        double b = shiyan1.zhouchang();
        double d = shiyan1.mianji();
        System.out.printf("zhouchang:%.2f\n", b);
        System.out.printf("mianji:%.2f\n", d);
        System.out.printf("is_sanjiaoxing:%b\n", shiyan1.is_sanjiaoxing());
        Path path1 = Paths.get("D:\\Student\\file1");
        path1 = Files.createDirectories(path1);
        file = Files.createFile(path1);
    }

}