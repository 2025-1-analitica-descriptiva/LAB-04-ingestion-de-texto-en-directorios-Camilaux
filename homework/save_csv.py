import pandas as pd


def save_csv(output_dir, train_data, test_data):
    train_df = pd.DataFrame(train_data)
    train_df.to_csv(output_dir / 'train_dataset.csv', index=False, encoding='utf-8')
    test_df = pd.DataFrame(test_data)
    test_df.to_csv(output_dir / 'test_dataset.csv', index=False, encoding='utf-8')
    return "Archivos train_dataset.csv y test_dataset.csv creados en la carpeta output."