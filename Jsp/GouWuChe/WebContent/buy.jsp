<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>购物车</title>
</head>
<body>
<h2 align="center">商品列表</h2>
    <div align="center">
      <form action="processbuy.jsp" method="post">
        <table border="0" cellspacing="30">
          <tr>
            <th>商品名称</th>
            <th>购买</th>
            <th>价格</th>
          </tr>
          <tr>
          	<td>凤求凰</td>
            <td><input type="checkbox" name="item" value="fqh"></td>
            <td>￥1788</td>
          </tr>
          <tr>
          	<td>街头霸王</td>
            <td><input type="checkbox" name="item" value="jtbw"></td>
            <td>￥888</td>
          </tr>
          <tr>
          	<td>地狱之眼</td>
            <td><input type="checkbox" name="item" value="dyzy"></td>
            <td>￥1688</td>
          </tr>
          <tr>
          	<td>荣耀水晶</td>
            <td><input type="checkbox" name="item" value="rysj"></td>
            <td>￥2220</td>
          </tr>
		</table>
		
		<input type="submit" value="购买">      
      </form>
    </div>
</body>
</html>