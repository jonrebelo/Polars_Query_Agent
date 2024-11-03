import pandas as pd

# List of tuples with (Polars code, Pandas code) pairs
data_pairs_df_series = [
    ("pl.Series('ints', [1, 2, 3, 4, 5])", "pd.Series([1, 2, 3, 4, 5], name='ints')"),
    ("pl.Series('floats', [1.1, 2.2, 3.3])", "pd.Series([1.1, 2.2, 3.3], name='floats')"),
    ("pl.Series('bools', [True, False, True])", "pd.Series([True, False, True], name='bools')"),
    ("pl.Series('dates', [date(2020, 1, 1), date(2021, 1, 1)])", "pd.Series([pd.Timestamp('2020-01-01'), pd.Timestamp('2021-01-01')], name='dates')"),
    
    ("pl.Series('strings', ['apple', 'banana', 'cherry'])", "pd.Series(['apple', 'banana', 'cherry'], name='strings')"),
    ("pl.Series('mixed', [1, 'two', 3.0])", "pd.Series([1, 'two', 3.0], name='mixed')"),
    ("pl.Series('empty', [])", "pd.Series([], dtype='object', name='empty')"),
    ("pl.Series('nulls', [None, None, None])", "pd.Series([None, None, None], name='nulls')"),
    
    ("pl.Series('complex', [complex(1, 2), complex(3, 4)])", "pd.Series([complex(1, 2), complex(3, 4)], name='complex')"),
    ("pl.Series('datetime', [datetime(2021, 1, 1), datetime(2021, 1, 2)])", "pd.Series([pd.Timestamp('2021-01-01'), pd.Timestamp('2021-01-02')], name='datetime')"),
    
    ("pl.DataFrame({'A': [1, 2], 'B': [3, 4]})", "pd.DataFrame({'A': [1, 2], 'B': [3, 4]})"),
    ("pl.DataFrame({'C': [5, 6], 'D': [7, 8]})", "pd.DataFrame({'C': [5, 6], 'D': [7, 8]})"),
    ("pl.DataFrame({'E': [9, 10], 'F': [11, 12]})", "pd.DataFrame({'E': [9, 10], 'F': [11, 12]})"),
    
    ("pl.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})", "pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})"),
    ("pl.DataFrame({'id': [1, 2, 3], 'score': [88, 92, 95]})", "pd.DataFrame({'id': [1, 2, 3], 'score': [88, 92, 95]})"),
    
    ("pl.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})", "pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})"),
    ("pl.DataFrame({'item': ['pen', 'pencil'], 'price': [1.5, 0.8]})", "pd.DataFrame({'item': ['pen', 'pencil'], 'price': [1.5, 0.8]})"),
    
    ("pl.DataFrame({'date': [date(2021, 1, 1), date(2021, 1, 2)], 'value': [100, 200]})", 
     "pd.DataFrame({'date': [pd.Timestamp('2021-01-01'), pd.Timestamp('2021-01-02')], 'value': [100, 200]})"),
    
    ("pl.DataFrame({'A': [1, 2, None], 'B': [None, 4, 5]})", "pd.DataFrame({'A': [1, 2, None], 'B': [None, 4, 5]})"),
    ("pl.DataFrame({'height': [1.76, 1.82, None], 'weight': [70, 85, 90]})", "pd.DataFrame({'height': [1.76, 1.82, None], 'weight': [70, 85, 90]})"),
    
    ("pl.DataFrame({'product': ['A', 'B'], 'quantity': [10, 20]})", "pd.DataFrame({'product': ['A', 'B'], 'quantity': [10, 20]})"),
    
    ("pl.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})", "pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]})"),
    ("pl.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4]})", "pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4]})"),
    ("pl.DataFrame({'timestamp': [datetime(2020, 1, 1), datetime(2020, 1, 2)]})", 
     "pd.DataFrame({'timestamp': [pd.Timestamp('2020-01-01'), pd.Timestamp('2020-01-02')]})"),
    
    ("pl.DataFrame({'name': ['Tom', 'Jerry'], 'score': [90, 85]})", "pd.DataFrame({'name': ['Tom', 'Jerry'], 'score': [90, 85]})"),
    ("pl.DataFrame({'id': [1, 2, 3], 'value': [3.14, 2.71, 1.41]})", "pd.DataFrame({'id': [1, 2, 3], 'value': [3.14, 2.71, 1.41]})"),
    
    ("pl.DataFrame({'category': ['A', 'B'], 'amount': [100, 200]})", "pd.DataFrame({'category': ['A', 'B'], 'amount': [100, 200]})"),
    ("pl.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})", "pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})"),
    
    ("pl.DataFrame({'numbers': [1, 2, 3, 4, 5]})", "pd.DataFrame({'numbers': [1, 2, 3, 4, 5]})"),
    ("pl.DataFrame({'a': [10, 20], 'b': [30, 40], 'c': [50, 60]})", "pd.DataFrame({'a': [10, 20], 'b': [30, 40], 'c': [50, 60]})"),
    
    ("pl.DataFrame({'X1': [1, 2], 'X2': [3, 4]})", "pd.DataFrame({'X1': [1, 2], 'X2': [3, 4]})"),
    ("pl.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})", "pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})"),
    
    ("pl.DataFrame({'year': [2020, 2021], 'revenue': [500, 600]})", "pd.DataFrame({'year': [2020, 2021], 'revenue': [500, 600]})"),
    ("pl.DataFrame({'product': ['A', 'B', 'C'], 'sales': [150, 200, 250]})", "pd.DataFrame({'product': ['A', 'B', 'C'], 'sales': [150, 200, 250]})"),
    
    ("pl.DataFrame({'X': [1.1, 2.2], 'Y': [3.3, 4.4]})", "pd.DataFrame({'X': [1.1, 2.2], 'Y': [3.3, 4.4]})"),
    ("pl.DataFrame({'city': ['NY', 'LA'], 'temperature': [80, 75]})", "pd.DataFrame({'city': ['NY', 'LA'], 'temperature': [80, 75]})"),
    
    ("pl.DataFrame({'student': ['John', 'Jane'], 'grade': [88, 92]})", "pd.DataFrame({'student': ['John', 'Jane'], 'grade': [88, 92]})"),
    ("pl.DataFrame({'time': [datetime(2022, 1, 1), datetime(2022, 1, 2)]})", 
     "pd.DataFrame({'time': [pd.Timestamp('2022-01-01'), pd.Timestamp('2022-01-02')]})"),
    
    ("pl.DataFrame({'class': ['A', 'B'], 'average_score': [75, 85]})", "pd.DataFrame({'class': ['A', 'B'], 'average_score': [75, 85]})"),
    ("pl.DataFrame({'genre': ['Action', 'Comedy'], 'rating': [5, 4]})", "pd.DataFrame({'genre': ['Action', 'Comedy'], 'rating': [5, 4]})"),
    
    ("pl.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})", "pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})"),
    
    ("pl.DataFrame({'ProductID': [101, 102, 103], 'Price': [15.99, 22.50, 9.99]})", "pd.DataFrame({'ProductID': [101, 102, 103], 'Price': [15.99, 22.50, 9.99]})"),
    ("pl.DataFrame({'Employee': ['John', 'Doe'], 'Salary': [50000, 60000]})", "pd.DataFrame({'Employee': ['John', 'Doe'], 'Salary': [50000, 60000]})"),
    
    ("pl.DataFrame({'Country': ['USA', 'Canada'], 'Population': [331, 38]})", "pd.DataFrame({'Country': ['USA', 'Canada'], 'Population': [331, 38]})"),
    ("pl.DataFrame({'Company': ['A', 'B', 'C'], 'Revenue': [1000, 2000, 3000]})", "pd.DataFrame({'Company': ['A', 'B', 'C'], 'Revenue': [1000, 2000, 3000]})"),
    
    ("pl.DataFrame({'Team': ['Red', 'Blue'], 'Wins': [10, 15]})", "pd.DataFrame({'Team': ['Red', 'Blue'], 'Wins': [10, 15]})"),
    
    ("pl.Series('binary', [0, 1, 0, 1])", "pd.Series([0, 1, 0, 1], name='binary')"),
    ("pl.Series('ratings', [1, 2, 3, 4, 5])", "pd.Series([1, 2, 3, 4, 5], name='ratings')"),
    ("pl.Series('float_series', [1.5, 2.5, 3.5])", "pd.Series([1.5, 2.5, 3.5], name='float_series')"),
    ("pl.Series('string_series', ['foo', 'bar', 'baz'])", "pd.Series(['foo', 'bar', 'baz'], name='string_series')"),
    
    ("pl.Series('status', ['active', 'inactive', 'pending'])", "pd.Series(['active', 'inactive', 'pending'], name='status')"),
    ("pl.Series('mixed_type', [1, 'two', 3.0])", "pd.Series([1, 'two', 3.0], name='mixed_type')"),
    ("pl.Series('time', [time(12, 0), time(12, 30)])", "pd.Series([pd.Timestamp('1970-01-01 12:00:00'), pd.Timestamp('1970-01-01 12:30:00')], name='time')"),
    
    ("pl.DataFrame({'height': [1.7, 1.8], 'weight': [65, 75]})", "pd.DataFrame({'height': [1.7, 1.8], 'weight': [65, 75]})"),
    ("pl.DataFrame({'A': [1, None], 'B': [None, 2]})", "pd.DataFrame({'A': [1, None], 'B': [None, 2]})"),
    ("pl.DataFrame({'Country': ['USA', 'Mexico', 'Canada'], 'Capital': ['Washington', 'Mexico City', 'Ottawa']})", 
     "pd.DataFrame({'Country': ['USA', 'Mexico', 'Canada'], 'Capital': ['Washington', 'Mexico City', 'Ottawa']})"),
    
    ("pl.DataFrame({'item': ['widget', 'gadget'], 'quantity': [5, 10], 'price': [19.99, 24.99]})", 
     "pd.DataFrame({'item': ['widget', 'gadget'], 'quantity': [5, 10], 'price': [19.99, 24.99]})"),
    ("pl.DataFrame({'username': ['user1', 'user2'], 'login_count': [5, 3]})", 
     "pd.DataFrame({'username': ['user1', 'user2'], 'login_count': [5, 3]})"),
    
    ("pl.DataFrame({'fruit': ['apple', 'banana'], 'color': ['red', 'yellow']})", 
     "pd.DataFrame({'fruit': ['apple', 'banana'], 'color': ['red', 'yellow']})"),
    ("pl.DataFrame({'brand': ['Nike', 'Adidas'], 'sales': [2000, 1500]})", 
     "pd.DataFrame({'brand': ['Nike', 'Adidas'], 'sales': [2000, 1500]})"),
    
    ("pl.DataFrame({'animal': ['dog', 'cat'], 'age': [5, 3]})", 
     "pd.DataFrame({'animal': ['dog', 'cat'], 'age': [5, 3]})"),
    ("pl.DataFrame({'car': ['Toyota', 'Honda'], 'price': [20000, 22000]})", 
     "pd.DataFrame({'car': ['Toyota', 'Honda'], 'price': [20000, 22000]})"),
    
    ("pl.DataFrame({'city': ['Paris', 'London'], 'population': [2140000, 8900000]})", 
     "pd.DataFrame({'city': ['Paris', 'London'], 'population': [2140000, 8900000]})"),
    ("pl.DataFrame({'language': ['Python', 'Java'], 'difficulty': [2, 3]})", 
     "pd.DataFrame({'language': ['Python', 'Java'], 'difficulty': [2, 3]})"),
    
    ("pl.DataFrame({'device': ['mobile', 'tablet'], 'os': ['iOS', 'Android']})", 
     "pd.DataFrame({'device': ['mobile', 'tablet'], 'os': ['iOS', 'Android']})"),
    ("pl.DataFrame({'product': ['A', 'B', 'C'], 'availability': [True, False, True]})", 
     "pd.DataFrame({'product': ['A', 'B', 'C'], 'availability': [True, False, True]})"),
    
    ("pl.DataFrame({'color': ['red', 'blue'], 'hex': ['#FF0000', '#0000FF']})", 
     "pd.DataFrame({'color': ['red', 'blue'], 'hex': ['#FF0000', '#0000FF']})"),
]

