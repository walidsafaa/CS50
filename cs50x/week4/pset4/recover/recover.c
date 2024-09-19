#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t  BYTE;

int main(int argc, char *argv[])
{
    //Check the input is correct
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    // Open card.raw
    FILE *raw_file = fopen(argv[1], "r");
    //Check that file is valid
    if (raw_file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    unsigned char buffer[512];

    // Track number of images
    int count = 0;
    //char filename[8]
    char filename[8];

    ///////File pointer for recovered images
    FILE *output_file = NULL;

    // Repeat until end of card:
    while (fread(buffer, 512, 1, raw_file) != 0)
    {
        // If start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If not first JPEG, close previous
            if (!(count == 0))
            {
                fclose(output_file);
            }
            //Making a new JPEG
            sprintf(filename, "%03i.jpg", count++);
            output_file = fopen(filename, "w");
        }
        // If JPEG has been found, write to file
        if (!(count == 0))
        {
            fwrite(buffer, 512, 1, output_file);
        }

    }
    // close last opened outptr
    fclose(output_file);
    //close input file (forensic image)
    fclose(raw_file);

    return 0;
}

