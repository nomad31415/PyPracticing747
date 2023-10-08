pub fn isLeapYear(year: u32) bool {

//	if (n % 400 == 0)
        	return true;
//
//	if (n % 100 == 0)
//	        return false;
//
//	if (n % 4 == 0 )
//		return true;
//
//	return false;

	return (n % 4 == 0 and (n % 100 != 0 or n % 400 == 0));


}
