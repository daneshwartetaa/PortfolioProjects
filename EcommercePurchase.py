{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f5cc7b0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2c00ffc7",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Address</th>\n",
       "      <th>Lot</th>\n",
       "      <th>AM or PM</th>\n",
       "      <th>Browser Info</th>\n",
       "      <th>Company</th>\n",
       "      <th>Credit Card</th>\n",
       "      <th>CC Exp Date</th>\n",
       "      <th>CC Security Code</th>\n",
       "      <th>CC Provider</th>\n",
       "      <th>Email</th>\n",
       "      <th>Job</th>\n",
       "      <th>IP Address</th>\n",
       "      <th>Language</th>\n",
       "      <th>Purchase Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>16629 Pace Camp Apt. 448\\nAlexisborough, NE 77...</td>\n",
       "      <td>46 in</td>\n",
       "      <td>PM</td>\n",
       "      <td>Opera/9.56.(X11; Linux x86_64; sl-SI) Presto/2...</td>\n",
       "      <td>Martinez-Herman</td>\n",
       "      <td>6011929061123406</td>\n",
       "      <td>02/20</td>\n",
       "      <td>900</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>pdunlap@yahoo.com</td>\n",
       "      <td>Scientist, product/process development</td>\n",
       "      <td>149.146.147.205</td>\n",
       "      <td>el</td>\n",
       "      <td>98.14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>9374 Jasmine Spurs Suite 508\\nSouth John, TN 8...</td>\n",
       "      <td>28 rn</td>\n",
       "      <td>PM</td>\n",
       "      <td>Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...</td>\n",
       "      <td>Fletcher, Richards and Whitaker</td>\n",
       "      <td>3337758169645356</td>\n",
       "      <td>11/18</td>\n",
       "      <td>561</td>\n",
       "      <td>Mastercard</td>\n",
       "      <td>anthony41@reed.com</td>\n",
       "      <td>Drilling engineer</td>\n",
       "      <td>15.160.41.51</td>\n",
       "      <td>fr</td>\n",
       "      <td>70.73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Unit 0065 Box 5052\\nDPO AP 27450</td>\n",
       "      <td>94 vE</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...</td>\n",
       "      <td>Simpson, Williams and Pham</td>\n",
       "      <td>675957666125</td>\n",
       "      <td>08/19</td>\n",
       "      <td>699</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>amymiller@morales-harrison.com</td>\n",
       "      <td>Customer service manager</td>\n",
       "      <td>132.207.160.22</td>\n",
       "      <td>de</td>\n",
       "      <td>0.95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7780 Julia Fords\\nNew Stacy, WA 45798</td>\n",
       "      <td>36 vm</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0 ...</td>\n",
       "      <td>Williams, Marshall and Buchanan</td>\n",
       "      <td>6011578504430710</td>\n",
       "      <td>02/24</td>\n",
       "      <td>384</td>\n",
       "      <td>Discover</td>\n",
       "      <td>brent16@olson-robinson.info</td>\n",
       "      <td>Drilling engineer</td>\n",
       "      <td>30.250.74.19</td>\n",
       "      <td>es</td>\n",
       "      <td>78.04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>23012 Munoz Drive Suite 337\\nNew Cynthia, TX 5...</td>\n",
       "      <td>20 IE</td>\n",
       "      <td>AM</td>\n",
       "      <td>Opera/9.58.(X11; Linux x86_64; it-IT) Presto/2...</td>\n",
       "      <td>Brown, Watson and Andrews</td>\n",
       "      <td>6011456623207998</td>\n",
       "      <td>10/25</td>\n",
       "      <td>678</td>\n",
       "      <td>Diners Club / Carte Blanche</td>\n",
       "      <td>christopherwright@gmail.com</td>\n",
       "      <td>Fine artist</td>\n",
       "      <td>24.140.33.94</td>\n",
       "      <td>es</td>\n",
       "      <td>77.82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9995</th>\n",
       "      <td>966 Castaneda Locks\\nWest Juliafurt, CO 96415</td>\n",
       "      <td>92 XI</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5352 ...</td>\n",
       "      <td>Randall-Sloan</td>\n",
       "      <td>342945015358701</td>\n",
       "      <td>03/22</td>\n",
       "      <td>838</td>\n",
       "      <td>JCB 15 digit</td>\n",
       "      <td>iscott@wade-garner.com</td>\n",
       "      <td>Printmaker</td>\n",
       "      <td>29.73.197.114</td>\n",
       "      <td>it</td>\n",
       "      <td>82.21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9996</th>\n",
       "      <td>832 Curtis Dam Suite 785\\nNorth Edwardburgh, T...</td>\n",
       "      <td>41 JY</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...</td>\n",
       "      <td>Hale, Collins and Wilson</td>\n",
       "      <td>210033169205009</td>\n",
       "      <td>07/25</td>\n",
       "      <td>207</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>mary85@hotmail.com</td>\n",
       "      <td>Energy engineer</td>\n",
       "      <td>121.133.168.51</td>\n",
       "      <td>pt</td>\n",
       "      <td>25.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9997</th>\n",
       "      <td>Unit 4434 Box 6343\\nDPO AE 28026-0283</td>\n",
       "      <td>74 Zh</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7...</td>\n",
       "      <td>Anderson Ltd</td>\n",
       "      <td>6011539787356311</td>\n",
       "      <td>05/21</td>\n",
       "      <td>1</td>\n",
       "      <td>VISA 16 digit</td>\n",
       "      <td>tyler16@gmail.com</td>\n",
       "      <td>Veterinary surgeon</td>\n",
       "      <td>156.210.0.254</td>\n",
       "      <td>el</td>\n",
       "      <td>83.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9998</th>\n",
       "      <td>0096 English Rest\\nRoystad, IA 12457</td>\n",
       "      <td>74 cL</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_8;...</td>\n",
       "      <td>Cook Inc</td>\n",
       "      <td>180003348082930</td>\n",
       "      <td>11/17</td>\n",
       "      <td>987</td>\n",
       "      <td>American Express</td>\n",
       "      <td>elizabethmoore@reid.net</td>\n",
       "      <td>Local government officer</td>\n",
       "      <td>55.78.26.143</td>\n",
       "      <td>es</td>\n",
       "      <td>38.84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9999</th>\n",
       "      <td>40674 Barrett Stravenue\\nGrimesville, WI 79682</td>\n",
       "      <td>64 Hr</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (X11; Linux i686; rv:1.9.5.20) Gec...</td>\n",
       "      <td>Greene Inc</td>\n",
       "      <td>4139972901927273</td>\n",
       "      <td>02/19</td>\n",
       "      <td>302</td>\n",
       "      <td>JCB 15 digit</td>\n",
       "      <td>rachelford@vaughn.com</td>\n",
       "      <td>Embryologist, clinical</td>\n",
       "      <td>176.119.198.199</td>\n",
       "      <td>el</td>\n",
       "      <td>67.59</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>10000 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                Address    Lot AM or PM  \\\n",
       "0     16629 Pace Camp Apt. 448\\nAlexisborough, NE 77...  46 in       PM   \n",
       "1     9374 Jasmine Spurs Suite 508\\nSouth John, TN 8...  28 rn       PM   \n",
       "2                      Unit 0065 Box 5052\\nDPO AP 27450  94 vE       PM   \n",
       "3                 7780 Julia Fords\\nNew Stacy, WA 45798  36 vm       PM   \n",
       "4     23012 Munoz Drive Suite 337\\nNew Cynthia, TX 5...  20 IE       AM   \n",
       "...                                                 ...    ...      ...   \n",
       "9995      966 Castaneda Locks\\nWest Juliafurt, CO 96415  92 XI       PM   \n",
       "9996  832 Curtis Dam Suite 785\\nNorth Edwardburgh, T...  41 JY       AM   \n",
       "9997              Unit 4434 Box 6343\\nDPO AE 28026-0283  74 Zh       AM   \n",
       "9998               0096 English Rest\\nRoystad, IA 12457  74 cL       PM   \n",
       "9999     40674 Barrett Stravenue\\nGrimesville, WI 79682  64 Hr       AM   \n",
       "\n",
       "                                           Browser Info  \\\n",
       "0     Opera/9.56.(X11; Linux x86_64; sl-SI) Presto/2...   \n",
       "1     Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...   \n",
       "2     Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...   \n",
       "3     Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0 ...   \n",
       "4     Opera/9.58.(X11; Linux x86_64; it-IT) Presto/2...   \n",
       "...                                                 ...   \n",
       "9995  Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5352 ...   \n",
       "9996  Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...   \n",
       "9997  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7...   \n",
       "9998  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_8;...   \n",
       "9999  Mozilla/5.0 (X11; Linux i686; rv:1.9.5.20) Gec...   \n",
       "\n",
       "                              Company       Credit Card CC Exp Date  \\\n",
       "0                     Martinez-Herman  6011929061123406       02/20   \n",
       "1     Fletcher, Richards and Whitaker  3337758169645356       11/18   \n",
       "2          Simpson, Williams and Pham      675957666125       08/19   \n",
       "3     Williams, Marshall and Buchanan  6011578504430710       02/24   \n",
       "4           Brown, Watson and Andrews  6011456623207998       10/25   \n",
       "...                               ...               ...         ...   \n",
       "9995                    Randall-Sloan   342945015358701       03/22   \n",
       "9996         Hale, Collins and Wilson   210033169205009       07/25   \n",
       "9997                     Anderson Ltd  6011539787356311       05/21   \n",
       "9998                         Cook Inc   180003348082930       11/17   \n",
       "9999                       Greene Inc  4139972901927273       02/19   \n",
       "\n",
       "      CC Security Code                  CC Provider  \\\n",
       "0                  900                 JCB 16 digit   \n",
       "1                  561                   Mastercard   \n",
       "2                  699                 JCB 16 digit   \n",
       "3                  384                     Discover   \n",
       "4                  678  Diners Club / Carte Blanche   \n",
       "...                ...                          ...   \n",
       "9995               838                 JCB 15 digit   \n",
       "9996               207                 JCB 16 digit   \n",
       "9997                 1                VISA 16 digit   \n",
       "9998               987             American Express   \n",
       "9999               302                 JCB 15 digit   \n",
       "\n",
       "                               Email                                     Job  \\\n",
       "0                  pdunlap@yahoo.com  Scientist, product/process development   \n",
       "1                 anthony41@reed.com                       Drilling engineer   \n",
       "2     amymiller@morales-harrison.com                Customer service manager   \n",
       "3        brent16@olson-robinson.info                       Drilling engineer   \n",
       "4        christopherwright@gmail.com                             Fine artist   \n",
       "...                              ...                                     ...   \n",
       "9995          iscott@wade-garner.com                              Printmaker   \n",
       "9996              mary85@hotmail.com                         Energy engineer   \n",
       "9997               tyler16@gmail.com                      Veterinary surgeon   \n",
       "9998         elizabethmoore@reid.net                Local government officer   \n",
       "9999           rachelford@vaughn.com                  Embryologist, clinical   \n",
       "\n",
       "           IP Address Language  Purchase Price  \n",
       "0     149.146.147.205       el           98.14  \n",
       "1        15.160.41.51       fr           70.73  \n",
       "2      132.207.160.22       de            0.95  \n",
       "3        30.250.74.19       es           78.04  \n",
       "4        24.140.33.94       es           77.82  \n",
       "...               ...      ...             ...  \n",
       "9995    29.73.197.114       it           82.21  \n",
       "9996   121.133.168.51       pt           25.63  \n",
       "9997    156.210.0.254       el           83.98  \n",
       "9998     55.78.26.143       es           38.84  \n",
       "9999  176.119.198.199       el           67.59  \n",
       "\n",
       "[10000 rows x 14 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv(r\"C:\\Users\\Ecommerce Purchases\")\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "521f9fe5",
   "metadata": {},
   "source": [
    " 1.Top 10 Rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ce43c9a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Address</th>\n",
       "      <th>Lot</th>\n",
       "      <th>AM or PM</th>\n",
       "      <th>Browser Info</th>\n",
       "      <th>Company</th>\n",
       "      <th>Credit Card</th>\n",
       "      <th>CC Exp Date</th>\n",
       "      <th>CC Security Code</th>\n",
       "      <th>CC Provider</th>\n",
       "      <th>Email</th>\n",
       "      <th>Job</th>\n",
       "      <th>IP Address</th>\n",
       "      <th>Language</th>\n",
       "      <th>Purchase Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>16629 Pace Camp Apt. 448\\nAlexisborough, NE 77...</td>\n",
       "      <td>46 in</td>\n",
       "      <td>PM</td>\n",
       "      <td>Opera/9.56.(X11; Linux x86_64; sl-SI) Presto/2...</td>\n",
       "      <td>Martinez-Herman</td>\n",
       "      <td>6011929061123406</td>\n",
       "      <td>02/20</td>\n",
       "      <td>900</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>pdunlap@yahoo.com</td>\n",
       "      <td>Scientist, product/process development</td>\n",
       "      <td>149.146.147.205</td>\n",
       "      <td>el</td>\n",
       "      <td>98.14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>9374 Jasmine Spurs Suite 508\\nSouth John, TN 8...</td>\n",
       "      <td>28 rn</td>\n",
       "      <td>PM</td>\n",
       "      <td>Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...</td>\n",
       "      <td>Fletcher, Richards and Whitaker</td>\n",
       "      <td>3337758169645356</td>\n",
       "      <td>11/18</td>\n",
       "      <td>561</td>\n",
       "      <td>Mastercard</td>\n",
       "      <td>anthony41@reed.com</td>\n",
       "      <td>Drilling engineer</td>\n",
       "      <td>15.160.41.51</td>\n",
       "      <td>fr</td>\n",
       "      <td>70.73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Unit 0065 Box 5052\\nDPO AP 27450</td>\n",
       "      <td>94 vE</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...</td>\n",
       "      <td>Simpson, Williams and Pham</td>\n",
       "      <td>675957666125</td>\n",
       "      <td>08/19</td>\n",
       "      <td>699</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>amymiller@morales-harrison.com</td>\n",
       "      <td>Customer service manager</td>\n",
       "      <td>132.207.160.22</td>\n",
       "      <td>de</td>\n",
       "      <td>0.95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7780 Julia Fords\\nNew Stacy, WA 45798</td>\n",
       "      <td>36 vm</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0 ...</td>\n",
       "      <td>Williams, Marshall and Buchanan</td>\n",
       "      <td>6011578504430710</td>\n",
       "      <td>02/24</td>\n",
       "      <td>384</td>\n",
       "      <td>Discover</td>\n",
       "      <td>brent16@olson-robinson.info</td>\n",
       "      <td>Drilling engineer</td>\n",
       "      <td>30.250.74.19</td>\n",
       "      <td>es</td>\n",
       "      <td>78.04</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>23012 Munoz Drive Suite 337\\nNew Cynthia, TX 5...</td>\n",
       "      <td>20 IE</td>\n",
       "      <td>AM</td>\n",
       "      <td>Opera/9.58.(X11; Linux x86_64; it-IT) Presto/2...</td>\n",
       "      <td>Brown, Watson and Andrews</td>\n",
       "      <td>6011456623207998</td>\n",
       "      <td>10/25</td>\n",
       "      <td>678</td>\n",
       "      <td>Diners Club / Carte Blanche</td>\n",
       "      <td>christopherwright@gmail.com</td>\n",
       "      <td>Fine artist</td>\n",
       "      <td>24.140.33.94</td>\n",
       "      <td>es</td>\n",
       "      <td>77.82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>7502 Powell Mission Apt. 768\\nTravisland, VA 3...</td>\n",
       "      <td>21 XT</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_8_5...</td>\n",
       "      <td>Silva-Anderson</td>\n",
       "      <td>30246185196287</td>\n",
       "      <td>07/25</td>\n",
       "      <td>7169</td>\n",
       "      <td>Discover</td>\n",
       "      <td>ynguyen@gmail.com</td>\n",
       "      <td>Fish farm manager</td>\n",
       "      <td>55.96.152.147</td>\n",
       "      <td>ru</td>\n",
       "      <td>25.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>93971 Conway Causeway\\nAndersonburgh, AZ 75107</td>\n",
       "      <td>96 Xt</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (compatible; MSIE 7.0; Windows NT ...</td>\n",
       "      <td>Gibson and Sons</td>\n",
       "      <td>6011398782655569</td>\n",
       "      <td>07/24</td>\n",
       "      <td>714</td>\n",
       "      <td>VISA 16 digit</td>\n",
       "      <td>olivia04@yahoo.com</td>\n",
       "      <td>Dancer</td>\n",
       "      <td>127.252.144.18</td>\n",
       "      <td>de</td>\n",
       "      <td>88.56</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>260 Rachel Plains Suite 366\\nCastroberg, WV 24...</td>\n",
       "      <td>96 pG</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (X11; Linux i686) AppleWebKit/5350...</td>\n",
       "      <td>Marshall-Collins</td>\n",
       "      <td>561252141909</td>\n",
       "      <td>06/25</td>\n",
       "      <td>256</td>\n",
       "      <td>VISA 13 digit</td>\n",
       "      <td>phillip48@parks.info</td>\n",
       "      <td>Event organiser</td>\n",
       "      <td>224.247.97.150</td>\n",
       "      <td>pt</td>\n",
       "      <td>44.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2129 Dylan Burg\\nNew Michelle, ME 28650</td>\n",
       "      <td>45 JN</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7...</td>\n",
       "      <td>Galloway and Sons</td>\n",
       "      <td>180041795790001</td>\n",
       "      <td>04/24</td>\n",
       "      <td>899</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>kdavis@rasmussen.com</td>\n",
       "      <td>Financial manager</td>\n",
       "      <td>146.234.201.229</td>\n",
       "      <td>ru</td>\n",
       "      <td>59.54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>3795 Dawson Extensions\\nLake Tinafort, ID 88739</td>\n",
       "      <td>15 Ug</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gec...</td>\n",
       "      <td>Rivera, Buchanan and Ramirez</td>\n",
       "      <td>4396283918371</td>\n",
       "      <td>01/17</td>\n",
       "      <td>931</td>\n",
       "      <td>American Express</td>\n",
       "      <td>qcoleman@hunt-huerta.com</td>\n",
       "      <td>Forensic scientist</td>\n",
       "      <td>236.198.199.8</td>\n",
       "      <td>zh</td>\n",
       "      <td>95.63</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Address    Lot AM or PM  \\\n",
       "0  16629 Pace Camp Apt. 448\\nAlexisborough, NE 77...  46 in       PM   \n",
       "1  9374 Jasmine Spurs Suite 508\\nSouth John, TN 8...  28 rn       PM   \n",
       "2                   Unit 0065 Box 5052\\nDPO AP 27450  94 vE       PM   \n",
       "3              7780 Julia Fords\\nNew Stacy, WA 45798  36 vm       PM   \n",
       "4  23012 Munoz Drive Suite 337\\nNew Cynthia, TX 5...  20 IE       AM   \n",
       "5  7502 Powell Mission Apt. 768\\nTravisland, VA 3...  21 XT       PM   \n",
       "6     93971 Conway Causeway\\nAndersonburgh, AZ 75107  96 Xt       AM   \n",
       "7  260 Rachel Plains Suite 366\\nCastroberg, WV 24...  96 pG       PM   \n",
       "8            2129 Dylan Burg\\nNew Michelle, ME 28650  45 JN       PM   \n",
       "9    3795 Dawson Extensions\\nLake Tinafort, ID 88739  15 Ug       AM   \n",
       "\n",
       "                                        Browser Info  \\\n",
       "0  Opera/9.56.(X11; Linux x86_64; sl-SI) Presto/2...   \n",
       "1  Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...   \n",
       "2  Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...   \n",
       "3  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0 ...   \n",
       "4  Opera/9.58.(X11; Linux x86_64; it-IT) Presto/2...   \n",
       "5  Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_8_5...   \n",
       "6  Mozilla/5.0 (compatible; MSIE 7.0; Windows NT ...   \n",
       "7  Mozilla/5.0 (X11; Linux i686) AppleWebKit/5350...   \n",
       "8  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7...   \n",
       "9  Mozilla/5.0 (X11; Linux i686; rv:1.9.7.20) Gec...   \n",
       "\n",
       "                           Company       Credit Card CC Exp Date  \\\n",
       "0                  Martinez-Herman  6011929061123406       02/20   \n",
       "1  Fletcher, Richards and Whitaker  3337758169645356       11/18   \n",
       "2       Simpson, Williams and Pham      675957666125       08/19   \n",
       "3  Williams, Marshall and Buchanan  6011578504430710       02/24   \n",
       "4        Brown, Watson and Andrews  6011456623207998       10/25   \n",
       "5                   Silva-Anderson    30246185196287       07/25   \n",
       "6                  Gibson and Sons  6011398782655569       07/24   \n",
       "7                 Marshall-Collins      561252141909       06/25   \n",
       "8                Galloway and Sons   180041795790001       04/24   \n",
       "9     Rivera, Buchanan and Ramirez     4396283918371       01/17   \n",
       "\n",
       "   CC Security Code                  CC Provider  \\\n",
       "0               900                 JCB 16 digit   \n",
       "1               561                   Mastercard   \n",
       "2               699                 JCB 16 digit   \n",
       "3               384                     Discover   \n",
       "4               678  Diners Club / Carte Blanche   \n",
       "5              7169                     Discover   \n",
       "6               714                VISA 16 digit   \n",
       "7               256                VISA 13 digit   \n",
       "8               899                 JCB 16 digit   \n",
       "9               931             American Express   \n",
       "\n",
       "                            Email                                     Job  \\\n",
       "0               pdunlap@yahoo.com  Scientist, product/process development   \n",
       "1              anthony41@reed.com                       Drilling engineer   \n",
       "2  amymiller@morales-harrison.com                Customer service manager   \n",
       "3     brent16@olson-robinson.info                       Drilling engineer   \n",
       "4     christopherwright@gmail.com                             Fine artist   \n",
       "5               ynguyen@gmail.com                       Fish farm manager   \n",
       "6              olivia04@yahoo.com                                  Dancer   \n",
       "7            phillip48@parks.info                         Event organiser   \n",
       "8            kdavis@rasmussen.com                       Financial manager   \n",
       "9        qcoleman@hunt-huerta.com                      Forensic scientist   \n",
       "\n",
       "        IP Address Language  Purchase Price  \n",
       "0  149.146.147.205       el           98.14  \n",
       "1     15.160.41.51       fr           70.73  \n",
       "2   132.207.160.22       de            0.95  \n",
       "3     30.250.74.19       es           78.04  \n",
       "4     24.140.33.94       es           77.82  \n",
       "5    55.96.152.147       ru           25.15  \n",
       "6   127.252.144.18       de           88.56  \n",
       "7   224.247.97.150       pt           44.25  \n",
       "8  146.234.201.229       ru           59.54  \n",
       "9    236.198.199.8       zh           95.63  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f38ccb54",
   "metadata": {},
   "source": [
    "2.Last 10 Rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d9e9e32b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Address</th>\n",
       "      <th>Lot</th>\n",
       "      <th>AM or PM</th>\n",
       "      <th>Browser Info</th>\n",
       "      <th>Company</th>\n",
       "      <th>Credit Card</th>\n",
       "      <th>CC Exp Date</th>\n",
       "      <th>CC Security Code</th>\n",
       "      <th>CC Provider</th>\n",
       "      <th>Email</th>\n",
       "      <th>Job</th>\n",
       "      <th>IP Address</th>\n",
       "      <th>Language</th>\n",
       "      <th>Purchase Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9990</th>\n",
       "      <td>75731 Molly Springs\\nWest Danielle, VT 96934-5102</td>\n",
       "      <td>93 ty</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4;...</td>\n",
       "      <td>Pace, Vazquez and Richards</td>\n",
       "      <td>869968197049750</td>\n",
       "      <td>04/24</td>\n",
       "      <td>877</td>\n",
       "      <td>JCB 15 digit</td>\n",
       "      <td>andersonmichael@sherman.biz</td>\n",
       "      <td>Early years teacher</td>\n",
       "      <td>54.170.3.185</td>\n",
       "      <td>ru</td>\n",
       "      <td>18.35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9991</th>\n",
       "      <td>PSC 8165, Box 8498\\nAPO AP 60327-0346</td>\n",
       "      <td>50 dA</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (compatible; MSIE 8.0; Windows NT ...</td>\n",
       "      <td>Snyder Inc</td>\n",
       "      <td>4221582137197481</td>\n",
       "      <td>02/24</td>\n",
       "      <td>969</td>\n",
       "      <td>Voyager</td>\n",
       "      <td>kking@wise-liu.com</td>\n",
       "      <td>IT sales professional</td>\n",
       "      <td>254.25.31.156</td>\n",
       "      <td>el</td>\n",
       "      <td>25.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9992</th>\n",
       "      <td>885 Allen Mountains Apt. 230\\nWallhaven, LA 16995</td>\n",
       "      <td>40 vH</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_5) A...</td>\n",
       "      <td>Wells Ltd</td>\n",
       "      <td>4664825258997302</td>\n",
       "      <td>10/20</td>\n",
       "      <td>431</td>\n",
       "      <td>Discover</td>\n",
       "      <td>bberry@wright.net</td>\n",
       "      <td>Set designer</td>\n",
       "      <td>174.173.51.32</td>\n",
       "      <td>de</td>\n",
       "      <td>67.96</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9993</th>\n",
       "      <td>7555 Larson Locks Suite 229\\nEllisburgh, MA 34...</td>\n",
       "      <td>72 jg</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8...</td>\n",
       "      <td>Colon and Sons</td>\n",
       "      <td>30025560104631</td>\n",
       "      <td>10/25</td>\n",
       "      <td>629</td>\n",
       "      <td>Maestro</td>\n",
       "      <td>chelseawilliams@lopez.biz</td>\n",
       "      <td>Designer, exhibition/display</td>\n",
       "      <td>177.46.82.128</td>\n",
       "      <td>el</td>\n",
       "      <td>65.61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9994</th>\n",
       "      <td>6276 Rojas Hollow\\nLake Louis, WY 56410-7837</td>\n",
       "      <td>93 Ex</td>\n",
       "      <td>PM</td>\n",
       "      <td>Opera/9.68.(X11; Linux x86_64; sl-SI) Presto/2...</td>\n",
       "      <td>Ritter-Smith</td>\n",
       "      <td>3112186784121077</td>\n",
       "      <td>01/25</td>\n",
       "      <td>1823</td>\n",
       "      <td>Maestro</td>\n",
       "      <td>iroberts@gmail.com</td>\n",
       "      <td>Education officer, museum</td>\n",
       "      <td>242.44.112.18</td>\n",
       "      <td>zh</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9995</th>\n",
       "      <td>966 Castaneda Locks\\nWest Juliafurt, CO 96415</td>\n",
       "      <td>92 XI</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5352 ...</td>\n",
       "      <td>Randall-Sloan</td>\n",
       "      <td>342945015358701</td>\n",
       "      <td>03/22</td>\n",
       "      <td>838</td>\n",
       "      <td>JCB 15 digit</td>\n",
       "      <td>iscott@wade-garner.com</td>\n",
       "      <td>Printmaker</td>\n",
       "      <td>29.73.197.114</td>\n",
       "      <td>it</td>\n",
       "      <td>82.21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9996</th>\n",
       "      <td>832 Curtis Dam Suite 785\\nNorth Edwardburgh, T...</td>\n",
       "      <td>41 JY</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...</td>\n",
       "      <td>Hale, Collins and Wilson</td>\n",
       "      <td>210033169205009</td>\n",
       "      <td>07/25</td>\n",
       "      <td>207</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>mary85@hotmail.com</td>\n",
       "      <td>Energy engineer</td>\n",
       "      <td>121.133.168.51</td>\n",
       "      <td>pt</td>\n",
       "      <td>25.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9997</th>\n",
       "      <td>Unit 4434 Box 6343\\nDPO AE 28026-0283</td>\n",
       "      <td>74 Zh</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7...</td>\n",
       "      <td>Anderson Ltd</td>\n",
       "      <td>6011539787356311</td>\n",
       "      <td>05/21</td>\n",
       "      <td>1</td>\n",
       "      <td>VISA 16 digit</td>\n",
       "      <td>tyler16@gmail.com</td>\n",
       "      <td>Veterinary surgeon</td>\n",
       "      <td>156.210.0.254</td>\n",
       "      <td>el</td>\n",
       "      <td>83.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9998</th>\n",
       "      <td>0096 English Rest\\nRoystad, IA 12457</td>\n",
       "      <td>74 cL</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_8;...</td>\n",
       "      <td>Cook Inc</td>\n",
       "      <td>180003348082930</td>\n",
       "      <td>11/17</td>\n",
       "      <td>987</td>\n",
       "      <td>American Express</td>\n",
       "      <td>elizabethmoore@reid.net</td>\n",
       "      <td>Local government officer</td>\n",
       "      <td>55.78.26.143</td>\n",
       "      <td>es</td>\n",
       "      <td>38.84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9999</th>\n",
       "      <td>40674 Barrett Stravenue\\nGrimesville, WI 79682</td>\n",
       "      <td>64 Hr</td>\n",
       "      <td>AM</td>\n",
       "      <td>Mozilla/5.0 (X11; Linux i686; rv:1.9.5.20) Gec...</td>\n",
       "      <td>Greene Inc</td>\n",
       "      <td>4139972901927273</td>\n",
       "      <td>02/19</td>\n",
       "      <td>302</td>\n",
       "      <td>JCB 15 digit</td>\n",
       "      <td>rachelford@vaughn.com</td>\n",
       "      <td>Embryologist, clinical</td>\n",
       "      <td>176.119.198.199</td>\n",
       "      <td>el</td>\n",
       "      <td>67.59</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                Address    Lot AM or PM  \\\n",
       "9990  75731 Molly Springs\\nWest Danielle, VT 96934-5102  93 ty       PM   \n",
       "9991              PSC 8165, Box 8498\\nAPO AP 60327-0346  50 dA       AM   \n",
       "9992  885 Allen Mountains Apt. 230\\nWallhaven, LA 16995  40 vH       PM   \n",
       "9993  7555 Larson Locks Suite 229\\nEllisburgh, MA 34...  72 jg       PM   \n",
       "9994       6276 Rojas Hollow\\nLake Louis, WY 56410-7837  93 Ex       PM   \n",
       "9995      966 Castaneda Locks\\nWest Juliafurt, CO 96415  92 XI       PM   \n",
       "9996  832 Curtis Dam Suite 785\\nNorth Edwardburgh, T...  41 JY       AM   \n",
       "9997              Unit 4434 Box 6343\\nDPO AE 28026-0283  74 Zh       AM   \n",
       "9998               0096 English Rest\\nRoystad, IA 12457  74 cL       PM   \n",
       "9999     40674 Barrett Stravenue\\nGrimesville, WI 79682  64 Hr       AM   \n",
       "\n",
       "                                           Browser Info  \\\n",
       "9990  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4;...   \n",
       "9991  Mozilla/5.0 (compatible; MSIE 8.0; Windows NT ...   \n",
       "9992  Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_5) A...   \n",
       "9993  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8...   \n",
       "9994  Opera/9.68.(X11; Linux x86_64; sl-SI) Presto/2...   \n",
       "9995  Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5352 ...   \n",
       "9996  Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...   \n",
       "9997  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7...   \n",
       "9998  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_8;...   \n",
       "9999  Mozilla/5.0 (X11; Linux i686; rv:1.9.5.20) Gec...   \n",
       "\n",
       "                         Company       Credit Card CC Exp Date  \\\n",
       "9990  Pace, Vazquez and Richards   869968197049750       04/24   \n",
       "9991                  Snyder Inc  4221582137197481       02/24   \n",
       "9992                   Wells Ltd  4664825258997302       10/20   \n",
       "9993              Colon and Sons    30025560104631       10/25   \n",
       "9994                Ritter-Smith  3112186784121077       01/25   \n",
       "9995               Randall-Sloan   342945015358701       03/22   \n",
       "9996    Hale, Collins and Wilson   210033169205009       07/25   \n",
       "9997                Anderson Ltd  6011539787356311       05/21   \n",
       "9998                    Cook Inc   180003348082930       11/17   \n",
       "9999                  Greene Inc  4139972901927273       02/19   \n",
       "\n",
       "      CC Security Code       CC Provider                        Email  \\\n",
       "9990               877      JCB 15 digit  andersonmichael@sherman.biz   \n",
       "9991               969           Voyager           kking@wise-liu.com   \n",
       "9992               431          Discover            bberry@wright.net   \n",
       "9993               629           Maestro    chelseawilliams@lopez.biz   \n",
       "9994              1823           Maestro           iroberts@gmail.com   \n",
       "9995               838      JCB 15 digit       iscott@wade-garner.com   \n",
       "9996               207      JCB 16 digit           mary85@hotmail.com   \n",
       "9997                 1     VISA 16 digit            tyler16@gmail.com   \n",
       "9998               987  American Express      elizabethmoore@reid.net   \n",
       "9999               302      JCB 15 digit        rachelford@vaughn.com   \n",
       "\n",
       "                               Job       IP Address Language  Purchase Price  \n",
       "9990           Early years teacher     54.170.3.185       ru           18.35  \n",
       "9991         IT sales professional    254.25.31.156       el           25.93  \n",
       "9992                  Set designer    174.173.51.32       de           67.96  \n",
       "9993  Designer, exhibition/display    177.46.82.128       el           65.61  \n",
       "9994     Education officer, museum    242.44.112.18       zh           31.85  \n",
       "9995                    Printmaker    29.73.197.114       it           82.21  \n",
       "9996               Energy engineer   121.133.168.51       pt           25.63  \n",
       "9997            Veterinary surgeon    156.210.0.254       el           83.98  \n",
       "9998      Local government officer     55.78.26.143       es           38.84  \n",
       "9999        Embryologist, clinical  176.119.198.199       el           67.59  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31c4862f",
   "metadata": {},
   "source": [
    "3.Check DataType"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "efb79043",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Address              object\n",
       "Lot                  object\n",
       "AM or PM             object\n",
       "Browser Info         object\n",
       "Company              object\n",
       "Credit Card           int64\n",
       "CC Exp Date          object\n",
       "CC Security Code      int64\n",
       "CC Provider          object\n",
       "Email                object\n",
       "Job                  object\n",
       "IP Address           object\n",
       "Language             object\n",
       "Purchase Price      float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "103f6bc3",
   "metadata": {},
   "source": [
    "4.Null Values in Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7b6b33ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Address             0\n",
       "Lot                 0\n",
       "AM or PM            0\n",
       "Browser Info        0\n",
       "Company             0\n",
       "Credit Card         0\n",
       "CC Exp Date         0\n",
       "CC Security Code    0\n",
       "CC Provider         0\n",
       "Email               0\n",
       "Job                 0\n",
       "IP Address          0\n",
       "Language            0\n",
       "Purchase Price      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "652e014e",
   "metadata": {},
   "source": [
    "5.No. of Rows and Columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "39004a36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a4c34985",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10000"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99fbeb48",
   "metadata": {},
   "source": [
    "6.Highest and Lowest Purchase Price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e7dbaee8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Address', 'Lot', 'AM or PM', 'Browser Info', 'Company', 'Credit Card',\n",
       "       'CC Exp Date', 'CC Security Code', 'CC Provider', 'Email', 'Job',\n",
       "       'IP Address', 'Language', 'Purchase Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "eb920eac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "99.99"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Purchase Price'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0fbb3fed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Purchase Price'].min()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc149dca",
   "metadata": {},
   "source": [
    "7.Average Purchase Price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8a89eb6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50.347302"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Purchase Price'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32727521",
   "metadata": {},
   "source": [
    "8.How Many People Have English 'el' As Their Language ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9caf4cf3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1137"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data[data['Language']=='el'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d6caf6ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Address             1137\n",
       "Lot                 1137\n",
       "AM or PM            1137\n",
       "Browser Info        1137\n",
       "Company             1137\n",
       "Credit Card         1137\n",
       "CC Exp Date         1137\n",
       "CC Security Code    1137\n",
       "CC Provider         1137\n",
       "Email               1137\n",
       "Job                 1137\n",
       "IP Address          1137\n",
       "Language            1137\n",
       "Purchase Price      1137\n",
       "dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['Language']=='el'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc71a6d6",
   "metadata": {},
   "source": [
    "9.Job Title Contains 'artist'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "7b1eecf0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "40"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data[data['Job'].str.contains(\"artist\", case=False)])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92d97b01",
   "metadata": {},
   "source": [
    "10.Find Email of The Person With The Following IP Address : 149.146.147.205"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "162e1226",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    pdunlap@yahoo.com\n",
       "Name: Email, dtype: object"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['IP Address']==\"149.146.147.205\"][\"Email\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1fd97293",
   "metadata": {},
   "source": [
    "11.How Many People Have Mastercard As Their Credit Card Provider and Made A Purchase Above 50 ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "467722fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Address', 'Lot', 'AM or PM', 'Browser Info', 'Company', 'Credit Card',\n",
       "       'CC Exp Date', 'CC Security Code', 'CC Provider', 'Email', 'Job',\n",
       "       'IP Address', 'Language', 'Purchase Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "0f251e00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "437"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data[(data['CC Provider']=='Discover') & (data['Purchase Price']>50)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "6fdae5f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Address             437\n",
       "Lot                 437\n",
       "AM or PM            437\n",
       "Browser Info        437\n",
       "Company             437\n",
       "Credit Card         437\n",
       "CC Exp Date         437\n",
       "CC Security Code    437\n",
       "CC Provider         437\n",
       "Email               437\n",
       "Job                 437\n",
       "IP Address          437\n",
       "Language            437\n",
       "Purchase Price      437\n",
       "dtype: int64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(data[(data['CC Provider']=='Discover') \\\n",
    "      & (data['Purchase Price']>50)]).count()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85468dfe",
   "metadata": {},
   "source": [
    "12.Find Email of The Person With The Following Credit Card No: 6011539787356311"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "2962bd9b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Address', 'Lot', 'AM or PM', 'Browser Info', 'Company', 'Credit Card',\n",
       "       'CC Exp Date', 'CC Security Code', 'CC Provider', 'Email', 'Job',\n",
       "       'IP Address', 'Language', 'Purchase Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "a57a3fef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9997    tyler16@gmail.com\n",
       "Name: Email, dtype: object"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data[\"Credit Card\"]==6011539787356311]['Email']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "730bc7e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "03c3ba49",
   "metadata": {},
   "source": [
    "13.How Many People Purchase During AM and How Many People Purchase During PM?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "8d715478",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Address', 'Lot', 'AM or PM', 'Browser Info', 'Company', 'Credit Card',\n",
       "       'CC Exp Date', 'CC Security Code', 'CC Provider', 'Email', 'Job',\n",
       "       'IP Address', 'Language', 'Purchase Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "ee99a9fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PM    5068\n",
       "AM    4932\n",
       "Name: AM or PM, dtype: int64"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['AM or PM'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f034574f",
   "metadata": {},
   "source": [
    "14.How Many People Have A Credit Card That Expires In 2020?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "f3778c44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Address', 'Lot', 'AM or PM', 'Browser Info', 'Company', 'Credit Card',\n",
       "       'CC Exp Date', 'CC Security Code', 'CC Provider', 'Email', 'Job',\n",
       "       'IP Address', 'Language', 'Purchase Price'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0646e9b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "49347e74",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       02/20\n",
       "1       11/18\n",
       "2       08/19\n",
       "3       02/24\n",
       "4       10/25\n",
       "        ...  \n",
       "9995    03/22\n",
       "9996    07/25\n",
       "9997    05/21\n",
       "9998    11/17\n",
       "9999    02/19\n",
       "Name: CC Exp Date, Length: 10000, dtype: object"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['CC Exp Date']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "be0bad2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun():\n",
    "    count=0\n",
    "    for date in data['CC Exp Date']:\n",
    "        if date.split('/')[1]=='20':\n",
    "            count==count+1\n",
    "    print(count)        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "b7c3acf0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "fun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "9e381fe5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "988"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data[data['CC Exp Date'].str.contains('/20')])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "c62bab55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Address             988\n",
       "Lot                 988\n",
       "AM or PM            988\n",
       "Browser Info        988\n",
       "Company             988\n",
       "Credit Card         988\n",
       "CC Exp Date         988\n",
       "CC Security Code    988\n",
       "CC Provider         988\n",
       "Email               988\n",
       "Job                 988\n",
       "IP Address          988\n",
       "Language            988\n",
       "Purchase Price      988\n",
       "dtype: int64"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6cf84ba",
   "metadata": {},
   "source": [
    "15.Top 5 Email Providers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "258bf170",
   "metadata": {},
   "outputs": [],
   "source": [
    "list1 = []\n",
    "for email in data['Email']:\n",
    "    list1.append(email.split('@')[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "092d625c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['temp']= list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "4b483ce9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Address</th>\n",
       "      <th>Lot</th>\n",
       "      <th>AM or PM</th>\n",
       "      <th>Browser Info</th>\n",
       "      <th>Company</th>\n",
       "      <th>Credit Card</th>\n",
       "      <th>CC Exp Date</th>\n",
       "      <th>CC Security Code</th>\n",
       "      <th>CC Provider</th>\n",
       "      <th>Email</th>\n",
       "      <th>Job</th>\n",
       "      <th>IP Address</th>\n",
       "      <th>Language</th>\n",
       "      <th>Purchase Price</th>\n",
       "      <th>temp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>16629 Pace Camp Apt. 448\\nAlexisborough, NE 77...</td>\n",
       "      <td>46 in</td>\n",
       "      <td>PM</td>\n",
       "      <td>Opera/9.56.(X11; Linux x86_64; sl-SI) Presto/2...</td>\n",
       "      <td>Martinez-Herman</td>\n",
       "      <td>6011929061123406</td>\n",
       "      <td>02/20</td>\n",
       "      <td>900</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>pdunlap@yahoo.com</td>\n",
       "      <td>Scientist, product/process development</td>\n",
       "      <td>149.146.147.205</td>\n",
       "      <td>el</td>\n",
       "      <td>98.14</td>\n",
       "      <td>yahoo.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>9374 Jasmine Spurs Suite 508\\nSouth John, TN 8...</td>\n",
       "      <td>28 rn</td>\n",
       "      <td>PM</td>\n",
       "      <td>Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...</td>\n",
       "      <td>Fletcher, Richards and Whitaker</td>\n",
       "      <td>3337758169645356</td>\n",
       "      <td>11/18</td>\n",
       "      <td>561</td>\n",
       "      <td>Mastercard</td>\n",
       "      <td>anthony41@reed.com</td>\n",
       "      <td>Drilling engineer</td>\n",
       "      <td>15.160.41.51</td>\n",
       "      <td>fr</td>\n",
       "      <td>70.73</td>\n",
       "      <td>reed.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Unit 0065 Box 5052\\nDPO AP 27450</td>\n",
       "      <td>94 vE</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...</td>\n",
       "      <td>Simpson, Williams and Pham</td>\n",
       "      <td>675957666125</td>\n",
       "      <td>08/19</td>\n",
       "      <td>699</td>\n",
       "      <td>JCB 16 digit</td>\n",
       "      <td>amymiller@morales-harrison.com</td>\n",
       "      <td>Customer service manager</td>\n",
       "      <td>132.207.160.22</td>\n",
       "      <td>de</td>\n",
       "      <td>0.95</td>\n",
       "      <td>morales-harrison.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7780 Julia Fords\\nNew Stacy, WA 45798</td>\n",
       "      <td>36 vm</td>\n",
       "      <td>PM</td>\n",
       "      <td>Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0 ...</td>\n",
       "      <td>Williams, Marshall and Buchanan</td>\n",
       "      <td>6011578504430710</td>\n",
       "      <td>02/24</td>\n",
       "      <td>384</td>\n",
       "      <td>Discover</td>\n",
       "      <td>brent16@olson-robinson.info</td>\n",
       "      <td>Drilling engineer</td>\n",
       "      <td>30.250.74.19</td>\n",
       "      <td>es</td>\n",
       "      <td>78.04</td>\n",
       "      <td>olson-robinson.info</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>23012 Munoz Drive Suite 337\\nNew Cynthia, TX 5...</td>\n",
       "      <td>20 IE</td>\n",
       "      <td>AM</td>\n",
       "      <td>Opera/9.58.(X11; Linux x86_64; it-IT) Presto/2...</td>\n",
       "      <td>Brown, Watson and Andrews</td>\n",
       "      <td>6011456623207998</td>\n",
       "      <td>10/25</td>\n",
       "      <td>678</td>\n",
       "      <td>Diners Club / Carte Blanche</td>\n",
       "      <td>christopherwright@gmail.com</td>\n",
       "      <td>Fine artist</td>\n",
       "      <td>24.140.33.94</td>\n",
       "      <td>es</td>\n",
       "      <td>77.82</td>\n",
       "      <td>gmail.com</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Address    Lot AM or PM  \\\n",
       "0  16629 Pace Camp Apt. 448\\nAlexisborough, NE 77...  46 in       PM   \n",
       "1  9374 Jasmine Spurs Suite 508\\nSouth John, TN 8...  28 rn       PM   \n",
       "2                   Unit 0065 Box 5052\\nDPO AP 27450  94 vE       PM   \n",
       "3              7780 Julia Fords\\nNew Stacy, WA 45798  36 vm       PM   \n",
       "4  23012 Munoz Drive Suite 337\\nNew Cynthia, TX 5...  20 IE       AM   \n",
       "\n",
       "                                        Browser Info  \\\n",
       "0  Opera/9.56.(X11; Linux x86_64; sl-SI) Presto/2...   \n",
       "1  Opera/8.93.(Windows 98; Win 9x 4.90; en-US) Pr...   \n",
       "2  Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...   \n",
       "3  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0 ...   \n",
       "4  Opera/9.58.(X11; Linux x86_64; it-IT) Presto/2...   \n",
       "\n",
       "                           Company       Credit Card CC Exp Date  \\\n",
       "0                  Martinez-Herman  6011929061123406       02/20   \n",
       "1  Fletcher, Richards and Whitaker  3337758169645356       11/18   \n",
       "2       Simpson, Williams and Pham      675957666125       08/19   \n",
       "3  Williams, Marshall and Buchanan  6011578504430710       02/24   \n",
       "4        Brown, Watson and Andrews  6011456623207998       10/25   \n",
       "\n",
       "   CC Security Code                  CC Provider  \\\n",
       "0               900                 JCB 16 digit   \n",
       "1               561                   Mastercard   \n",
       "2               699                 JCB 16 digit   \n",
       "3               384                     Discover   \n",
       "4               678  Diners Club / Carte Blanche   \n",
       "\n",
       "                            Email                                     Job  \\\n",
       "0               pdunlap@yahoo.com  Scientist, product/process development   \n",
       "1              anthony41@reed.com                       Drilling engineer   \n",
       "2  amymiller@morales-harrison.com                Customer service manager   \n",
       "3     brent16@olson-robinson.info                       Drilling engineer   \n",
       "4     christopherwright@gmail.com                             Fine artist   \n",
       "\n",
       "        IP Address Language  Purchase Price                  temp  \n",
       "0  149.146.147.205       el           98.14             yahoo.com  \n",
       "1     15.160.41.51       fr           70.73              reed.com  \n",
       "2   132.207.160.22       de            0.95  morales-harrison.com  \n",
       "3     30.250.74.19       es           78.04   olson-robinson.info  \n",
       "4     24.140.33.94       es           77.82             gmail.com  "
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "e9749a42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "hotmail.com     1638\n",
       "yahoo.com       1616\n",
       "gmail.com       1605\n",
       "smith.com         42\n",
       "williams.com      37\n",
       "Name: temp, dtype: int64"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['temp'].value_counts().head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "ba033edb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "hotmail.com     1638\n",
       "yahoo.com       1616\n",
       "gmail.com       1605\n",
       "smith.com         42\n",
       "williams.com      37\n",
       "Name: Email, dtype: int64"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "91f739f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                    pdunlap@yahoo.com\n",
       "1                   anthony41@reed.com\n",
       "2       amymiller@morales-harrison.com\n",
       "3          brent16@olson-robinson.info\n",
       "4          christopherwright@gmail.com\n",
       "                     ...              \n",
       "9995            iscott@wade-garner.com\n",
       "9996                mary85@hotmail.com\n",
       "9997                 tyler16@gmail.com\n",
       "9998           elizabethmoore@reid.net\n",
       "9999             rachelford@vaughn.com\n",
       "Name: Email, Length: 10000, dtype: object"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Email']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5531eba",
   "metadata": {},
   "outputs": [],
   "source": [
    "16."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96839b5f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb77fe99",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20b2dcd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "17."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f41f888",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f622363",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c6d7b37",
   "metadata": {},
   "outputs": [],
   "source": [
    "18."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d96a70b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd73eadf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7bb233a",
   "metadata": {},
   "outputs": [],
   "source": [
    "19."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64120690",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2eebc83",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f879e194",
   "metadata": {},
   "outputs": [],
   "source": [
    "20."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7e75c8e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}