import tkinter as tk

root = tk.Tk()
root.title('0-1背包问题')
root.geometry('800x500+100+100')

menu = tk.Menu(root,tearoff=False)

algo_menu = tk.Menu(menu,tearoff=False)#二级菜单
algo_menu.add_command(label='动态规划算法')
algo_menu.add_command(label='回溯算法')
algo_menu.add_command(label='贪心算法')
algo_menu.add_command(label='遗传算法')
menu.add_cascade(label='算法选择',menu=algo_menu)

other_menu = tk.Menu(menu,tearoff=False)#二级菜单
other_menu.add_command(label='散点图')
other_menu.add_command(label='排序')
menu.add_cascade(label='其他',menu=other_menu)

about_menu = tk.Menu(menu,tearoff=False)#二级菜单
about_menu.add_command(label='小组成员')
menu.add_cascade(label='关于',menu=about_menu)

status_str_var = tk.StringVar()
status_label = tk.Label(root,textvariable=status_str_var,bd=1,relief=tk.SUNKEN,anchor=tk.W)
status_label.pack(side=tk.BOTTOM,fill=tk.X)

var_line = tk.StringVar()
line_label = tk.Label(root,textvariable=var_line,width=1,bg='#faebd7',anchor=tk.N,font=18)
line_label.pack(side=tk.LEFT,fill=tk.Y)

text_pad = tk.Text(root,font=18)
text_pad.pack(fill=tk.BOTH,expand=True)

scroll = tk.Scrollbar(text_pad)
text_pad.config(yscrollcommand=scroll.set)
scroll.config(command=text_pad.yview)#下拉框与文本框绑定
scroll.pack(side=tk.RIGHT,fill=tk.Y)
root.config(menu=menu)

root.config(menu=menu)   #一级菜单
root.mainloop()

