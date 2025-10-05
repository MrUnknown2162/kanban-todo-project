# Danh sách lưu trữ các công việc
tasks = []

def add_task(task_name):
    """Thêm công việc mới"""
    task = {
        "id": len(tasks) + 1,
        "name": task_name,
        "completed": False
    }
    #vui lòng push task vào danh sách
    # YOUR CODE HERE
    print(f"✅ Added task: {task_name}")

def list_tasks():
    """Hiển thị tất cả công việc"""
    if not tasks:
        print("📝 No tasks available")
        return
    
    print("📋 Task List:")
    for task in tasks:
        status = "✅" if task["completed"] else "⏳"
        print(f"{task['id']}. {task['name']} {status}")

def complete_task(task_id):
    """Đánh dấu công việc hoàn thành"""
    #PUSH YOUR CODE HERE


    pass

def delete_task(task_id):
    """Xóa công việc"""
    #PUSH YOUR CODE HERE


    pass

def get_task_stats():
    """Thống kê công việc"""
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    
    print(f"📊 Task Statistics:")
    print(f"   Total: {total}")
    print(f"   Completed: {completed}")
    print(f"   Pending: {pending}")

# Demo chương trình
def main():
    print("🚀 Welcome to Simple TODO Manager!")
    
    # Thêm một số task mẫu
    add_task("Learn Python basics")
    add_task("Practice with lists and dictionaries")
    add_task("Write first function")
    add_task("Handle exceptions properly")
    
    # Hiển thị danh sách
    list_tasks()
    
    # Hoàn thành một task
    
    # Hiển thị lại danh sách

    # Thống kê

    # Xóa một task
    
    # Hiển thị cuối cùng
    print("\n" + "="*30)
    list_tasks()
    get_task_stats()

# Chạy chương trình
if __name__ == "__main__":
    main()
