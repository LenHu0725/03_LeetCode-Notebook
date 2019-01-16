������
��һ�������ַ������ݸ������������Դ������¡������ҽ��� Z �������С�
���������ַ���Ϊ "LEETCODEISHIRING" ����Ϊ 3 ʱ���������£�
L   C   I   R
E T O E S I I G
E   D   H   N
֮����������Ҫ�����������ж�ȡ��������һ���µ��ַ��������磺"LCIRETOESIIGEDHN"��
����ʵ��������ַ�������ָ�������任�ĺ�����
string convert(string s, int numRows);
ʾ�� 1:
	����: s = "LEETCODEISHIRING", numRows = 3
	���: "LCIRETOESIIGEDHN"
ʾ�� 2:
	����: s = "LEETCODEISHIRING", numRows = 4
	���: "LDREOEIIECIHNTSG"
	����:

	L     D     R
	E   O E   I I
	E C   I H   N
	T     S     G
������

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        node_length = 2*numRows - 2
        result = ""
        
        if str_length == 0 or numRows == 0 or numRows == 1:
            return s
        
        for i in range(numRows):
            for j in range(i, str_length, node_length):
                result += s[j]
                if i != 0 and i != numRows-1 and j-2*i + node_length < str_length:
                    result += s[j-2*i+node_length]  # �����е�����
        
        return result
