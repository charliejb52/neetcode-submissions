func hasDuplicate(nums []int) bool {
	counts := make(map[int]struct{})

	for i := 0; i < len(nums); i++ {
		if _, ok := counts[nums[i]]; ok {
			return true
		} else {
			counts[nums[i]] = struct{}{}
		}
	}

	return false
}
