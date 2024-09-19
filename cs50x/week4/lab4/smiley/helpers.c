#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int i = 0; i < height; i++)
    {
        for (int x = 0; x < width; x++)
        {
            // Make black pixels turn red
            if (image[i][x].rgbtRed == 0x00 && image[i][x].rgbtGreen == 0x00 && image[i][x].rgbtBlue == 0x00)
            {
                image[i][x].rgbtRed = 0xff;
            }
        }
    }
}
