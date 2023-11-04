const std = @import("std");

const LetterScore = struct {
    letter: u8,
        score: u32,
	};

const letterScores = [_]LetterScore{
		LetterScore{ .letter = 'A', .score = 1 },
	        LetterScore{ .letter = 'E', .score = 1 },
		LetterScore{ .letter = 'I', .score = 1 },
		LetterScore{ .letter = 'O', .score = 1 },
		LetterScore{ .letter = 'U', .score = 1 },
		LetterScore{ .letter = 'L', .score = 1 },
		LetterScore{ .letter = 'N', .score = 1 },
		LetterScore{ .letter = 'R', .score = 1 },
		LetterScore{ .letter = 'S', .score = 1 },
		LetterScore{ .letter = 'T', .score = 1 },
		LetterScore{ .letter = 'D', .score = 2 },
		LetterScore{ .letter = 'G', .score = 2 },

							    LetterScore{ .letter = 'B', .score = 3 },
							        LetterScore{ .letter = 'C', .score = 3 },
								    LetterScore{ .letter = 'M', .score = 3 },
								        LetterScore{ .letter = 'P', .score = 3 },

									    LetterScore{ .letter = 'F', .score = 4 },
									        LetterScore{ .letter = 'H', .score = 4 },
										    LetterScore{ .letter = 'V', .score = 4 },
										        LetterScore{ .letter = 'W', .score = 4 },
											    LetterScore{ .letter = 'Y', .score = 4 },

											         LetterScore{ .letter = 'K', .score = 5 },


												     LetterScore{ .letter = 'J', .score = 8 },
												         LetterScore{ .letter = 'X', .score = 8 },
													    
													        LetterScore{ .letter = 'Z', .score = 10 },
														    LetterScore{ .letter = 'Q', .score = 10 },
														    };

														    fn getScore(letter: u8) u32 {
														        for (letterScores) |item| {
															        if (item.letter == letter) {
																            return item.score;
																	            }
																		        }
																			    return 0;
																			    }

																			    pub fn score(word: []const u8) u32 {
																			        var total_score: u32 = 0;
																				    for (word) |raw_letter| {
																				            const letter = std.ascii.toUpper(raw_letter);
																					            total_score += getScore(letter);
																						        }
																							    return total_score;
																							    }




