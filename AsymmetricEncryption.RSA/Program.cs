

using System.Numerics;

public class EncryptMessage
{
    static void Main(string[] args)
    {
        while (true)
        {
            int n = 1024;
            long prime_candidate = getLowLevelPrime(n);
            if (isMillerRabinPassed(prime_candidate))
            {
                Console.WriteLine($"{n} bit prime is \n{prime_candidate}");
                break;
            }
        }

        /*
        Console.WriteLine("Digite a mensagem que deseja encriptografar");
        string messageToEncrypt = Console.ReadLine();
        string messageEncrypt = "";
        string messageToDecrypt = "";

        BigInteger n, d, e, p, q, m;

        int bitLength = 4096;

        Random valueRandom = new Random();

        BigInteger()

        p = new BigInteger(1, new Random().NextBytes());
        */
    }

    static int[] first_primes_list = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 
        83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 
        197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
        331, 337, 347, 349 };

    static long nBitRandom(int n)
    {
        var rand = new Random();

        // Returns a random number
        // between 2**(n-1)+1 and 2**n-1'''
        var twoBig = new BigInteger(2);
        var maxbi = twoBig.()


        BigInteger maxBig = new BigInteger(Math.Pow(2, n) - 1);
        BigInteger minBig = new BigInteger(Math.Pow(2, n - 1) + 1);

        long max = (long)Math.Pow(2, n) - 1;
        long min = (long)Math.Pow(2, n - 1) + 1;
        return rand.NextInt64(min, max + 1);
    }

    static long getLowLevelPrime(int n)
    {

        // Generate a prime candidate divisible
        // by first primes

        //  Repeat until a number satisfying
        //  the test isn't found
        while (true)
        {
            //  Obtain a random number
            long prime_candidate = nBitRandom(n);

            foreach (int divisor in first_primes_list)
            {
                if (prime_candidate % divisor == 0
                    && divisor * divisor <= prime_candidate)
                    break;
                //  If no divisor found, return value
                else
                    return prime_candidate;
            }
        }
    }

    static long expmod(long bayse, long exp, long mod)
    {
        if (exp == 0) return 1;
        if (exp % 2 == 0)
        {
            return (long)Math.Pow(expmod(bayse, (exp / 2), mod), 2) % mod;
        }
        else
        {
            return (bayse * expmod(bayse, (exp - 1), mod)) % mod;
        }
    }

    static bool trialComposite(long round_tester, long evenComponent,
                               long miller_rabin_candidate, int maxDivisionsByTwo)
    {
        if (expmod(round_tester, evenComponent, miller_rabin_candidate) == 1)
            return false;
        for (int i = 0; i < maxDivisionsByTwo; i++)
        {
            if (expmod(round_tester, (1 << i) * evenComponent,
                       miller_rabin_candidate) == miller_rabin_candidate - 1)
                return false;
        }
        return true;
    }

    static bool isMillerRabinPassed(long miller_rabin_candidate)
    {
        // Run 20 iterations of Rabin Miller Primality test

        int maxDivisionsByTwo = 0;
        long evenComponent = miller_rabin_candidate - 1;

        while (evenComponent % 2 == 0)
        {
            evenComponent >>= 1;
            maxDivisionsByTwo += 1;
        }

        // Set number of trials here
        int numberOfRabinTrials = 20;
        for (int i = 0; i < (numberOfRabinTrials); i++)
        {
            Random rand = new Random();
            long round_tester = rand.NextInt64(2, miller_rabin_candidate);

            if (trialComposite(round_tester, evenComponent,
                               miller_rabin_candidate, maxDivisionsByTwo))
                return false;
        }
        return true;
    }
}




