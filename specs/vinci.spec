Name:           vinci
Version:        1.0.5
Release:        28%{?dist}
Summary:        Algorithms for volume computation

License:        GPL-1.0-or-later
URL:            https://www.multiprecision.org/vinci/
Source0:        https://www.multiprecision.org/downloads/%{name}-%{version}.tar.gz
# Man page written by Jerry James using text found in the sources.  Therefore,
# the man page has the same copyright and license as the sources.
Source1:        %{name}.1

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tex(latex)

Requires:       coreutils
Requires:       lrslib-utils

%description
The volume is one of the central properties of a convex body, and volume
computation is involved in many hard problems.  Applications range from
rather classical ones as in convex optimization to problems in remote
fields like algebraic geometry where the number of common roots of
polynomials can be related to a special polytope volume.

Part of the fascination of the subject stems from the discrepancy
between the intuitive notion of "volume" and the actual hardness of
computing it.  Despite this discouraging complexity - algorithms in
general need exponential time in the input dimension - steadily growing
computer power enables us to attack problems of practical interest.

Vinci is an easy to install C package that implements the state of the
art algorithms for volume computation.  It is the fruit of a research
project carried out at the IFOR (Institute for Operations Research) at
ETH Zürich, in collaboration with Benno Büeler and Komei Fukuda.

%prep
%autosetup

%build
# Link with the right flags
sed -i 's|-o vinci|& %{build_ldflags}|' makefile

%make_build OPT='%{build_cflags}'
pdflatex manual.tex
pdflatex manual.tex

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
sed -e "s/@VERSION@/%{version}/" %{SOURCE1} > \
  %{buildroot}%{_mandir}/man1/%{name}.1
touch -r %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc ChangeLog manual.pdf
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 1.0.5-25
- Stop building for 32-bit x86

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Jerry James <loganjerry@gmail.com> - 1.0.5-23
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 1.0.5-22
- Fix a package notes snafu
- Minor spec file cleanups

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 1.0.5-9
- Use license macro
- Fix sed expression separator for new RPM_LD_FLAGS

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr  7 2014 Jerry James <loganjerry@gmail.com> - 1.0.5-6
- Update project and source URLs
- Link with RPM_LD_FLAGS

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Jerry James <loganjerry@gmail.com> - 1.0.5-2
- Fix permissions on the binary

* Tue Feb 14 2012 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Initial RPM
