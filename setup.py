from setuptools import setup, find_packages

setup(
    name='dsss_homework_2',
    version='0.1',
    packages=find_packages(),  # 自动发现并包括所有子包
    url='https://github.com/liltan666/dsss_homework_2.git',
    license='MIT',
    author='Microsoft',
    author_email='contact@microsoft.com',  # 假设的邮箱，实际使用时需要替换为正确的邮箱
    description='A Python package for DSSS Homework 2.',  # 添加一句描述项目的简单说明
    long_description=open('README.md').read(),  # 添加长描述，通常是README文件的内容
    long_description_content_type='text/markdown',  # 指定长描述的格式是Markdown
    classifiers=[
        'Development Status :: 3 - Alpha',  # 根据项目的实际情况调整
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',  # 根据支持的Python版本调整
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='homework example project',  # 添加一些关键词，描述项目
    install_requires=[
        # 这里可以列出项目运行需要的依赖，例如:
        # 'numpy',
        # 'requests'
    ],
    python_requires='>=3.6',  # 指定支持的Python最低版本
)
entry_points={
    'console_scripts': [
        'math_quiz=math_quiz_module:main_function'
    ]
}