data_pairs_head_tail_glimpse = [
    # Using previously defined DataFrames
    ("print(df.head(3))", "print(df.head(3))"),
    ("print(df.tail(3))", "print(df.tail(3))"),
    ("print(df.glimpse(return_as_string=True))", "print(df.info())"),
    
    # New examples
    ("df1 = pl.DataFrame({'A': [1, 2, 3, 4, 5]}); print(df1.head(3))", "df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5]}); print(df1.head(3))"),
    ("df1 = pl.DataFrame({'B': [10, 20, 30, 40, 50]}); print(df1.tail(3))", "df1 = pd.DataFrame({'B': [10, 20, 30, 40, 50]}); print(df1.tail(3))"),
    
    ("df2 = pl.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva']}); print(df2.glimpse(return_as_string=True))", 
     "df2 = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva']}); print(df2.info())"),
    
    ("df3 = pl.DataFrame({'x': [1.5, 2.5, 3.5, 4.5]}); print(df3.head(2))", "df3 = pd.DataFrame({'x': [1.5, 2.5, 3.5, 4.5]}); print(df3.head(2))"),
    ("df4 = pl.DataFrame({'y': [5, 6, 7, 8]}); print(df4.tail(2))", "df4 = pd.DataFrame({'y': [5, 6, 7, 8]}); print(df4.tail(2))"),
    
    ("df5 = pl.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}); print(df5.glimpse(return_as_string=True))", 
     "df5 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}); print(df5.info())"),
    
    ("df6 = pl.DataFrame({'date': [date(2020, 1, 1), date(2020, 1, 2), date(2020, 1, 3)]}); print(df6.head(2))", 
     "df6 = pd.DataFrame({'date': [pd.Timestamp('2020-01-01'), pd.Timestamp('2020-01-02'), pd.Timestamp('2020-01-03')]}); print(df6.head(2))"),
    
    ("df7 = pl.DataFrame({'city': ['New York', 'Los Angeles', 'Chicago']}); print(df7.tail(1))", 
     "df7 = pd.DataFrame({'city': ['New York', 'Los Angeles', 'Chicago']}); print(df7.tail(1))"),
    
    ("df8 = pl.DataFrame({'product': ['A', 'B', 'C', 'D']}); print(df8.glimpse(return_as_string=True))", 
     "df8 = pd.DataFrame({'product': ['A', 'B', 'C', 'D']}); print(df8.info())"),
    
    ("df9 = pl.DataFrame({'temperature': [70, 80, 90]}); print(df9.head(1))", 
     "df9 = pd.DataFrame({'temperature': [70, 80, 90]}); print(df9.head(1))"),
    
    ("df10 = pl.DataFrame({'score': [100, 200, 300, 400, 500]}); print(df10.tail(4))", 
     "df10 = pd.DataFrame({'score': [100, 200, 300, 400, 500]}); print(df10.tail(4))"),
    
    ("df11 = pl.DataFrame({'id': [1, 2, 3, 4]}); print(df11.glimpse(return_as_string=True))", 
     "df11 = pd.DataFrame({'id': [1, 2, 3, 4]}); print(df11.info())"),
    
    ("df12 = pl.DataFrame({'name': ['Tom', 'Jerry', 'Spike']}); print(df12.head(2))", 
     "df12 = pd.DataFrame({'name': ['Tom', 'Jerry', 'Spike']}); print(df12.head(2))"),
    
    ("df13 = pl.DataFrame({'sales': [150, 200, 250, 300]}); print(df13.tail(2))", 
     "df13 = pd.DataFrame({'sales': [150, 200, 250, 300]}); print(df13.tail(2))"),
    
    ("df14 = pl.DataFrame({'height': [1.70, 1.75, 1.80]}); print(df14.glimpse(return_as_string=True))", 
     "df14 = pd.DataFrame({'height': [1.70, 1.75, 1.80]}); print(df14.info())"),
    
    ("df15 = pl.DataFrame({'product': ['Laptop', 'Phone', 'Tablet']}); print(df15.head(1))", 
     "df15 = pd.DataFrame({'product': ['Laptop', 'Phone', 'Tablet']}); print(df15.head(1))"),
    
    ("df16 = pl.DataFrame({'price': [999.99, 499.99, 299.99]}); print(df16.tail(3))", 
     "df16 = pd.DataFrame({'price': [999.99, 499.99, 299.99]}); print(df16.tail(3))"),
]

