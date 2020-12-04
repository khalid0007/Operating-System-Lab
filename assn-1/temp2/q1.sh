#!/home/khalid/os/a1
#/bin/bash
echo -e "Enter value of \"userv1\": \c"
read userv1

echo -e "Enter value of \"userv2\": \c"
read userv2

sum=$( expr "$userv1+$userv2" | bc )

if [ $? -eq 0 ]
then
	echo Addition of \"userv1\" and \"userv2\" is $sum
else
	echo Can not perform addition
fi	

mul=$( expr "$userv1*$userv2" | bc )


if [ $? -eq 0 ]
then
	echo Multiplication of \"userv1\" and \"userv2\" is $mul
else
	echo Can not perform multiplication
fi	

div=$( expr "scale=5;$userv1/$userv2" | bc )

if [ $? -eq 0 ]
then
	echo Division of \"userv1\" and \"userv2\" is $div
else
	echo Can not perform division
fi	


concat="${userv1}${userv2}"

if [ $? -eq 0 ]
then
	echo Concateration of \"userv1\" and \"userv2\" is $concat
else
	echo Can not perform concaternation
fi

word1="$userv1"
word2="$userv2"
if [ ${#word1} -lt ${#word2} ]
then
        word1="$2"
        word2="$1"
fi
for ((i=${#word2}; i>0; i--)); do
	for ((j=0; j<=${#word2}-i; j++)); do
  	if [[ $word1 =~ ${word2:j:i} ]]
    then
      	echo "Longest common substring of \"userv1\" and \"userv2\": " ${word2:j:i}
	exit
    fi
	done
done
