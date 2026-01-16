# Upstream doesn't make releases.  We have to check the code out of git.
# Use the cvc5 branch.
%global gittag   e6ac3af9c2c574498ea171c957425b407625448b
%global shorttag %{sub %{gittag} 1 7}
%global gitdate  20230627

# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           symfpu
Version:        0
Release:        0.20.%{gitdate}git%{shorttag}%{?dist}
Summary:        An implementation of IEEE-754 / SMT-LIB floating-point 

License:        GPL-3.0-or-later
URL:            https://github.com/cvc5/symfpu
VCS:            git:%{url}.git
Source:         %{url}/archive/%{gittag}/%{name}-%{shorttag}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
SymFPU is an implementation of the SMT-LIB / IEEE-754 operations in terms of
bit-vector operations.  It is templated in terms of the bit-vectors,
propositions, floating-point formats and rounding mode types used.  This
allows the same code to be executed as an arbitrary precision "SoftFloat"
library (although it's performance would not be good) or to be used to build
symbolic representations of floating-point operations suitable for use in
"bit-blasting" SMT solvers (you could also generate circuits from them but
again, performance will likely not be good).

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description devel
This package contains header files and library links for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{gittag}

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -a core utils %{buildroot}%{_includedir}/%{name}

%files devel
%license LICENSE
%{_includedir}/%{name}/

%changelog
* Thu Dec 18 2025 Jerry James <loganjerry@gmail.com> - 0-0.20.20230627gite6ac3af
- Switch to the cvc5 git branch
- Drop all patches
- Package is now header-only and therefore noarch

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20190517gitc3acaf6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

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
