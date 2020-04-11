package com.jay.example.locklist;

import java.lang.reflect.Method;

import com.android.internal.telephony.ITelephony;

import android.app.Activity;
import android.os.Bundle;
import android.os.IBinder;
import android.telephony.PhoneStateListener;
import android.telephony.TelephonyManager;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;


public class MainActivity extends Activity {

	private TelephonyManager tManager;
	private PhoneStateListener pListener;
	private String number;
	private EditText locknum;
	private Button btnlock;
	
	public class PhonecallListener extends PhoneStateListener
	{
		@Override
		public void onCallStateChanged(int state, String incomingNumber) {
			switch(state)
			{
			case TelephonyManager.CALL_STATE_IDLE:break;
			case TelephonyManager.CALL_STATE_OFFHOOK:break;
			//���е绰����ʱ
			case TelephonyManager.CALL_STATE_RINGING:
				if(isBlock(incomingNumber))
				{
					try
					{
						Method method = Class.forName("android.os.ServiceManager")
								.getMethod("getService", String.class);
						// ��ȡԶ��TELEPHONY_SERVICE��IBinder����Ĵ���
						IBinder binder = (IBinder) method.invoke(null,
							new Object[] { TELEPHONY_SERVICE });
						// ��IBinder����Ĵ���ת��ΪITelephony����
						ITelephony telephony = ITelephony.Stub.asInterface(binder);
						// �Ҷϵ绰
						telephony.endCall();
					}catch(Exception e){e.printStackTrace();}
				}
				break;
			}
			super.onCallStateChanged(state, incomingNumber);
		}
	}
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		locknum = (EditText) findViewById(R.id.locknum);
		btnlock = (Button) findViewById(R.id.btnlock);
		
		//��ȡϵͳ��TelephonyManager������
		tManager = (TelephonyManager) getSystemService(TELEPHONY_SERVICE);
		pListener = new PhoneStateListener();
		tManager.listen(pListener, PhoneStateListener.LISTEN_CALL_STATE);
		
		btnlock.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				number = locknum.getText().toString();				
			}
		});
		
	}
	
	public boolean isBlock(String phone)
	{
		if(phone.equals(number))return true;
		return false;
	}
	
}
