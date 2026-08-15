class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix = [], ""
        for char in searchWord:
            prefix += char
            i = bisect_left(products, prefix)
            res.append([w for w in products[i : i + 3] if w.startswith(prefix)])
        return res