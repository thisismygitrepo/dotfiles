
# install https://visualstudio.microsoft.com/visual-cpp-build-tools/
# winget install Microsoft.VisualStudio.2022.BuildTools
winget install Graphviz.Graphviz
~/scritps/activate_ve.ps1
cd C:
python -m pip install --global-option=build_ext --global-option="-IC:\Program Files\Graphviz\include" --global-option="-LC:\Program Files\Graphviz\lib" pygraphviz

