Name: sextractor
Version: 2.25.0
Release: 12%{?dist}
Summary: Extract catalogs of sources from astronomical images

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://astromatic.iap.fr/software/%{name}
Source0: https://github.com/astromatic/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: sextractor-format-sec.patch

# https://gcc.gnu.org/gcc-10/porting_to.html#common
# https://github.com/astromatic/sextractor/issues/12
%define _legacy_common_support 1

BuildRequires: make
BuildRequires: gcc
BuildRequires: automake autoconf libtool
BuildRequires: fftw-devel >= 3.1
BuildRequires: openblas-devel

%description
SExtractor is a program that builds a catalogue of objects from an 
astronomical image. Although it is particularly oriented towards 
reduction of large scale galaxy-survey data, it performs rather 
well on moderately crowded star fields.

%prep
%setup -q
%patch -P0 -p1
sh ./autogen.sh

%build
%configure --enable-openblas
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 -p config/*.conv %{buildroot}%{_datadir}/%{name}
install -m 644 -p config/default.nnw %{buildroot}%{_datadir}/%{name}

%files
%doc AUTHORS BUGS COPYRIGHT HISTORY README.md THANKS config/default.sex config/default.param config/README
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/manx/*
%{_datadir}/%{name}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.25.0-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2.25.0-1
- New upstream release (2.25.0)
- Built with openblas (bz#1619130)
- Enable legacy_common_support (-fcommon) temporarely

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.19.5-2
- License is GPLv3+

* Wed Mar 26 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 2.19.5-1
- New upstream release (2.19.5)

* Thu Dec 05 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 2.8.6-8
- Fix format-security error (bz #1037322)

* Wed Oct 02 2013 Sergio Pascual <sergiopr@fedoraproject.org> - 2.8.6-7
- Hack to build with monolithic ATLAS
- Cleanup of the specfile

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 26 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 2.8.6-1
- New upstream source

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  1 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2.5.0-7
- Include unowned directory.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5.0-6.1
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 2.5.0-5.1
- Rebuild for Fedora 8 to get the build-id

* Tue Sep 12 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.5.0-5
- Rebuilt for FC6.

* Wed Jul 26 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.5.0-4
- Patch to resolve pointer aliasing problems (bug #199700)
- Removed -DXSL_URL flag, as the file sextractor.xsl does not exist yet

* Mon Jul 24 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.5.0-3
- Reverting optimization to -O2, it breaks debug infos

* Fri Jul 21 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.5.0-2
- fitsconv.c has correct permissions
- changed optimization from -O2 to -O1 (bug #199700)
- additional define allows VOTable output

* Wed Jul 19 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.5.0-1
- New upstream version 2.5.0

* Tue Jun 20 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.4.4-2
- Fixed executable permission in src/fits/fitsconv.c
- default.sex and default.param moved to docs

* Mon Jun 19 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 2.4.4-1
- Initial spec file.