data_pairs_sample_describe_schema = [
    ("df.sample(2)", "df.sample(2)"),
    ("df.describe()", "df.describe()"),
    ("df.schema", "df_pandas.dtypes"),
    
    ("df2.sample(1)", "df2_pandas.sample(1)"),
    ("df3.sample(3)", "df3_pandas.sample(3)"),
    ("df4.sample(2)", "df4_pandas.sample(2)"),
    
    ("df.sample(n=1)", "df.sample(n=1)"),
    ("df2.sample(frac=0.5)", "df2_pandas.sample(frac=0.5)"),
    ("df3.sample(n=2)", "df3_pandas.sample(n=2)"),
    
    ("df.describe().to_dict()", "df_pandas.describe().to_dict()"),
    ("df2.describe().to_dict()", "df2_pandas.describe().to_dict()"),
    ("df3.describe().to_dict()", "df3_pandas.describe().to_dict()"),
    
    ("df4.describe().to_string()", "df4_pandas.describe().to_string()"),
    ("df.describe(include='all')", "df_pandas.describe(include='all')"),
    
    ("df.schema.to_string()", "df_pandas.dtypes.to_string()"),
    ("df2.schema.to_string()", "df2_pandas.dtypes.to_string()"),
    ("df3.schema.to_string()", "df3_pandas.dtypes.to_string()"),
    
    ("df4.schema.to_string()", "df4_pandas.dtypes.to_string()"),
    ("df.schema", "df_pandas.dtypes"),
]

