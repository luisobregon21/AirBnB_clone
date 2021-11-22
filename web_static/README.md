# 0x01. AirBnB clone - Web static

## Web static, what?

The first step is to “design” / “sketch” / “prototype” each element:

Create simple HTML static pages
Style guide
Fake contents
No Javascript
No data loaded from anything

## HTML 
HTML is the structure of your page, it should be the first thing to write. (Gives content structure and meaning to a page).

**Defines:** headers, images, paragraphs ...
### Documment type
```HTML
<!DOCTYPE html>
```
**Elements** define structures and contents of objects within a page.
```HTML
<h1> to <h6> [are the the levels of heading]
<p> are paragraphs

Elements are surrounded with a left (<) and right angle bracket (>).
```

**Tags**  are the less-than and greater-than angle brackets that surround an element.
**Attributes** add additional info about an element. 

![html](https://learn.shayhowe.com/assets/images/courses/html-css/building-your-first-web-page/html-syntax-outline.png)

### Most common properties of HTML
|   Name  | description  |
| ------- | ------------ |
| **id** | Identifies an element |
|**class** | classifies an element.|
|**src**| specifies a source embeddable content.|
|**href** | hyperlink reference to link source |

### Self-closing Elements
```HTML
<br>
<img>
<hr>
<meta>
<wbr>
<link>
<source>
<embedded>
<input>
<param>
```

## HTML CODE SAMPLE
```HTML
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>AirBnB clone</title>
  </head>
  <body>
    <footer>
			<p>Best School</p>
    </footer>
  </body>
</html>
```

## CSS
CSS is the styling of your page, the design. . Without any structure, you can’t apply any design. It is a presentational language. 

**Examples:** Fonts, colors


**Selectors** designate which element(s) to edit styles...
 ``` for example, to target all  <p> in CSS would be:  p{...} ```
**Type Selectors** target elements by their type
```
In CSS:
div{...}

In HTML:
<div>...</div>
<div>...</div>
```

**Class selectors** select elements based on class attributes.
```
In CSS:
.class_name{...}

In HTML:
<div class="class_name">...</div>
<p class="class_name">...</p>
```
** ID selectors** are more precise than class selectors. They use id attribute as the selector.
```
 In CSS:
#id_name{...}

In HTML:
<div id="id_name">...</div>
```
**Properties** decides the style that will be applied to selected element. (what goes in side the brackets).
**Values** are the behavior that the property will have. 

![CSS](https://learn.shayhowe.com/assets/images/courses/html-css/building-your-first-web-page/css-syntax-outline.png)

## Reference to CSS in HTML file
```HTML
<head>
		<meta charset="utf-8">
		<title>AirBnB clone</title>	
		<link rel="stylesheet" href="styles/2-header.css">
	</head>
```

## CSS sample
```CSS
header {
	background-color: #FF0000;
	height: 70px;
	width: 100%;
}
```
