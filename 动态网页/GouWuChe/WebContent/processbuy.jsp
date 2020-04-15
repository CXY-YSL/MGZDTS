<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
	String path = request.getContextPath();
	String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
 
	request.setCharacterEncoding("utf-8");
	
	Map<String, Integer> map1 = (Map<String, Integer>)session.getAttribute("map1");
	if(map1 == null){
		map1 = new HashMap<String, Integer>();
		map1.put("凤求凰", 0);
		map1.put("街头霸王", 0);
		map1.put("地狱之眼", 0);
		map1.put("荣耀水晶", 0);
	}
	
	String[] buys = request.getParameterValues("item");
	
	for(String item:buys){
		if(item.equals("fqh")){
			int num1 = map1.get("凤求凰").intValue();
			map1.put("凤求凰", num1+1);
		}
		else if(item.equals("jtbw")){
			int num2 = map1.get("街头霸王").intValue();
			map1.put("街头霸王", num2+1);
		}
		else if(item.equals("dyzy")){
			int num3 = map1.get("地狱之眼").intValue();
			map1.put("地狱之眼", num3+1);
		}
		else{
			int num4 = map1.get("荣耀水晶").intValue();
			map1.put("荣耀水晶", num4+1);
		}
	}
 
	session.setAttribute("map1", map1);
	request.getRequestDispatcher("show.jsp").forward(request, response);
%>