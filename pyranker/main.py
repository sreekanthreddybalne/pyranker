import string
from typing import List, Union

def get_next_rank(rank: str, letters: Union[str, List] =string.ascii_lowercase, is_sorted=False):
    """
    returns the next possible string
    """
    if type(letters) is not list and not is_sorted:
        letters = sorted(set(letters))
    if not rank:
        return letters[0]
    letters_next_dict = {key: letters[idx+1] if idx!=len(letters)-1 else None for idx, key in enumerate(letters)}
    rank = list(rank)
    index = -1
    while not letters_next_dict[rank[index]]:
        index = index-1
        if index ==-1* len(rank)-1:
            rank.append(letters[0])
            return "".join(rank)
    if letters_next_dict[rank[index]]:
        rank[index] = letters_next_dict[rank[index]]
        return "".join(rank)

def get_previous_rank(rank: str, letters: Union[str, List] =string.ascii_lowercase, is_sorted=False, min_length=5):
    """
    returns the next possible string
    """
    if type(letters) is not list and not is_sorted:
        letters = sorted(set(letters))
    if not rank:
        return letters[0]*min_length
    letters_prev_dict = {key: letters[idx-1] if idx>0 else None for idx, key in enumerate(letters)}
    rank = list(rank)
    index = -1
    print(letters_prev_dict)
    while not letters_prev_dict[rank[index]]:
        index = index-1
        if index ==-1* len(rank)-1:
            rank.append(letters[0])
            return "".join(rank)
    if letters_prev_dict[rank[index]]:
        rank[index] = letters_prev_dict[rank[index]]
        return "".join(rank)

def get_rank(rank: str=None, next_rank:str =None, letters: str = string.ascii_lowercase, start_length=5):
    """
    returns the next possible string between two strings
    """
    letters = sorted(set(letters))
    if next_rank and (not rank or len(rank) < len(next_rank)):
        if next_rank[-1]>letters[1]:
            new_rank = get_previous_rank(next_rank, letters, is_sorted=True)
        else:
            new_rank = next_rank[:-1]+letters[0]+letters[len(letters)//2]
    elif not rank and not next_rank:
        new_rank = letters[len(letters)//2]*start_length
    else:
        new_rank = get_next_rank(rank, letters, is_sorted=True)
    if next_rank and new_rank==next_rank:
        new_rank = rank+letters[len(letters)//2]
    return new_rank


if __name__=="__main__":
    print(get_rank("nnnnnpl", next_rank="nnlao", start_length=20))
    