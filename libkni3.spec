Name:           libkni3
Version:        3.9.2
Release:        48%{?dist}
Summary:        C++ KNI library v3 for the Katana 300 robot arm

License:        GPLv2+
URL:            http://www.neuronics.ch/cms_de/web/index.php?id=386
Source0:        http://www.neuronics.ch/cms_de/mediabase/KNI_3.9.2.tar.gz
Patch0:         kni-3.9.2-gcc43.patch
Patch1:         kni-3.9.2-sofixes.patch
Patch2:         kni-3.9.2-ctor.patch
Patch3:         kni-3.9.2-noexit.patch
Patch4:         kni-3.9.2-gcc47.patch
# Make makefiles verbose
Patch5:         kni-3.9.2-verbose.patch
Patch6:         kni-3.9.2-format-security.patch

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

BuildRequires: make
BuildRequires:  gcc, gcc-c++
BuildRequires:  doxygen, graphviz
%if 0%{?fedora} >= 18
BuildRequires:  texlive-collection-latexrecommended
%else
BuildRequires:  tetex
%endif

BuildRequires:  boost-devel

%description
Katana Native Interface is a C++ library for programmers who would like to
write their own programs, but don't want to implement the protocol and
device stuff katana is using.

This package contains the library for the Katana 300 series of the arm. For
newer robots use libkni (version 4 and above).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel = %{version}-%{release}

%description    static
This package contains static libraries that can be used to
compile static binaries using %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains the documentation for developing with %{name}.

%package        examples
Summary:        Example applications for %{name}
Requires:       %{name} = %{version}-%{release}

%description    examples
This package contains demo applications for %{name}.

%prep
%setup -q -n KNI_%{version}
%patch0 -p1 -b .gcc43
%patch1 -p1 -b .sofixes
%patch2 -p1 -b .ctor
%patch3 -p1 -b .noexit
%patch4 -p1 -b .gcc47
%patch5 -p1
%patch6 -p1 -b .format

