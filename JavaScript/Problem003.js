function isPrime2(num) {
    //    alert(num);
    if (isPrime.primeList.indexOf(num) != -1) return true;

    for (var i=2;i <= num/2;i++) {
	//alert('i = ' + i);
        if (isPrime(i)) {
	    if ( num % i == 0 ) {
		return false;
	    }
	}
    }
  
    isPrime.primeList.push(num); // cache results
    return true;
}
isPrime2.primeList = [2];


function lpf(num) {
    for (var i=2;i <= num/2;i++) {
        if (num % i == 0) {
	    if (isPrime(i)) {
		var largestPrime = i;
	    }
	}
    }
    if (!largestPrime) return num; //number is prime
    return largestPrime;
}

function allPrimes(limit) {

    var primes = [2];

    function isPrime(x) {
	for (var j in primes) {
	    if (x % primes[j] == 0) return false;
	}
	return true;
    }

    if (limit < 2) return null;
  
    for (var i=3; i <= limit; i += 2) {
	if (isPrime(i)) primes.push(i);
    }

    return primes;
}