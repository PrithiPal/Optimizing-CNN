#!/bin/bash
FILENAME='/etc/hosts'

add_node(){
## code to add this entry to the /etc/hsots
echo -e "$2\t$1" >> $FILENAME
cat $FILENAME

}

remove_node(){
STR="^$2.*$1$"
echo -e "removing $STR"
sudo sed -e "s/^$2.*$1$/*/g" -i .backup $FILENAME
cat $FILENAME
}

subcommand=$1

shift;
case $subcommand in
  add)

    while getopts "n:i:" node_details;do
      case $node_details in
        n)
          NODE_NAME="$OPTARG"
          ;;
        i)
          NODE_IP="$OPTARG"
          ;;
      esac
    done
    add_node $NODE_NAME $NODE_IP
    ;;
  remove)
    while getopts "n:i:" node_details;do
      case $node_details in
        n)
          NODE_NAME="$OPTARG"
          ;;
        i)
          NODE_IP="$OPTARG"
          ;;
      esac
    done
      remove_node $NODE_NAME $NODE_IP
      ;;
esac
