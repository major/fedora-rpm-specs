%global with_check 1

Name:           gecode
Version:        6.2.0
Release:        18%{?dist}
Summary:        Generic constraint development environment

License:        MIT
URL:            http://www.gecode.org/
Source0:        https://github.com/Gecode/%{name}/archive/release-%{version}.tar.gz
Patch0:         gecode-4.0.0-no_examples.patch
Patch1:         gecode-6.2.0-unbundle_boost.patch
Patch2:         gecode-6.2.0-autoconf_builtin.patch
Patch3:         gecode-6.2.0-builtin_unreachable.patch
Patch4:         gecode-6.2.0-fix_warnings.patch
Patch5:         gecode-6.2.0-const_removal.patch

BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  flex >= 2.5.33
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  qt5-qtbase-devel

# for documentation
BuildRequires:  doxygen tex(latex) tex(dvips)

%description
Gecode is a toolkit for developing constraint-based systems and
applications. Gecode provides a constraint solver with state-of-the-art
performance while being modular and extensible.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package examples
Summary:        Example code for %{name}
BuildArch: noarch

%description examples
The %{name}-examples package contains example code for %{name}.

%prep
%setup -n %{name}-release-%{version}
%patch -P0 -p1 -b .no_examples
%patch -P1 -p1 -b .unbundle_boost
%patch -P2 -p1 -b .autoconf_builtin
%patch -P3 -p1 -b .builtin_unreachable
%patch -P4 -p1 -b .fix_warnings
%patch -P5 -p1 -b .const_removal

# Fix permissions
find -O3 . \( -name '*.hh' -o -name '*.hpp' -o -name '*.cpp' -o \
    -name CMakeLists.txt \) -perm /0111 -exec chmod 0644 '{}' \+
