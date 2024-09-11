from src import question

def test_question_case1():    
    result = question.solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])
    assert result == 5

def test_question_case2():    
    result = question.solution(	[3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
    assert result == -1
    
def test_question_case3():    
    result = question.solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
    assert result == -1