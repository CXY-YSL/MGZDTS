package character;
import strategy.SkillStrategy;
public abstract class Shooter {
	private String heroName;
	public void setHeroName(String heroName) {
		this.heroName = heroName;
	}
	public String getheroName(){
		return heroName;
	}
	public abstract void display();
	public abstract void normalAttack();
	private SkillStrategy skillStrategy;
	public void setSkillStrategy(SkillStrategy skillStrategy) {
		this.skillStrategy = skillStrategy;
	}
	public void skill() {
		skillStrategy.useSkill();
	}
}
