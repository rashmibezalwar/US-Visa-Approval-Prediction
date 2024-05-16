import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'us_visa')))




from us_visa.pipline.training_pipeline import TrainPipeline


pipline  = TrainPipeline()
pipline.run_pipeline()

