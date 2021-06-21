public class ArthematicNo {
    static int inSequence(int A, int B, int C) {
        // code here
        if (C == 0 && A == B)
            return 1;
        if (C != 0 && (B - A) / C >= 0 && (B - A) % C == 0)
            return 1;
        return 0;
    }

    public static void main(String args[]) {
        // ArthematicNo a = new ArthematicNo();
        System.out.println(inSequence(1, 3, 2));
    }
}
