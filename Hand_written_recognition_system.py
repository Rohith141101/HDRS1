{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zI_AXKKHobQp"
      },
      "source": [
        "**Importing Necessary Libraries**\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "g9S-8HF3pHPk"
      },
      "outputs": [],
      "source": [
        "import numpy #used for numerical analysis\n",
        "import tensorflow #open source used for both ML and DL for computation\n",
        "from tensorflow.keras.datasets import mnist #Mnist dataset\n",
        "from tensorflow.keras.models import Sequential #it is a plain stack of layers\n",
        "from tensorflow.keras import layers #A layer consistes of a tensor-in tensor-out computation function\n",
        "from tensorflow.keras.layers import Dense, Flatten #Dense-Dense layer is the regular deeply connected\n",
        "#Flatten-used for flattening the input or change the dimension\n",
        "from tensorflow.keras.layers import Conv2D #Convolutional Layer\n",
        "from keras.optimizers import Adam #optimizer\n",
        "from keras.utils import np_utils #used for one-hot coding"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LEThdTpSiChl"
      },
      "source": [
        "**Load Data**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W3XQ_d0czNNV",
        "outputId": "ff1b15e3-3582-4ceb-d7ed-66a710197c6a"
      },
      "outputs": [],
      "source": [
        "(x_train, y_train), (X_test, y_test)=mnist.load_data() #splitting the mnist data into train and test"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YNh-ejtY0J-7",
        "outputId": "1463fc0e-30b4-4b61-c2c2-3eed6f262419"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "(60000, 28, 28)\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "(10000, 28, 28)"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "print(x_train.shape)#shape is used for give the dimension values #60000-rows 28x28-pixels paint\n",
        "(68000, 28, 28)\n",
        "(10000, 28, 28)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "R00MOD9diNkV"
      },
      "source": [
        "**Understanding the data**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XSZ_Pp1q09vR",
        "outputId": "12b14490-06a5-4ae6-8e60-f66649cb4193"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "array([[  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   3,\n",
              "         18,  18,  18, 126, 136, 175,  26, 166, 255, 247, 127,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,  30,  36,  94, 154, 170,\n",
              "        253, 253, 253, 253, 253, 225, 172, 253, 242, 195,  64,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,  49, 238, 253, 253, 253, 253,\n",
              "        253, 253, 253, 253, 251,  93,  82,  82,  56,  39,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,  18, 219, 253, 253, 253, 253,\n",
              "        253, 198, 182, 247, 241,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,  80, 156, 107, 253, 253,\n",
              "        205,  11,   0,  43, 154,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,  14,   1, 154, 253,\n",
              "         90,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 139, 253,\n",
              "        190,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  11, 190,\n",
              "        253,  70,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  35,\n",
              "        241, 225, 160, 108,   1,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "         81, 240, 253, 253, 119,  25,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,  45, 186, 253, 253, 150,  27,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,  16,  93, 252, 253, 187,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0, 249, 253, 249,  64,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,  46, 130, 183, 253, 253, 207,   2,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  39,\n",
              "        148, 229, 253, 253, 253, 250, 182,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  24, 114, 221,\n",
              "        253, 253, 253, 253, 201,  78,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,  23,  66, 213, 253, 253,\n",
              "        253, 253, 198,  81,   2,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,  18, 171, 219, 253, 253, 253, 253,\n",
              "        195,  80,   9,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,  55, 172, 226, 253, 253, 253, 253, 244, 133,\n",
              "         11,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0, 136, 253, 253, 253, 212, 135, 132,  16,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0],\n",
              "       [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,\n",
              "          0,   0]], dtype=uint8)"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "x_train[0] #printing the first image"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HwfP60n80B5k",
        "outputId": "d81d5ded-0cfb-42b7-86ba-8ee547fb3d3d"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "y_train[0] #print the label of first image"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "2LkfKV6h1aDW",
        "outputId": "3b81cdcf-d88a-4916-a148-b8026f250857"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<matplotlib.image.AxesImage at 0x24569ba83d0>"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        },
        {
          "data": {
            "image/png": "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wAQBAgCYIEAAABMECABgggABAEwQIACACQIEADBBgAAAJrgZKfAVgWsme8/85V/8b9z5qxkvec/MuuC498y51OW6vWfqPy/wP1Bvi/8MBiSugAAAJggQAMAEAQIAmCBAAAATBAgAYIIAAQBMECAAgAkCBAAwQYAAACYIEADABAECAJggQAAAE9yMFAPeiILx3jP778yL61hPLH7Ne2bRRZ/FdayB7JG2a7xnan9xnffMt16q857B0MEVEADABAECAJjwClBlZaWuvfZapaWlKSsrSwsWLFBDQ0PMPseOHVN5ebkuvvhiXXTRRVq0aJHa2toSumgAwODnFaDa2lqVl5ervr5e7777rrq7uzV37lx1dnZG97n//vv11ltvaePGjaqtrdXBgwd18803J3zhAIDBzetDCFu3bo35uqqqSllZWdq1a5dmzZqlcDisX//619qwYYO+973vSZLWr1+vK6+8UvX19bruOv83KQEAQ9M3eg8oHA5LkjIyMiRJu3btUnd3t0pKSqL7TJo0SePGjVNdXd+fdunq6lIkEonZAABDX9wB6u3t1cqVKzVjxgxNnjxZktTa2qrU1FSNHj06Zt/s7Gy1trb2+fdUVlYqFApFt/z8/HiXBAAYROIOUHl5ufbu3avXXvP/uYmvqqioUDgcjm7Nzc3f6O8DAAwOcf0g6ooVK/T2229r+/btGjt2bPTxnJwcHT9+XO3t7TFXQW1tbcrJyenz7woGgwoGg/EsAwAwiHldATnntGLFCm3atEnbtm1TQUFBzPPTpk1TSkqKqquro481NDTowIEDKi4uTsyKAQBDgtcVUHl5uTZs2KAtW7YoLS0t+r5OKBTSyJEjFQqFdNddd2nVqlXKyMhQenq67rvvPhUXF/MJOABADK8APf/885Kk2bNnxzy+fv16LV26VJL085//XMOGDdOiRYvU1dWl0tJS/fKXv0zIYgEAQ0fAOeesF/FVkUhEoVBIszVfIwIp1svBGYy4ZJz3THharvfM4h9vPftOp7hn9F+9Zwa6B1r8v4tQ90v/m4pKUkbV7/2HenviOhaGnhOuWzXaonA4rPT09H73415wAAATBAgAYIIAAQBMECAAgAkCBAAwQYAAACYIEADABAECAJggQAAAEwQIAGCCAAEATBAgAIAJAgQAMBHXb0TFwDUit+/fPHsmn794YVzHWl5Q6z1z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6yUlVTgcliRlZGRIknbt2qXu7u6Y18OkSZM0bty4If16OPU8fOmVV15RZmamJk+erIqKCh09etRief0acDcjPdVnn32mnp4eZWdnxzyenZ2tP//5z0arslFUVKSqqipdccUVamlp0Zo1a3T99ddr7969SktLs16eidbWVknq8/Xx5XPni3nz5unmm29WQUGB9u/fr0ceeURlZWWqq6vT8OHDrZeXcL29vVq5cqVmzJihyZMnSzr5ekhNTdXo0aNj9h3Kr4e+zoMk3X777Ro/frzy8vK0Z88ePfzww2poaNCbb75puNpYAz5A+IeysrLon6dOnaqioiKNHz9eb7zxhu666y7DlWEguPXWW6N/njJliqZOnaqJEyeqpqZGc+bMMVxZcpSXl2vv3r3nxfugZ9Lfebj77rujf54yZYpyc3M1Z84c7d+/XxMnTjzXy+zTgP8WXGZmpoYPH37ap1ja2tqUk5NjtKqBYfTo0br88svV2NhovRQzX74GeH2cbsKECcrMzBySr48VK1bo7bff1vvvvx/z61tycnJ0/Phxtbe3x+w/VF8P/Z2HvhQVFUnSgHo9DPgApaamatq0aaquro4+1tvbq+rqahUXFxuuzN6RI0e0f/9+5ebmWi/FTEFBgXJycmJeH5FIRDt27DjvXx+ffvqpDh8+PKReH845rVixQps2bdK2bdtUUFAQ8/y0adOUkpIS83poaGjQgQMHhtTr4WznoS+7d++WpIH1erD+FMTX8dprr7lgMOiqqqrcH//4R3f33Xe70aNHu9bWVuulnVMPPPCAq6mpcU1NTe53v/udKykpcZmZme7QoUPWS0uqjo4O9/HHH7uPP/7YSXJPP/20+/jjj93f/vY355xzP/3pT93o0aPdli1b3J49e9z8+fNdQUGB++KLL4xXnlhnOg8dHR3uwQcfdHV1da6pqcm999577rvf/a677LLL3LFjx6yXnjDLly93oVDI1dTUuJaWluh29OjR6D733HOPGzdunNu2bZvbuXOnKy4udsXFxYarTryznYfGxkb34x//2O3cudM1NTW5LVu2uAkTJrhZs2YZrzzWoAiQc84999xzbty4cS41NdVNnz7d1dfXWy/pnFu8eLHLzc11qamp7tvf/rZbvHixa2xstF5W0r3//vtO0mnbkiVLnHMnP4r92GOPuezsbBcMBt2cOXNcQ0OD7aKT4Ezn4ejRo27u3LluzJgxLiUlxY0fP94tW7ZsyP2ftL7++SW59evXR/f54osv3L333uu+9a1vuVGjRrmFCxe6lpYWu0UnwdnOw4EDB9ysWbNcRkaGCwaD7tJLL3U/+tGPXDgctl34Kfh1DAAAEwP+PSAAwNBEgAAAJggQAMAEAQIAmCBAAAATBAgAYIIAAQBMECAAgAkCBAAwQYAAACYIEADABAECAJj4f4W4/AnknuSPAAAAAElFTkSuQmCC",
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "import matplotlib.pyplot as plt #used for data visualization \n",
        "plt.imshow(x_train[0])  #ploting the index=0 image\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "869lfQ-2it74"
      },
      "source": [
        "**Reshaping Dataset**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "M566wpc319ka"
      },
      "outputs": [],
      "source": [
        "\n",
        "#Reshaping to format which CNN expects (batch, height, width, channels)\n",
        "x_train=x_train.reshape(60000, 28, 28, 1).astype('float32') \n",
        "X_test= X_test.reshape(10000, 28, 28, 1).astype('float32')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CDCUdDzmi4JF"
      },
      "source": [
        "**One-Hot Encoding**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "WqB9Q0W427sy"
      },
      "outputs": [],
      "source": [
        "\n",
        "#one hot encode\n",
        "number_of_classes = 10 #storing the no. of classes in a variable\n",
        "y_train= np_utils.to_categorical (y_train, number_of_classes) #converts the output in binary format\n",
        "y_test= np_utils.to_categorical (y_test, number_of_classes)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rXL4lJCs3ZvT",
        "outputId": "68e9848f-11de-4612-f03b-66b3409c4a4d"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "array([0., 0., 0., 0., 0., 1., 0., 0., 0., 0.], dtype=float32)"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "y_train[0]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "S4Wr_kp6jPsG"
      },
      "source": [
        "**Creating the Model**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "SKoe5brj3eEv"
      },
      "outputs": [],
      "source": [
        "\n",
        "#create model\n",
        "model=Sequential()\n",
        "#adding model Layer\n",
        "model.add(Conv2D (64, (3, 3), input_shape=(28, 28, 1), activation='relu'))\n",
        "model.add(Conv2D (32, (3, 3), activation='relu'))\n",
        "#model.add(Conv2D (32, (3, 3), activation=\"relu\"))\n",
        "#flatten the dimension of the image\n",
        "model.add(Flatten())\n",
        "#output Layer with 10 neurons\n",
        "model.add(Dense(number_of_classes, activation='softmax'))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wHhsUwlhjbET"
      },
      "source": [
        "**Compiling the Model**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "8WBg3P9d3tb7"
      },
      "outputs": [],
      "source": [
        "#compile model\n",
        "model.compile(loss='categorical_crossentropy', optimizer=\"Adam\", metrics=['accuracy'])\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VVILJWPcjmYv"
      },
      "source": [
        "**Fitting the Model**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t3WKvA1r4SOy",
        "outputId": "8edcdd84-16c7-4dd1-de19-98fcfac0b3e4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Epoch 1/5\n",
            "1875/1875 [==============================] - 132s 70ms/step - loss: 0.2377 - accuracy: 0.9516 - val_loss: 0.0848 - val_accuracy: 0.9724\n",
            "Epoch 2/5\n",
            "1875/1875 [==============================] - 737s 393ms/step - loss: 0.0690 - accuracy: 0.9789 - val_loss: 0.0888 - val_accuracy: 0.9734\n",
            "Epoch 3/5\n",
            "1875/1875 [==============================] - 2060s 1s/step - loss: 0.0506 - accuracy: 0.9839 - val_loss: 0.0849 - val_accuracy: 0.9750\n",
            "Epoch 4/5\n",
            "1875/1875 [==============================] - 142s 76ms/step - loss: 0.0385 - accuracy: 0.9880 - val_loss: 0.0799 - val_accuracy: 0.9783\n",
            "Epoch 5/5\n",
            "1875/1875 [==============================] - 146s 78ms/step - loss: 0.0292 - accuracy: 0.9912 - val_loss: 0.1118 - val_accuracy: 0.9770\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "<keras.callbacks.History at 0x2456bda0eb0>"
            ]
          },
          "execution_count": 16,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "#fit the model\n",
        "model.fit(x_train,y_train, validation_data=(X_test,y_test),epochs=5,batch_size=32)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dGLqObJcj5Kv"
      },
      "source": [
        "**Observing the Metrics**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y0z8HZxZ5lvn",
        "outputId": "e35fa2a4-aa94-44d6-e26f-ae34a275ec85"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Metrics(Test loss & Test Accuracy): \n",
            "[0.11176875233650208, 0.9769999980926514]\n"
          ]
        }
      ],
      "source": [
        "# final evaluation of the model\n",
        "metrics = model.evaluate(X_test, y_test, verbose=0) \n",
        "print(\"Metrics(Test loss & Test Accuracy): \") \n",
        "print(metrics)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-5Hik7xlkF0i"
      },
      "source": [
        "**Predicting the Output**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nSbvqOgc5-Ui",
        "outputId": "535ca0e3-4cbd-47cd-bfe4-2ea4ec876d16"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1/1 [==============================] - 0s 88ms/step\n",
            "[[2.0987873e-15 1.3553919e-11 7.8879001e-16 1.2282751e-10 7.5598208e-20\n",
            "  1.0000000e+00 3.3646277e-16 8.9681826e-16 5.7064644e-12 5.2672003e-15]\n",
            " [1.0000000e+00 1.6331215e-16 4.9389035e-11 1.5317940e-18 2.7015812e-19\n",
            "  7.0999600e-18 2.3778626e-10 1.3106278e-18 9.0027822e-13 1.9716367e-14]\n",
            " [1.9264086e-25 3.8128017e-10 9.7486106e-18 2.1892119e-17 1.0000000e+00\n",
            "  1.3107735e-17 2.7074762e-16 2.9170167e-13 1.8926358e-14 2.1987608e-10]\n",
            " [8.9771508e-15 9.9999952e-01 2.4637039e-08 3.0933966e-12 1.2311122e-07\n",
            "  3.9244551e-14 1.9319325e-12 7.8979687e-12 3.8027650e-07 7.5201941e-17]]\n"
          ]
        }
      ],
      "source": [
        "prediction=model.predict(x_train[:4]) \n",
        "print(prediction)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F-GEugLL61VG",
        "outputId": "58a990af-62d2-4cd5-8623-aacc9f35a6a5"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[5 0 4 1]\n",
            "[[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]\n",
            " [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]\n",
            " [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]\n",
            " [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "print(np.argmax(prediction, axis=1)) #print our label from first 4 images\n",
        "print(y_test[:4]) #printing the actual labels"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rzJq_QLokSM6"
      },
      "source": [
        "**Saving the Model**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "id": "9FoS6QTW7Nrz"
      },
      "outputs": [],
      "source": [
        "# save the model\n",
        "model.save(r'models/mnistCNN.h5')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kl1jeZlukWZC"
      },
      "source": [
        "**Taking images as inputs and checking results**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h1qvucww90ru",
        "outputId": "15ba829c-793a-4670-c0a6-8bf7bb434af0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1/1 [==============================] - 0s 138ms/step\n",
            "0\n",
            "1/1 [==============================] - 0s 24ms/step\n",
            "0\n",
            "1/1 [==============================] - 0s 26ms/step\n",
            "2\n",
            "1/1 [==============================] - 0s 24ms/step\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "from tensorflow.keras.models import load_model\n",
        "model = load_model(r'models/mnistCNN.h5')\n",
        "from PIL import Image\n",
        "import numpy as np\n",
        "for index in range(4):\n",
        "    img = Image.open('static/uploads/' + str(index) + '.png').convert(\"L\")\n",
        "    img = img.resize((28,28))\n",
        "    im2arr=np.array(img)\n",
        "    im2arr = im2arr.reshape(1,28,28,1)\n",
        "    y_pred = model.predict(im2arr)\n",
        "    predict = np.argmax(y_pred)\n",
        "    print(predict)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jjAHw18tzPza"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "collapsed_sections": [],
      "provenance": []
    },
    "gpuClass": "standard",
    "kernelspec": {
      "display_name": "Python 3.10.7 64-bit",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.7"
    },
    "vscode": {
      "interpreter": {
        "hash": "18827b9f982ff3f53faeefbfa66b7ef20a546d37fb0bf69af0413a338fc94c05"
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
