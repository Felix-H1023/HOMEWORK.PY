{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print ('Hello! This is restaurant_bill_calculator')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "food_fee=int(input('What does all your food cost? (plz do not enter the dollar sign or decimals)'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "tax=int(input('What is your state tax? (plz do not enter percent sign thingy)'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tax_in_dollars=food_fee%tax"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "yes_or_no_tip =input('Will you leave any tips? Yes or no. (plz only put \"yes\" or \"no\")')\n",
    "a='yes'\n",
    "if yes_or_no_tip==a :\n",
    "    tip=int(input('How much money will u leave as a tip? (plz do not put the percent sign thing, what do you call it?)'))\n",
    "    tip_in_dollars=food_fee%tip\n",
    "else: tip_in_dollars=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "entire_bill=food_fee+tax_in_dollars+tip_in_dollars\n",
    "print ('The entire bill is $',entire_bill)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "print ('Thank you for using restaurant_bill_calculator!')"
   ]
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
