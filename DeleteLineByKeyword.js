// DeleteLineByKeyword.js
// �L�[���[�h�Ƀ}�b�`����s���폜����
// �g�ݍ��݂�SearchNext()���A�z(������Ȃ��ꍇ��������Ȃ�)�Ȃ̂ŁA���͂Ō������Ă���ww

// ��MUST
var KEYWORD = '\\t\\.git\\t';  // �L�[���[�h
var isReg = true;  // ���K�\��ON/OFF


var shell = new ActiveXObject("WScript.Shell");

// �s���Ɉړ�
GoFileTop();

// �s�����擾(0�͂��܂��Ȃ�)
var lineCount = GetLineCount(0);
//shell.Popup("lineCount=" + lineCount);

var line = 0;

//�S�s�����[�v
while (++line <= lineCount){
	var lineStr = GetLineStr(line);

	//shell.Popup("lineStr="+lineStr+"  line="+line+"  lineCount="+lineCount);

	if( isDeleteLine(lineStr, KEYWORD, isReg) ){
		DeleteLine();

		lineCount = GetLineCount(0);
		--line;

		//shell.Popup("lineStr="+lineStr+"  line="+line+"  lineCount="+lineCount);

		continue;
	}
	GoLineEnd();
	Right();
}
//shell.Popup("END");

function isDeleteLine(l, k, r) {
	if(r === true){
		var reg = new RegExp(k);
		return l.match(reg) != null;
	}
	else{
		return l.indexOf(k) != -1;
	}
}