%build
make CXXFLAGS="%{optflags} -fPIC"
make doc
echo "prefix=%{prefix}
exec_prefix=%{prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: %{summary}
Version: %{version}
Libs: -L\${libdir} -lKNIBase3 -lKNI_InvKin3 -lKNI_LM3
Cflags: -I\${includedir}/kni3" > libkni3.pc


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
mkdir -p %{buildroot}%{_libdir}
install -m 0644 -p lib/linux/*.a %{buildroot}%{_libdir}
install -p lib/linux/*.so.* %{buildroot}%{_libdir}
for f in `find %{buildroot}%{_libdir} -name '*.so.*.*.*'`; do
    ln -s `basename $f` %{buildroot}%{_libdir}/`echo \`basename $f\` | sed -e 's/\(\(.*\).so\)\(.*\)/\1/'`
    ln -s `basename $f` %{buildroot}%{_libdir}/`objdump --private-headers $f | grep SONAME | awk '{print $2}'`
done
mkdir -p %{buildroot}%{_bindir}
for f in `find demo/ -perm /a+x -type f`; do
    install -p $f %{buildroot}%{_bindir}/kni_`basename $f`
done
mkdir -p %{buildroot}%{_sysconfdir}/kni3
mkdir -p %{buildroot}%{_sysconfdir}/kni3/hd300
mkdir -p %{buildroot}%{_sysconfdir}/kni3/hd400
install -p -m 0644 configfiles300/*.cfg %{buildroot}%{_sysconfdir}/kni3/hd300
install -p -m 0644 configfiles400/*.cfg %{buildroot}%{_sysconfdir}/kni3/hd400
mkdir -p %{buildroot}%{_includedir}/kni3
cp -a include/* %{buildroot}%{_includedir}/kni3
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a doc/html %{buildroot}%{_pkgdocdir}
install -p -m 0644 doc/*.pdf %{buildroot}%{_pkgdocdir}
find %{buildroot} -name '.svn' | xargs rm -rf
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -p -m 0644 libkni3.pc %{buildroot}%{_libdir}/pkgconfig



%ldconfig_scriptlets


%files
%doc LICENSE.txt readme.txt AUTHORS.txt
%exclude %{_pkgdocdir}/html
%exclude %{_pkgdocdir}/*.pdf
%{_libdir}/*.so.*
%dir %{_sysconfdir}/kni3
%dir %{_sysconfdir}/kni3/hd300
%dir %{_sysconfdir}/kni3/hd400
%config(noreplace)%{_sysconfdir}/kni3/*/*.cfg

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files static
%{_libdir}/*.a

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%{_pkgdocdir}/*.pdf

%files examples
%{_bindir}/kni_*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Tim Niemueller <tim@niemueller.de> - 3.9.2-39
- BR gcc and gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.9.2-34
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 3.9.2-32
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.9.2-31
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-30
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.9.2-29
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.9.2-27
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.9.2-26
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.9.2-24
- Fix FTBFS with -Werror=format-security (#1037167, #1106032)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.9.2-22
- Rebuild for boost 1.55.0

* Mon Aug 26 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.9.2-21
- Address F20FTBFS (RHBZ#991895), F19FTBFS (RHBZ#914134):
  - Package did not acknowledge RPM_OPT_FLAGS.
  - Fix link order.
  - BR: texlive-collection-latexrecommended
- Make Makefiles verbose (Add libkni3-3.9.2-verbose.patch).
- Reflect docdir changes (RHBZ#993829).
- Fold-in *doc package's contents into %%{_pkgdocdir}.
- Make *doc-package noarch.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 3.9.2-19
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar  8 2012 Tom Callaway <spot@fedoraproject.org> - 3.9.2-16
- fix build with gcc 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-15
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 14 2009 Tim Niemueller <tim@niemueller.de> - 3.9.2-12
- doc package contains doc dir, not docs

* Fri Aug 28 2009 Tim Niemueller <tim@niemueller.de> - 3.9.2-11
- Rename shared libs to allow parallel installation for libkni
- Merge all shared lib related patches to one sofixes patch

* Sat Jun 13 2009 Tim Niemueller <tim@niemueller.de> - 3.9.2-10
- Update ctor and gcc43 patch for F11

* Tue Jun 09 2009 Tim Niemueller <tim@niemueller.de> - 3.9.2-9
- Rename to libkni3, libkni will be the most up2date version (v4), but this
  version is still required for older Katana 300 arms
- Add patch to fix library building, did work on my machin only because libs
  were installed on the system

* Wed Dec 03 2008 Tim Niemueller <tim@niemueller.de> - 3.9.2-8
- Fix noexit patch

* Mon Dec 01 2008 Tim Niemueller <tim@niemueller.de> - 3.9.2-7
- Make patch 3 apply with fuzz=0
- Added patch that removes calls to exit() but throws exceptions

* Sun Nov 09 2008 Tim Niemueller <tim@niemueller.de> - 3.9.2-6
- Updated license tag
- Consistent (non-)macro usage

* Tue Jul 15 2008 Tim Niemueller <tim@niemueller.de> - 3.9.2-5
- Added ctor patch which adds an optional argument to the ctor to allow for
  accessing an arbitrary device, for example a usb2ser converter
  (RoboCup 2008)

* Mon Jun 23 2008 Tim Niemueller <tim@niemueller.de> - 3.9.2-4
- More .so fixes, link libs against base lib to get rid of
  undefined-non-weak-symbol rpmlint warnings

* Mon Jun 16 2008 Tim Niemueller <tim@niemueller.de> - 3.9.2-3
- Fixed summary

* Thu Jun 12 2008 Tim Niemueller <tim@niemueller.de> - 3.9.2-2
- Upgraded BR to support building on Fedora version < 9

* Sat Jun 07 2008 Tim Niemueller <tim@niemueller.de> - 3.9.2-1
- Initial package

