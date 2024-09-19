#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    // Open Memory Card
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 2;
    }

    unsigned char buffer[512];

    // Track number of images
    int count = 0;
    //char filename[8]
    char filename[8];

    ///////File pointer for recovered images
    FILE *img = NULL;

    while (fread(buffer, 512, 1, file) != 0)
    {
        // If start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (count!=0)
            {
                fclose(img);
            }

            sprintf(filename,"%03i.jpg", count++);
            img = fopen(filename, "w");
        }

        if (count!=0)
        {
            fwrite(buffer, 512, 1, img);
        }
    }
    fclose(file);
    fclose(img);
    return 0;
}