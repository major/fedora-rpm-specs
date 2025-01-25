Name: swarp
Version: 2.38.0
Release: 27%{?dist}
Summary: Tool that resamples and co-adds together FITS images

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.astromatic.net/software/%{name}
Source: http://www.astromatic.net/download/swarp/swarp-%{version}.tar.gz
Patch: fix-gcc15.patch

# https://gcc.gnu.org/gcc-10/porting_to.html#common
# https://github.com/astromatic/sextractor/issues/12
%define _legacy_common_support 1

BuildRequires: make
BuildRequires: gcc

%description
SWarp is a program that resamples and co-adds together FITS images 
using any arbitrary astrometric projection defined in the WCS standard. 

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1

%build
%configure --enable-threads
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS BUGS COPYRIGHT HISTORY README THANKS TODO
%license COPYRIGHT
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/manx/*
%{_datadir}/%{name}/

%files doc
%doc doc/swarp.pdf 
%license COPYRIGHT

%changelog
* Thu Jan 23 2025 Sergio Pascual <sergiopr@fedoraproject.org> - 2.38.0-27
- Patch wrong function definition with gcc15 (fixes rhbz #2341402)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.38.0-25
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2.38.0-15
- Enable legacy_common_support (-fcommon) temporarily

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.38.0-11
- BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.38.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.38.0-1
- Correct source url
- License is GPLv3+
- New upstream source (2.38)

* Thu Dec 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 2.19.1-8
- Fix format security error (bz #1037344)
- Spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 2.19.1-2
- EVR bump to rebuild

* Mon Dec 13 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 2.19.1-1
- New upstream version
- Removed patch, it's in upstream now

* Fri Jul 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 2.17.6-2
- License in -doc subpackage

* Tue Mar 30 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 2.17.6-1
- New version from astromatic.iap.fr. 
- License is Cecill know
- Documentation in -doc subpackage

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> 2.17.1-3
- Include unowned /usr/share/swarp directory

* Sat Jun 21 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.17.1-2
- Spec cleanup

* Thu Jun 19 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.17.1-1
- Initial spec file.
