package character;
import skill.ShanXian;
public class ShooterTest {
	public static void main(String[] args) {
		System.out.println("-------��ӭ����������ҫ-------�о�����5�뵽��ս��-------ȫ������-------");
		Shooter shooter=null;  
		shooter =new LuBanQiHao();
		System.out.print("Ӣ��"+shooter.getheroName()+"��¼�������ף�");
		shooter.display();
		System.out.print("��ͨ������");
		shooter.normalAttack();
		shooter.setSkillStrategy(new ShanXian());
		System.out.print("�ٻ�ʦ���ܣ�");
		shooter.skill();
		}
	}
