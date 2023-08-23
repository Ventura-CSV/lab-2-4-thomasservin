def main():
    #########################################

    # Complete your code here

    #########################################
    original_str = 'Python Programming'
    index_slicing = 7

    sub1 = original_str[:index_slicing]
    sub2 = original_str[index_slicing:]
    merge_str = sub2 + sub1
    
    print(sub2)
    print(sub1)
    print(merge_str)
pass
if __name__ == '__main__':
    main()