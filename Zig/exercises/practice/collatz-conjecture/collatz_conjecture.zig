//pub fn steps(number: usize) anyerror!usize {
//    _ = number;
//    @compileError("please implement the steps function");
//}



pub const ComputationError = error{IllegalArgument,};

pub fn steps(number: usize) anyerror!usize {

    if (number < 1) return ComputationError.IllegalArgument;

    var count: usize = 0;
    var current: usize = number;

    while (current != 1) {
	if (current % 2 == 0) {
	    current /= 2;
	} else {
	    current = 3 * current + 1;
	}

	count += 1;
     }


    return count;
}



