function z
    if [ (count $argv) -lt 1 ]
        echo "Usage:"
        echo \t"z --add [directory]: add visited directory"
        echo \t"z [pattern]: print matched directory to jump to"
        return
    end
    set dir (dirname (status -f))
    if [ $argv[1] = "--add" ]
        python $dir/z.py $argv
    else
        set -l dir (python $dir/z.py $argv)
        cd $dir
    end
end

