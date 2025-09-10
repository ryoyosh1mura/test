---
marp: true
theme: custom_uncover
size: 16:9
paginate: true
footer: "aaaaaa"
header: "aa"
---

# theme:uncoverのカスタム

---
# メモ
- [フリー画像素材リンク](https://icon-design.jp/news/illustration-materials/)
![フリーイラスト](https://jp.freepik.com/icon/html-file_2786969#fromView=keyword&page=1&position=8&uuid=95ac8681-024c-4955-bac0-50cf6281b964)

---
# 段組みレイアウト(css必要)
<div class="flex fw">
<div style="--fw: 1; --bg-color:rgb(0,0,0);">

# a
</div>
<div style="--fw: 2; --bg-color:rgba(185, 6, 6, 1);">

# a
</div>
</div>

---
# 吹き出し
<p class="speechBubble left">aaa</p><br>
<p class="speechBubble right">aaa</p>

---
# 画像をボタンっぽい挙動へ
<img src="https://ryoyosh1mura.github.io/img/sample/setting.png" class="push">