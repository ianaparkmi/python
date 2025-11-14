import matplotlib.pyplot as plt
import matplotlib.patches as patches

def owl():
     fig, ax = plt.subplots(figsize=(8, 8))
     ax.set_xlim(0,10)
     ax.set_ylim(0,10)
     ax.axis('off')

     ax.add_patch(plt.Circle((5,5), 3, fill=True, color='brown'))
     ax.add_patch(plt.Circle((4,6),1,fill=True, color='yellow'))
     ax.add_patch(plt.Circle((6, 6), 1, fill=True, color='yellow'))

     ax.add_patch(plt.Circle((4,6),0.4,fill=True, color='black'))
     ax.add_patch(plt.Circle((6, 6), 0.4, fill=True, color='black'))
     ax.add_patch(plt.Polygon([[5, 5], [4.5, 4.5], [5.5, 4.5]], facecolor='orange'))

     ax.add_patch(plt.Polygon([[4, 7.5], [3.5, 8.5], [4.5, 8]], facecolor='brown'))  
     ax.add_patch(plt.Polygon([[6, 7.5], [5.5, 8], [6.5, 8.5]], facecolor='brown'))

     ax.add_patch(plt.Rectangle((3.5, 2), 1, 0.5, facecolor='orange'))
     ax.add_patch(plt.Rectangle((5.5, 2), 1, 0.5, facecolor='orange'))
     plt.tight_layout()
     plt.show()
     print("owl was printed")

owl()
