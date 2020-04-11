/*import java.util.HeroConfig;
import java.util.HeroBuilder;*/
public class HeroConfig {
    HeroBuilder mBuilder = null;
    //Ӣ�۵���������
    private String firstSkill;
    private String secondSkill;
    private String thirdSkill;
    private String TPeffect = "�޻س���Ч";
    private String skin = "��ͨƤ��";
    private String attack = "��ս����";

    public HeroConfig(HeroBuilder builder) {
        mBuilder = builder;
        init();
    }

    private void init() {
        //�������ж��Ƿ񹹽���δ������Ĭ��ֵ
        if (mBuilder.firstSkill != null) {
            firstSkill = mBuilder.firstSkill;
        }
        if (mBuilder.secondSkill != null) {
            secondSkill = mBuilder.secondSkill;
        }
        if (mBuilder.thirdSkill != null) {
            thirdSkill = mBuilder.thirdSkill;
        }
        if (mBuilder.TPeffects != null) {
            TPeffect = mBuilder.TPeffects;
        }
        if (mBuilder.skin != null) {
            skin = mBuilder.skin;
        }
        if (mBuilder.attack != null) {
            attack = mBuilder.attack;
        }

    }

    @Override
    public String toString() {
        return
                "����1����>" + firstSkill +
                        "  ����2����>" + secondSkill +
                        "  ����3����>" + thirdSkill +
                        "  �س���Ч����>" + TPeffect +
                        "  Ƥ���ǡ���>" + skin +
                        "  ��ͨ��������-->" + attack;
    }
	public static class HeroBuilder {
	//3������
    private String firstSkill; 
    private String secondSkill;
    private String thirdSkill;
    private String TPeffects; //�س�Ч��
    private String skin;    //Ƥ��
    private String attack;  //������ʽ

    //��������չһ�£�����Ӣ�۵����������Ǳ�ѡ�ģ����سǵ���Ч��������ʽ��Ƥ���ǿ�ѡ��
    //�����ṩһ�����췽���ڹ����ʱ��һ������3�����ܼ���
    public HeroBuilder(String firstSkill, String secondSkill, String thirdSkill) {
        this.firstSkill = firstSkill;
        this.secondSkill = secondSkill;
        this.thirdSkill = thirdSkill;
    }
    
    public HeroConfig create() {
        HeroConfig mHeroConfig = new HeroConfig(this);
        return mHeroConfig;
    }

    public HeroBuilder buildAttack(String attack) {
        this.attack = attack;
        return this;
    }

    public HeroBuilder buildSkin(String skin) {
        this.skin = skin;
        return this;
    }

    public HeroBuilder buildTPeffects(String effect) {
        this.TPeffects = effect;
        return this;
    }
}

class Activity {	
	HeroConfig ����=
        new HeroConfig.HeroBuilder("������","��ˮһս","����!--��ʿ��˫")
        .buildSkin("������")
        .create();

	HeroConfig ���=
        new HeroConfig.HeroBuilder("������","����֮��","����!--��������")
        .buildSkin("�����")
        .create();

	HeroConfig ����=
        new HeroConfig.HeroBuilder("����֮��","����֮��","����!--����֮��")
        .buildAttack("Զ�̹���")
        .buildSkin("��ִ��")
        .create();

	HeroConfig �����=
        new HeroConfig.HeroBuilder("������Ϯ","ʱ�մ���","����!--Ԫ����")
        .buildAttack("Զ�̹���")
        .buildSkin("��ز")
        .create();

	Log.e("����"+����.toString());
	Log.e("���"+���.toString());
	Log.e("����"+����.toString());
	Log.e("�����"+ �����.toString());
	}
}
