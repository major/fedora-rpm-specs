Name: psfex
Version: 3.24.1
Release: 4%{?dist}
Summary: Model the Point Spread Function from FITS images

License: GPL-3.0-only
URL: http://astromatic.iap.fr/software/%{name}
Source0: https://github.com/astromatic/psfex/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

BuildRequires: fftw-devel
BuildRequires: openblas-devel
BuildRequires: plplot-devel

%description
PSFEx (“PSF Extractor”) extracts models of the Point Spread Function (PSF) 
from FITS images processed with SExtractor and measures the quality of images. 
The generated PSF models can be used for model-fitting photometry or 
morphological analyses.

%prep
%autosetup -p1

%build
./autogen.sh
%configure --enable-plplot=yes --enable-openblas=yes
%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS HISTORY README.md THANKS 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/manx/%{name}.x*
%{_datadir}/%{name}/

%changelog
* Mon Dec 23 2024 Orion Poplawski <orion@nwra.com> - 3.24.1-4
- Use openblas

* Sun Oct 06 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 3.24.1-3
- Rebuild to fix FTBFS 2301104

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 01 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 3.24.1-1
- New upstream source
- Using SPDX license name

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Florian Weimer <fweimer@redhat.com> - 3.17.1-28
- Fix C99 compatibility issue

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 3.17.1-24
- Fix FTBS in F35

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Than Ngo <than@redhat.com> - 3.17.1-20
- Fixed FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Orion Poplawski <orion@nwra.com> - 3.17.1-18
- Rebuild for plplot 5.15

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Orion Poplawski <orion@nwra.com> - 3.17.1-16
- Rebuild for plplot 5.14.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Orion Poplawski <orion@cora.nwra.com> - 3.17.1-14
- Rebuild for plplot 5.13
- Use %%license
- Modernize spec

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> - 3.17.1-9
- rebuild for new plplot

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Orion Poplawski <orion@cora.nwra.com> - 3.17.1-5
- Rebuild for plplot 5.11.0, fix name in configure

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 3.17.1-3
- Bug #1082054 fixed in Rawhide, workaround removed

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 3.17.1-1
- New upstream source (3.17.1)
- Add workaround for bug #1082054 in Rawhide

* Thu Dec 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 3.9.1-10
- Fix formar security bug (bz #1037258)
- Spec cleanups

* Wed Oct 2 2013 Orion Poplawski <orion@cora.nwra.com> - 3.9.1-9
- Rebuild for plplot 5.9.10
- Patch configure for atlas 3.10 library names

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 18 2011 Orion Poplawski <orion@cora.nwra.com> - 3.9.1-4
- Rebuild for plplot 5.9.8
- Add patch to fix use of deprecated plplot functions

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 3.9.1-2
- Dropped psfex.x and BUGS
- files section more explicit

* Mon Nov 08 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 3.9.1-1
- New upstream source

