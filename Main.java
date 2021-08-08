package antgame3;

public class Main {

    public static void antGameStart(int number_simulation,int length_tab,int secondForAMove,int diagmove) {
    int compteur_time =0;
    int compteur_mean_time =0;
    ant ant1 = new ant(0,0);
    ant ant2 = new ant(length_tab-1,length_tab-1);
    for(int i=0;i<number_simulation;i++) {
        while(ant1.ants_same_cell(ant2)) {
            if (diagmove == 0) {
                ant1.update_position_adjacente(length_tab);
                ant2.update_position_adjacente(length_tab);
                compteur_time = compteur_time+1;
            }
            else {
            	if (diagmove == 1) {
	                ant1.update_position_adjacenteAndDiagonale(length_tab);
	                ant2.update_position_adjacenteAndDiagonale(length_tab);
	                compteur_time = compteur_time+1;
            	}
            	else {
	                ant1.update_previousmove_notallowed(length_tab);
	                ant2.update_previousmove_notallowed(length_tab);
	                compteur_time = compteur_time+1;
            	}
            }
        }        
        compteur_mean_time =compteur_mean_time+compteur_time;
        compteur_time=0;
        ant1 = new ant(0,0);
        ant2 = new ant(length_tab-1,length_tab-1);
    }    
    float meanProba=(float) compteur_mean_time /(float)number_simulation;
    float meanProbaSec =    secondForAMove*meanProba;     
    System.out.println("Average step : "+meanProba+" average step sec : "+meanProbaSec);
}


	public static void main(String[] args) {
		// TODO Auto-generated method stub
        int number_simulation =10000000;  
        int secondForAMove=10;
        int length_tab=8;
        System.out.println("Adjacente moves");
        //antGameStart(number_simulation,length_tab,secondForAMove,0);
        System.out.println("Diagonale moves");
        //antGameStart(number_simulation,length_tab,secondForAMove,1);
        System.out.println("Diagonale moves and previous step not allowed");
        antGameStart(number_simulation,length_tab,secondForAMove,2);

        //Average step : 82.73601 average step sec : 827.3601
        //Average step : 94.46292 average step sec : 944.6292
        //Average step : 85.858986 average step sec : 858.58984


	}

}
