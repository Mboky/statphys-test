{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the calculating time was 0.000000000\n",
      "the calculating time was 0.000000000\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'error(%)')"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import time\n",
    "import scipy\n",
    "from matplotlib import pyplot as plt\n",
    "\n",
    "N = np.arange(30,100.1,1)\n",
    "n = 20\n",
    "\n",
    "def time_function(y,N,n):\n",
    "    \"times a function. returns a string of the time. and the calculated answer.\"\n",
    "    start_time = time.time()\n",
    "    answer = y(N,n)\n",
    "    end_time = time.time()\n",
    "    return \"the calculating time was {:.9f}\".format(end_time-start_time) , answer\n",
    "\n",
    "def fact_method(N,n):\n",
    "    \"using factorials\"\n",
    "    answer = scipy.special.factorial(N,exact=True)/ (scipy.special.factorial(n,exact=True) * scipy.special.factorial(N-n,exact=True))\n",
    "    return answer\n",
    "\n",
    "def sterling(N):\n",
    "    N_fact = np.sqrt(2*np.pi*N) * np.float_power(N,N) * np.exp(-N)\n",
    "    return N_fact\n",
    "\n",
    "def sterling_method(N,n):\n",
    "    answer = sterling(N) / (sterling(n)*sterling(N-n))\n",
    "    return answer\n",
    "    \n",
    "check_fact, ans_fact = time_function(fact_method,N,n)\n",
    "check_sterling,ans_ster = time_function(sterling_method,N,n)\n",
    "\n",
    "\n",
    "print(check_fact)\n",
    "print(check_sterling)\n",
    "\n",
    "error = abs(ans_fact - ans_ster) / ans_fact\n",
    "\n",
    "\n",
    "plt.plot(N,error)\n",
    "\n",
    "plt.xlabel(\"Number of coin tosses\")\n",
    "plt.ylabel(\"error(%)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "27\n"
     ]
    }
   ],
   "source": [
    "a = np.where(error <0.005)\n",
    "print(a[0][0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
