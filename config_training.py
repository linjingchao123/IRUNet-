config = {'train_data_path': ['../$DOWNLOADLUNA16PATH/LUNA16/subset0/'],
          # '../../pytorch/DeepLung-master/$DOWNLOADLUNA16PATH/subset1/',
          # '../../pytorch/DeepLung-master/$DOWNLOADLUNA16PATH/subset2/',
          # '../../pytorch/DeepLung-master/$DOWNLOADLUNA16PATH/subset3/',
          # '../../pytorch/DeepLung-master/$DOWNLOADLUNA16PATH/subset4/',
          # '../../pytorch/DeepLung-master/$DOWNLOADLUNA16PATH/subset5/',
          # '../../pytorch/DeepLung-master/$DOWNLOADLUNA16PATH/subset6/',
          # '../../pytorch/DeepLung-master/$DOWNLOADLUNA16PATH/subset7/',
          # '../../pytorch/DeepLung-master/$DOWNLOADLUNA16PATH/subset8/'],
          'val_data_path': ['../$DOWNLOADLUNA16PATH/LUNA16/subset9/'],
          'test_data_path': ['../$DOWNLOADLUNA16PATH/LUNA16/subset9/'],

          'train_preprocess_result_path': '../$LUNA16PROPOCESSPATH/',
          # contains numpy for the data and label, which is generated by prepare.py
          'val_preprocess_result_path': '../$LUNA16PROPOCESSPATH/',
          'test_preprocess_result_path': '../$LUNA16PROPOCESSPATH/',

          'train_annos_path': '../$LUNA16ANNOTATIONPATH/luna16/CSVFILES/annotations.csv',
          'val_annos_path': '../$LUNA16ANNOTATIONPATH/luna16/CSVFILES/annotations.csv',
          'test_annos_path': '../$LUNA16ANNOTATIONPATH/luna16/CSVFILES/annotations.csv',

          'black_list': [],

          'preprocessing_backend': 'python',
          }
