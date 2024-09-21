import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    res = []
    combine_df = sales.merge(product, left_on = 'product_id', right_on = 'product_id', how = 'left')
    for i in range(len(combine_df)):
        p_name = combine_df['product_name'][i]
        sales_date = combine_df['sale_date'][i]
        p_id = combine_df['product_id'][i]

        if (sales_date >= '2019-01-01') & (sales_date <= '2019-03-31'):
            res.append([p_id, p_name])
    print(*res)
    return product