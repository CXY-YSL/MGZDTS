/*import java.util.HeroConfig;
import java.util.HeroBuilder;*/
public class HeroConfig {
    HeroBuilder mBuilder = null;
    //英雄的三个技能
    private String firstSkill;
    private String secondSkill;
    private String thirdSkill;
    private String TPeffect = "无回城特效";
    private String skin = "普通皮肤";
    private String attack = "近战攻击";

    public HeroConfig(HeroBuilder builder) {
        mBuilder = builder;
        init();
    }

    private void init() {
        //这里是判断是否构建，未构建用默认值
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
                "技能1——>" + firstSkill +
                        "  技能2——>" + secondSkill +
                        "  技能3——>" + thirdSkill +
                        "  回城特效——>" + TPeffect +
                        "  皮肤是——>" + skin +
                        "  普通攻击属性-->" + attack;
    }
	public static class HeroBuilder {
	//3个技能
    private String firstSkill; 
    private String secondSkill;
    private String thirdSkill;
    private String TPeffects; //回城效果
    private String skin;    //皮肤
    private String attack;  //攻击方式

    //在这里扩展一下，由于英雄的三个技能是必选的，而回城的特效、攻击方式和皮肤是可选的
    //所以提供一个构造方法在构造的时候一定设置3个技能即可
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
	HeroConfig 韩信=
        new HeroConfig.HeroBuilder("无情冲锋","背水一战","大招!--国士无双")
        .buildSkin("白龙吟")
        .create();

	HeroConfig 李白=
        new HeroConfig.HeroBuilder("将进酒","神来之笔","大招!--青莲剑歌")
        .buildSkin("凤求凰")
        .create();

	HeroConfig 赵云=
        new HeroConfig.HeroBuilder("天翔之龙","破云之龙","大招!--惊雷之龙")
        .buildAttack("远程攻击")
        .buildSkin("白执事")
        .create();

	HeroConfig 诸葛亮=
        new HeroConfig.HeroBuilder("东风破袭","时空穿梭","大招!--元气弹")
        .buildAttack("远程攻击")
        .buildSkin("桃夭")
        .create();

	Log.e("韩信"+韩信.toString());
	Log.e("李白"+李白.toString());
	Log.e("赵云"+赵云.toString());
	Log.e("诸葛亮"+ 诸葛亮.toString());
	}
}
