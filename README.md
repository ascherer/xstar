# The XStar N-body Solver

This is a specfile for packaging [Wayne Schlitt's
XStar](http://www.schlitt.net/xstar/index.html) program in the **deb** and
**rpm** formats. It has been built and tested with **debbuild 17.1.2** and
**rpmbuild 4.12.0.1**.

Download [the SOURCE package](http://www.schlitt.net/xstar/xstar.tar.gz),
add the **patch file** to the **SOURCES** directory,
put **xstar.spec** in the **SPECS** directory and run

    debbuild -ba SPECS/xstar.spec
    rpmbuild -ba SPECS/xstar.spec
