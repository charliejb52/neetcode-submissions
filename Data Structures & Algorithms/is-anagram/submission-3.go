func isAnagram(s string, t string) bool {
	counts_1 := make(map[string]int)
	counts_2 := make(map[string]int)

	if len(s) != len(t) {
		return false
	}

	for i := 0; i < len(s); i++ {
		// add 1 to the count for current character in s
		if _, ok1 := counts_1[string(s[i])]; !ok1 {
			counts_1[string(s[i])] = 0
		}
		counts_1[string(s[i])]++

		// add 1 to the count for current character in t
		if _, ok2 := counts_2[string(t[i])]; !ok2 {
			counts_2[string(t[i])] = 0
		}
		counts_2[string(t[i])]++
	}

	// compare the contents of counts_1 to counts_2
	for key := range(counts_1) {
		if counts_1[key] != counts_2[key] {
			return false
		}
	}
	
	return true
}
