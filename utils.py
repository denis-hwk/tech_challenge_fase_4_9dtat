import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, OrdinalEncoder

class OneHotEncodingFeatures(BaseEstimator, TransformerMixin):
  def __init__(self, one_hot_feature=['MTRANS']):
    self.one_hot_feature = one_hot_feature

  def fit(self, df):
    return self


  def transform(self, df):
    if (set(self.one_hot_feature).issubset(df.columns)):
      def one_hot_encoding(df, one_hot_feature):
        one_hot_encoder = OneHotEncoder()
        one_hot_encoder.fit(df[one_hot_feature])

        # Obter nomes das features
        feature_names = one_hot_encoder.get_feature_names_out(one_hot_feature)

        # Criando DataFrame para as novas features
        df = pd.DataFrame(one_hot_encoder.transform(df[self.one_hot_feature]).toarray(), columns=feature_names, index=df.index)

        return df

      def concat_df(df, one_hot_df, one_hot_feature):
        df_features = [feature for feature in df.columns if feature not in one_hot_feature]

        # Concatenando novas features One Hot com as outras features do DataFrame
        df_concat = pd.concat([one_hot_df, df[df_features]], axis=1)

        return df_concat

      df_one_hot_features = one_hot_encoding(df, self.one_hot_feature)

      df_completo = concat_df(df, df_one_hot_features, self.one_hot_feature)

      return df_completo

    else:
      print('Uma ou mais features não estão no DataFrame')
      return df
    
class MinMaxScalerFeatures(BaseEstimator, TransformerMixin):
  def __init__(self, min_max_features = ['Age', 'Height', 'Weight']):
    self.min_max_features = min_max_features

  def fit(self, df):
    return self

  def transform(self, df):
    if (set(self.min_max_features).issubset(df.columns)):
      min_max_scaler = MinMaxScaler()
      df[self.min_max_features] = min_max_scaler.fit_transform(df[self.min_max_features])
      return df

    else:
      print('Uma ou mais features não estão no DataFrame')
      return df