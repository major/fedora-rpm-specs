%?mingw_package_header

%global name1 qwt

# build qt4 support (or not)
%global qt4 0
# build qt5 support (or not)
%global qt5 1

Name:           mingw-%{name1}
Summary:        MinGW Windows Qwt library
Version:        6.1.5
Release:        5%{?dist}
URL:            http://qwt.sourceforge.net
License:        LGPLv2 with exceptions
Source:         http://downloads.sourceforge.net/%{name1}/%{name1}-%{version}.tar.bz2
# fix pkgconfig support
Patch50:        qwt-6.1.1-pkgconfig.patch
# use QT_INSTALL_ paths instead of custom prefix
Patch51:        qwt-6.1.5-qt_install_paths.patch
# parallel-installable qt5 version
Patch52:        qwt-qt5.patch
BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  perl
%if 0%{?qt4}
BuildRequires:  mingw32-qt
BuildRequires:  mingw64-qt
%endif
%if 0%{?qt5}
BuildRequires:  mingw32-qt5-qmake
BuildRequires:  mingw64-qt5-qmake
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw32-qt5-qtbase-devel
BuildRequires:  mingw64-qt5-qtbase-devel
BuildRequires:  mingw32-qt5-qtsvg
BuildRequires:  mingw64-qt5-qtsvg
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw64-qt5-qttools
%endif
BuildArch:      noarch

%description
MinGW Windows Qwt library.


%if 0%{?qt4}
%package -n mingw32-%{name1}
Summary:        MinGW Windows Qwt library

%description -n mingw32-%{name1}
MinGW Windows Qwt library.

%package -n mingw64-%{name1}
Summary:        MinGW Windows Qwt library

%description -n mingw64-%{name1}
MinGW Windows Qwt library.
%endif

%if 0%{?qt5}
%package -n mingw32-%{name1}-qt5
Summary:        MinGW Windows Qwt library

%description -n mingw32-%{name1}-qt5
MinGW Windows Qwt library.

%package -n mingw64-%{name1}-qt5
Summary:        MinGW Windows Qwt library

%description -n mingw64-%{name1}-qt5
MinGW Windows Qwt library.
%endif


%?mingw_debug_package

%prep
%setup -qcn %{name1}-%{version}
pushd %{name1}-%{version}
%patch50 -p1 -b .pkgconfig
%patch51 -p1 -b .qt_install_paths
%patch52 -p1 -b .qt5
popd
mv %{name1}-%{version} win32
cp -r win32 win64
%if 0%{?qt5}
cp -r win32 win32qt5
cp -r win64 win64qt5
perl -i -pe 's,debug_and_release,release,' win32qt5/qwtbuild.pri
perl -i -pe 's,debug_and_release,release,' win64qt5/qwtbuild.pri
echo "CONFIG -= debug" >> win32qt5/qwtbuild.pri
echo "CONFIG -= debug" >> win64qt5/qwtbuild.pri
echo "CONFIG -= debug" >> win32qt5/src/src.pro
echo "CONFIG -= debug" >> win64qt5/src/src.pro
echo "CONFIG -= debug_and_release" >> win32qt5/src/src.pro
echo "CONFIG -= debug_and_release" >> win64qt5/src/src.pro
echo "CONFIG -= debug" >> win32qt5/textengines/mathml/mathml.pro
echo "CONFIG -= debug" >> win64qt5/textengines/mathml/mathml.pro
echo "CONFIG -= debug_and_release" >> win32qt5/textengines/mathml/mathml.pro
echo "CONFIG -= debug_and_release" >> win64qt5/textengines/mathml/mathml.pro
%endif

%build
%if 0%{?qt5}
%if 0%{?mingw_build_win32} == 1
pushd win32qt5
%mingw32_qmake_qt5 QWT_CONFIG+=QwtPkgConfig
make %{?_smp_mflags}
popd
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64qt5
%mingw64_qmake_qt5 QWT_CONFIG+=QwtPkgConfig
make %{?_smp_mflags}
popd
%endif
%endif

%if 0%{?qt4}
%if 0%{?mingw_build_win32} == 1
pushd win32
%mingw32_qmake_qt4 QWT_CONFIG+=QwtPkgConfig
make qmake
pushd textengines
make qmake
popd
perl -i -pe 's,qwt4,qwt,' textengines/mathml/Makefile.Release
perl -i -pe 's,qwt4d,qwtd,' textengines/mathml/Makefile.Debug
make %{?_smp_mflags}
popd
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64
%mingw64_qmake_qt4 QWT_CONFIG+=QwtPkgConfig
make qmake
pushd textengines
make qmake
popd
perl -i -pe 's,qwt4,qwt,' textengines/mathml/Makefile.Release
perl -i -pe 's,qwt4d,qwtd,' textengines/mathml/Makefile.Debug
make %{?_smp_mflags}
popd
%endif
%endif

