mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#339966'\n\
backgroundColor = '#F1F7FD'\n\
secondaryBackgroundColor = '#D4F0EC'\n\
textColor = '#003366'\n\
" > ~/.streamlit/config.toml
