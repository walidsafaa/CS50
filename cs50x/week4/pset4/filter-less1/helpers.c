#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int x = 0; x < width; x++)
        {
            // Average
            int tempAvg = (image[i][x].rgbtRed + image[i][x].rgbtGreen + image[i][x].rgbtBlue) / 3.0;

                image[i][x].rgbtRed = tempAvg;
                image[i][x].rgbtGreen = tempAvg;
                image[i][x].rgbtBlue = tempAvg;

        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int x = 0; x < width; x++)
        {
            int sepiaRed = .393 * image[i][x].rgbtRed + .769 * image[i][x].rgbtGreen + .189 * image[i][x].rgbtBlue;
            int sepiaGreen = .349 * image[i][x].rgbtRed + .686 * image[i][x].rgbtGreen + .168 * image[i][x].rgbtBlue;
            int sepiaBlue = .272 * image[i][x].rgbtRed + .534 * image[i][x].rgbtGreen + .131 * image[i][x].rgbtBlue;

            image[i][x].rgbtRed = sepiaRed;
            image[i][x].rgbtGreen = sepiaGreen;
            image[i][x].rgbtBlue = sepiaBlue;

            if (sepiaRed > 255 || sepiaGreen > 255 || sepiaBlue > 255)
            {
                image[i][x].rgbtRed = 255;
                image[i][x].rgbtGreen = 255;
                image[i][x].rgbtBlue = 255;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int x = 0; x < width / 2; x++)
        {
            // Average
            int tempR = image[i][x].rgbtRed;
            int tempG = image[i][x].rgbtGreen;
            int tempB = image[i][x].rgbtBlue;

            image[i][x].rgbtRed = image[i][width - x - 1].rgbtRed;
            image[i][x].rgbtGreen = image[i][width- x - 1].rgbtGreen;
            image[i][x].rgbtBlue = image[i][width - x - 1].rgbtBlue;

            image[i][width - x - 1].rgbtRed = tempR;
            image[i][width - x - 1].rgbtGreen = tempG;
            image[i][width - x - 1].rgbtBlue = tempB;

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int y = 0; y < width; y++)
        {
            // Average
            int total_Red, total_Blue, total_Green;
            total_Red = total_Blue = total_Green = 0;
            float counter = 0.00;

            //Get the neighbouring pexels
            for (int a = -1; a < 2; a++)
            {
                for (int j = -1; j < 2; j++)
                {
                    int currentA = i + a;
                    int currentJ = y + j;

                    //check for valid neighbouring pixels
                    if (currentA < 0 || currentA > (height - 1) || currentJ < 0 || currentJ > (width - 1))
                    {
                        continue;
                    }

                    //Get the image value
                    total_Red += image[currentA][currentJ].rgbtRed;
                    total_Green += image[currentA][currentJ].rgbtGreen;
                    total_Blue += image[currentA][currentJ].rgbtBlue;

                    counter++;
                }

                //do the average of neigbhouring pixels
                temp[i][y].rgbtRed = round(total_Red / counter);
                temp[i][y].rgbtGreen = round(total_Green / counter);
                temp[i][y].rgbtBlue = round(total_Blue / counter);
            }
        }
    }
    //copy from the blur image write into the original image
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