%install
%if 0%{?qt5}
%if 0%{?mingw_build_win32} == 1
pushd win32qt5
make INSTALL_ROOT=$RPM_BUILD_ROOT install
popd
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/doc
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
mv $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll $RPM_BUILD_ROOT%{mingw32_bindir}
mv $RPM_BUILD_ROOT%{mingw32_libdir}/qt5/plugins/designer/%{name1}_designer_plugin.dll $RPM_BUILD_ROOT%{mingw32_bindir}/%{name1}_designer_plugin-qt5.dll
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64qt5
make INSTALL_ROOT=$RPM_BUILD_ROOT install
popd
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/doc
mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll $RPM_BUILD_ROOT%{mingw64_bindir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/qt5/plugins/designer/%{name1}_designer_plugin.dll $RPM_BUILD_ROOT%{mingw64_bindir}/%{name1}_designer_plugin-qt5.dll
%endif
%endif

%if 0%{?qt4}
%if 0%{?mingw_build_win32} == 1
pushd win32
make INSTALL_ROOT=$RPM_BUILD_ROOT install
popd
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/doc
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
mv $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll $RPM_BUILD_ROOT%{mingw32_bindir}
mv $RPM_BUILD_ROOT%{mingw32_libdir}/qt4/plugins/designer/%{name1}_designer_plugin.dll $RPM_BUILD_ROOT%{mingw32_bindir}
%endif
%if 0%{?mingw_build_win64} == 1
pushd win64
make INSTALL_ROOT=$RPM_BUILD_ROOT install
popd
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/doc
mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll $RPM_BUILD_ROOT%{mingw64_bindir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/qt4/plugins/designer/%{name1}_designer_plugin.dll $RPM_BUILD_ROOT%{mingw64_bindir}
%endif
%endif

%if 0%{?qt4}
%files -n mingw32-%{name1}
%doc win32/COPYING
%doc win32/README
%{mingw32_bindir}/%{name1}.dll
%{mingw32_bindir}/%{name1}d.dll
%{mingw32_bindir}/%{name1}mathml.dll
%{mingw32_bindir}/%{name1}mathmld.dll
%{mingw32_bindir}/%{name1}_designer_plugin.dll
%{mingw32_includedir}/%{name1}
%{mingw32_libdir}/lib%{name1}.a
%{mingw32_libdir}/lib%{name1}d.a
%{mingw32_libdir}/lib%{name1}mathml.a
%{mingw32_libdir}/lib%{name1}mathmld.a
%{mingw32_datadir}/qt4/mkspecs/features/qwt*
%{mingw32_libdir}/pkgconfig/*.pc

%files -n mingw64-%{name1}
%doc win64/COPYING
%doc win64/README
%{mingw64_bindir}/%{name1}.dll
%{mingw64_bindir}/%{name1}d.dll
%{mingw64_bindir}/%{name1}mathml.dll
%{mingw64_bindir}/%{name1}mathmld.dll
%{mingw64_bindir}/%{name1}_designer_plugin.dll
%{mingw64_includedir}/%{name1}
%{mingw64_libdir}/lib%{name1}.a
%{mingw64_libdir}/lib%{name1}d.a
%{mingw64_libdir}/lib%{name1}mathml.a
%{mingw64_libdir}/lib%{name1}mathmld.a
%{mingw64_datadir}/qt4/mkspecs/features/qwt*
%{mingw64_libdir}/pkgconfig/*.pc
%endif

%if 0%{?qt5}
%files -n mingw32-%{name1}-qt5
%doc win32/COPYING
%doc win32/README
%{mingw32_bindir}/%{name1}-qt5.dll
%{mingw32_bindir}/%{name1}mathml-qt5.dll
%{mingw32_libdir}/lib%{name1}-qt5.dll.a
%{mingw32_libdir}/lib%{name1}mathml-qt5.dll.a
%{mingw32_bindir}/%{name1}_designer_plugin-qt5.dll
%{mingw32_includedir}/qt5/%{name1}
%{mingw32_datadir}/qt5/mkspecs/features/qwt*
%{mingw32_libdir}/pkgconfig/Qt5Qwt6.pc
%{mingw32_libdir}/pkgconfig/qwtmathml-qt5.pc

%files -n mingw64-%{name1}-qt5
%doc win64/COPYING
%doc win64/README
%{mingw64_bindir}/%{name1}-qt5.dll
%{mingw64_bindir}/%{name1}mathml-qt5.dll
%{mingw64_libdir}/lib%{name1}-qt5.dll.a
%{mingw64_libdir}/lib%{name1}mathml-qt5.dll.a
%{mingw64_bindir}/%{name1}_designer_plugin-qt5.dll
%{mingw64_includedir}/qt5/%{name1}
%{mingw64_datadir}/qt5/mkspecs/features/qwt*
%{mingw64_libdir}/pkgconfig/Qt5Qwt6.pc
%{mingw64_libdir}/pkgconfig/qwtmathml-qt5.pc
%endif

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.1.5-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 01 2021 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.1.5-1
- update to 6.1.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 6.1.3-8
- Rebuild (Changes/Mingw32GccDwarf2)
- Drop Qt4 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Richard W.M. Jones <rjones@redhat.com> - 6.1.3-4
- Remove buildroot.

* Mon May 28 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.1.3-3
- fix build failure

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 05 2017 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.1.3-1
- update to 6.1.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.1.2-2
- enable qt5 build

* Fri Jan 02 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.1.2-1
- update to 6.1.2

* Wed Nov 05 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.1.1-1
- update to 6.1.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.1.0-1
- update to 6.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 6.0.1-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Tue Dec  4 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 6.0.1-1
- update to 6.0.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-7
- Use the correct qmake macros to build this package

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 5.2.1-6
- Renamed the source package to mingw-qwt (#801020)
- Modernize the spec file
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2.1-5
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 5.2.1-3
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 23 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.2.1-1
- update to 5.2.1

* Sat Feb 13 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.2.0-3
- qt 4.6.1 compile workaround

* Wed Dec  2 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.2.0-2
- qt 4.6.0 compile workarounds

* Tue Nov 24 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.2.0-1
- update to 5.2.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.1.1-8
- add debuginfo packages

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.1.1-7
- replace %%define with %%global

* Mon Mar 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.1.1-6
- actually fix the source line as required by the reviewer
- remove commented out designer files in files section

* Mon Mar 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.1.1-5
- fix missing BR

* Fri Mar 13 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.1.1-4
- enable debug build

* Wed Mar 11 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 5.1.1-3
- copied from native qwt
