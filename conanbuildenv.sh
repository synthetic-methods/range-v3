echo "echo Restoring environment" > "/Users/adventurer/Documents/synthetic-methods/C++/Packages/range-v3/deactivate_conanbuildenv.sh"
for v in 
do
    is_defined="true"
    value=$(printenv $v) || is_defined="" || true
    if [ -n "$value" ] || [ -n "$is_defined" ]
    then
        echo export "$v='$value'" >> "/Users/adventurer/Documents/synthetic-methods/C++/Packages/range-v3/deactivate_conanbuildenv.sh"
    else
        echo unset $v >> "/Users/adventurer/Documents/synthetic-methods/C++/Packages/range-v3/deactivate_conanbuildenv.sh"
    fi
done

