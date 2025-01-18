Name:           coin-or-lemon
Version:        1.3.1
Release:        36%{?dist}
Summary:        A C++ template library providing many common graph algorithms

License:        BSL-1.0 AND BSD-3-Clause
URL:            http://lemon.cs.elte.hu/trac/lemon
VCS:            hg:http://lemon.cs.elte.hu/hg/lemon
Source:         http://lemon.cs.elte.hu/pub/sources/lemon-%{version}.tar.gz

# https://lemon.cs.elte.hu/trac/lemon/ticket/502
Patch:          lemon-%{version}-cmake-policy.patch

# https://lemon.cs.elte.hu/trac/lemon/ticket/503
Patch:          lemon-%{version}-buildfix.patch

# Work around FTBFS due to this gcc error: non-type template parameters of
# class type only available with '-std=c++2a' or '-std=gnu++2a'.
Patch:          lemon-%{version}-template.patch

# Fix a test failure due to using references to temporary objects that go
# out of scope.
Patch:          lemon-%{version}-test.patch

# Adapt to recent versions of SoPlex
Patch:          lemon-%{version}-soplex.patch

# Fix warnings that the register storage class is not permitted in C++17
Patch:          lemon-%{version}-register.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  coin-or-Cbc-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  help2man
BuildRequires:  libsoplex-devel
BuildRequires:  make
BuildRequires:  zlib-devel

%description
LEMON stands for Library for Efficient Modeling and Optimization in
Networks. It is a C++ template library providing efficient
implementations of common data structures and algorithms with focus on
combinatorial optimization tasks connected mainly with graphs and
networks.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:        Command-line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools package contains a handful of command-line tools that
come with %{name}.


%package        doc
Summary:        Documentation for for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains a %{name}'s API documentation.


%prep
%autosetup -n lemon-%{version} -p1


%conf
# Fix the library directory name on 64-bit systems
if [ "%{_lib}" = "lib64" ]; then
    sed -i 's,/lib,/lib64,' cmake/FindCOIN.cmake cmake/FindGLPK.cmake \
        cmake/LEMONConfig.cmake.in lemon/lemon.pc.in
    sed -i 's,DESTINATION lib,&64,' lemon/CMakeLists.txt
fi

# We ship a shared library, not a static library
sed -i 's/libemon\.a/libemon.so/' cmake/LEMONConfig.cmake.in


%build
export CXXFLAGS='%{build_cxxflags} -I%{_includedir}/soplex'

# CPLEX (aka ILOG) is non-free, so don't try to detect it.
#
# We suppress detection of ghostscript, doxygen, and python to make
# the build behave the same way with and without them installed -- we
# don't actually need them, since we don't need to rebuild the docs.
%cmake \
  -DDOXYGEN_EXECUTABLE= \
  -DGHOSTSCRIPT_EXECUTABLE= \
  -DPYTHON_EXECUTABLE= \
  -DLEMON_ENABLE_COIN:BOOL=YES \
  -DLEMON_ENABLE_GLPK:BOOL=YES \
  -DLEMON_ENABLE_ILOG:BOOL=NO \
  -DLEMON_ENABLE_SOPLEX:BOOL=YES

%cmake_build


%install
%cmake_install

# Fix up the symlinks the way ldconfig wants them
%global majver %(cut -d. -f1 <<< %{version})
cd %{buildroot}%{_libdir}
rm libemon.so
ln -s libemon.so.%{version} libemon.so.%{majver}
ln -s libemon.so.%{majver} libemon.so
cd -

# Put the cmake file where Fedora cmake expects to find it
mv %{buildroot}%{_datadir}/lemon %{buildroot}%{_libdir}/cmake
mv %{buildroot}%{_libdir}/cmake/cmake %{buildroot}%{_libdir}/cmake/lemon

# Make man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
for fil in dimacs-solver dimacs-to-lgf lgf-gen; do
  help2man -N --no-discard-stderr --version-string=%{version} \
    %{buildroot}%{_bindir}/$fil > %{buildroot}%{_mandir}/man1/$fil.1
done

# Install the documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS NEWS README doc/html %{buildroot}%{_docdir}/%{name}


%check
%cmake_build --target check


%files
%license LICENSE
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README
%{_libdir}/libemon.so.1
%{_libdir}/libemon.so.1.*

%files devel
%{_includedir}/lemon/
%{_libdir}/libemon.so
%{_libdir}/cmake/lemon
%{_libdir}/pkgconfig/lemon.pc

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%{_docdir}/%{name}/html


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Jerry James <loganjerry@gmail.com> - 1.3.1-35
- Fix the build with soplex 7.1.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Jerry James <loganjerry@gmail.com> - 1.3.1-33
- Rebuild for soplex 7.1.0

* Wed Jun 19 2024 Jerry James <loganjerry@gmail.com> - 1.3.1-32
- Rebuild for soplex 7.0.1

* Thu Mar  7 2024 Jerry James <loganjerry@gmail.com> - 1.3.1-31
- Rebuild for soplex 7.0.0

* Wed Jan 31 2024 Jerry James <loganjerry@gmail.com> - 1.3.1-30
- Build with SoPlex support
- Convert License tag to SPDX
- Stop building for 32-bit x86

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.3.1-18
- Make cmake file refer to shared instead of static library (bz 1526647)
- Install cmake file in the right place
- Add -template patch to fix FTBFS (bz 1674751)
- Add -test patch to fix a test failure
- Eliminate unnecessary BRs and Rs
- Eliminate rpath from the library
- Be explicit about library versions as required by latest guidelines
- Add -doc subpackage to hold doxygen output
- Use help2man to generate man pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.3.1-15
- Rebuild for glpk 4.65
- Fix pkgconfig and cmake files on 64-bit systems (bz 1526647)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 1.3.1-10
- Rebuild for glpk 4.61

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 luto@kernel.org - 1.3.1-8
- Rebuild for libglpk.so.40

* Fri Feb 19 2016 luto@kernel.org - 1.3.1-7
- Rebuild for updated glpk

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Andy Lutomirski <luto@mit.edu> - 1.3.1-2
- Switch to the upstream fix for bug 503.

* Tue Jul 08 2014 Andy Lutomirski <luto@mit.edu> - 1.3.1-1
- New minor release.
- Drop now-unnecessary patches (thanks, LEMON upstream!).

* Mon Jun 09 2014 Andy Lutomirski <luto@mit.edu> - 1.3-6
- Fix BR.

* Mon Jun 09 2014 Andy Lutomirski <luto@mit.edu> - 1.3-5
- Enable GLPK, Clp, and Cbc.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Andy Lutomirski <luto@mit.edu> - 1.3-3
- Use _pkgdocdir consistently (f19 fix)

* Wed Jun 04 2014 Andy Lutomirski <luto@mit.edu> - 1.3-2
- Add a downstream soname for libemon.so.
- Fix conflicts with the package called 'lemon'.
- Fix directory ownership.
- Fix license.
- Fix doc timestamps.

* Wed Feb  5 2014 Andy Lutomirski <luto@mit.edu> - 1.3-1
- Initial version.
