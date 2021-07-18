import numpy as np
def reconstruct_from_noisy_patches(input_dict, shape):
    """
    input_dict:
    key: 4-tuple: (topleft_row, topleft_col, bottomright_row, bottomright_col): location of the patch in the original image. topleft_row, topleft_col are inclusive but bottomright_row, bottomright_col are exclusive. i.e. if M is the reconstructed matrix. M[topleft_row:bottomright_row, topleft_col:bottomright_col] will give the patch.

    value: 2d numpy array: the image patch.

    shape: shape of the original matrix.
    """
    # Initialization: Initialise M, black_count, mid_count, white_count, mid_total

    M=np.zeros(shape)
    black_count=np.zeros(shape)
    white_count=np.zeros(shape)
    mid_count=np.zeros(shape)
    mid_total=np.zeros(shape)


    for topleft_row, topleft_col, bottomright_row, bottomright_col in input_dict: # no loop except this!
        tlr, tlc, brr, brc = topleft_row, topleft_col, bottomright_row, bottomright_col
        patch = input_dict[(tlr, tlc, brr, brc)]

        black_count[tlr:brr,tlc:brc]+= patch==0
        white_count[tlr:brr,tlc:brc]+= patch==255
        patch=patch%255
        mid_count[tlr:brr,tlc:brc]+= patch>0
        mid_total[tlr:brr,tlc:brc]+= patch

        # change black_count, mid_count, white_count, mid_total here

    # Finally change M here
    M = 255*(white_count>=black_count)
    M *= white_count>0
    M *= mid_count==0
    mid_count += mid_count==0
    temp = mid_total//mid_count
    M += temp.astype(int)

    return M # You have to return the reconstructed matrix (M).
