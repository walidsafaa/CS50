#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            int r = image[x][y].rgbtRed;
            int g = image[x][y].rgbtGreen;
            int b = image[x][y].rgbtBlue;

            int gray = round(((float) r + g + b) / 3);
            image[x][y].rgbtBlue = gray;
            image[x][y].rgbtGreen = gray;
            image[x][y].rgbtRed = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            int r = image[x][y].rgbtRed;
            int g = image[x][y].rgbtGreen;
            int b = image[x][y].rgbtBlue;

            int sepiaRed = round((float) (.393 * r) + (.769 * g) + (.189 * b));

            if (sepiaRed > 255)
            {
                image[x][y].rgbtRed = 255;
            }
            else
            {
                image[x][y].rgbtRed = sepiaRed;
            }

            int sepiaGreen = round((float) (.349 * r) + (.686 * g) + (.168 * b));

            if (sepiaGreen > 255)
            {
                image[x][y].rgbtGreen = 255;
            }
            else
            {
                image[x][y].rgbtGreen = sepiaGreen;
            }

            int sepiaBlue = round((float) (.272 * r) + (.534 * g) + (.131 * b));

            if (sepiaBlue > 255)
            {
                image[x][y].rgbtBlue = 255;
            }
            else
            {
                image[x][y].rgbtBlue = sepiaBlue;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int temp[3];
    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width / 2; y++)
        {
            /** Swap pixels from left to right */
            temp[0] = image[x][y].rgbtBlue;
            temp[1] = image[x][y].rgbtGreen;
            temp[2] = image[x][y].rgbtRed;

            image[x][y].rgbtBlue = image[x][width - y - 1].rgbtBlue;
            image[x][y].rgbtGreen = image[x][width - y - 1].rgbtGreen;
            image[x][y].rgbtRed = image[x][width - y - 1].rgbtRed;

            image[x][width - y - 1].rgbtBlue = temp[0];
            image[x][width - y - 1].rgbtGreen = temp[1];
            image[x][width - y - 1].rgbtRed = temp[2];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // create a temporary image to implement blurred algorithm on it.
    RGBTRIPLE temp[height][width];

    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {

            int total_Red, total_Blue, total_Green;
            total_Red = total_Blue = total_Green = 0;
            float counter = 0.00;

            // Get the neighbouring pexels
            for (int i = -1; i < 2; i++)
            {
                for (int j = -1; j < 2; j++)
                {
                    int currentI = x + i;
                    int currentJ = y + j;

                    // check for valid neighbouring pexels
                    if (currentI < 0 || currentI > (height - 1) || currentJ < 0 || currentJ > (width - 1))
                    {
                        continue;
                    }

                    // Get the image value
                    total_Red += image[currentI][currentJ].rgbtRed;
                    total_Green += image[currentI][currentJ].rgbtGreen;
                    total_Blue += image[currentI][currentJ].rgbtBlue;

                    counter++;
                }

                // do the average of neigbhouring pexels
                temp[x][y].rgbtRed = round(total_Red / counter);
                temp[x][y].rgbtGreen = round(total_Green / counter);
                temp[x][y].rgbtBlue = round(total_Blue / counter);
            }
        }
    }
    // copy the blurr image to the original image
    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            image[x][y].rgbtRed = temp[x][y].rgbtRed;
            image[x][y].rgbtGreen = temp[x][y].rgbtGreen;
            image[x][y].rgbtBlue = temp[x][y].rgbtBlue;
        }
    }
    return;
}