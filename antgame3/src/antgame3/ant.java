package antgame3;
import java.util.ArrayList; 


public class ant {
	private int x;
	private int y;
	private int previousx;
	private int previousy;
	
public ant(int x, int y) {
	    this.x = x;
	    this.y = y;
	    this.previousx=x;
	    this.previousy=y;
} 

public boolean ants_same_cell(ant ant2) {
    boolean indicator = true;
    if (this.x==ant2.x && this.y==ant2.y) {
        indicator = false;
    }
    return indicator;
}



public void update_position_adjacente(int length_tab) {
	ArrayList<int[]> possiblemoves = new ArrayList<int[]>();
    if(this.x>0) {
    	int[] li = {-1, 0};
    	possiblemoves.add(li);
    }
    if(this.y>0) {
    	int[] li = {0,-1};
    	possiblemoves.add(li);
    }
    if(this.x<length_tab-1) {
    	int[] li = {1, 0};
    	possiblemoves.add(li);
    }
    if(this.y<length_tab-1){
    	int[] li = {0,1};
    	possiblemoves.add(li);
    }

    int aleatorymove = (int) (Math.random() * (possiblemoves.size()));
    int[] newposition = possiblemoves.get(aleatorymove);
    this.x = this.x+ newposition[0];
    this.y = this.y+newposition[1];
}

public void update_position_adjacenteAndDiagonale(int length_tab) {
	ArrayList<int[]> possiblemoves = new ArrayList<int[]>();
    if(this.x>0) {
    	int[] li = {-1, 0};
    	possiblemoves.add(li);
    }
    if(this.y>0) {
    	int[] li = {0,-1};
    	possiblemoves.add(li);
    }
    if(this.x<length_tab-1) {
    	int[] li = {1, 0};
    	possiblemoves.add(li);
    }
    if(this.y<length_tab-1){
    	int[] li = {0,1};
    	possiblemoves.add(li);
    }
    
    if(this.x>0&&this.y>0) {
    	int[] li = {-1, -1};
    	possiblemoves.add(li);
    }
    if(this.x>0&&this.y<length_tab-1) {
    	int[] li = {-1, 1};
    	possiblemoves.add(li);
    }
    if(this.y>0&&this.x<length_tab-1) {
    	int[] li = {1, -1};
    	possiblemoves.add(li);
    }
    if(this.y<length_tab-1&&this.x<length_tab-1){
    	int[] li = {1,1};
    	possiblemoves.add(li);
    }
    int aleatorymove = (int) (Math.random() * (possiblemoves.size()));
    int[] newposition = possiblemoves.get(aleatorymove);
    this.x = this.x+ newposition[0];
    this.y = this.y+newposition[1];
}

public void update_previousmove_notallowed(int length_tab) {
	ArrayList<int[]> possiblemoves = new ArrayList<int[]>();
    if(this.x>0&&(this.x-1!=this.previousx||this.y!=this.previousy)) {
    	int[] li = {-1, 0};
    	possiblemoves.add(li);
    }
    if(this.y>0&&(this.x!=this.previousx||this.y-1!=this.previousy)) {
    	int[] li = {0,-1};
    	possiblemoves.add(li);
    }
    if(this.x<length_tab-1&&(this.x+1!=this.previousx||this.y!=this.previousy)) {
    	int[] li = {1, 0};
    	possiblemoves.add(li);
    }
    if(this.y<length_tab-1&&(this.x!=this.previousx||this.y+1!=this.previousy)){
    	int[] li = {0,1};
    	possiblemoves.add(li);
    }
    
    if(this.x>0&&this.y>0&&(this.x-1!=this.previousx||this.y-1!=this.previousy)) {
    	int[] li = {-1, -1};
    	possiblemoves.add(li);
    }
    if(this.x>0&&this.y<length_tab-1&&(this.x-1!=this.previousx||this.y!=this.previousy)) {
    	int[] li = {-1, 1};
    	possiblemoves.add(li);
    }
    if(this.y>0&&this.x<length_tab-1&&(this.x+1!=this.previousx||this.y-1!=this.previousy)) {
    	int[] li = {1, -1};
    	possiblemoves.add(li);
    }
    if(this.y<length_tab-1&&this.x<length_tab-1&&(this.x+1!=this.previousx||this.y+1!=this.previousy)){
    	int[] li = {1,1};
    	possiblemoves.add(li);
    }
    int aleatorymove = (int) (Math.random() * (possiblemoves.size()));
    int[] newposition = possiblemoves.get(aleatorymove);
    this.previousx=this.x;
    this.previousy=this.y;
    this.x = this.x+ newposition[0];
    this.y = this.y+newposition[1];
}
}
