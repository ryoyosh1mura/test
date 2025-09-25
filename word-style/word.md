# MarkdownをWordの代替として使えるかの検証

- pdf出力: [拡張機能で…](https://github.com/yzane/vscode-markdown-pdf/)

```markdown
# 第1章
## 1節
### １項
```
てな感じで書いていく。。？
以下はmarkdownでよく使うものの表示のされ方

(スタイルはcssでも変更可能っぽい)
```markdown
- リスト
- リスト2

> 引用
>
> abcabc
```
 
- リスト
- リスト2

> 引用
>
> abcabc
<div class="page"/>

以下はpdf出力の拡張機能のなかで必須機能を見ていく
## 改ページ
```html
<div class="page"/>
```
<div class="page"/>

## UML埋め込み
```markdown
@startuml
Bob -[#red]> Alice : hello
Alice -[#0000FF]->Bob : ok
@enduml
```
@startuml
Bob -[#red]> Alice : hello
Alice -[#0000FF]->Bob : ok
@enduml

## markdownのなかにmarkdownを挿入
(コードブロックの中にも表示されるっぽいね)
```markdown
:[Plugins](./src.md)
```

:[Plugins](./src.md)