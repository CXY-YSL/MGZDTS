package character;

public class LuBanQiHao extends Shooter {
	public LuBanQiHao() {
		super.setHeroName("³���ߺ�");
	}
	
	@Override
	public void display() {
		System.out.println("³���ʦ������250�������������Ұ�");
	}
	
	@Override
	public void normalAttack() {
		System.out.println("biubiubiu~");
	}

}
