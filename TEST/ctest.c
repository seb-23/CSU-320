


#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>

static FILE *open_file ( char *file, char *mode )
{
  FILE *fp = fopen ( file, mode );

  if ( fp == NULL ) {
    perror ( "Unable to open file" );
    exit ( EXIT_FAILURE );
  }

  return fp;
}

int main ( int argc, char *argv[] )
{
  int ch;
  FILE *in;
  FILE *out;


  if ( argc != 3 ) {
    fprintf ( stderr, "Usage: %s <readfile1> <writefile2>\n", argv[0] );
    exit ( EXIT_FAILURE );
  }

  in = open_file ( argv[1], "r" );
  out = open_file ( argv[2], "w" );

   int counter = 0;
  char yes[200000] = "";
  while ( ( ch = fgetc ( in ) ) != EOF ) {
	long long xx = ch;
	char tot[30];
	sprintf(tot, "%lld ", xx);
	printf(" %s ", tot);
	strcat(yes, tot);
	counter ++;
  }
  
 
  char * Miller = &yes[0];
	  

  printf("---counter--- %d", counter);
  fclose ( in );
  fclose ( out );



  return EXIT_SUCCESS;
}

/*
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>

static FILE *open_file ( char *file, char *mode )
{
  FILE *fp = fopen ( file, mode );

  if ( fp == NULL ) {
    perror ( "Unable to open file" );
    exit ( EXIT_FAILURE );
  }

  return fp;
}

int main ( int argc, char *argv[] )
{
  int ch;
  FILE *in;
  FILE *out;


  if ( argc != 3 ) {
    fprintf ( stderr, "Usage: %s <readfile1> <writefile2>\n", argv[0] );
    exit ( EXIT_FAILURE );
  }

  in = open_file ( argv[1], "r" );
  out = open_file ( argv[2], "w" );

 
  for (int k = 0; k < 5; k++) {
	  int i = 0;
	  char yes[25000][30];
	  while ( ( ch = fgetc ( in ) ) != EOF ) {
		 if (i == 24999) {
			 break;
		 }
		long long xx = ch;
		char tot[30];
		sprintf(tot, "%lld ", xx);
		strcpy(yes[i++], tot);
	  }
	  
	  
	  for (int von = 0; von<=i; von++) {
		fputc ( atol(yes[von]) , out);
	  }
  }


  fclose ( in );
  fclose ( out );


  return EXIT_SUCCESS;
}
*/


/*	long long xx = fgetc(in);
	char strr[2560];
	sprintf(strr, "%lld ", xx);
	printf("%s\n", strr);
  
	long long xxx = fgetc(in);
	printf("%d",xxx);
	char sstrr[2560];
	sprintf(sstrr, "%lld ", xxx);
	printf("%s\n\n", sstrr);
  
  strcpy(out[0], strr);
  strcpy(out[1], sstrr);
  //strcat(out, sstrr);
  printf("OUT: %s", out[0]);
  printf("OUT: %s", out[1]);
  
    char delim[] = " ";
	char s[20], a[20];
	//strcpy(s, strtok(out, delim));
	//strcpy(a, strtok(NULL, delim));
  //printf("\n%s", s);
  //printf("\n%s\n", a); */



/*
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>

static FILE *open_file ( char *file, char *mode )
{
  FILE *fp = fopen ( file, mode );

  if ( fp == NULL ) {
    perror ( "Unable to open file" );
    exit ( EXIT_FAILURE );
  }

  return fp;
}

int main ( int argc, char *argv[] )
{
	
	FILE * fpr;
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	

	printf("\nleft print statements\n");
	
	fpr = fopen("Joe2017.jpg", "r");					 
	if (fpr == NULL) {
		printf("Error Opening File!");
		exit(1);
	}
	
	

	
	// NEWWWWW NEWWW
	
	char large_buff[1000][1000];
	int large_index = 0;
	while ((read = getline(&line, &len, fpr)) != -1) {
		printf("% d ", large_index); // Total Number of Lines
		strcpy(large_buff[large_index++], line);
	}
	fclose(fpr);
	
	
	
	
  int ch;
  FILE *in;
  FILE *out;

  if ( argc != 3 ) {
    fprintf ( stderr, "Usage: %s <readfile1> <writefile2>\n", argv[0] );
    exit ( EXIT_FAILURE );
  }

  in = open_file ( argv[1], "r" );
  out = open_file ( argv[2], "w" );

  int tt = 0;
  while ( ( ch = fgets ( in ) ) != EOF ) {
    if (tt == large_index-1) {
		
	}
    fputc ( ch, out );
    tt++;
   }



  fclose ( in );
  fclose ( out );
	
	
	
	
  int ch;
  FILE *in;
  FILE *out;

  if ( argc != 3 ) {
    fprintf ( stderr, "Usage: %s <readfile1> <writefile2>\n", argv[0] );
    exit ( EXIT_FAILURE );
  }

  in = open_file ( argv[1], "r" );
  out = open_file ( argv[2], "w" );

  while ( ( ch = fgetc ( in ) ) != EOF )
    fputc ( ch, out );

  fclose ( in );
  fclose ( out );

  return EXIT_SUCCESS;
}


*/








/*

#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>

static FILE *open_file ( char *file, char *mode )
{
  FILE *fp = fopen ( file, mode );

  if ( fp == NULL ) {
    perror ( "Unable to open file" );
    exit ( EXIT_FAILURE );
  }

  return fp;
}

int main ( int argc, char *argv[] )
{
  int ch;
  FILE *in;
  FILE *out;


  if ( argc != 3 ) {
    fprintf ( stderr, "Usage: %s <readfile1> <writefile2>\n", argv[0] );
    exit ( EXIT_FAILURE );
  }

  in = open_file ( argv[1], "r" );
  out = open_file ( argv[2], "w" );

 
  for (int k = 0; k < 10; k++) {
	  int i = 0;
	  char yes[1024][30];
	  while ( ( ch = fgetc ( in ) ) != EOF ) {
		 if (i == 1023) {
			 break;
		 }
		long long xx = ch;
		char tot[30];
		sprintf(tot, "%lld ", xx);
		strcpy(yes[i++], tot);
	  }
	  
	  
	  if (i == 0) {
		  //break;
	  }
	  
	  
	  for (int von = 0; von<=i; von++) {
		fputc ( atol(yes[von]) , out);
	  }
  }

   
  fclose ( in );
  fclose ( out );













  return EXIT_SUCCESS;
}

*/






