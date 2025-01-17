# Upstream doesn't make releases.  We have to check the code out of git.
%global gittag   c3acaf62b137c36aae5eb380f1d883bfa9095f60
%global shorttag %(cut -b -7 <<< %{gittag})
%global gitdate  20190517

Name:           symfpu
Version:        0
Release:        0.17.%{gitdate}git%{shorttag}%{?dist}
Summary:        An implementation of IEEE-754 / SMT-LIB floating-point 

License:        GPL-3.0-or-later
URL:            https://github.com/cvc5/symfpu
VCS:            git:%{url}.git
Source:         %{url}/archive/%{gittag}/%{name}-%{shorttag}.tar.gz
# Fedora-only patch: build a shared library instead of a static library
Patch:          %{name}-shared.patch
# Fix an infinite recursion
# See https://github.com/martin-cs/symfpu/issues/3
Patch:          %{name}-infinite-recursion.patch
# Upstream PR to fix invalid creation of a zero-size bitvector
Patch:          %{url}/pull/9.patch
# CVC5 patch for symfpu (apparently authored by the symfpu maintainer)
Patch:          %{name}-cvc5.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make

%description
SymFPU is an implementation of the SMT-LIB / IEEE-754 operations in
terms of bit-vector operations.  It is templated in terms of the
bit-vectors, propositions, floating-point formats and rounding mode
types used.  This allow the same code to be executed as an arbitrary
precision "SoftFloat" library (although it's performance would not be
good) or to be used to build symbolic representation of floating-point
operations suitable for use in "bit-blasting" SMT solvers (you could
also generate circuits from them but again, performance will likely not
be good).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files and library links for developing
applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{gittag}

%conf
# Use Fedora build flags
sed -e 's/ -Wall -W//' \
    -e 's/ -msse2 -mfpmath=sse//' \
    -e 's|-mfma -mno-fma4|-I. %{build_cxxflags} -fno-strict-aliasing %{build_ldflags}|' \
    -i flags

# Fix header file include paths
ln -s .. applications/symfpu
ln -s .. baseTypes/symfpu
ln -s .. core/symfpu
ln -s .. utils/symfpu

%build
# Cannot use smp_mflags due to missing subdir dependencies
make

%install
# There is no install target.  Install by hand.
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p libsymfpu.so.0.0.0 %{buildroot}%{_libdir}
ln -s libsymfpu.so.0.0.0 %{buildroot}%{_libdir}/libsymfpu.so.0
ln -s libsymfpu.so.0 %{buildroot}%{_libdir}/libsymfpu.so

# Install the header files
mkdir -p %{buildroot}%{_includedir}/%{name}/baseTypes
mkdir -p %{buildroot}%{_includedir}/%{name}/core
mkdir -p %{buildroot}%{_includedir}/%{name}/utils
cp -p baseTypes/*.h %{buildroot}%{_includedir}/%{name}/baseTypes
cp -p core/*.h %{buildroot}%{_includedir}/%{name}/core
cp -p utils/*.h %{buildroot}%{_includedir}/%{name}/utils

%check
export LD_LIBRARY_PATH=$PWD
# The test return values are backwards: 0 is an error, 1 is test success
! ./test --allTests

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
* Wed Jan 15 2025 Jerry James <loganjerry@gmail.com> - 0-0.17.20190517gitc3acaf6
- New project URL
- Move configuration steps to %conf

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0-0.15.20190517gitc3acaf6
- Stop building for 32-bit x86

* Fri Jul 28 2023 Jerry James <loganjerry@gmail.com> - 0-0.15.20190517gitc3acaf6
- Add patch needed by CVC5

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 0-0.12.20190517gitc3acaf6
- Add upstream patch to fix creation of zero-size bitvector
- Add patch to avoid infinite recursion
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Jerry James <loganjerry@gmail.com> - 0-0.4.20190517gitc3acaf6
- Update to latest git snapshot to fix a CVC4 bug

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180523git0444c86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20180523git0444c86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul  6 2018 Jerry James <loganjerry@gmail.com> - 0-0.1.20180523git0444c86
- Initial RPM
