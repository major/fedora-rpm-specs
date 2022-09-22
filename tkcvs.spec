Name:		tkcvs
Version:	8.2.3
Release:	16%{?dist}

Summary:	TkCVS and TkDiff

# No version specified.
License:	GPL+
URL:		https://sourceforge.net/projects/tkcvs
Source:		http://www.twobarleycorns.net/%{name}-%{version}.tar.gz
BuildRequires:	perl-interpreter
Requires:	tk
Requires:	tcl
Requires:	cvs
BuildArch:	noarch
Provides:	mergetool

%description
TkCVS is a Tcl/Tk-based graphical interface to the CVS and Subversion
configuration management systems. It will also help with RCS. TkDiff
is included for browsing and merging your changes.

TkCVS shows the status of the files in the current working directory,
and has tools for tagging, merging, importing, exporting, checking
in/out, and other user operations.

TkCVS also aids in browsing the repository. For Subversion, the
repository tree is browsed like an ordinary file tree. For CVS, the
CVSROOT/modules file is read. TkCVS extends CVS with a method to
produce a "user friendly" listing of modules. This requires special
comments in the CVSROOT/modules file.

Although TkCVS now supports Subversion, it will still work happily
without it in your CVS directories. It didn't abandon CVS, it just
grew some new capabilities.


%prep
%autosetup


%build
perl -pi -e 's|set TCDIR \[file join \$TclRoot tkcvs\]|set TCDIR "%{_datadir}/tkcvs"|' tkcvs/tkcvs.tcl
perl -pi -e 's|\[file join \$TclRoot tkcvs bitmaps\]|\[file join \$TCDIR bitmaps\]|' tkcvs/tkcvs.tcl


%install
install -d ${RPM_BUILD_ROOT}%{_datadir}
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
cd tkcvs
install -m 0755 tkcvs.tcl ${RPM_BUILD_ROOT}%{_bindir}/tkcvs
rm -f tkcvs.blank mklocal mkmanpage.pl
install -m 0644 tkcvs.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
cd ../tkdiff
install -m 0755 tkdiff ${RPM_BUILD_ROOT}%{_bindir}
cd ..
cp -fr tkcvs ${RPM_BUILD_ROOT}%{_datadir}


%files
%doc CHANGELOG.txt LICENSE.txt FAQ.txt
%{_datadir}/tkcvs
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 8.2.3-7
- Rebuilt to fix FTBFS in rawhide + spec cleanup
- Fixes rhbz #1424132 and rhbz #990450

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep  2 2014 Lubomir Rintel <lkundrak@v3.sk> - 8.2.3-1
- new release 8.2.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb  5 2011 Gérard Milmeister <gemi@bluewin.ch> - 8.2.2-1
- new release 8.2.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec  7 2008 Gerard Milmeister <gemi@bluewin.ch> - 8.2-1
- mew release 8.2

* Sat Nov 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 8.1-1
- new release 8.1

* Mon May 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 8.0.4-1
- new version 8.0.4

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 8.0.3-2
- Rebuild for FE6

* Sun Mar 26 2006 Gerard Milmeister <gemi@bluewin.ch> - 8.0.3-1
- new version 8.0.3

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 8.0.2-2
- Rebuild for Fedora Extras 5

* Tue Jan 31 2006 Gerard Milmeister <gemi@bluewin.ch> - 8.0.2-1
- new version 8.0.2

* Sun Jan 15 2006 Gerard Milmeister <gemi@bluewin.ch> - 8.0.1-1
- new version 8.0.1

* Mon Jan  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 8.0
- new version 8.0

* Sat Aug 13 2005 Gerard Milmeister <gemi@bluewin.ch> - 7.2.4
- new version 7.2.4

* Tue Jul  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 7.2.3-1
- new version 7.2.3

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb 14 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:7.2.2-2
- Changed tk-devel and tcl-devel to tk and tcl
- Moved %%{_libdir}/tkcvs to %%{_datadir}/tkcvs

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:7.2.2-1
- New Version 7.2.2

* Sun May  2 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:7.2.1-0.fdr.1
- New Version 7.2.1

* Sun Jan  4 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:7.2-0.fdr.1
- New Version 7.2

* Wed Nov  5 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:7.1.4-0.fdr.1
- New Version 7.1.4

* Sun Oct 26 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:7.1.3-0.fdr.2
- Improved specfile

* Tue Oct 21 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:7.1.3-0.fdr.1
- New Version 7.1.3

* Sat Oct 18 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:7.1.2-0.fdr.1
- First Fedora release