data_pairs_selet = [
    ("df.select(bmi=bmi_expr, avg_bmi=bmi_expr.mean(), ideal_max_bmi=25)", "df_pandas[['bmi']].assign(avg_bmi=df_pandas['bmi'].mean(), ideal_max_bmi=25)"),
    ("df.select(deviation=(bmi_expr - bmi_expr.mean()) / bmi_expr.std())", "df_pandas.assign(deviation=(df_pandas['bmi'] - df_pandas['bmi'].mean()) / df_pandas['bmi'].std())"),
    ("df.select(height_to_weight_ratio=(pl.col('height') / pl.col('weight')))","df_pandas.assign(height_to_weight_ratio=lambda x: x['height'] / x['weight'])"),
    ("df.select(birth_year=pl.col('birthdate').dt.year)", "df_pandas.assign(birth_year=df_pandas['birthdate'].dt.year)"),
    ("df.select(name_length=pl.col('name').str.lengths())", "df_pandas.assign(name_length=df_pandas['name'].str.len())"),
    ("df.select(bmi_category=pl.when(bmi_expr < 18.5).then('Underweight').when(bmi_expr < 25).then('Normal').otherwise('Overweight'))", "df_pandas.assign(bmi_category=pd.cut(df_pandas['bmi'], bins=[-np.inf, 18.5, 25, np.inf], labels=['Underweight', 'Normal', 'Overweight']))"),
    ("df.select(weight_kg=pl.col('weight') * 0.453592)", "df_pandas.assign(weight_kg=df_pandas['weight'] * 0.453592)"),
    ("df.select(height_meters=pl.col('height') * 0.3048)", "df_pandas.assign(height_meters=df_pandas['height'] * 0.3048)"),
    ("df.select(weight_category=pl.when(pl.col('weight') < 60).then('Light').when(pl.col('weight') < 80).then('Medium').otherwise('Heavy'))", "df_pandas.assign(weight_category=pd.cut(df_pandas['weight'], bins=[-np.inf, 60, 80, np.inf], labels=['Light', 'Medium', 'Heavy']))"),
    ("df.select(bmi_index=(pl.col('weight') / (pl.col('height') ** 2)))", "df_pandas.assign(bmi_index=(df_pandas['weight'] / (df_pandas['height'] ** 2)))"),
    ("df.select(age=pl.col('birthdate').dt.year - 2023)", "df_pandas.assign(age=2023 - df_pandas['birthdate'].dt.year)"),
    ("df.select(max_weight=pl.col('weight').max())", "pd.DataFrame({'max_weight': [df_pandas['weight'].max()]})"),
    ("df.select(min_weight=pl.col('weight').min())", "pd.DataFrame({'min_weight': [df_pandas['weight'].min()]})"),
    ("df.select(mean_weight=pl.col('weight').mean())", "pd.DataFrame({'mean_weight': [df_pandas['weight'].mean()]})"),
    ("df.select(count=pl.count())", "pd.DataFrame({'count': [df_pandas.shape[0]]})"),
    ("df.select(median_bmi=bmi_expr.median())", "pd.DataFrame({'median_bmi': [df_pandas['bmi'].median()]})"),
    ("df.select(weight_variance=pl.col('weight').var())", "pd.DataFrame({'weight_variance': [df_pandas['weight'].var()]})"),
    ("df.select(bmi_stddev=bmi_expr.std())", "pd.DataFrame({'bmi_stddev': [df_pandas['bmi'].std()]})"),
    ("df.select(sum_weight=pl.col('weight').sum())", "pd.DataFrame({'sum_weight': [df_pandas['weight'].sum()]})"),
    ("df.select(avg_height=pl.col('height').mean())", "pd.DataFrame({'avg_height': [df_pandas['height'].mean()]})"),
    ("df.select(bmi_distribution=pl.col('bmi').value_counts())", "df_pandas['bmi'].value_counts().reset_index(name='count').rename(columns={'index': 'bmi'})"),
    ("df.select(weight_percentile=pl.col('weight').quantile(0.75))", "pd.DataFrame({'weight_percentile': [df_pandas['weight'].quantile(0.75)]})"),
    ("df.select(bmi_range=(bmi_expr.max() - bmi_expr.min()))", "pd.DataFrame({'bmi_range': [df_pandas['bmi'].max() - df_pandas['bmi'].min()]})"),
    ("df.select(bmi_rounded=pl.round(bmi_expr, 1))", "df_pandas.assign(bmi_rounded=df_pandas['bmi'].round(1))"),
    ("df.select(log_weight=pl.col('weight').log())", "df_pandas.assign(log_weight=np.log(df_pandas['weight']))"),
    ("df.select(exp_height=pl.col('height').exp())", "df_pandas.assign(exp_height=np.exp(df_pandas['height']))"),
    ("df.select(sqrt_weight=pl.col('weight').sqrt())", "df_pandas.assign(sqrt_weight=np.sqrt(df_pandas['weight']))"),
    ("df.select(inverse_bmi=1 / bmi_expr)", "df_pandas.assign(inverse_bmi=1 / df_pandas['bmi'])"),
    ("df.select(bmi_to_category=pl.when(bmi_expr < 18.5).then('Underweight').when(bmi_expr < 25).then('Normal').otherwise('Overweight'))", "df_pandas.assign(bmi_to_category=pd.cut(df_pandas['bmi'], bins=[-np.inf, 18.5, 25, np.inf], labels=['Underweight', 'Normal', 'Overweight']))"),
    ("df.select(age_group=pl.when(pl.col('age') < 18).then('Minor').when(pl.col('age') < 65).then('Adult').otherwise('Senior'))", "df_pandas.assign(age_group=pd.cut(df_pandas['age'], bins=[-np.inf, 18, 65, np.inf], labels=['Minor', 'Adult', 'Senior']))"),
    ("df.select(bmi_mean_category=pl.when(bmi_expr.mean() < 18.5).then('Underweight').when(bmi_expr.mean() < 25).then('Normal').otherwise('Overweight'))", "pd.DataFrame({'bmi_mean_category': [df_pandas['bmi'].mean()]}).assign(bmi_mean_category=lambda x: np.where(x['bmi_mean_category'] < 18.5, 'Underweight', np.where(x['bmi_mean_category'] < 25, 'Normal', 'Overweight')))[['bmi_mean_category']]"),
    ("df.select(weight_histogram=pl.col('weight').histogram(10))", "df_pandas['weight'].plot.hist(bins=10)"),
    ("df.select(name_upper=pl.col('name').str.to_uppercase())", "df_pandas.assign(name_upper=df_pandas['name'].str.upper())"),
    ("df.select(name_lower=pl.col('name').str.to_lowercase())", "df_pandas.assign(name_lower=df_pandas['name'].str.lower())"),
    ("df.select(birthdate_day=pl.col('birthdate').dt.day())", "df_pandas.assign(birthdate_day=df_pandas['birthdate'].dt.day)"),
    ("df.select(birthdate_month=pl.col('birthdate').dt.month())", "df_pandas.assign(birthdate_month=df_pandas['birthdate'].dt.month)"),
    ("df.select(birthdate_year=pl.col('birthdate').dt.year())", "df_pandas.assign(birthdate_year=df_pandas['birthdate'].dt.year)"),
    ("df.select(weight_percentage=(pl.col('weight') / pl.col('weight').sum()) * 100)", "df_pandas.assign(weight_percentage=(df_pandas['weight'] / df_pandas['weight'].sum()) * 100)"),
]

