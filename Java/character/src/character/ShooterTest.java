package character;
import skill.ShanXian;
public class ShooterTest {
	public static void main(String[] args) {
		System.out.println("-------欢迎来到王者荣耀-------敌军还有5秒到达战场-------全军出击-------");
		Shooter shooter=null;  
		shooter =new LuBanQiHao();
		System.out.print("英雄"+shooter.getheroName()+"登录，开场白：");
		shooter.display();
		System.out.print("普通攻击：");
		shooter.normalAttack();
		shooter.setSkillStrategy(new ShanXian());
		System.out.print("召唤师技能：");
		shooter.skill();
		}
	}
