/* The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator. */

// solution created by chatGPT

int numeratorProduct = 1;
        int denominatorProduct = 1;

        for (int numerator = 10; numerator < 100; numerator++) {
            for (int denominator = numerator + 1; denominator < 100; denominator++) {
                if (numerator % 10 == 0 && denominator % 10 == 0) {
                    continue; // Trivial example, skip it
                }

                double originalFraction = (double) numerator / denominator;

                int numeratorTensDigit = numerator / 10;
                int numeratorOnesDigit = numerator % 10;
                int denominatorTensDigit = denominator / 10;
                int denominatorOnesDigit = denominator % 10;

                if (numeratorTensDigit == denominatorOnesDigit && denominatorTensDigit != 0 && originalFraction == (double) numeratorOnesDigit / denominatorTensDigit) {
                    numeratorProduct *= numeratorOnesDigit;
                    denominatorProduct *= denominatorTensDigit;
                } else if (numeratorOnesDigit == denominatorTensDigit && denominatorOnesDigit != 0 && originalFraction == (double) numeratorTensDigit / denominatorOnesDigit) {
                    numeratorProduct *= numeratorTensDigit;
                    denominatorProduct *= denominatorOnesDigit;
                }
            }
        }

        int gcd = GCD(numeratorProduct, denominatorProduct);
        int lowestDenominator = denominatorProduct / gcd;

        Console.WriteLine(lowestDenominator);
    

    static int GCD(int a, int b) {
        return b == 0 ? a : GCD(b, a % b);
    }