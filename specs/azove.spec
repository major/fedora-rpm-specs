Name:           azove
Version:        2.0
Release:        30%{?dist}
Summary:        Another Zero-One Vertex Enumeration tool

License:        GPL-2.0-or-later
URL:            https://people.mpi-inf.mpg.de/alumni/d1/2019/behle/azove.html
Source0:        https://people.mpi-inf.mpg.de/alumni/d1/2019/behle/%{name}-%{version}.tar.gz
# Man page written by Jerry James from text found in the sources.  Therefore,
# the copyright and license of the man page is the same as the sources.
Source1:        %{name}2.1
# Sent upstream 2 Mar 2012: add an include that used to be implicit.
Patch:          %{name}-include.patch
# Polymake patch to use static node allocation.  Dynamic node allocation is
# unreliable on newer Linux kernels.
Patch:          %{name}-memory.patch
# Use std::unordered_multimap instead of the deprecated __gnu_cxx::hash_multimap
Patch:          %{name}-map.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make

%description
Azove is a tool designed for counting (without explicit enumeration) and
enumeration of 0/1 vertices.  Given a polytope by a linear relaxation or
facet description P = {x | Ax <= b}, all 0/1 points lying in P can be
counted or enumerated.  This is done by intersecting the polytope P with
the unit-hypercube [0,1] d.  The integral vertices (no fractional ones)
of this intersection will be enumerated.  If P is a 0/1 polytope, azove
solves the vertex enumeration problem.  In fact it can also solve the
0/1 knapsack problem and the 0/1 subset sum problem.

%prep
%autosetup -p0

%build
%make_build COMPILER_FLAGS='%{build_cflags} %{build_ldflags}'

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -p %{name}2 %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 -p %{SOURCE1} %{buildroot}%{_mandir}/man1

%files
%doc INSTALL README
%license COPYING
%{_bindir}/%{name}2
%{_mandir}/man1/%{name}2.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 2.0-26
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 11 2022 Jerry James <loganjerry@gmail.com> - 2.0-24
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Jerry James <loganjerry@gmail.com> - 2.0-19
- Add -memory and -map patches
- Build with RPM_LD_FLAGS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 2.0-7
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug  3 2012 Jerry James <loganjerry@gmail.com> - 2.0-2
- Fix permissions on installed files

* Fri Mar  2 2012 Jerry James <loganjerry@gmail.com> - 2.0-1
- Initial RPM
