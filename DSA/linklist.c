#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}node;

void main(){
    int n;
    printf("Enter the limit: ");
    scanf("%d",&n);
    struct node* head=NULL,*temp,*current;
    for(int i=0;i<n;i++){
        struct node* newnode=(struct node*)malloc(sizeof(node));
        printf("Enter the data: "); 
        scanf("%d",&newnode->data);
        newnode->next=NULL;
        node* temp=head;
        if(head==NULL){
            head=newnode;
            current = newnode;
        }
        else{
        current->next=newnode;
        current=newnode;
        }
    }
    temp=head;
    while (temp!=NULL)
    {
        printf("%d->",temp->data);
        temp=temp->next;
    }
    printf("NULL");
}