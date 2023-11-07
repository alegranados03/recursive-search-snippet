from collections import defaultdict
# 1->2,3,4->5,6,7,8,9,10,11,12,13->14,15,16
# 30->31,32,33->34,35,36
folders_data = [
    {'id': 1, 'name': 'Root', 'parent_id': None},
    {'id': 2, 'name': 'Child 1', 'parent_id': 1},
    {'id': 3, 'name': 'Child 2', 'parent_id': 1},
    {'id': 4, 'name': 'Child 3', 'parent_id': 1},
    {'id': 5, 'name': 'Subchild 1-1', 'parent_id': 2},
    {'id': 6, 'name': 'Subchild 1-2', 'parent_id': 2},
    {'id': 7, 'name': 'Subchild 1-3', 'parent_id': 2},
    {'id': 8, 'name': 'Subchild 2-1', 'parent_id': 3},
    {'id': 9, 'name': 'Subchild 2-2', 'parent_id': 3},
    {'id': 10, 'name': 'Subchild 2-3', 'parent_id': 3},
    {'id': 11, 'name': 'Subchild 3-1', 'parent_id': 4},
    {'id': 12, 'name': 'Subchild 3-2', 'parent_id': 4},
    {'id': 13, 'name': 'Subchild 3-3', 'parent_id': 4},
    {'id': 14, 'name': 'Sub-subchild 1-1-1', 'parent_id': 5},
    {'id': 15, 'name': 'Sub-subchild 1-1-2', 'parent_id': 5},
    {'id': 16, 'name': 'Sub-subchild 1-1-3', 'parent_id': 5},
    {'id': 30, 'name': 'Root2', 'parent_id': None},
    {'id': 31, 'name': 'Child 2-1', 'parent_id': 30},
    {'id': 32, 'name': 'Child 2-2', 'parent_id': 30},
    {'id': 33, 'name': 'Child 2-3', 'parent_id': 30},
    {'id': 34, 'name': 'Subchild 2-1-1', 'parent_id': 31},
    {'id': 35, 'name': 'Subchild 2-1-2', 'parent_id': 31},
    {'id': 36, 'name': 'Subchild 2-1-3', 'parent_id': 31},
]
#build tree nodes and leafs
tree = defaultdict(list)
for folder in folders_data:
    tree[folder['parent_id']].append(folder)


#first approach
def search_child_path(tree,ids_to_visit, result_id_list):
    new_visits = []
    for _id in ids_to_visit:
        for subfolder in tree[_id]:
            new_visits.append(subfolder["id"])
            result_id_list.append(subfolder["id"])
    return search_child_path(tree,new_visits,result_id_list) if len(new_visits) > 0 else []
 

#second approach
def recursive_folder_id_search(tree,starting_point):
    if starting_point not in tree:
        return []
    subfolders = tree[starting_point]
    result_id_list = [folder['id'] for folder in subfolders]
    for subfolder in subfolders:
        result_id_list.extend(recursive_folder_id_search(tree, subfolder['id']))

    return result_id_list


# calls

#first approach
ids_to_visit = [30]
result_id_list = []
result_id_list.extend(ids_to_visit)
result_id_list.extend(search_child_path(tree, ids_to_visit, result_id_list))
print(result_id_list) #should print 30,31,32,33,34,35,36

#second approach
arr=[30]
arr.extend(recursive_folder_id_search(tree,arr[0]))
print(arr) # should print 30,31,32,33,34,35,36

