Name:           astyle
Version:        3.6.6
Release:        2%{?dist}
Summary:        Source code formatter for C-like programming languages

%global soversion       %{version}

License:        MIT
URL:            https://astyle.sourceforge.net/
Source0:        https://gitlab.com/saalen/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++

# Fix (hardcoded) path to html-help
Patch1:         astyle-html-help.patch

%description
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.

%package devel
Summary:        Source code formatter for C-like programming languages
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.

This package contains the shared library.


%prep
%autosetup -p1

# drop executable bit from all files
find . -type f -exec chmod a-x {} \;


%build
pushd AStyle/src
    # it's much easier to compile it here than trying to fix the Makefile
    g++ %{build_cxxflags} -DASTYLE_LIB -fPIC -c ASBeautifier.cpp ASEnhancer.cpp ASFormatter.cpp ASResource.cpp astyle_main.cpp
    g++ %{build_ldflags} -shared -o libastyle.so.%{soversion} *.o -Wl,-soname,libastyle.so.%{soversion}
    ln -s libastyle.so.%{soversion} libastyle.so
    g++ %{build_cxxflags} -c ASLocalizer.cpp astyle_main.cpp
    g++ %{build_ldflags} -o astyle ASLocalizer.o astyle_main.o -L. -lastyle
popd


%install
pushd AStyle/src
    mkdir -p %{buildroot}{%{_bindir},%{_libdir},%{_includedir}}

    install -p -m 755 astyle %{buildroot}%{_bindir}
    install -p -m 755 libastyle.so.%{soversion} %{buildroot}%{_libdir}
    cp -P libastyle.so %{buildroot}%{_libdir}
    install -p -m 644 astyle.h %{buildroot}%{_includedir}
popd


%files
%license AStyle/LICENSE.md
%doc AStyle/doc/*.html
%{_bindir}/astyle
%{_libdir}/libastyle.so.%{soversion}

%files devel
%{_libdir}/libastyle.so
%{_includedir}/astyle.h


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.6.6-1
- Update to 3.6.6 (rhbz#2323142)

* Mon Sep 30 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.6.3-1
- Update to 3.6.3 (rhbz#2311785)

* Thu Sep 05 2024 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1 (rhbz#2303916)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Dan Horák <dan[at]danny.cz> - 3.5.2-1
- updated to 3.5.2 (rhbz#2276712)

* Thu Mar 21 2024 Dan Horák <dan[at]danny.cz> - 3.4.13-1
- updated to 3.4.13 (rhbz#2264433)

* Thu Feb 15 2024 Dan Horák <dan[at]danny.cz> - 3.4.12-1
- updated to 3.4.12 (rhbz#2264433)

* Thu Feb 15 2024 Dan Horák <dan[at]danny.cz> - 3.1-22
- explicitly add library %%{majorversion} symlink

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Dan Horák <dan[at]danny.cz> -  3.1-16
- rebuild without JNI support (#2104020)
- use distro-wide build flags

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.1-15
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.1-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1-5
- Fix abort with gcc8 -Wp,-D_GLIBCXX_ASSERTION (bug 1573092)

* Mon Feb 19 2018 Jens Lody <fedora@jenslody.de> - 3.1-4
- Add BuildRequires for gcc-c++.

* Tue Feb 13 2018 Jens Lody <fedora@jenslody.de> - 3.1-3
- Build fix
- Consistently use macros instead of variables in spec-file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Jens Lody <fedora@jenslody.de> - 3.1-1
- Update to 3.1 (#1533678)
- Fix project url (no https !)

* Sun Sep 24 2017 Jens Lody <fedora@jenslody.de> - 3.0.1-4
- Fix #1493473 (astyle --html does not find documentation).

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Jens Lody <fedora@jenslody.de> - 3.0.1-1
- Update to 3.0.1

* Sat Apr 29 2017 Jens Lody <fedora@jenslody.de> - 3.0-2
- Make the astyle-lib usable for arduino.

* Mon Apr 10 2017 Jens Lody <fedora@jenslody.de> - 3.0-1
- Update to 3.0

* Sun Feb 12 2017 Jens Lody <fedora@jenslody.de> - 2.06-1
- update to 2.06 (#1411164)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.05.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.05.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.05.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Dec 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.05.1-1
- update to 2.05.1 (#1175136), but stay at same soversion for library

* Thu Nov 20 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.05-1
- update to 2.05 (#1166336)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Dan Horák <dan[at]danny.cz> - 2.04-3
- compile directly in %%build so the astyle binary links against our library
- include public header file in devel subpackage
- use full version info in soname as there is no API/ABI compatibility guaranteed

* Fri Jan 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.04-2
- build shared library without SONAME (opened bug upstream to provide a SONAME in the next release, #1054422)
- remove defattr
- remove clean section

* Tue Nov  5 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.04-1
- update to new version (fixes #1025982, #996008)

* Tue Jul 30 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.03-1
- update to new version (fixes #990162)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.02.1-1
- update to new version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.01-1
- update to new version

* Sat Jan 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.24-1
- update to new version
- change license to LGPLv3+ (changed since 1.23, but missed there)

* Tue Oct 13 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.23-1
- Update to new version
- patch from Sep 24 2008 not needed anymore for gcc-4.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.21-9
- Fixed build failure with gcc-4.3. Closes Red Hat Bugzilla bug #433971.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.21-8
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.21-7
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.21-6
- Rebuild for selinux ppc32 issue.

* Mon Jul 2 2007 Adam M. Dutko <gnome at dux-linux org> 1.21-5
- Fixed sourceforge Source0 link.
- Updated to 1.21.

* Tue Jun 19 2007 Adam M. Dutko <gnome at dux-linux org> 1.20.2-4
- Removed macros from changelog
- Formatted changelog from 1.20.2-2

* Tue Jun 19 2007 Adam M. Dutko <gnome at dux-linux org> 1.20.2-3
- Changed licensing to LGPL from GPL
- Removed execute bit from src/*
- Used bindir/install instead of /usr/bin/install

* Thu Jun 14 2007 Mary Ellen Foster <mefoster gmail com> 1.20.2-2
- Modifications from Ralf Corsepius (thanks!):
- Eliminated use of build/Makefile; just compile and install directly
- Use bindir rather than /usr/bin

* Sat May 12 2007 Adam Monsen <haircut@gmail.com> 1.20.2-1
- removed Makefile patch

* Thu Sep 21 2006 Mary Ellen Foster <mefoster gmail com> 1.19-1
- Initial package
