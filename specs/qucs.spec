# Support a digital simulation with FreeHDL
%bcond_with qucs_enables_freehdl

Summary: Circuit simulator
Name:    qucs
Version: 0.0.20~rc2
Release: 9%{?dist}
License: GPL-1.0-or-later
URL:     http://qucs.sourceforge.net/
Source0: https://github.com/Qucs/%{name}/archive/%{name}-%{version_no_tilde}/%{name}-%{version_no_tilde}.tar.gz

# Desktop file categories must terminate with a semicolon, bug #1424234
Patch0:  qucs-0.0.19-fix-desktop-file.patch
# https://github.com/Qucs/qucs/pull/1069
Patch1:  qucs-0.0.20-rc2-gcc13.patch

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: coreutils
BuildRequires: desktop-file-utils
BuildRequires: qt-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: gperf
BuildRequires: mot-adms >= 2.3.4
BuildRequires: octave-devel
BuildRequires: doxygen
BuildRequires: transfig
BuildRequires: latex2html
BuildRequires: texlive
BuildRequires: texlive-SIunits
BuildRequires: texlive-relsize
BuildRequires: texlive-IEEEtran
BuildRequires: texlive-savesym
BuildRequires: texlive-subfigure
BuildRequires: texlive-keystroke
BuildRequires: texlive-epstopdf
BuildRequires: texlive-stmaryrd
%if %{with qucs_enables_freehdl}
Requires: freehdl
%endif
Requires: perl-interpreter, iverilog
Requires: electronics-menu
Requires: mot-adms >= 2.3.4
Requires: hicolor-icon-theme


%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.


%package lib
Summary:  Qucs library


%description lib
Qucs circuit simulator library


%package devel
Summary:  Qucs development headers
Requires: %{name}-lib%{?_isa} = %{version}-%{release}


%description devel
Qucs circuit simulator development headers


%prep
%autosetup -n %{name}-%{name}-%{version_no_tilde} -p1

# fix file modes
chmod 644 qucs/{AUTHORS,COPYING,ChangeLog,NEWS,README,THANKS,TODO}


%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"

autoreconf -fi
# latex docs seems broken, disable for now
%configure --disable-dependency-tracking --enable-debug=yes --disable-doc

# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' qucs-core/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' qucs-core/libtool

# drop rpath from the LDFLAGS
# parallel build not working
%make_build -j1 qucsconv_LDFLAGS= qucsator_LDFLAGS=


%install
%make_install
install -d %{buildroot}%{_datadir}/applications

