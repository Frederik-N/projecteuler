// Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

// 21 22 23 24 25
// 20  7  8  9 10
// 19  6  1  2 11
// 18  5  4  3 12
// 17 16 15 14 13

// It can be verified that the sum of the numbers on the diagonals is 101.

// What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

// solution
var solution = 1; // 1 is added instead of having it in code
var spiralSize = 1001;
for(var i = 2; i <= spiralSize*spiralSize; i++) {
    solution += IsDiagonalNumber(i, spiralSize);
}

int IsDiagonalNumber(int i, int spiralSize)
{
    // start with inner layer and work out
    for(var spiralLayer = 3; spiralLayer <= spiralSize; spiralLayer += 2) {
        var layerSum = spiralLayer*spiralLayer;
        if(layerSum >= i) {
            // this is the layer of the number
            for(var k = (spiralLayer-2)*(spiralLayer-2)+spiralLayer-1; k <= layerSum; k += spiralLayer -1) {
                if(i < k) {
                    return 0;
                }
                if(i == k) {
                    return k;
                }
            }
        } else {
            continue;
        }

    }
    return 0;
}

Console.WriteLine("solution: " + solution);
