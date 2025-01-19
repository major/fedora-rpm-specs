Name:           ogmtools
Version:        1.5
Release:        39%{?dist}
Summary:        Tools for Ogg media streams

License:        GPL-2.0-or-later
URL:            https://www.bunkus.org/videotools/ogmtools
Source:         %{url}/%{name}-%{version}.tar.bz2
Patch:          ogmtools-1.5-optflags.patch
Patch:          ogmtools-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  libdvdread-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel

# Bundled and forked copy
Provides:       bundled(avilib)

%description
These tools allow information about (ogminfo) or extraction from (ogmdemux) or
creation of (ogmmerge) OGG media streams. Note that OGM is used for "OGG media
streams".

%prep
%autosetup -p1

# Convert Changelog to UTF-8
iconv -f iso8859-1 -t utf8 ChangeLog -o ChangeLog.txt
touch -r ChangeLog ChangeLog.txt
mv ChangeLog.txt ChangeLog

%build
export CXXFLAGS="-std=c++14 %{optflags}"
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/dvdxchap
%{_bindir}/ogmcat
%{_bindir}/ogmdemux
%{_bindir}/ogminfo
%{_bindir}/ogmmerge
%{_bindir}/ogmsplit
%{_mandir}/man1/dvdxchap.1*
%{_mandir}/man1/ogmcat.1*
%{_mandir}/man1/ogmdemux.1*
%{_mandir}/man1/ogminfo.1*
%{_mandir}/man1/ogmmerge.1*
%{_mandir}/man1/ogmsplit.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Florian Weimer <fweimer@redhat.com> - 1.5-35
- Fix C99 compatibility issue in the configure script

* Mon Aug 28 2023 Davide Cavalca <dcavalca@fedoraproject.org> - 1.5-34
- Rework specfile to follow latest guidelines
- Convert license tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.5-29
- rebuild for libdvdread-6.1 ABI bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff Law <law@redhat.com> - 1.5-27
- Use C++14 as this code is not C++17 ready

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.5-25
- rebuild for libdvdread ABI bump

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5-15
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Gianluca Sforna <giallu gmail com> - 1.5-6
- honour RPM_OPT_FLAGS
- use --disable-dependency-tracking

* Thu Apr  9 2009 Gianluca Sforna <giallu gmail com> - 1.5-5
- Fix rpmlint issues
- Fix license tag

* Thu Dec 16 2008 Gianluca Sforna <giallu gmail com> - 1.5-4
- New spec based off freshrpms for Fedora submission
