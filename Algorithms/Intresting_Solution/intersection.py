def intersect(nums1, nums2):
    ret_list = []
    if (nums1 is None or nums2 is None):
        return ret_list
    
    nums1.sort() #Assume already sorted 
    nums2.sort()  #Assume already sorted
    
    i = 0
    j = 0
    
    while(i < len(nums1) and j < len(nums2)):
        if(nums1[i] == nums2[j]):
            ret_list.append(nums1[i])
            i += 1
            j += 1
        
        elif(nums1[i] > nums2[j]):
            j += 1
        
        elif(nums1[i] < nums2[j]):
            i += 1
            
    return ret_list

print(intersect([1,2,3,4],[1,1,4]))