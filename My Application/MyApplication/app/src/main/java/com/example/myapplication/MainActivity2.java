package com.example.myapplication;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity2 extends AppCompatActivity {

    TextView txtResVeiculo;
    TextView txtResCombustivel;
    TextView txtResLitros;
    TextView txtResCusto;
    TextView txtResDistancia;
    TextView txtResConsumo;
    TextView txtResGastoViagem;
    Button btnVoltar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        txtResVeiculo     = findViewById(R.id.txtResVeiculo);
        txtResCombustivel = findViewById(R.id.txtResCombustivel);
        txtResLitros      = findViewById(R.id.txtResLitros);
        txtResCusto       = findViewById(R.id.txtResCusto);
        txtResDistancia   = findViewById(R.id.txtResDistancia);
        txtResConsumo     = findViewById(R.id.txtResConsumo);
        txtResGastoViagem = findViewById(R.id.txtResGastoViagem);
        btnVoltar         = findViewById(R.id.btnVoltar);

        String veiculo     = getIntent().getStringExtra("VEICULO");
        String combustivel = getIntent().getStringExtra("COMBUSTIVEL");
        double litros      = getIntent().getDoubleExtra("LITROS",    0.0);
        double distancia   = getIntent().getDoubleExtra("DISTANCIA", 0.0);
        double consumo     = getIntent().getDoubleExtra("CONSUMO",   0.0);

        double precoPorLitro;
        if (combustivel.equals("Etanol")) {
            precoPorLitro = 3.89;
        } else if (combustivel.equals("Gasolina")) {
            precoPorLitro = 5.79;
        } else {
            precoPorLitro = 6.09;
        }

        double custoAbastecimento = litros * precoPorLitro;
        double litrosViagem = distancia / consumo;

        txtResVeiculo.setText("Veículo: " + veiculo);
        txtResCombustivel.setText("Combustível: " + combustivel + " (R$ " + String.format("%.2f", precoPorLitro) + "/L)");
        txtResLitros.setText("Litros a abastecer: " + String.format("%.1f", litros) + " L");
        txtResCusto.setText("Custo total: R$ " + String.format("%.2f", custoAbastecimento));
        txtResDistancia.setText("Distância da viagem: " + String.format("%.1f", distancia) + " km");
        txtResConsumo.setText("Consumo do veículo: " + String.format("%.1f", consumo) + " km/L");
        txtResGastoViagem.setText("Litros gastos na viagem: " + String.format("%.2f", litrosViagem) + " L");

        btnVoltar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
    }
}