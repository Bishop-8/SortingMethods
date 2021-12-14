using namespace std;

int* BubbleSort (int array[], int size){
  int passvalue = 0;
  int unsortedSize = size;
  while (passvalue == 0){
    passvalue = 1;
    for (int k = 0; k < unsortedSize - 1; k++){
	  if (array[k] > array[k + 1]){
	    swap (array[k], array[k + 1]);
	    passvalue = 0;
	  }
	}   
  }
  return array;
}

//Don't really need this stuff, but included just in case
int main ()
{
  srand (time (0));
  int size = 50;
  int Arr[size];
  for (int i = 0; i < size; i++)
    {
      Arr[i] = rand () % 100;
    }
  for (int j = 0; j < size; j++)
    {
      cout << Arr[j] << ' ';
    }
  BubbleSort (Arr, size);
  cout << '\n';
  for (int j = 0; j < size; j++)
    {
      cout << Arr[j] << ' ';
    }
  return 0;
}
