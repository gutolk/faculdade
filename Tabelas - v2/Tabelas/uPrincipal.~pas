unit uPrincipal;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, Grids, StdCtrls;

type
  TForm1 = class(TForm)
    grid1: TStringGrid;
    edt1: TEdit;
    edt2: TEdit;
    btnNovo: TButton;
    edt3: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    btnAlterar: TButton;
    btnExcluir: TButton;
    btnSalvar: TButton;
    btnCancelar: TButton;
    procedure FormCreate(Sender: TObject);
    procedure btnNovoClick(Sender: TObject);
    procedure grid1Click(Sender: TObject);
    procedure btnExcluirClick(Sender: TObject);
    procedure btnSalvarClick(Sender: TObject);
    procedure btnAlterarClick(Sender: TObject);
    procedure btnCancelarClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  count : integer;

implementation

{$R *.dfm}

procedure TForm1.FormCreate(Sender: TObject);
begin
    grid1.Cells[0,0] := 'ID';
    grid1.Cells[1,0] := 'Nome';
    grid1.Cells[2,0] := 'Idade';
    grid1.Cells[3,0] := 'Cidade';
    count :=0;

    edt1.Enabled := false;
    edt2.Enabled := false;
    edt3.Enabled := false;

    btnExcluir.Enabled := false;
    btnAlterar.Enabled := false;
    btnCancelar.Enabled := false;
    btnSalvar.Enabled := false;

end;

procedure TForm1.btnNovoClick(Sender: TObject);
begin
    edt1.Enabled := true;
    edt2.Enabled := true;
    edt3.Enabled := true;
    btnSalvar.Enabled := true;
    btnCancelar.Enabled := true;
end;

procedure TForm1.grid1Click(Sender: TObject);
begin
    edt1.Enabled := true;
    edt2.Enabled := true;
    edt3.Enabled := true;

    if grid1.RowCount > 1 then
    btnExcluir.Enabled := true;
    btnAlterar.Enabled := true;
    btnCancelar.Enabled := true;
    btnNovo.Enabled := false;

    edt1.text := grid1.Cells[1,grid1.Row];
    edt2.text := grid1.Cells[2,grid1.Row];
    edt3.text := grid1.Cells[3,grid1.Row];
end;

procedure TForm1.btnExcluirClick(Sender: TObject);
begin
    
    grid1.RowCount := grid1.RowCount - 1;

    grid1.Cells[0,grid1.RowCount] := IntToStr(count);

    btnExcluir.Enabled := false;
    btnAlterar.Enabled := false;
    btnCancelar.Enabled := false;
    btnNovo.Enabled := true;

    edt1.text := '';
    edt2.text := '';
    edt3.text := '';
end;

procedure TForm1.btnSalvarClick(Sender: TObject);
begin
    if (edt1.text = '') or (edt2.text = '') or (edt3.text = '') then
    ShowMessage('O campo não pode ser inserido vazio!')

    else

    begin

    grid1.Cells[1,grid1.RowCount] := edt1.text;
    grid1.Cells[2,grid1.RowCount] := edt2.text;
    grid1.Cells[3,grid1.RowCount] := edt3.text;


    count := count+1;
    grid1.Cells[0,grid1.RowCount] := IntToStr(count);

    grid1.RowCount := grid1.RowCount + 1;

    edt1.text := '';
    edt2.text := '';
    edt3.text := '';

    edt1.Enabled := false;
    edt2.Enabled := false;
    edt3.Enabled := false;

    btnExcluir.Enabled := false;
    btnAlterar.Enabled := false;
    btnCancelar.Enabled := false;
    btnSalvar.Enabled := false;

    end
end;

procedure TForm1.btnAlterarClick(Sender: TObject);
begin
    btnExcluir.Enabled := false;


    grid1.Cells[1,grid1.Row] := edt1.text;
    grid1.Cells[2,grid1.Row] := edt2.text;
    grid1.Cells[3,grid1.Row] := edt3.text;

    btnAlterar.Enabled := false;
    btnNovo.Enabled := true;
    btnCancelar.Enabled := false;

    edt1.text := '';
    edt2.text := '';
    edt3.text := '';

    edt1.Enabled := false;
    edt2.Enabled := false;
    edt3.Enabled := false;

end;

procedure TForm1.btnCancelarClick(Sender: TObject);
begin
    edt1.text := '';
    edt2.text := '';
    edt3.text := '';

    edt1.Enabled := false;
    edt2.Enabled := false;
    edt3.Enabled := false;

    btnExcluir.Enabled := false;
    btnAlterar.Enabled := false;
    btnCancelar.Enabled := false;
    btnSalvar.Enabled := false;
    btnNovo.Enabled := true;
end;

end.


