package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Spinner spinnerVeiculo;
    RadioGroup radioGroupCombustivel;
    EditText edtLitros;
    EditText edtDistancia;
    EditText edtConsumo;
    Button btnEnviar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        spinnerVeiculo        = findViewById(R.id.spinnerVeiculo);
        radioGroupCombustivel = findViewById(R.id.radioGroupCombustivel);
        edtLitros             = findViewById(R.id.edtLitros);
        edtDistancia          = findViewById(R.id.edtDistancia);
        edtConsumo            = findViewById(R.id.edtConsumo);
        btnEnviar             = findViewById(R.id.btnEnviar);

        btnEnviar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                validarEEnviar();
            }
        });
    }

    private void validarEEnviar() {

        if (spinnerVeiculo.getSelectedItemPosition() == 0) {
            Toast.makeText(MainActivity.this, "Selecione um veículo!", Toast.LENGTH_LONG).show();
            return;
        }

        if (radioGroupCombustivel.getCheckedRadioButtonId() == -1) {
            Toast.makeText(MainActivity.this, "Selecione o tipo de combustível!", Toast.LENGTH_LONG).show();
            return;
        }

        if (edtLitros.getText().toString().trim().isEmpty()) {
            Toast.makeText(MainActivity.this, "Informe quantos litros vai abastecer!", Toast.LENGTH_LONG).show();
            return;
        }

        if (edtDistancia.getText().toString().trim().isEmpty()) {
            Toast.makeText(MainActivity.this, "Informe a distância da viagem!", Toast.LENGTH_LONG).show();
            return;
        }

        if (edtConsumo.getText().toString().trim().isEmpty()) {
            Toast.makeText(MainActivity.this, "Informe o consumo do veículo (km/l)!", Toast.LENGTH_LONG).show();
            return;
        }

        String veiculo = spinnerVeiculo.getSelectedItem().toString();

        int idRadioMarcado = radioGroupCombustivel.getCheckedRadioButtonId();
        RadioButton radioMarcado = (RadioButton) findViewById(idRadioMarcado);
        String combustivel = radioMarcado.getText().toString();

        double litros    = Double.parseDouble(edtLitros.getText().toString());
        double distancia = Double.parseDouble(edtDistancia.getText().toString());
        double consumo   = Double.parseDouble(edtConsumo.getText().toString());

        Intent i = new Intent(MainActivity.this, MainActivity2.class);
        i.putExtra("VEICULO",     veiculo);
        i.putExtra("COMBUSTIVEL", combustivel);
        i.putExtra("LITROS",      litros);
        i.putExtra("DISTANCIA",   distancia);
        i.putExtra("CONSUMO",     consumo);
        startActivity(i);
    }
}