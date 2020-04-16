<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
    <div align="center">
      <h2>结算</h2>
      <%
    	Map<String, Integer> map1 = (Map<String, Integer>)session.getAttribute("map1");
      %>
      	
      	<table border="0" cellspacing="30">
          <tr>
            <th>商品名称</th>
            <th>数量</th>
            <th>总价</th>
          </tr>
          <tr>
          	<td>凤求凰</td>
            <td><%=map1.get("凤求凰") %></td>
            <td><%=map1.get("凤求凰") %>*1788</td>
          </tr>
          <tr>
          	<td>街头霸王</td>
            <td><%=map1.get("街头霸王")%></td>
            <td><%=map1.get("街头霸王")%>*788</td>
          </tr>
          <tr>
          	<td>地狱之眼</td>
            <td><%=map1.get("地狱之眼")%></td>
            <td><%=map1.get("地狱之眼")%>*1688</td>
          </tr>
          <tr>
          	<td>荣耀水晶</td>
            <td><%=map1.get("荣耀水晶") %></td>
            <td><%=map1.get("荣耀水晶") %>*2220</td>
          </tr>
		</table>
		<p>总金额：<%=map1.get("凤求凰")*1788+map1.get("街头霸王")*788+map1.get("地狱之眼")*1688+map1.get("荣耀水晶")*2220 %></p>
		<p><a href="buy.jsp">继续购买</a></p>
    </div>