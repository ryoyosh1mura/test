# git-svn 使い方


## cloneからbranch作成&同期まで
- cloneする
```sh
git svn clone -s https://svn.example.com/repo
```

- svn上にブランチを作成する
```sh
svn copy https://svn.example.com/repo/trunk \
         https://svn.example.com/repo/branches/sample \
        - m "サンプルブランチ作成"
```

- git側でsvnの最新ブランチ情報を取得 
```sh
git svn fetch
```

- ブランチが作成できているか確認する
```sh
git branch -r
```
`origin/trunk`
`origin/sample`
になってる？

- git側にsampleブランチを作る
```sh
git checkout -b sample origin/sample
```

- svnに変更を反映 
```sh
git svn dcommit
```

## svnの変更をgitへマージ

- svnの最新を取得
```sh
git checkout master
git svn rebase
```

- sampleにtrunkの変更をマージしたい場合
```sh
git checkout sample
git merge mater # コンフリクト起きたら解消して

# svnにも反映したい場合
git svn dcommit
```