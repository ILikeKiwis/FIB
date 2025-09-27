package IA.ProbIA5;

import aima.search.framework.SuccessorFunction;
import aima.search.framework.Successor;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by bejar on 17/01/17
 */
public class ProbIA5SuccesorFunction implements SuccessorFunction{

    public List getSuccessors(Object state){
        ArrayList retval = new ArrayList();
        ProbIA5Board board = (ProbIA5Board) state;
        
        // Some code here
        // (flip all the consecutive pairs of coins and generate new states
        // Add the states to retval as Succesor("flip i j", new_state)
        // new_state has to be a copy of state
        int l = board.getBoardLength();
 
        for (int i = 0; i < l; i++) {
            ProbIA5Board res = board.clone();
            res.flip_it(i);
            Successor s = new Successor(String.format("flip %d %d", i, i+1), res);
            retval.add(s);
        }
        

        return retval;

    }

}
