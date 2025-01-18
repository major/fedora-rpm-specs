Name:	 frobby
Summary: Computations With Monomial Ideals
Version: 0.9.5
Release: 7%{?dist}

# GPL-2.0-or-later: the frobby code
# OFL-1.1-RFN: AMS fonts embedded in the PDF manual
# Knuth-CTAN: Computer Modern fonts embedded in the PDF manual
License: GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN
URL:	 https://github.com/Macaulay2/frobby
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# make makefile a wee bit more sane
Patch0:  frobby-0.9.0-makefile.patch

BuildRequires: gcc-c++
BuildRequires: gmp-devel
BuildRequires: make
# docs
BuildRequires: doxygen-latex

Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
Frobby is a software system and project for computations with monomial
ideals. Frobby is free software and it is intended as a vehicle for
research on monomial ideals, as well as a useful practical tool for
investigating monomial ideals.

The current functionality includes Hilbert series, maximal standard
monomials, combinatorial optimization on monomial ideals, primary
decomposition, irreducible decomposition, Alexander dual, associated
primes, minimization and intersection of monomial ideals as well as
the computation of Frobenius problems (using 4ti2) with very large
numbers. Frobby is also able to translate between formats that can be used
with several different computer systems, such as Macaulay 2, Monos, 4ti2,
CoCoA4 and Singular. Thus Frobby can be used with any of those systems.


%package -n libfrobby
License:        GPL-2.0-or-later
Summary:        Frobby internals as a library

%description -n libfrobby
This package contains the frobby internals as a library, often called
libfrobby.


%package -n libfrobby-devel
License:        GPL-2.0-or-later
Summary:        Developer files for libfrobby
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description -n libfrobby-devel
Header files and library links to develop applications that use the
Frobby internals as a library (libfrobby).


%prep
%autosetup


%build
%make_build \
  BIN_INSTALL_DIR=%{_bindir} \
  CFLAGS="${CFLAGS:-%build_cflags}" \
  CXXFLAGS="${CXXFLAGS:-%build_cxxflags}" \
  GMP_INC_DIR=%{_includedir} \
  LDFLAGS="${LDFLAGS:-%build_ldflags}" \
  MODE=shared \
  library all

# Relink the binary against the library
rm bin/frobby
mv bin/libfrobby.so bin/libfrobby.so.0.0.0
ln -s libfrobby.so.0.0.0 bin/libfrobby.so.0
ln -s libfrobby.so.0 bin/libfrobby.so
g++ bin/shared/main.o ${CFLAGS:-%build_cflags} ${LDFLAGS:-%build_ldflags} \
  -L$PWD/bin -lfrobby -o bin/frobby

# generate docs
make docPdf


%install
# Install the binary
mkdir -p %{buildroot}/%{_bindir}
cp -p bin/frobby %{buildroot}%{_bindir}

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p bin/libfrobby.so.0.0.0 %{buildroot}%{_libdir}
ln -s libfrobby.so.0.0.0 %{buildroot}%{_libdir}/libfrobby.so.0
ln -s libfrobby.so.0 %{buildroot}%{_libdir}/libfrobby.so

# Install the header files
mkdir -p %{buildroot}%{_includedir}/frobby
cp -p src/{frobby,stdinc}.h %{buildroot}%{_includedir}/frobby


%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
test/runTests


%files
%doc bin/manual.pdf
%{_bindir}/frobby

%files -n libfrobby
%doc COPYING
%{_libdir}/*.so.0*

%files -n libfrobby-devel
%{_includedir}/frobby/
%{_libdir}/*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Jerry James <loganjerry@gmail.com> - 0.9.5-1
- Version 0.9.5
- New URLs
- Drop upstreamed Macaulay2 patch
- Convert License tag to SPDX
- Minor spec file cleanups

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 0.9.0-20
- Update the Macaulay2 patch
- Reverse the order of the patches so we can use an unmodified Macaulay2 patch
- Fix underlinking so that -Wl,--as-needed can be used

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.9.0-18
- workaround FTBFS, disable -Wl,--as-needed (#1674902)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.9.0-15
- use %%make_build %%ldconfig_scriptlets

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.9.0-14
- BR: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 0.9.0-10
- Also ship the stdinc.h header file

* Fri Feb 24 2017 Jerry James <loganjerry@gmail.com> - 0.9.0-9
- Add libfrobby and libfrobby-devel subpackages

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 07 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-3
- fix W: spurious-executable-perm /usr/share/doc/frobby/COPYING

* Mon Jun 23 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-2
- explicitly set CFLAGS, LDFLAGS

* Mon Jun 23 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-1
- frobby-0.9.0

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.2-1
- first try

