package IA.ProbIA5;

import java.util.Arrays;

/**
 * Created by bejar on 17/01/17.
 */
public class ProbIA5Board {
    /* Class independent from AIMA classes
       - It has to implement the state of the problem and its operators
     *

    /* State data structure
        vector with the parity of the coins (we can assume 0 = heads, 1 = tails
     */

    private int [] board;
    private static int [] solution;

    /* Constructor */
    public ProbIA5Board(int []init, int[] goal) {

        board = new int[init.length];
        solution = new int[init.length];

        for (int i = 0; i< init.length; i++) {
            board[i] = init[i];
            solution[i] = goal[i];
        }

    }

    /* vvvvv TO COMPLETE vvvvv */
    public void flip_it(int i){
        // flip the coins i and i + 1
        int max = board.length;
        int next = (i+1)%max;
        int aux = board[next];
        board[next] = board[i];
        board[i] = aux;
    }

    /* Heuristic function */
    public double heuristic(){
        // compute the number of coins out of place respect to solution
        int res = 0;
        for (int i = 0; i < board.length; i++) {
            if (board[i] != solution[i]) res++;
        }
        return res;
    }

     /* Goal test */
     public boolean is_goal(){
        
        return Arrays.equals(solution, board);
     }

     /* auxiliary functions */

     // Some functions will be needed for creating a copy of the state
    public ProbIA5Board clone() {
        ProbIA5Board res = new ProbIA5Board(board, solution);
        return res;
    }

    public int getBoardLength() {
        return board.length;
    }
    /* ^^^^^ TO COMPLETE ^^^^^ */

}
