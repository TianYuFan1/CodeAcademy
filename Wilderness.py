
class TreeNode:

    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while story_node.choices != []:
            choice = int(input("Enter 1 or 2 to continue the story: "))
            while choice not in [1, 2]:
                choice = int(input("Enter 1 or 2 to continue the story: "))
            choice += -1
            chosen_child = story_node.choices[choice]
            print(chosen_child.story_piece)
            story_node = chosen_child


print("One upon a time...")

root = """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""
choice_a = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
choice_b = """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
choice_a_1 = """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
choice_a_2 = """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
"""
choice_b_1 = """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""
choice_b_2 = """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""

story_root = TreeNode(root)
story_a = TreeNode(choice_a)
story_b = TreeNode(choice_b)
story_a_1 = TreeNode(choice_a_1)
story_a_2 = TreeNode(choice_a_2)
story_b_1 = TreeNode(choice_b_1)
story_b_2 = TreeNode(choice_b_2)

story_root.add_child(story_a)
story_root.add_child(story_b)
story_a.add_child(story_a_1)
story_a.add_child(story_a_2)
story_b.add_child(story_b_1)
story_b.add_child(story_b_2)
story_root.traverse()


