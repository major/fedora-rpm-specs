Name:           check
Version:        0.15.2
Release:        7%{?dist}
Summary:        A unit test framework for C
Source0:        https://github.com/libcheck/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License:        LGPLv2+
URL:            https://libcheck.github.io/check/
# Only needed for autotools in Fedora
Patch0:         %{name}-0.11.0-info-in-builddir.patch
# Fix test failures due to varying floating point behavior across platforms
Patch1:         %{name}-0.11.0-fp.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  patchutils
BuildRequires:  pkgconfig
%if ! 0%{?rhel}
BuildRequires:  pkgconfig(libsubunit)
%endif
BuildRequires:  texinfo, texlive-tex, graphviz

%description
Check is a unit test framework for C. It features a simple interface for 
defining unit tests, putting little in the way of the developer. Tests 
are run in a separate address space, so Check can catch both assertion 
failures and code errors that cause segmentation faults or other signals. 
The output from unit tests can be used within source code editors and IDEs.

%package devel
Summary:        Libraries and headers for developing programs with check
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and headers for developing programs with check

%package static
Summary:        Static libraries of check

%description static
Static libraries of check.

%package checkmk
Summary:        Translate concise versions of test suites into C programs
License:        BSD
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description checkmk
The checkmk binary translates concise versions of test suites into C
programs suitable for use with the Check unit test framework.

%prep
%setup -q
%if 0%{?fedora}
%patch0 -p1 -b .info-in-builddir
%endif
%patch1 -p1

# Fix detection of various time-related function declarations
sed -e '/DECLS(\[a/s|)|,,,[AC_INCLUDES_DEFAULT\n[#include <time.h>\n #include <sys/time.h>]]&|' \
    -i configure.ac

# Get rid of version control files
find . -name .cvsignore -delete

# Regenerate configure due to patch 0
autoreconf -ivf

# Fix libdir for the cmake build
sed -i 's,set(libdir .*),set(libdir "%{_libdir}"),' CMakeLists.txt

%build
# The autotools build does not create the cmake files.
# The cmake build does not create the info or aclocal files.
# Therefore we build with both and combine the results to get everything.
mkdir autotools_build
cd autotools_build
%global _configure ../configure
%configure --disable-timeout-tests

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build
cd -

%cmake -DCHECK_ENABLE_TIMEOUT_TESTS:BOOL=OFF
%cmake_build

%install
cd autotools_build
%make_install
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_docdir}/%{name}
cd -

%cmake_install

# The library does not really depend on -pthread
sed -i 's/ -pthread//' %{buildroot}%{_libdir}/pkgconfig/check.pc

%check
cd autotools_build
export LD_LIBRARY_PATH=$PWD/src/.libs
%ifnarch s390x
make check
%endif
# Don't need to package the sh, log or trs files
# when we scoop the other checkmk/test files for doc
rm -rf checkmk/test/check_checkmk*
# these files are empty
rm -rf checkmk/test/empty_input
cd -

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS
%license COPYING.LESSER
%{_libdir}/libcheck.so.0*
%{_infodir}/check*

%files devel
%doc doc/example
%{_includedir}/check.h
%{_includedir}/check_stdint.h
%{_libdir}/cmake/check/
%{_libdir}/libcheck.so
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4

#check used to be static only, hence this.
%files static
%license COPYING.LESSER
%{_libdir}/libcheck.a

%files checkmk
%doc checkmk/README checkmk/examples
%doc checkmk/test
%{_bindir}/checkmk
%{_mandir}/man1/checkmk.1*

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 16 2021 Jerry James <loganjerry@gmail.com> - 0.15.2-5
- Fix pkgconfig file on 64-bit systems (bz 2014748)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Tomas Popela <tpopela@redhat.com> - 0.15.2-3
- Don't build with subunit support in RHEL

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug  9 2020 Jerry James <loganjerry@gmail.com> - 0.15.2-1
- Version 0.15.2
- Drop upstreamed -fail-macros patch

* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 0.15.1-3
- Add -fail-macros patch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jerry James <loganjerry@gmail.com> - 0.15.1-1
- Version 0.15.1
- Drop upstreamed -format-spec patch

* Tue Jun 23 2020 Jerry James <loganjerry@gmail.com> - 0.15.0-2
- Drop -attribute-format patch, causes other issues (bz 1850198)

