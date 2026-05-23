"""BFCL评估工具

Berkeley Function Calling Leaderboard (BFCL) 一键评估工具

本工具封装了完整的BFCL评估流程：
1. 自动检查和准备BFCL数据
2. 运行HelloAgents评估
3. 导出BFCL格式结果
4. 调用BFCL官方评估工具（可选）
5. 生成评估报告

使用示例：
    from hello_agents import SimpleAgent, HelloAgentsLLM
    from hello_agents.tools.builtin import BFCLEvaluationTool

    # 创建智能体
    llm = HelloAgentsLLM()
    agent = SimpleAgent(name="TestAgent", llm=llm)

    # 创建评估工具
    bfcl_tool = BFCLEvaluationTool()

    # 运行评估（默认会运行BFCL官方评估）
    results = bfcl_tool.run(
        agent=agent,
        category="simple_python",
        max_samples=5
    )

    print(f"准确率: {results['overall_accuracy']:.2%}")
    # 报告自动生成到: evaluation_reports/bfcl_report_{timestamp}.md
"""