%if !%{with qucs_enables_freehdl}
rm -f %{buildroot}/%{_bindir}/qucsdigi*
rm -f %{buildroot}/%{_mandir}/man1/qucsdigi*
rm -f %{buildroot}/%{_datadir}/qucs/docs/*/{qucsdigi.png,start_digi.html}
%endif

desktop-file-install \
    --add-category "X-Fedora" \
    --add-category "Engineering" \
    --set-icon "qucs" \
    --dir=%{buildroot}%{_datadir}/applications \
    qucs/qucs/%{name}.desktop

# drop .la
rm -f %{buildroot}%{_libdir}/libqucs.la


%files
%license qucs/COPYING
%doc qucs/AUTHORS qucs/ChangeLog qucs/NEWS NEWS.md README.md qucs/README qucs/THANKS qucs/TODO
%{_bindir}/qucs*
%{_bindir}/ps2sp*
%{_datadir}/%{name}
%{_datadir}/qucsator
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/icons/*/*/*


%files lib
%{_libdir}/libqucsator.so.*


%files devel
%{_includedir}/*
%{_libdir}/libqucsator.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20~rc2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20~rc2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.20~rc2-7
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20~rc2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20~rc2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20~rc2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20~rc2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.20~rc2-1
- New version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.19-4
- Improved icons packaging

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.19-2
- Switched to the upstream latex-fix patch

* Wed Aug 12 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.0.19-1
- New version
  Resolves: rhbz#1416791

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Petr Pisar <ppisar@redhat.com> - 0.0.18-19
- Restore compatibility with GCC 10 (bug #1799962)
- Remove a dependency on a nonexistent freehdl (bug #1732605)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.0.18-14
- rebuilt due new iverilog

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.18-13
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.0.18-10
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>
- Correct desktop file installation (bug #1424234)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Rafael Fonseca <rdossant@redhat.com> - 0.0.18-7
- Workaround gcc bug on ppc64le (#1299599)

* Tue Jan 19 2016 Jaromir Capik <jcapik@redhat.com> - 0.0.18-6
- Dropping built-in adms and using the system one (#1230751)
- Fixing the qucrescodes->qucsrescodes program name typo

* Wed Jan 13 2016 Jaromir Capik <jcapik@redhat.com> - 0.0.18-5
- Fixing the icon path (#1279203)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.18-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Sep 10 2014 Jaromir Capik <jcapik@redhat.com> - 0.0.18-2
- Disabling the debug

* Tue Sep 02 2014 Jaromir Capik <jcapik@redhat.com> - 0.0.18-1
- Update to 0.0.18

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Jaromir Capik <jcapik@redhat.com> - 0.0.17-3
- Fixing format-security flaws (#1037299)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.17-1
- Update to 0.0.17
- Fixing Source0 URL

* Fri May 24 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.16-7
- Adding electronics-menu in the requires
- Minor spec file changes according to the latest guidelines

* Mon Apr 08 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.16-6
- aarch64 support (#926417)
- fixing bogus date in the changelog

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.0.16-5
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 03 2011 Bruno Wolff III <bruno@wolff.to> - 0.0.16-1
- Update to upstream 0.0.16
- Fix FTBFS - bug 631404

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-3
- Patch no longer needed with freehdl-0.0.7

* Sun May 03 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-2
- Correct a problem in digital simulation

* Fri May 01 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-1
- Update to 0.0.15

* Sat Apr 05 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.14-1
- Update to 0.0.14

* Sat Apr 05 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.13-3
- Modify BR from qt-devel to qt3-devel

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.13-2
- Autorebuild for GCC 4.3

* Tue Jan 01 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.13-1
- Update to 0.0.13

* Sun Sep 09 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-4
- Modifiy qucs.desktop BZ 283941

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.12-3
- Rebuild for selinux ppc32 issue.

* Sun Jun 17 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-2
- Add perl and iverilog as require

* Sun Jun 17 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-1
- Update to 0.0.12

* Sat May 05 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.11-2
- Rebuild

* Sun Mar 18 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.11-1
- Update to 0.0.11

* Fri Sep 01 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.10-1
- Update to 0.0.10

* Sat Jun 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-4
- Solve typo problem in changelog

* Sat Jun 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-3
- Delete %%{_bindir}/qucsdigi.bat which is a windows bat file and useless under linux
- add --disable-dependency-tracking to %%configure
- add --enable-debug to %%configure to make debuginfo package usefull

* Thu Jun 01 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-2
- Delete ${RPM_OPT_FLAGS} modification using -ffriend-injection for "%%{?fedora}" > "4"

* Mon May 29 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-1
- Update to 0.0.9

* Mon Jan 23 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.8-1
- Update to 0.0.8
- Add -ffriend-injection to $RPM_OPT_FLAGS for building against gcc-4.1
 
* Fri Nov 4 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-8
- Modify ctaegories in qucs.desktop

* Wed Oct 19 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-7
- Add qucs-0.0.7-2.diff for the x86_64 target

* Tue Oct 18 2005 Ralf Corsepius <rc040203@freenet.de> - 0.0.7-6
- Add qucs-0.0.7-config.diff to make configure script aware of RPM_OPT_FLAGS.

* Tue Oct 11 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-5
-add qucs.desktop
-modify buildroot

* Tue Aug 2 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.7.

* Thu Jun 23 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- rebuilt for Fedora Core 4

* Mon May 30 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.6.

* Thu Mar 3 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.5.

* Fri Dec 10 2004 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.4 for Fedora Core 3
