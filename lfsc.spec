# NOTE: upstream does not make releases and has no version numbering scheme.
# We check the code out of git and use the date of the last commit as the
# version number.
%global owner    CVC4
%global gittag   15f53d6feb84e4ddb41deaf2b5630f5c1303b06d
%global shorttag %(cut -b -7 <<< %{gittag})

Name:           lfsc
Version:        0.20210305
Release:        4%{?dist}
Summary:        SMT proof checker

License:        BSD
URL:            https://github.com/%{owner}/LFSC
Source0:        https://github.com/%{owner}/LFSC/archive/%{gittag}/%{name}-%{shorttag}.tar.gz
# The next few sources contain commonly used proof definitions
Source1:        http://clc.cs.uiowa.edu/lfsc/euf_interpolation.plf
Source2:        http://clc.cs.uiowa.edu/lfsc/sat.plf
Source3:        http://clc.cs.uiowa.edu/lfsc/smt.plf
Source4:        http://clc.cs.uiowa.edu/lfsc/th_base.plf
Source5:        http://clc.cs.uiowa.edu/lfsc/th_real.plf
Source6:        http://clc.cs.uiowa.edu/lfsc/th_lra.plf
Source7:        http://clc.cs.uiowa.edu/lfsc/th_lra-cvc3.plf
Source8:        http://clc.cs.uiowa.edu/lfsc/color_base.plf
Source9:        http://clc.cs.uiowa.edu/lfsc/color_euf.plf
# Use std::unordered_map instead of the deprecated __gnu_cxx::hash_map
Patch0:         %{name}-map.patch

BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  python3

%description
This package contains an SMT proof checker.

%package devel
Summary:        Files needed to compile side conditions
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the files needed to compile a version of %{name} that
can execute a side condition.

%prep
%autosetup -p0 -n LFSC-%{gittag}

# We want to know about use of deprecated interfaces
sed -i '/Wno-deprecated/d' CMakeLists.txt

# Build a shared library instead of a static library, and give it an soname
sed -e 's/STATIC/SHARED/' \
    -e '/^[[:blank:]]*OUTPUT_NAME lfscc/i\  VERSION 0.0.0\n  SOVERSION 0' \
    -e 's/ARCHIVE DESTINATION/LIBRARY DESTINATION/' \
    -e '/^set_target_properties/iTARGET_LINK_LIBRARIES(liblfscc gmp)' \
    -i src/CMakeLists.txt

# Fix the library install path
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's,/lib,/lib64,' src/CMakeLists.txt
fi

# Fix the test script
sed -i 's,%{_bindir}/env python,%{python3},' tests/run_test.py

%build
%cmake
%cmake_build

%install
%cmake_install

# Install the proof files
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
   %{SOURCE7} %{SOURCE8} %{SOURCE9} %{buildroot}%{_datadir}/%{name}

# Generate a man page
cd %{_vpath_builddir}/src
mkdir -p %{buildroot}%{_mandir}/man1
export LD_LIBRARY_PATH=$PWD
help2man -N --version-string=%{version} ./lfscc > \
  %{buildroot}%{_mandir}/man1/lfscc.1
# Fix line breaks in the man page
sed -i 's/\\fB/.TP\n&/;s/\\fR: /\\fR\n/' %{buildroot}%{_mandir}/man1/lfscc.1

# Help the debuginfo generator
cp -p ../../src/lexer.flex .
cd -

%check
%ctest

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/lfscc
%{_datadir}/%{name}/
%{_libdir}/liblfscc.so.*
%{_mandir}/man1/lfscc.1*

%files devel
%{_includedir}/lfscc.h
%{_libdir}/liblfscc.so

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210305-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210305-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210305-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Jerry James <loganjerry@gmail.com> - 0.20210305-1
- Update to 20210305 git snapshot

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20201110-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Jerry James <loganjerry@gmail.com> - 0.20201110-1
- Update to 20201110 snapshot

* Mon Aug 24 2020 Jerry James <loganjerry@gmail.com> - 0.20200815-1
- Update to 20200815 git snapshot

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20200719-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Jerry James <loganjerry@gmail.com> - 0.20200719-1
- Update to 20200719 git snapshot
- Adapt to cmake changes in Rawhide

* Thu Mar  5 2020 Jerry James <loganjerry@gmail.com> - 0.20200115-1
- Update to latest git snapshot
- Link the library with gmp
- Generate a man page for the binary with help2man

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20190808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep  9 2019 Jerry James <loganjerry@gmail.com> - 0.20190808-1
- Update to latest git snapshot

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20190226-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Jerry James <loganjerry@gmail.com> - 0.20190226-1
- Update to latest git snapshot

* Thu Feb  7 2019 Jerry James <loganjerry@gmail.com> - 0.20190113-1
- Update to latest git snapshot for identifier bug fix
- Add -map patch to fix use of deprecated interface

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20181122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 0.20181122-1
- Update to latest git snapshot for 2 bug fixes
- Use upstream's new test suite

* Wed Nov  7 2018 Jerry James <loganjerry@gmail.com> - 0.20181029-1
- Update to latest git snapshot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20180322-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Jerry James <loganjerry@gmail.com> - 0.20180322-1
- Initial RPM (unretired)
