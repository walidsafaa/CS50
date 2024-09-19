#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Error command: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Counld not open the input file.\n");
        fclose(input);
        return 2;
    }

    // Read header
    // TODO #3
    WAVHEADER head;
    fread(&head, 1, sizeof(WAVHEADER), input);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(head) != 0)
    {
        printf("No WAV format is detected.\n");
        fclose(input);
        return 3;
    }

    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Counld not write the output file.\n");
        fclose(output);
        return 4;
    }
    // Write header to file
    // TODO #6
    fwrite(&head, 1, sizeof(WAVHEADER), output);

    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(head);

    // Write reversed audio to file
    // TODO #8
    // Declare an array to store each block we read in
    BYTE buffer[block_size];

    // Move Pointer to the End (takes in the pointer, the offset amount of 0, and moves it the end of the file)
    fseek(input, 0, SEEK_END);

    // Finding the Buffer Audio Size (excluding the header) // (ftell): This function is used to get the total size of file after
    // moving the file pointer at the end of the file. It returns the current position in long type and file can have more than
    // 32767 bytes of data.
    long audio_size = ftell(input) - sizeof(WAVHEADER);
    int audio_block = (int) audio_size / block_size;

    // Iterate through the input file audio data
    // Maintain the order of the channels for each audio block (Reversed)
    for (int i = audio_block - 1; i >= 0; i--)
    {
        // Starting From End of the File (Block by Block Transferring)
        fseek(input, sizeof(WAVHEADER) + i * block_size, SEEK_SET);
        fread(buffer, block_size, 1, input);
        fwrite(buffer, block_size, 1, output);
    }
}

int check_format(WAVHEADER header)
{
    // TODO #4
    int count = 0;
    for (int i = 0; i < 4; i++)
    {
        switch (header.format[i])
        {
            case 'W':
                count++;
                break;
            case 'A':
                count++;
                break;
            case 'V':
                count++;
                break;
            case 'E':
                count++;
                break;
        }
    }
    if (count == 4)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int block_size = header.numChannels * (header.bitsPerSample / 8);
    return block_size;
}