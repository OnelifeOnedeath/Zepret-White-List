public class MainActivity extends AppCompatActivity {
    private Button vpnButton;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        vpnButton = findViewById(R.id.vpn_button);
        vpnButton.setOnClickListener(v -> {
            // Запрос разрешения VPN
            Intent intent = VpnService.prepare(this);
            if (intent != null) {
                startActivityForResult(intent, 0);
            } else {
                startVPNService();
            }
        });
    }
    
    private void startVPNService() {
        Intent intent = new Intent(this, SurvivalVPN.class);
        startService(intent);
        vpnButton.setText("VPN ЗАПУЩЕН");
        vpnButton.setBackgroundColor(Color.GREEN);
    }
}
