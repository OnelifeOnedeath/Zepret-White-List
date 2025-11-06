package com.onelifeonedeath.whitelist;

import android.app.Activity;
import android.content.Intent;
import android.net.VpnService;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.graphics.Color;

public class MainActivity extends Activity {
    private Button vpnButton;
    private TextView statusText;
    private static final int VPN_REQUEST_CODE = 1;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        vpnButton = findViewById(R.id.vpn_button);
        statusText = findViewById(R.id.status_text);
        
        vpnButton.setOnClickListener(v -> {
            Intent intent = VpnService.prepare(this);
            if (intent != null) {
                startActivityForResult(intent, VPN_REQUEST_CODE);
            } else {
                startVPNService();
            }
        });
    }
    
    private void startVPNService() {
        Intent intent = new Intent(this, WhiteListVPN.class);
        startService(intent);
        vpnButton.setText("VPN АКТИВЕН");
        vpnButton.setBackgroundColor(Color.GREEN);
        statusText.setText("✅ WhiteList 1.0 активирован!\nДоступ ко всему интернету открыт");
    }
    
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == VPN_REQUEST_CODE && resultCode == RESULT_OK) {
            startVPNService();
        }
    }
}
