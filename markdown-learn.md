Markdown 语法练习
----------------
https://guides.github.com/features/mastering-markdown

# HEADERS（标题）
标题级别一共有6级
```Markdown
 # This is a headline 1
 ## This is a headline 2
 ###### This is a headline 6 
```

# EMPHASIS（强调）

斜体

*This text will be italic*
_This will also be italic_

加粗

**This text will be bold**
__This will also be bold__

斜体及加粗

*You **can** combine them*

#  BLOCKQUOTES（引用）
As Grace Hopper said:

> I've always been more interested
> in the future than in the past.

#  LISTS（列表）
Unordered（无序）
* Item 1
* Item 2
* Item 3
  * Item 2a
  * Item 3b

Ordered（有序）
1. Item 1
2. Item 2
3. Item 3
  * Item 3a
  * Item 3b

# IMAGES（图片）
![Github Logo](/images/logo.png)

Format: ![Alt Text](url)

# LINKS（连接）

http://github.com - automatic!

# BACKSLASH ESCAPES（反斜杠转义）

\*literal asterisks\*

# USERNAME @MENTIONS（用户名）
Typing an @ symbol, followed by a username, will notify that person to come and view the comment. This is called an "@MENTIONS", because you're mentioning the individual. You can also @MENTIONS teams within an organization.

# ISSUE REFERENCES（注脚）
Any number that refers to an Issue or Pull Request will be automatically converted into a link.

#1
github-flavored-markdown#1
defunkt/git-flavored-markdown#1

# EMOJI（绘文字）
To see a list of every image we support, check out

http://www.emoji-cheat-sheet.com 

Github supports emoji!

:+1: :sparkles: :camel: :tada:
:rocket: :metal: :octocat:

# FENCED CODE BLOCKS（受保护代码块） 
Markdown coverts text with four leading spaces into a code block; with GFM you can wrap your code with ``` to create a code block without the leading spaces. Add an optional language identifier and you code will get syntax highlighting.

```javascript
function test() {
  console.log("look ma', no spaces");
}
```
```python
print("Hello, world")
```

# TASK LISTS（任务清单）
- [x] this is a complete item
- [ ] this is an incomplete item 
- [x] @mentions, #refs, [links](),
**formatting**, and <del>tag</del>
supported
- [x] list syntax required (any unordered or ordered list supported)

# TABLES（表格）
You can create tables by assembling a list of words and dividing them with hyphens - (for the first row), and then separating each column with a pipe | :

First Header | Second Header
------------ | -------------
Content cell 1 | Content cell 2  
Content column 1 | Content column 2   

# Other Pages
https://help.github.com/articles/basic-writing-and-formatting-syntax/

# Quoting text（引用文本）
You can quote text with a `>`.

In the words of Abraham Lincoln:
> Pardon my French

# Quoting code（引用代码）

You can call out code or a command within a sentence with single cackitcks. The text within the backticks will not be formatted.

use `git status` to list all new or modified files that haven't yet been committed.

To format code or text into its own distinct block, use triple backticks.

Some basic Git commands are:
```
git status
git add
git commit
```

# Links（链接）

You can create an inline link by wrapping link text in bracket `[ ]`, and then wrapping the URL in parentheses `( )`. You can also use the keyboard shortcut `command + k` to create a link.

This site was built using [Github Pages](https://pages.github.com/).

# Relative links（相关链接）
（可以链接文件）
[contribution guideline for this project](docs/CONTRIBUTING.md)

# Lists（列表）

You can make a list by preceding one or more lines of text with `-` or `*`.

# Nested Lists（嵌套列表）

1. First list item in first line.
   - First nested list item 
     - Second nested list item 
