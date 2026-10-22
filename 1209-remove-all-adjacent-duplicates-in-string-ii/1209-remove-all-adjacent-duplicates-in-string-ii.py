class Solution:

  def removeDuplicates(self, s: str, k: int) -> str:
    st = []
    for c in s:
      st.append([c, st.pop()[1] + 1] if st and st[-1][0] == c else [c, 1])
      if st[-1][1] == k:
        st.pop()
    return "".join(c * cnt for c, cnt in st)