* Mon Jun 22 2020 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0
- Add -formatspec and -attribute-format patches
- Build with both cmake and autotools

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 0.14.0-3
- disable tests on s390x

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Tom Callaway <spot@fedoraproject.org> - 0.14.0-1
- update to 0.14.0

* Mon Dec  2 2019 Tom Callaway <spot@fedoraproject.org> - 0.13.0-2
- package NEWS instead of the obsolete ChangeLog file

* Tue Oct 22 2019 Tom Callaway <spot@fedoraproject.org> - 0.13.0-1
- update to 0.13.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Jerry James <loganjerry@gmail.com> - 0.12.0-3
- Disable unreliable timeout tests (sometimes fail on busy builders)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Jerry James <loganjerry@gmail.com> - 0.12.0-1
- Update to 0.12.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Tom Callaway <spot@fedoraproject.org> - 0.11.0-1
- update to 0.11.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 0.10.0-2
- rebuild for ICU 56.1

* Fri Aug  7 2015 Jerry James <loganjerry@gmail.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Jerry James <loganjerry@gmail.com> - 0.9.14-1
- New upstream version
- Drop -volatile patch, no longer needed
- Update time-related configure fix again

* Mon Jun  9 2014 Jerry James <loganjerry@gmail.com> - 0.9.13-2
- Add -volatile patch to fix test failure
- Update time-related configure fix

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Tom Callaway <spot@fedoraproject.org> - 0.9.13-1
- update to 0.9.13

* Fri Apr 25 2014 Jerry James <loganjerry@gmail.com> - 0.9.12-2
- Build with subunit support
- Remove unused aarch64 patch

* Tue Jan 21 2014 Tom Callaway <spot@fedoraproject.org> - 0.9.12-1
- update to 0.9.12

* Tue Nov  5 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.11-1
- update to 0.9.11
- use autoreconf -ivf instead of the patch

* Mon Aug  5 2013 Jerry James <loganjerry@gmail.com> - 0.9.10-3
- Drop -format patch, upstreamed
- Fix detection of more time-related functions
- Give checkmk its own subpackage for licensing reasons
- Add a check script

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 18 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.10-1
- update to 0.9.10

* Mon Mar 25 2013 Jerry James <loganjerry@gmail.com> - 0.9.9-3
- Enable aarch64 support (bz 925218)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Jerry James <loganjerry@gmail.com> - 0.9.9-1
- New upstream version
- Drop upstream patch for 0.9.8; fix now merged

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Jerry James <loganjerry@gmail.com> - 0.9.8-5
- Add upstream patch for bz 821933

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.9.8-4
- Rebuild for GCC 4.7
- Minor spec file cleanups.

* Mon Feb 14 2011 Jerry James <loganjerry@gmail.com> - 0.9.8-3
- Rebuild for new gcc (Fedora 15 mass rebuild)

* Mon Nov 29 2010 Jerry James <loganjerry@gmail.com> - 0.9.8-2
- Add license file to -static package.
- Remove BuildRoot tag.

* Mon Sep 28 2009 Jerry James <loganjerry@gmail.com> - 0.9.8-1
- Update to 0.9.8

* Thu Aug  6 2009 Jerry James <loganjerry@gmail.com> - 0.9.6-5
- Support --excludedocs (bz 515933)
- Replace broken upstream info dir entry

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr  7 2009 Jerry James <loganjerry@gmail.com> - 0.9.6-3
- Add check-0.9.6-strdup.patch

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.6-1
- update to 0.9.6

* Mon Dec  1 2008 Jerry James <loganjerry@gmail.com> - 0.9.5-3
- Fix unowned directory (bz 473635)
- Drop unnecessary BuildRequires
- Replace patches with addition of -fPIC to CFLAGS in the spec file
- Add some more documentation files

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.5-2.1
- Autorebuild for GCC 4.3

* Thu Aug  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.5-1
- 0.9.5 bump

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 0.9.3-5
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9.3-4.fc5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9.3-4.fc5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 19 2005 Warren Togami <wtogami@redhat.com> 0.9.2-4
- import into FC5 for gstreamer-0.10

* Fri Dec  2 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.2-3
- enabled -fPIC to resolve bz 174313

* Sat Sep 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.2-2
- get rid of the so file (not needed)
- only make devel package

* Sun Aug 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.2-1
- initial package for Fedora Extras
