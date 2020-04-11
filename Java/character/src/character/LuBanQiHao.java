package character;

public class LuBanQiHao extends Shooter {
	public LuBanQiHao() {
		super.setHeroName("鲁班七号");
	}
	
	@Override
	public void display() {
		System.out.println("鲁班大师，智商250！来啊！来打我啊");
	}
	
	@Override
	public void normalAttack() {
		System.out.println("biubiubiu~");
	}

}
