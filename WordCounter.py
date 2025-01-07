essay = open("essay.txt",  encoding="utf8")
wordcount = 0
reference_count = 0
ref_exclude = 0
currently_reference = False
current_reference = ""
excluded = ""
for index, x in enumerate(essay):
    if x.find("Bibliography") == -1 and x.find("bibliography") == -1 and x.find("References") == -1 and x.find("references") == -1:
        
        # count each word
        #if word starts with (, if this word or a following word ends with , 
        # and a following word is a year ending with ),
            # do not include these words in the wordcount
        sentence = x.split()
        for y in sentence:
            
            if currently_reference:
                if y.find(')') != -1:
                    if (y.startswith('1') or y.startswith('2')) and current_reference.find(',') != -1 :
                        reference_count += 1
                        ref_exclude = 0
                        currently_reference = False
                        current_reference += y
                        excluded += current_reference
                        current_reference = ""
                    else:
                        wordcount += ref_exclude
                        print(current_reference)
                        ref_exclude = 0
                        currently_reference = False
                        current_reference = ""
                else:
                    ref_exclude += 1
                    current_reference += y
                    

            elif y.startswith('('):
                if y.endswith(')'):
                    print(y)
                    wordcount += 1
                else:
                    currently_reference = True
                    ref_exclude = 1
                    current_reference = y

            else:
                print(y)
                wordcount += 1
    
    else:
        break

print(f"Wordcount is: {wordcount} reference count is: {reference_count}")
print(excluded)





    

