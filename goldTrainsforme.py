# 📦 Importação de bibliotecas
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

from imblearn.combine import SMOTEENN
from xgboost import XGBClassifier

# ===============================
# ⚙️ Funções utilitárias
# ===============================

def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv)

def codificar_dados(df):
    df = df.copy()
    for col in df.select_dtypes(include='object').columns:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))
    for col in df.select_dtypes(include='bool').columns:
        df[col] = df[col].astype(int)
    return df

def tratar_nulos(X):
    imputer = SimpleImputer(strategy='median')
    return pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

def preparar_dados(df):
    df = df.dropna(subset=['fraud_bool'])
    X = df.drop(columns=["fraud_bool"])
    y = df["fraud_bool"]
    X = codificar_dados(X)
    X = tratar_nulos(X)
    return train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

def balancear_amostras(X_train, y_train):
    X_sampled, _, y_sampled, _ = train_test_split(
        X_train, y_train, stratify=y_train, test_size=0.8, random_state=42
    )
    smote_enn = SMOTEENN(random_state=42)
    return smote_enn.fit_resample(X_sampled, y_sampled)

def treinar_modelo(X, y):
    model = XGBClassifier(
        scale_pos_weight=10,
        eval_metric='logloss',
        use_label_encoder=False,
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        random_state=42
    )
    model.fit(X, y)
    return model

# ===============================
# 🚀 Execução
# ===============================

def main():
    caminho_csv = r"C:\estudos\POS\Base_silver.csv"
    df = carregar_dados(caminho_csv)

    X_train, X_test, y_train, y_test = preparar_dados(df)
    X_bal, y_bal = balancear_amostras(X_train, y_train)
    modelo = treinar_modelo(X_bal, y_bal)

    df_pred = df.copy()
    X_all = df.drop(columns=["fraud_bool"])
    X_all = codificar_dados(X_all)
    X_all = tratar_nulos(X_all)

    probabilidade = modelo.predict_proba(X_all)[:, 1]
    df_pred["fraude_predita"] = (probabilidade > 0.1).astype(int)

    print("🔍 Colunas disponíveis no dataframe:")
    print(df_pred.columns.tolist())

    # 🔧 Selecionar colunas para a camada GOLD
    colunas_gold = ['fraud_bool', 'month', 'month_named', 'fraude_predita', 'credit_risk_score', 'source', 'payment_type']
    colunas_existentes = [col for col in colunas_gold if col in df_pred.columns]

    if len(colunas_existentes) < len(colunas_gold):
        faltantes = set(colunas_gold) - set(colunas_existentes)
        print(f"⚠️ Atenção! As seguintes colunas não estão no dataframe: {faltantes}")

    df_gold = df_pred[colunas_existentes].copy()

    output_csv = r"C:\estudos\POS\df_gold.csv"
    df_gold.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"✅ Camada GOLD exportada com sucesso para {output_csv}")



if __name__ == "__main__":
    main()