chmod 0644 LICENSE misc/doxygen/*.png

# Fix encoding
pushd examples
for file in bin-packing.cpp black-hole.cpp dominating-queens.cpp scowl.hpp word-square.cpp; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
popd

# Remove default flags
sed -e 's|-ggdb||g' -i configure gecode.m4
sed -e 's|-O3||g' -i configure gecode.m4
sed -i 's|qt4|qt5|g' gecode.m4

%build
autoreconf -ivf

export DLLFLAGS="%{__global_ldflags}"
%configure \
 --disable-examples \
 --enable-float-vars \
 --enable-cbs

%make_build
make doc
make ChangeLog

iconv --from=ISO-8859-1 --to=UTF-8 -o ChangeLog.new ChangeLog
touch -r ChangeLog ChangeLog.new
mv ChangeLog.new ChangeLog

%install
%make_install
# Clean up third-party installed boost
rm -r $RPM_BUILD_ROOT%{_includedir}/%{name}/third-party

%ldconfig_scriptlets

%if 0%{?with_check}
%check
make test
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:%{_libdir}
make check
%endif

%files
%{!?_licensedir:%global license %doc}
%doc ChangeLog
%license LICENSE
%{_libdir}/lib%{name}driver.so.*
%{_libdir}/lib%{name}flatzinc.so.*
%{_libdir}/lib%{name}float.so.*
%{_libdir}/lib%{name}gist.so.*
%{_libdir}/lib%{name}int.so.*
%{_libdir}/lib%{name}kernel.so.*
%{_libdir}/lib%{name}minimodel.so.*
%{_libdir}/lib%{name}search.so.*
%{_libdir}/lib%{name}set.so.*
%{_libdir}/lib%{name}support.so.*

%files devel
%{_bindir}/fzn-gecode
%{_bindir}/mzn-gecode
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/lib%{name}driver.so
%{_libdir}/lib%{name}flatzinc.so
%{_libdir}/lib%{name}float.so
%{_libdir}/lib%{name}gist.so
%{_libdir}/lib%{name}int.so
%{_libdir}/lib%{name}kernel.so
%{_libdir}/lib%{name}minimodel.so
%{_libdir}/lib%{name}search.so
%{_libdir}/lib%{name}set.so
%{_libdir}/lib%{name}support.so

%files doc
%{!?_licensedir:%global license %doc}
%doc doc/html ChangeLog
%license LICENSE

%files examples
%{!?_licensedir:%global license %doc}
%doc examples/*
%license LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb  6 2024 Jerry James <loganjerry@gmail.com> - 6.2.0-16
- Add const removal patch to fix FTBFS (rhbz#2261125)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Julian C. Dunn <jdunn@aquezada.com> - 6.2.0-13
- Removed deprecated %patchN syntax
- Significantly cut down compiler deprecation warnings (gecode-6.2.0-fix_warnings.patch)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 10 2021 Fabio Valentini <decathorpe@gmail.com> - 6.2.0-7
- Rebuild to account for koji snafu at the f34 branch point.

* Mon Feb 08 2021 Jerry James <loganjerry@gmail.com> - 6.2.0-6
- Completely unbundle boost (gecode-6.2.0-unbundle_boost.patch)
- Remove RHEL 6 support
- Fix detection of gcc builtins (gecode-6.2.0-autoconf_builtin.patch)
- Improve compiler diagnostics (gecode-6.2.0-builtin_unreachable.patch)
- Build with gmp and mpfr support
- Build without leak debugging support
- Build with CBS enabled
- Minor spec file cleanups

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Julian C. Dunn <jdunn@aquezada.com> - 6.2.0-4
- Remove bundled boost in devel package (bz#1894891)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Merlin Mathesius <mmathesi@redhat.com> - 6.2.0-2
- Minor conditional fixes for ELN

* Sun May 03 2020 Vasiliy Glazov <vascom2@gmail.com> - 6.2.0-2
- Switch to Qt5

* Sun Apr 26 2020 Julian C. Dunn <jdunn@aquezada.com> - 6.2.0-1
- Upgrade to gecode 6.2.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Julian C. Dunn <jdunn@aquezada.com> - 5.1.0-3
- Ensure that we have BR against gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Julian C. Dunn <jdunn@aquezada.com> - 5.1.0-1
- Upgrade to gecode 5.1.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 5.0.0-2
- Rebuilt for Boost 1.64

* Wed Mar 15 2017 Julian Dunn <jdunn@aquezada.com> - 5.0.0-1
- Upgrade to gecode 5.0.0
- Drop bz#1334212 patch; fixed upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 4.4.0-13
- Rebuilt for Boost 1.63

* Mon May 30 2016 Julian Dunn <jdunn@aquezada.com> - 4.4.0-12
- Do not apply the bz#1334212 patch unless on GCC >= 6.x

* Sun May 29 2016 Julian Dunn <jdunn@aquezada.com> - 4.4.0-11
- Rebuilt for EPEL6
- Download targz source archive
- Using cmake to configure
- Set compiler flags
- Tests performed
- Built against Boost-1.48 on EPEL

* Wed May 25 2016 Than Ngo <than@redhat.com> - 4.4.0-10
- fix typo

* Tue May 17 2016 Than Ngo <than@redhat.com> - 4.4.0-9
- add better fix for bz#1334212

* Fri May 13 2016 Than Ngo <than@redhat.com> - 4.4.0-8
- fix bz#1334212, narrowing conversion
- cleanup

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 4.4.0-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 4.4.0-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.4.0-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.3.3-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 4.3.3-2
- Rebuild for boost 1.57.0

* Fri Jan 23 2015 Julian C. Dunn <jdunn@aquezada.com> - 4.3.3-1
- Update to 4.3.3

* Mon Sep 29 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.3.0-1
- Update to 4.3.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 4.2.1-2
- Rebuild for boost 1.55.0

* Sat Nov 16 2013 Julian C. Dunn <jdunn@aquezada.com> 4.2.1-1
- Update to 4.2.1

* Fri Aug 23 2013 Julian C. Dunn <jdunn@aquezada.com> 4.2.0-1
- Update to 4.2.0
- Switch to unversioned docdir for >= F20 (bz#993768)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 4.0.0-2
- Rebuild for boost 1.54.0

* Sat Jun 15 2013 Julian C. Dunn <jdunn@aquezada.com> 4.0.0-1
- Update to 4.0.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Julian C. Dunn <jdunn@aquezada.com> 3.7.3-3
- Fix build on EPEL6

* Tue Aug 21 2012 Julian C. Dunn <jdunn@aquezada.com> 3.7.3-2
- Post-review comments in bz#843695

* Sun May 20 2012 Julian C. Dunn <jdunn@aquezada.com> 3.7.3-1
- Update for 3.7.3
- Drop support for EPEL5. flex is too old

* Fri Apr 01 2011 Erik Sabowski and James Sulinski <team@aegisco.com> 3.5.0-1
- Update for gecode-3.5.0
- Disabled "gist" and "qt" configure options

* Sat May  8 2010 ELMORABITY Mohamed <melmorabity@fedoraproject.org> 3.3.1-1
- Initial RPM release
