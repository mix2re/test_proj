import os
import pandas as pd
import matplotlib.pyplot as plt
class dr_plots:
    def draw_plots(json_file):

        cur_dir = os.path.dirname(__file__)
        results_dir = os.path.join(cur_dir, 'plots/')  
        if not os.path.isdir(results_dir):
             os.makedirs(results_dir)

        df = pd.read_json(json_file)
        title="distribution of gt_corners by rooms"
        df.plot.scatter(x ="name",y='gt_corners',c='DarkBlue',ylabel='corners',xlabel="rooms",xticks=[],title=title) 
        plt.savefig(results_dir + title+".png")

        title="distribution of rb_corners by rooms"
        df.plot.scatter(x ="name",y='rb_corners',c='DarkBlue',ylabel='corners',xlabel="rooms",xticks=[],title=title)
        plt.savefig(results_dir + title+".png")
        
        df=df.sort_values(by=['mean'])
        title="min-max dispersion"
        df.plot(x='name', y=['mean', 'max', 'min'],title=title,figsize=(10,6))
        plt.savefig(results_dir + title+".png")

        df=df.sort_values(by=['floor_mean'])
        title="floor_min-max dispersion"
        df.plot(x='name', y=['floor_mean', 'floor_max', 'floor_min'],title=title,figsize=(10,6))
        plt.savefig(results_dir + title+".png")

        df=df.sort_values(by=['ceiling_mean'])
        title="ceiling_min-max dispersion"
        df.plot(x='name', y=['ceiling_mean', 'ceiling_max', 'ceiling_min'],title=title,figsize=(10,6))
        plt.savefig(results_dir + title+".png")
        return results_dir

        
dr_plots.draw_plots('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')