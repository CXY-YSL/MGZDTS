
public class Activity {
    HeroConfig ����=
            new HeroConfig.HeroBuilder("������","��ˮһս","����!--��ʿ��˫")
            .buildSkin("������")
            .create();
    
    HeroConfig ���=
            new HeroConfig.HeroBuilder("������","����֮��","����!--��������")
            .buildSkin("�����")
            .create();
    
    HeroConfig ����=
            new HeroConfig.HeroBuilder("����֮��","��ԭ����","����!--һ֧���Ƽ�")
            .buildAttack("Զ�̹���")
            .buildSkin("�ƽ�������")
            .create();
    
    HeroConfig �����=
            new HeroConfig.HeroBuilder("������Ϯ","ʱ�մ���","����!--Ԫ����")
            .buildAttack("Զ�̹���")
            .buildSkin("��ʸ")
            .create();

 //   Log.e("����"+����.toString());
 //  Log.e("���"+���.toString());
 //  Log.e("����"+����.toString());
 //  Log.e("�����"+ �����.toString());
    
}