data_pairs_with_columns = [
    ("df.with_columns(bmi=bmi_expr, avg_bmi=bmi_expr.mean(), ideal_max_bmi=25)", "df_pandas.assign(bmi=df_pandas['weight'] / (df_pandas['height'] ** 2), avg_bmi=df_pandas['bmi'].mean(), ideal_max_bmi=25)"),
    ("df.with_columns(deviation=(bmi_expr - bmi_expr.mean()) / bmi_expr.std())", "df_pandas.assign(deviation=(df_pandas['bmi'] - df_pandas['bmi'].mean()) / df_pandas['bmi'].std())"),
    ("df.with_columns(height_to_weight_ratio=(pl.col('height') / pl.col('weight')))","df_pandas.assign(height_to_weight_ratio=df_pandas['height'] / df_pandas['weight'])"),
    ("df.with_columns(birth_year=pl.col('birthdate').dt.year)", "df_pandas.assign(birth_year=df_pandas['birthdate'].dt.year)"),
    ("df.with_columns(name_length=pl.col('name').str.lengths())", "df_pandas.assign(name_length=df_pandas['name'].str.len())"),
    ("df.with_columns(bmi_category=pl.when(bmi_expr < 18.5).then('Underweight').when(bmi_expr < 25).then('Normal').otherwise('Overweight'))", "df_pandas.assign(bmi_category=pd.cut(df_pandas['bmi'], bins=[-np.inf, 18.5, 25, np.inf], labels=['Underweight', 'Normal', 'Overweight']))"),
    ("df.with_columns(weight_kg=pl.col('weight') * 0.453592)", "df_pandas.assign(weight_kg=df_pandas['weight'] * 0.453592)"),
    ("df.with_columns(height_meters=pl.col('height') * 0.3048)", "df_pandas.assign(height_meters=df_pandas['height'] * 0.3048)"),
    ("df.with_columns(weight_category=pl.when(pl.col('weight') < 60).then('Light').when(pl.col('weight') < 80).then('Medium').otherwise('Heavy'))", "df_pandas.assign(weight_category=pd.cut(df_pandas['weight'], bins=[-np.inf, 60, 80, np.inf], labels=['Light', 'Medium', 'Heavy']))"),
    ("df.with_columns(bmi_index=(pl.col('weight') / (pl.col('height') ** 2)))", "df_pandas.assign(bmi_index=(df_pandas['weight'] / (df_pandas['height'] ** 2)))"),
    ("df.with_columns(age=pl.col('birthdate').dt.year - 2023)", "df_pandas.assign(age=2023 - df_pandas['birthdate'].dt.year)"),
    ("df.with_columns(max_weight=pl.col('weight').max())", "pd.DataFrame({'max_weight': [df_pandas['weight'].max()]})"),
    ("df.with_columns(min_weight=pl.col('weight').min())", "pd.DataFrame({'min_weight': [df_pandas['weight'].min()]})"),
    ("df.with_columns(mean_weight=pl.col('weight').mean())", "pd.DataFrame({'mean_weight': [df_pandas['weight'].mean()]})"),
    ("df.with_columns(count=pl.count())", "pd.DataFrame({'count': [df_pandas.shape[0]]})"),
    ("df.with_columns(median_bmi=bmi_expr.median())", "pd.DataFrame({'median_bmi': [df_pandas['bmi'].median()]})"),
    ("df.with_columns(weight_variance=pl.col('weight').var())", "pd.DataFrame({'weight_variance': [df_pandas['weight'].var()]})"),
    ("df.with_columns(bmi_stddev=bmi_expr.std())", "pd.DataFrame({'bmi_stddev': [df_pandas['bmi'].std()]})"),
    ("df.with_columns(sum_weight=pl.col('weight').sum())", "pd.DataFrame({'sum_weight': [df_pandas['weight'].sum()]})"),
    ("df.with_columns(avg_height=pl.col('height').mean())", "pd.DataFrame({'avg_height': [df_pandas['height'].mean()]})"),
    ("df.with_columns(bmi_distribution=pl.col('bmi').value_counts())", "df_pandas['bmi'].value_counts().reset_index(name='count').rename(columns={'index': 'bmi'})"),
    ("df.with_columns(weight_percentile=pl.col('weight').quantile(0.75))", "pd.DataFrame({'weight_percentile': [df_pandas['weight'].quantile(0.75)]})"),
    ("df.with_columns(bmi_range=(bmi_expr.max() - bmi_expr.min()))", "pd.DataFrame({'bmi_range': [df_pandas['bmi'].max() - df_pandas['bmi'].min()]})"),
    ("df.with_columns(bmi_rounded=pl.round(bmi_expr, 1))", "df_pandas.assign(bmi_rounded=df_pandas['bmi'].round(1))"),
    ("df.with_columns(log_weight=pl.col('weight').log())", "df_pandas.assign(log_weight=np.log(df_pandas['weight']))"),
    ("df.with_columns(exp_height=pl.col('height').exp())", "df_pandas.assign(exp_height=np.exp(df_pandas['height']))"),
    ("df.with_columns(sqrt_weight=pl.col('weight').sqrt())", "df_pandas.assign(sqrt_weight=np.sqrt(df_pandas['weight']))"),
    ("df.with_columns(inverse_bmi=1 / bmi_expr)", "df_pandas.assign(inverse_bmi=1 / df_pandas['bmi'])"),
    ("df.with_columns(bmi_to_category=pl.when(bmi_expr < 18.5).then('Underweight').when(bmi_expr < 25).then('Normal').otherwise('Overweight'))", "df_pandas.assign(bmi_to_category=pd.cut(df_pandas['bmi'], bins=[-np.inf, 18.5, 25, np.inf], labels=['Underweight', 'Normal', 'Overweight']))"),
    ("df.with_columns(age_group=pl.when(pl.col('age') < 18).then('Minor').when(pl.col('age') < 65).then('Adult').otherwise('Senior'))", "df_pandas.assign(age_group=pd.cut(df_pandas['age'], bins=[-np.inf, 18, 65, np.inf], labels=['Minor', 'Adult', 'Senior']))"),
    ("df.with_columns(bmi_mean_category=pl.when(bmi_expr.mean() < 18.5).then('Underweight').when(bmi_expr.mean() < 25).then('Normal').otherwise('Overweight'))", "pd.DataFrame({'bmi_mean_category': [df_pandas['bmi'].mean()]}).assign(bmi_mean_category=lambda x: np.where(x['bmi_mean_category'] < 18.5, 'Underweight', np.where(x['bmi_mean_category'] < 25, 'Normal', 'Overweight')))[['bmi_mean_category']]"),
    ("df.with_columns(weight_histogram=pl.col('weight').histogram(10))", "df_pandas['weight'].plot.hist(bins=10)"),
    ("df.with_columns(name_upper=pl.col('name').str.to_uppercase())", "df_pandas.assign(name_upper=df_pandas['name'].str.upper())"),
    ("df.with_columns(name_lower=pl.col('name').str.to_lowercase())", "df_pandas.assign(name_lower=df_pandas['name'].str.lower())"),
    ("df.with_columns(birthdate_day=pl.col('birthdate').dt.day())", "df_pandas.assign(birthdate_day=df_pandas['birthdate'].dt.day)"),
    ("df.with_columns(birthdate_month=pl.col('birthdate').dt.month())", "df_pandas.assign(birthdate_month=df_pandas['birthdate'].dt.month)"),
    ("df.with_columns(birthdate_year=pl.col('birthdate').dt.year())", "df_pandas.assign(birthdate_year=df_pandas['birthdate'].dt.year)"),
    ("df.with_columns(weight_percentage=(pl.col('weight') / pl.col('weight').sum()) * 100)", "df_pandas.assign(weight_percentage=(df_pandas['weight'] / df_pandas['weight'].sum()) * 100)"),
]

