//        ���������������ؼ��飬��һ������һ��
var current_fs, next_fs, previous_fs;
//        ��ȡliԪ��Ҳ���ǽ������ļ���
var lis=document.getElementsByTagName("li");

//�����һ����ť���ø÷���
function nextbtn(obj,num){
    current_fs=obj.parentNode;
    next_fs=  getNearEle(current_fs,0);
//            ͨ��js�����ƿռ������ʾ����
    next_fs.style.display="block";
//            ͨ��jsΪĳ��liԪ�����class="active";,�����ƽ���������ʽ
    lis[num].className+="active";

}
//�����һ����ť���ø÷���
function prevbtn(obj,num){
    current_fs=obj.parentNode;
    previous_fs= getNearEle(current_fs,1);
    //            ͨ��js�����ƿռ������ʾ����
    current_fs.style.display="none";
    previous_fs.style.display="block";
    lis[num].className="";
}

/**
 * ��ȡ����Ԫ��
 * @param ele �ο���Ԫ��
 * @param type ���ͣ���һ��(1)or��һ��(0)
 * @return ���ز��ҵ���Ԫ��Dom�������򷵻�null
 */
function getNearEle(ele, type) {
    type = type == 1 ? "previousSibling" : "nextSibling";
    var nearEle = ele[type];
    while(nearEle) {
        if(nearEle.nodeType === 1) {
            return nearEle;
        }
        nearEle = nearEle[type];
        if(!nearEle) {
            break;
        }
    }
    return null;
}