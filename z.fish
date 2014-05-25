function z
    set dir (dirname (status -f))
    if [ $argv[1] = "--add" ]
        python $dir/z.py $argv
    else
        set -l dir (python $dir/z.py $argv)
        cd $dir
    end
end