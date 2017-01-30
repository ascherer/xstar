# The XStar N-body Solver

This is a specfile for packaging [Wayne Schlitt's
XStar](http://www.schlitt.net/xstar/index.html) program in the **deb** and
**rpm** formats. It has been built and tested with **debbuild 17** and
**rpmbuild 4.2**.

Download [the SOURCE package](http://www.schlitt.net/xstar/xstar.tar.gz),
put **xstar.spec** in the **SPECS** directory and run

    debbuild -ba SPECS/xstar.spec
    rpmbuild -ba SPECS/xstar.spec
