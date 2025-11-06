package com.onelifeonedeath.whitelist;

import android.net.VpnService;
import android.os.ParcelFileDescriptor;
import java.io.IOException;

public class WhiteListVPN extends VpnService {
    
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Builder builder = new Builder();
        builder.setSession("WhiteList 1.0 - OnelifeOnedeath");
        builder.addAddress("10.8.0.2", 32);
        builder.addRoute("0.0.0.0", 0);
        builder.setMtu(1500);
        
        try {
            ParcelFileDescriptor vpnInterface = builder.establish();
            // Запускаем туннелирование всех данных
            startTunnel(vpnInterface);
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        return START_STICKY;
    }
    
    private native void startTunnel(ParcelFileDescriptor vpnInterface);
    
    static {
        System.loadLibrary("whitelist-tunnel");
    }
}
