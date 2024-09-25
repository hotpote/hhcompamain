from main import get_parser,main
import logo

if __name__=="__main__":
    logo.logo()
    args=get_parser()
    # print(args.name,args.output)
    if args.output:
        main(args.name,args.output)
    main(args.name)
    
    