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

def get_rank(rank: str, next_rank:str =None, letters: str = string.ascii_lowercase):
    """
    returns the next possible string between two strings
    """
    letters = sorted(set(letters))
    new_rank = get_next_rank(rank, letters, is_sorted=True)
    if next_rank and new_rank==next_rank:
        new_rank = rank+letters[0]
    return new_rank


if __name__=="__main__":
    print(get_rank("aaaa", "a"))
    