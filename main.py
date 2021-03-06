#Color Palettes in Seaborn and their application to data representations:
"""
Seaborn offers multiple colour palettes which can be used in collaboration
with your data plots in matplotlib to make eye catching data visuals
Following are the varied range of colour palettes that can be displayed
The following codes output them in a horizontal array (pyplot)
But, the same can be applied to any data representation form
"""
import matplotlib.pyplot as plt
import seaborn as sns

#: Basic Default Colour palette
palette = sns.color_palette()
sns.palplot(palette)
plt.show()

# Seaborn offers 6 different abstracts that can be applied to any palette
# Testing abstracts on default palette:

#1: Dark Default Colour palette
palette = sns.color_palette("dark")
sns.palplot(palette)
plt.show()

#2: Pastel (faded) Default Colour palette
palette = sns.color_palette("pastel")
sns.palplot(palette)
plt.show()

#3: Deep Default Colour palette
palette = sns.color_palette("deep")
sns.palplot(palette)
plt.show()

#4: Muted Default Colour palette
palette = sns.color_palette("muted")
sns.palplot(palette)
plt.show()

#5: Colorblind Default Colour palette
palette = sns.color_palette("colorblind")
sns.palplot(palette)
plt.show()

#6: Bright Default Colour palette
palette = sns.color_palette("bright")
sns.palplot(palette)
plt.show()

#: Colour Scheme Specific Palettes:
palette = sns.color_palette("Blues")
sns.palplot(palette)
plt.show()
# The various shades of Blue colour will be displayed in a light to dark order
# A similar palette can be made for other colours (Orange, Purple, Green, Red)
# Be sure to add a 's' after the colour name and capitalize the first letter

#: Perceptually uniform palettes:
# Using any of 6 specified color-maps,light to dark or dark to light heatmaps are displayed
# All these heatmaps can be reversed by trailing thier name with a "_r"
#1: rocket
palette = sns.color_palette("rocket")
sns.palplot(palette)
plt.show()

#2: mako
palette = sns.color_palette("mako")
sns.palplot(palette)
plt.show()

#3: flare
palette = sns.color_palette("flare")
sns.palplot(palette)
plt.show()

#4: crest
palette = sns.color_palette("crest")
sns.palplot(palette)
plt.show()

#5: magma
palette = sns.color_palette("magma")
sns.palplot(palette)
plt.show()

#6: viridis
palette = sns.color_palette("viridis")
sns.palplot(palette)
plt.show()

#: Diverging Colour Palettes:
# Dark from either side, but converge into the center towards a lighter/white spectra or vice versa
#1: vlag: dark to light
palette = sns.color_palette("vlag")
sns.palplot(palette)
plt.show()

#2: icefire: light to dark
palette = sns.color_palette("icefire")
sns.palplot(palette)
plt.show()

#3: coolwarm : Blue & Red
palette = sns.color_palette("coolwarm")
sns.palplot(palette)
plt.show()

#: Rainbow Palette:
palette = sns.color_palette("Spectral")
sns.palplot(palette)
plt.show()

#________________________________________________________________________________________