data_pairs_filter = [
    ("df.filter(pl.col('birthdate').is_between(date(1982, 12, 31), date(1996, 1, 1)))", "df_pandas[(df_pandas['birthdate'] > '1982-12-31') & (df_pandas['birthdate'] < '1996-01-01')]"),
    ("df.filter(pl.col('height') > 1.7)", "df_pandas[df_pandas['height'] > 1.7]"),
    ("df.filter(pl.col('weight') < 60)", "df_pandas[df_pandas['weight'] < 60]"),
    ("df.filter(pl.col('weight').is_in([55, 60, 65]))", "df_pandas[df_pandas['weight'].isin([55, 60, 65])]"),
    ("df.filter(pl.col('height').is_not_null())", "df_pandas[df_pandas['height'].notnull()]"),
    ("df.filter(pl.col('name').str.contains('A'))", "df_pandas[df_pandas['name'].str.contains('A')]"),
    ("df.filter(pl.col('weight') > 70).filter(pl.col('height') < 1.8)", "df_pandas[(df_pandas['weight'] > 70) & (df_pandas['height'] < 1.8)]"),
    ("df.filter(pl.col('birthdate').dt.year() > 1990)", "df_pandas[df_pandas['birthdate'].dt.year > 1990]"),
    ("df.filter(pl.col('weight') >= 50)", "df_pandas[df_pandas['weight'] >= 50]"),
    ("df.filter(pl.col('name').str.lengths() > 10)", "df_pandas[df_pandas['name'].str.len() > 10]"),
    ("df.filter(pl.col('height').is_between(1.6, 1.9))", "df_pandas[(df_pandas['height'] >= 1.6) & (df_pandas['height'] <= 1.9)]"),
    ("df.filter(pl.col('birthdate').dt.month() == 12)", "df_pandas[df_pandas['birthdate'].dt.month == 12]"),
    ("df.filter(pl.col('weight') < pl.col('height') * 100)", "df_pandas[df_pandas['weight'] < df_pandas['height'] * 100]"),
    ("df.filter(pl.col('name').str.startswith('A'))", "df_pandas[df_pandas['name'].str.startswith('A')]"),
    ("df.filter(pl.col('birthdate').dt.year() < 1985)", "df_pandas[df_pandas['birthdate'].dt.year < 1985]"),
    ("df.filter(pl.col('height') >= 1.75)", "df_pandas[df_pandas['height'] >= 1.75]"),
    ("df.filter(pl.col('weight').is_between(50, 80))", "df_pandas[(df_pandas['weight'] >= 50) & (df_pandas['weight'] <= 80)]"),
    ("df.filter(pl.col('name').str.contains('Cooper'))", "df_pandas[df_pandas['name'].str.contains('Cooper')]"),
    ("df.filter(pl.col('birthdate').dt.day() == 1)", "df_pandas[df_pandas['birthdate'].dt.day == 1]"),
    ("df.filter(pl.col('weight').is_not_null())", "df_pandas[df_pandas['weight'].notnull()]"),
    ("df.filter(pl.col('height') < 1.6)", "df_pandas[df_pandas['height'] < 1.6]"),
    ("df.filter(pl.col('bmi') > 25)", "df_pandas[df_pandas['weight'] / (df_pandas['height'] ** 2) > 25]"),
    ("df.filter(pl.col('height') == 1.75)", "df_pandas[df_pandas['height'] == 1.75]"),
    ("df.filter(pl.col('birthdate').is_not_between(date(1980, 1, 1), date(1990, 1, 1)))", "df_pandas[~df_pandas['birthdate'].between('1980-01-01', '1990-01-01')]"),
    ("df.filter(pl.col('name').str.contains('Brown'))", "df_pandas[df_pandas['name'].str.contains('Brown')]"),
    ("df.filter(pl.col('birthdate').dt.month() != 12)", "df_pandas[df_pandas['birthdate'].dt.month != 12]"),
    ("df.filter(pl.col('weight') > 100)", "df_pandas[df_pandas['weight'] > 100]"),
    ("df.filter(pl.col('height') <= 1.5)", "df_pandas[df_pandas['height'] <= 1.5]"),
    ("df.filter(pl.col('birthdate') < date(2000, 1, 1))", "df_pandas[df_pandas['birthdate'] < '2000-01-01']"),
    ("df.filter(pl.col('weight').is_not_null() & (pl.col('height') > 1.6))", "df_pandas[df_pandas['weight'].notnull() & (df_pandas['height'] > 1.6)]"),
    ("df.filter(pl.col('name').str.endswith('er'))", "df_pandas[df_pandas['name'].str.endswith('er')]"),
    ("df.filter(pl.col('height') != 1.8)", "df_pandas[df_pandas['height'] != 1.8]"),
    ("df.filter(pl.col('weight') < pl.col('height') * 100)", "df_pandas[df_pandas['weight'] < df_pandas['height'] * 100]"),
    ("df.filter(pl.col('name').is_not_null())", "df_pandas[df_pandas['name'].notnull()]"),
    ("df.filter(pl.col('birthdate') >= date(1980, 1, 1))", "df_pandas[df_pandas['birthdate'] >= '1980-01-01']"),
    ("df.filter(pl.col('height').is_in([1.6, 1.7, 1.8]))", "df_pandas[df_pandas['height'].isin([1.6, 1.7, 1.8])]"),
    ("df.filter(pl.col('birthdate').dt.year().is_in([1985, 1986, 1987]))", "df_pandas[df_pandas['birthdate'].dt.year.isin([1985, 1986, 1987])]"),
]

