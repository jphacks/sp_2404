# Mirodyssey

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2024/07/JPHACKS2024_ogp.jpg)](https://www.youtube.com/watch?v=DZXUkEj-CSI)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
- 休日あまり外出をしないインドア派にとって休日の終わりに感じるのは用事がないことからくる虚無感です。
- XなどのSNSで外出したことを写真などで投稿すると達成感や充足感が得られることに注目。
- 生成AIを用いて架空の外出した画像を生成し、休日の充足感も生成できるのではないかと考えたのがきっかけです。
### 製品説明（具体的な製品の説明）
- 本プロダクトは、画像生成AIを使用して投稿の説明文から自動的に最適な画像を生成。あたかも旅行に行ったかのような内容をシェアすることができます。
### 特長
#### 1. 高品質な画像生成
- Stable Diffusion 3.5 Large Turbo APIを使用し、高品質な画像生成を可能にしています。
#### 2. 快適なSNSライフを妨げない生成速度
- 後述する独自のプロンプト生成機構によって旅行写真に最適化された画像を高速で生成、待ち時間を削減。
#### 3. Djangoによるクロスプラットフォームの実現
- PCやスマートフォンなど、端末を選ばず利用可能です。開発保守も環境を選びません。
#### 4.PWAによるアプリ化
- インストール不要でネイティブアプリのように使うことが可能。

### 解決出来ること
- 日々の心に癒しを。新しいエンターテイメントの提供。
- インドア派の休日充足感の向上。
- 観光名所の魅力をこのプロダクトを通じて発見、実際に旅行に行くきっかけづくり。
- PWAとしてインストール不要でネイティブアプリのように使うことが可能。
### 今後の展望
- 基本的なCRUD機能の拡張、改善
- UIの改善
- ~~コメント機能の追加~~ 済
- いいねや他のSNSシェア機能などの拡張
- 文章校正LLMの導入
- 推論レベルでのさらなる最適化
- ~~さくらのクラウドへのデプロイ~~ 済
- 架空のコメントを投稿するBOTの実装
### 注力したこと（こだわり等）
- 文章の意図通りに正確に画像生成を行うための調整
- Docomo様のgooラボAPIを使用した日本語解析の生成プロンプトへの応用
- 画像生成速度の高速化

## 開発技術
### 活用した技術
#### API・データ
* Stable Diffusion 3.5 Large Turbo API
* Deepl API
* gooラボAPI(キーワード抽出API, 固有表現抽出API)

#### フレームワーク・ライブラリ・モジュール
* Django==5.0.6
* django-sslserver==0.22
* djangorestframework==3.15.1
* pillow==10.3.0
* python-dotenv==1.0.1
* mysqlclient==2.1.0
* django-bootstrap5==24.2
* django-bootstrap-icons==0.8.7

#### デバイス
* Ubuntu-22.04
* 

### 独自技術
#### ハッカソンで開発した独自機能・技術
* ユーザーの投稿説明文から生成プロンプトを作成する機能

### デモ・デモ動画リンク
* 動画リンクは以下
* https://youtu.be/FRivBcmhBeA
* 動作デモは以下で行えます(さくらのクラウドにデプロイ済、要ユーザ登録)
* http://163.43.218.62/users/register/
