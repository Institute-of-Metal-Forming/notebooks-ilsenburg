# Notebooks Workshop Ilsenburg

## How to Use

### Running From a Local Copy

Download or clone the contents of the repository, then create a virtual environment holding the respective dependencies with [uv](https://docs.astral.sh/uv) with:

```shell
uv sync
```

Then, run the Jupyter Lab server with the command line below and open the displayed URL in your browser to start working.

```shell
uv run jupyter lab
```

> [!WARNING]
> Do not execute the cells labeled with `# only for Google Colab` when working this way or unnecessary/destructive files will be created in your local copy.

### Running in Google Colab

Click on the badge beneath the notebooks listed below to open them in Colab. 

> [!IMPORTANT]
> Remember to always run the cell labeled with `# only for Google Colab` to install required dependencies and fetch required additional files.

- Parameter Fitting of Emprical Flow Stress Models (Freiberg Model) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institute-of-metal-forming/notebooks-ilsenburg/blob/master/flow-stress/Freiberg.ipynb)
- Parameter Fitting of Emprical Flow Stress Models (Sellars-Tegart Model) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institute-of-metal-forming/notebooks-ilsenburg/blob/master/flow-stress/SellarsTegart.ipynb)
- Parameter Fitting of Emprical Flow Stress Models (Artificial Neural Network Model) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institute-of-metal-forming/notebooks-ilsenburg/blob/master/flow-stress/NeuralNetwork.ipynb)
- Predict Hot Flow Stress Curves Qualitively by Using Avrami Recrystallisation Model [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institute-of-metal-forming/notebooks-ilsenburg/blob/master/flow-stress/LutonSellarsHotFlowStressModelling.ipynb)
- Flat Rolling with PyRolL [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institute-of-metal-forming/notebooks-ilsenburg/blob/master/flat-rolling/pyroll-flat-rolling.ipynb)
- Elastic Response of the Roll (Roll-Flattening) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institute-of-metal-forming/notebooks-ilsenburg/blob/master/roll-flattening/roll_flattening_hitchcock.ipynb)
- Elastic Response of the Rolling Mill (Mill Spring) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institute-of-metal-forming/notebooks-ilsenburg/blob/master/elastic-mill-spring/elastic_mill_spring.ipynb)


## License

The contents of this repository are distributed under the terms of the [MIT License](LICENSE).