data_pairs_group_by = [
    (
        "df.group_by((pl.col('birthdate').dt.year() // 10 * 10).alias('decade')).agg(pl.col('name'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year // 10 * 10)['name'].apply(list)"
    ),
    (
        "df.group_by((pl.col('birthdate').dt.year() // 10 * 10).alias('decade'), (pl.col('height') < 1.7).alias('short?')).agg(pl.col('name'))",
        "df_pandas.groupby([df_pandas['birthdate'].dt.year // 10 * 10, df_pandas['height'] < 1.7])['name'].apply(list)"
    ),
    (
        "df.group_by((pl.col('birthdate').dt.year() // 10 * 10).alias('decade'), (pl.col('height') < 1.7).alias('short?')).agg(pl.len(), pl.col('height').max().alias('tallest'), pl.col('weight', 'height').mean().name.prefix('avg_'))",
        "df_pandas.groupby([df_pandas['birthdate'].dt.year // 10 * 10, df_pandas['height'] < 1.7]).agg({'weight': 'mean', 'height': 'max'}).rename(columns={'weight': 'avg_weight', 'height': 'tallest'})"
    ),
    (
        "df.group_by(pl.col('name')).agg(pl.count().alias('count'))",
        "df_pandas.groupby('name').size().reset_index(name='count')"
    ),
    (
        "df.group_by(pl.col('weight')).agg(pl.mean('height').alias('avg_height'))",
        "df_pandas.groupby('weight')['height'].mean().reset_index(name='avg_height')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.sum('weight').alias('total_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['weight'].sum().reset_index(name='total_weight')"
    ),
    (
        "df.group_by(pl.col('name')).agg(pl.min('height').alias('shortest'))",
        "df_pandas.groupby('name')['height'].min().reset_index(name='shortest')"
    ),
    (
        "df.group_by(pl.col('name')).agg(pl.max('weight').alias('heaviest'))",
        "df_pandas.groupby('name')['weight'].max().reset_index(name='heaviest')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.month()).agg(pl.mean('weight').alias('avg_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.month)['weight'].mean().reset_index(name='avg_weight')"
    ),
    (
        "df.group_by((pl.col('birthdate').dt.year() // 5 * 5).alias('half_decade')).agg(pl.col('height').std().alias('std_height'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year // 5 * 5)['height'].std().reset_index(name='std_height')"
    ),
    (
        "df.group_by(pl.col('height')).agg(pl.count()).sort('count', reverse=True)",
        "df_pandas.groupby('height').size().reset_index(name='count').sort_values(by='count', ascending=False)"
    ),
    (
        "df.group_by(pl.col('weight')).agg(pl.first('name').alias('first_name'))",
        "df_pandas.groupby('weight')['name'].first().reset_index(name='first_name')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.count().alias('count'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year).size().reset_index(name='count')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.week()).agg(pl.mean('weight').alias('avg_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.isocalendar().week)['weight'].mean().reset_index(name='avg_weight')"
    ),
    (
        "df.group_by(pl.col('name')).agg(pl.count().alias('occurrences'))",
        "df_pandas['name'].value_counts().reset_index(name='occurrences').rename(columns={'index': 'name'})"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.sum('weight').alias('total_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['weight'].sum().reset_index(name='total_weight')"
    ),
    (
        "df.group_by(pl.col('height')).agg(pl.mean('weight').alias('avg_weight'))",
        "df_pandas.groupby('height')['weight'].mean().reset_index(name='avg_weight')"
    ),
    (
        "df.group_by((pl.col('height') // 0.5).cast(pl.Int32).alias('height_bucket')).agg(pl.mean('weight').alias('avg_weight'))",
        "df_pandas.groupby((df_pandas['height'] // 0.5).astype(int))['weight'].mean().reset_index(name='avg_weight')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.col('weight').median().alias('median_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['weight'].median().reset_index(name='median_weight')"
    ),
    (
        "df.group_by(pl.col('height')).agg(pl.max('weight').alias('max_weight'))",
        "df_pandas.groupby('height')['weight'].max().reset_index(name='max_weight')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.month()).agg(pl.count().alias('count'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.month)['birthdate'].count().reset_index(name='count')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.day()).agg(pl.mean('weight').alias('avg_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.day)['weight'].mean().reset_index(name='avg_weight')"
    ),
    (
        "df.group_by((pl.col('weight') > 70).alias('heavy')).agg(pl.count().alias('count'))",
        "df_pandas.groupby(df_pandas['weight'] > 70).size().reset_index(name='count')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.mean('height').alias('avg_height'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['height'].mean().reset_index(name='avg_height')"
    ),
    (
        "df.group_by(pl.col('name')).agg(pl.std('weight').alias('std_weight'))",
        "df_pandas.groupby('name')['weight'].std().reset_index(name='std_weight')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.first('height').alias('first_height'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['height'].first().reset_index(name='first_height')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.last('weight').alias('last_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['weight'].last().reset_index(name='last_weight')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.month()).agg(pl.count().alias('count'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.month).size().reset_index(name='count')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.mean('height').alias('avg_height'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['height'].mean().reset_index(name='avg_height')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.sum('weight').alias('total_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['weight'].sum().reset_index(name='total_weight')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.month()).agg(pl.sum('weight').alias('total_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.month)['weight'].sum().reset_index(name='total_weight')"
    ),
    (
        "df.group_by(pl.col('name')).agg(pl.count('weight').alias('count_weight'))",
        "df_pandas.groupby('name')['weight'].count().reset_index(name='count_weight')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.col('height').min().alias('min_height'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['height'].min().reset_index(name='min_height')"
    ),
    (
        "df.group_by(pl.col('height')).agg(pl.mean('weight').alias('avg_weight'))",
        "df_pandas.groupby('height')['weight'].mean().reset_index(name='avg_weight')"
    ),
    (
        "df.group_by(pl.col('weight')).agg(pl.count().alias('count'))",
        "df_pandas.groupby('weight').size().reset_index(name='count')"
    ),
    (
        "df.group_by(pl.col('name')).agg(pl.first('birthdate').alias('first_birthdate'))",
        "df_pandas.groupby('name')['birthdate'].first().reset_index(name='first_birthdate')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.last('weight').alias('last_weight'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['weight'].last().reset_index(name='last_weight')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.std('height').alias('std_height'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year)['height'].std().reset_index(name='std_height')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.month()).agg(pl.mean('height').alias('avg_height'))",
        "df_pandas.groupby(df_pandas['birthdate'].dt.month)['height'].mean().reset_index(name='avg_height')"
    ),
    (
        "df.group_by(pl.col('birthdate').dt.year()).agg(pl.count()).alias('count')",
        "df_pandas.groupby(df_pandas['birthdate'].dt.year).size().reset_index(name='count')"
    ),
]



# Create a DataFrame
df = pd.DataFrame(data_pairs, columns=["Polars Code", "Pandas Code"])

# Save to CSV
df.to_csv('pandas_to_polars_pairs.csv', index=False)
