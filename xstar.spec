Name: xstar
Summary: XStar by Wayne Schlitt <wayne@schlitt.net>
Version: 2.2.0
Release: 6
Packager: Andreas Scherer <https://ascherer.github.io/>
License: GPLv2+

URL: http://www.schlitt.net/xstar/index.html
Source: http://www.schlitt.net/xstar/%{name}.tar.gz
Patch: 0001-Replace-oldstyle-typedefs-with-C99-standard-types.patch

%if %{_vendor} == "debbuild"
Distribution: Kubuntu 18.04 (x86_64)
Group: science
%else
Distribution: openSUSE 42 (x86_64)
Group: Productivity/Scientific/Astronomy
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The 'xstar' program "solves" the n-body problem, and displays the results
on the screen.  It starts by putting a bunch of stars on the screen, and
then it lets the inter-body gravitational forces move the stars around.
The result is a lot of neat wandering paths, as the stars interact and
collide.

XStar can be used to animate the root window, as a screen saver or just
to display stuff in a regular window.

%prep
%autosetup

%build
%{__make} -f Makefile.simple

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} \
	%{buildroot}/%{_docdir}/%{name} \
	%{buildroot}/%{_mandir}/man1
%{__install} xstar %{buildroot}%{_bindir}
%{__install} -pm 664 n-body.ps theory_of_op.ltr %{buildroot}/%{_docdir}/%{name}
%{__install} -m 644 xstar.1 %{buildroot}/%{_mandir}/man1

%files
%defattr(-,root,root,-)
%{_bindir}/xstar
%doc %{_docdir}/xstar
%doc %{_mandir}/man1/xstar.1.gz

%changelog
* Sun Jan 15 2017 Andreas Scherer <andreas_tex@freenet.de> 2.2.0-6
- Cleanup specfile
* Thu Oct 29 2015 Andreas Scherer <andreas_tex@freenet.de> 2.2.0-6
- Fully parametrized specfile
* Sat Mar 02 2013 Andreas Scherer <andreas_tex@freenet.de> 2.2.0-5
- dpkg --configure complains about format error in description
* Mon Aug 01 2011 Andreas Scherer <andreas_tex@freenet.de> 2.2.0-4
- dpkg complains about missing maintainer
* Wed Jan 19 2011 Andreas Scherer <andreas_tex@freenet.de> 2.2.0-3
- Rebuild for KUbuntu
* Mon Oct 31 2005 Andreas Scherer <andreas_tug@freenet.de> 2.2.0-2
- Not-quite-local installation
* Mon Oct 31 2005 Andreas Scherer <andreas_tug@freenet.de> 2.2.0-1
- Initial build
