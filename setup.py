from setuptools import setup, find_packages

setup(
    name='math-quiz',
    version='0.1',
    description='A simple math quiz game',
    author='zeyu.tan',
    author_email='liltan0303@outlook.com',
    url='https://github.com/liltan666/dsss_homework_2.git',
    packages=find_packages(),
    install_requires=[
        'certifi==2024.8.30',
        'charset-normalizer==3.4.0',
        'docopt==0.6.2',
        'idna==3.10',
        'pipreqs==0.4.13',
        'requests==2.32.3',
        'urllib3==2.2.3',
        'yarg==0.1.10'
    ],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz:main'  # 假设 'math_quiz.py' 文件中有一个名为 'main' 的函数
        ]
    },
    license='MIT',  # 确认使用的许可证
    keywords='math game educational',  # 添加适用的关键词
    classifiers=[
        'Development Status :: 3 - Alpha',  # 根据实际开发状态调整
        'Intended Audience :: Education',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',  # 确认许可证类型
        'Programming Language :: Python :: 3',  # 确认支持的 Python 版本
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
