
Name:           scamp
Version:        2.10.0
Release:        12%{?dist}
Summary:        compute astrometric and photometric solutions from sextractor catalogs

License:        GPL-3.0-only
URL:            http://www.astromatic.net/software/scamp
Source0:        https://github.com/astromatic/scamp/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: wrong-pointer-i386.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  cdsclient
BuildRequires:  curl-devel
BuildRequires:  fftw-devel
BuildRequires:  libtool
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig
BuildRequires:  plplot-devel

Requires:       cdsclient

%description
SCAMP is a program that computes astrometric and photometric solutions from
SExtractor catalogs

%prep
%autosetup  -p1


%build
sh autogen.sh
%configure --enable-openblas \
  --enable-plplot
%make_build


%install
%make_install


%files
%license COPYRIGHT LICENSE
%doc AUTHORS ChangeLog HISTORY README.md THANKS
%{_bindir}/scamp
%{_datadir}/scamp/
%{_mandir}/*/scamp.*.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 06 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 2.10.0-11
- Rebuild to fix FTBFS 2301268

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 07 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 2.10.0-9
- Patch to fix compilation error in i386

* Thu Feb 01 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 2.10.0-8
- Rebuild to fix FTBS
- Using SPDX license name

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Christian Dersch <lupinix@fedoraproject.org> - 2.10.0-1
- new version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Christian Dersch <lupinix@fedoraproject.org> - 2.7.8-1
- new version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Orion Poplawski <orion@nwra.com> - 2.0.4-16
- Rebuild for plplot 5.15

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Orion Poplawski <orion@nwra.com> - 2.0.4-14
- Rebuild for plplot 5.14.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Christian Dersch <lupinix.fedora@gmail.com> - 2.0.4-12
- Fix segfault in field.c:343

* Mon Jul 23 2018 Orion Poplawski <orion@nwra.com> - 2.0.4-11
- Rebuild for plplot 5.13
- Cleanup spec

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Tom Callaway <spot@fedoraproject.org> - 2.0.4-6
- rebuild for plplot 5.12.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.4-2
- Rebuild for plplot 5.11.0, fix name in configure

* Mon Jan 12 2015 Christian Dersch <lupinix@fedoraproject.org> - 2.0.4-1
- initial spec
