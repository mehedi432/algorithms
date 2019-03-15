function linearSearch(Arr, x){
	let n = Arr.length;
	let i = 0;

	while(i < n){
		if (Arr[i] == x) return i;
		i += 1;
	}

	return -1;
}

let result = linearSearch([1, 2, 3, 5, 8, 13], 21);
console.log(result);

