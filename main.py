class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """
        Перетворює бінарне дерево у рядок.

        Використовується прямий обхід дерева (Preorder):
        root -> left -> right.

        Для відсутніх вузлів записується "null".
        """

        result = []

        def preorder(node):
            if node is None:
                result.append("null")
                return

            result.append(str(node.val))

            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ",".join(result)


    def deserialize(self, data):
        """
        Відновлює бінарне дерево
        з рядка, отриманого функцією serialize().
        """

        if not data:
            return None

        values = data.split(",")
        index = 0

        def build():
            nonlocal index

            # Якщо всі елементи вже оброблені
            if index >= len(values):
                return None

            value = values[index]
            index += 1

            # "null" означає відсутній вузол
            if value == "null":
                return None

            # Створюємо новий вузол
            node = TreeNode(int(value))

            # Відновлюємо ліве піддерево
            node.left = build()

            # Відновлюємо праве піддерево
            node.right = build()

            return node

        return build()


# ==========================================
# ФУНКЦІЯ ДЛЯ ВИВЕДЕННЯ ДЕРЕВА
# ==========================================

def treeToList(root):
    """
    Перетворює бінарне дерево
    у список у форматі, схожому на LeetCode.
    """

    if root is None:
        return []

    result = []
    queue = [root]

    while queue:

        node = queue.pop(0)

        if node is None:
            result.append(None)
            continue

        result.append(node.val)

        queue.append(node.left)
        queue.append(node.right)

    # Видаляємо зайві None з кінця
    while result and result[-1] is None:
        result.pop()

    return result


# ==========================================
# ТЕСТУВАННЯ
# ==========================================

codec = Codec()


# ==========================================
# Приклад 1
# ==========================================
# Input:
# root = [1,2,3,null,null,4,5]
#
# Output:
# [1,2,3,null,null,4,5]

root1 = TreeNode(1)

root1.left = TreeNode(2)
root1.right = TreeNode(3)

root1.right.left = TreeNode(4)
root1.right.right = TreeNode(5)


# Серіалізація
serialized1 = codec.serialize(root1)

print("Приклад 1 — серіалізація:")
print(serialized1)


# Десеріалізація
restored1 = codec.deserialize(serialized1)

print("Приклад 1 — після десеріалізації:")
print(treeToList(restored1))


# Перевірка
print(
    "Перевірка:",
    treeToList(root1) == treeToList(restored1)
)


# ==========================================
# Приклад 2
# ==========================================
# Input:
# root = []
#
# Output:
# []

root2 = None

serialized2 = codec.serialize(root2)

print("\nПриклад 2 — серіалізація:")
print(serialized2)

restored2 = codec.deserialize(serialized2)

print("Приклад 2 — після десеріалізації:")
print(treeToList(restored2))

print(
    "Перевірка:",
    treeToList(root2) == treeToList(restored2)
)