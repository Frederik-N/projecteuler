// // We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
//  for example, the 5-digit number, 15234, is 1 through 5 pandigital.

// // The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
// multiplier, and product is 1 through 9 pandigital.

// // Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

// // HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
// // solution

using System.Linq;

var maxProductNumber = 20000;
var sumNumbers = new List<int>();
for(var product1 = 1; maxProductNumber > product1; product1++) {
    for(var product2 = product1; maxProductNumber > product2; product2++) {
        var productCalc = product1 * product2;
        if(product1.ToString().Length + product2.ToString().Length + productCalc.ToString().Length != 9) {
            continue; // this does not have 9 numbers
        }
        var allNumbers = (product1.ToString() + product2.ToString() + productCalc.ToString())
        .ToCharArray()
        .Select(c => int.Parse(c.ToString())).OrderBy(c => c.ToString());
        var stringAllNumbers = "";
        foreach(var number in allNumbers) {
            stringAllNumbers = stringAllNumbers +number.ToString();
        }
        if(stringAllNumbers == "123456789") {
            if(!sumNumbers.Contains(productCalc)) {
            sumNumbers.Add(productCalc);
            }
        } else {
            continue;
        }
    }
}

var solution = sumNumbers.Sum(); // 1 is added instead of having it in code

Console.WriteLine("solution: " + solution);