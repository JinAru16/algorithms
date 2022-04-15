class SuperObj {
    public void show() {
        print();
    }
    public void print() {
        print();
        System.out.print("super");
    }
}

class SubObj extends SuperObj {
    public void show() {
        super.print();
    }
    public void prirnt() {
        System.out.print("Sub");
    }
}
    
public class jbcr {
    public static void main(String[] args) {
        SuperObj s = new SubObj();
        s.show();

    }
}
