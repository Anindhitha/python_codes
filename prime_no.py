{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6b1b064a-d979-445e-82ea-145b93632de2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the no 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a prime no\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"enter the no\"))\n",
    "if a>1:\n",
    "    for x in range(2,a):\n",
    "        if(a%x)==0:\n",
    "            print(\"not a prime\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"a prime no\")\n",
    "            break\n",
    "else:\n",
    "    print(\"not a prime\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "69e030f9-eb23-472e-9f5e-ea1e5cc1ce96",
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
   "version": "3.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
