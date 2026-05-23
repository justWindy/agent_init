
from dotenv import load_dotenv
from datetime import datetime
from typing import List
from hello_agents.tools import MemoryTool

load_dotenv()

def memory_tool_execute_demo():
	"""MemoryToolf方法演示"""
	print("MemoryTool基础操作演示")
	print("="*50)

	# init the memoryTool
	memroy_tool = MemoryTool(
		user_id="demo_user",
		memory_types=["working", "episodic", "semantic", "perceptual"],
	)

	print("MemoryTool init successfully")
	print("supported operations: add, search, summary, stats, update, remove, forget, consolidate, clear_all")

	return memroy_tool

def add_memory_demo(memroy_tool: MemoryTool):
	"""add memory demo"""
	print("\n添加记忆演示")
	print("-"*30)

	# add work memory
	result = memroy_tool.run({
		"action": "add",
		"memory_type": "working",
		"content": "正在学习HelloAgents框架的记忆系统",
		"importance": 0.7,
		"task_type": "learning"
	})
	print(f"工作记忆: {result}")

	# add the episodic memory
	result = memroy_tool.run({
		"action": "add",
		"memory_type": "episodic",
		"content": "HelloAgents是一个基于LangChain的Agent框架",
		"importance": 0.9,
		"task_type": "learning"
	})
	print(f"情景记忆: {result}")

	# 添加语义记忆
	result = memroy_tool.run({
		"action": "add",
		"content": "记忆系统包括工作记忆、情景记忆、语义记忆和感知记忆四种类型",
		"memory_type": "semantic",
		"importance": 0.9,
		"concept": "memory_types",
		"domain": "cognitive_science"
	})

	print(f"语义记忆: {result}")

	# 添加感知记忆
	result = memroy_tool.run({
		"action": "add",
		"memory_type": "perceptual",
		"content": "查看了记忆系统的架构图和实现代码",
		"importance": 0.6,
		"modality":"document",
		"source": "technical_documentation"
	})
	print(f"感知记忆: {result}")

def search_memory_demo(memory_tool: MemoryTool):
	"""搜索记忆演示 - 实现语义理解的检索"""
	print("\n搜索记忆演示")
	print("-"*30)

	# 基础搜索
	print("基础搜索 - '记忆系统':")
	result = memory_tool.run({
		"action": "search",
		"query": "记忆",
		"memory_type": "semantic",
		"limit": 3
	})
	print(result)

	# 按类型搜索
	print("\n按类型搜索 - 语义记忆中的'记忆':")
	result = memory_tool.run({
		"action": "search",
		"query": "记忆",
		"memory_type": "semantic",
		"limit": 2
	})
	print(result)

	# 设置重要性阈值
	print("\n高级重要性记忆搜索:")
	result = memory_tool.run({
		"action": "search",
		"query": "AI Agent",
		"importance_threshold": 0.7,
		"limit": 3
	})
	print(result)

def memory_summary_demo(memory_tool: MemoryTool):
	"""记忆摘要演示 - 提供系统全貌"""
	print("\n记忆摘要演示")
	print("-"*30)

	# 获取记忆摘要
	result = memory_tool.run({
		"action": "summary",
		"limit": 5
	})
	print("记忆摘要:")
	print(result)

	# 获取统计信息
	print("\n统计信息:")
	result = memory_tool.run({
		"action": "stats"
	})
	print(result)


def memory_management_demo(memory_tool: MemoryTool):
	"""记忆管理演示 - 删除特定记忆"""
	print("\n记忆管理演示")
	print("-"*30)

	# 添加一个低重要性记忆用于遗忘测试
	memory_tool.run({
		"action": "add",
		"content": "这是一个临时的测试记忆，重要性很低",
		"memory_type": "working",
		"importance": 0.1
	})

	# 基于重要性遗忘
	print("基于重要性的遗忘(阈值=0.2):")
	result = memory_tool.run({
		"action": "forget",
		"startegy": "importance_based",
		"threshold": 0.2
	})
	print(result)

	# 记忆整合 - 将重要的工作记忆转为情景记忆
	print("\n记忆整合(working -> episodic):")
	result = memory_tool.run({
		"action": "consolidate",
		"from_type": "working",
		"to_type": "episodic",
		"importance_threshold": 0.6
	})
	print(result)

def main():
	"""主函数"""
	print("MemoryTool基础操作演示完成")
	print("展示记忆系统的核心功能和操作方法")
	print("="*60)

	try:
		# 1. init memory tool
		memory_tool = memory_tool_execute_demo()

		# 2. add the memory demo
		add_memory_demo(memory_tool)

		# 3. search the memory
		search_memory_demo(memory_tool)

		# 4. summary the memory
		memory_summary_demo(memory_tool)

		# 5. manage the memory
		memory_management_demo(memory_tool)

		print("\n" + "="*60)
		print("MemoryTool基础操作演示完成!")
		print("="*60)

		print("\n演示的核心功能:")
		print("1. 四种记忆类型的添加和管理")
		print("2. 智能语义搜索和过滤")
		print("3. 记忆摘要和统计分析")
		print("4. 记忆整合和选择性遗忘")

		print("\n设计特点:")
		print("* 统一的execute接口，操作简洁一致")
		print("* 丰富的元数据支持，便于分类和检索")
		print("* 智能的重要性评估和时间衰减机制")
		print("* 模拟人类认知的记忆管理策略")

	except Exception as e:
		print(f"\n演示过程中发生错误: {e}")
		import traceback
		traceback.print_exc()

if __name__ == "__main__":
	main()










