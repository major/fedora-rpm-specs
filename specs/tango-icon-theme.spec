Name:           tango-icon-theme
Version:        0.8.90
Release:        30%{?dist}
Summary:        Icon theme from Tango Project
Summary(de):    Symbolthema vom Tango Projekt
Summary(es):    Iconos del Proyecto Tango
Summary(pl):    Ikony Projektu Tango


# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            http://tango.freedesktop.org/Tango_Desktop_Project

Source0:        http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
#VCS: git:git://anongit.freedesktop.org/tango/tango-icon-theme
Patch0:         tango-icon-theme-0.8.90-transparency.patch

# https://bugs.freedesktop.org/show_bug.cgi?id=45803
Patch1:         tango-icon-theme-0.8.90-rsvg-convert.patch
Patch2:         tango-icon-theme-0.8.90-rsvg-convert-configure.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  icon-naming-utils >= 0.8.90
BuildRequires:  ImageMagick-devel >= 5.5.7
BuildRequires:  intltool
BuildRequires:  librsvg2-devel >= 2.35.2
BuildRequires:  librsvg2-tools
BuildRequires:  pkgconfig >= 0.19

%description
Contains icons from Tango Project.

%description -l de
Enthält Symbole vom Tango Projekt.

%description -l es
Contiene iconos del Proyecto Tango.

%description -l pl
Zawiera ikony Projektu Tango.


%prep
%setup -q
%patch -P0 -p1 -b .transparency
%patch -P1 -p1
%patch -P2 -p1

%build
%configure --enable-png-creation
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL='install -p'



%post
touch --no-create %{_datadir}/icons/Tango &>/dev/null || :


%postun
touch --no-create %{_datadir}/icons/Tango &>/dev/null || :
gtk-update-icon-cache -q %{_datadir}/icons/Tango &>/dev/null || :


%posttrans
gtk-update-icon-cache -q %{_datadir}/icons/Tango &>/dev/null || :


%files
%{_datadir}/icons/Tango
%doc AUTHORS ChangeLog COPYING README 


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 24 2013 Peter Oliver <rpm@mavit.org.uk> - 0.8.90-10
- Build with rsvg-convert.  Fixes #992774.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 11 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.90-5
- Fix transparency issue (#709763)
- Update icon-cache scriptlets

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.8.90-3
- Use bzipped upstream tarball.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Feb 28 2009 Peter Gordon <peter@thecodergeek.com> - 0.8.90-1
- Update to new upstream release (0.8.90)
- License change: from CC-BY-SA to Public Domain

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8.1-2
- fix license tag

* Sun Sep 09 2007 Peter Gordon <peter@thecodergeek.com> - 0.8.1-1
- Update to new upstream release (0.8.1)

* Sat Feb 17 2007 Peter Gordon <peter@thecodergeek.com> - 0.8.0-1
- Update to new upstream release (0.8.0).
- Fix URL, and some other whitespace issues in the spec.
- Add Spanish (es) translations of Summary and %%description.
- Fix %%defattr line.
- Use macros instead of $RPM_* variables.

* Thu Sep 07 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-5
- Added %%{?dist}
- Removed unnecessary automake BuildRequire

* Thu Jul 27 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-4
- Drop unnecessary BuildRequires

* Thu Jul 27 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-3
- Added --enable-png-creation
- Added librsvg2-devel BuildRequire

* Thu Jul 27 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-2
- New scriptlets
- Changed the license name

* Thu Jul 27 2006 Piotr Drąg <raven at pmail dot pl> - 0.7.2-1
- Initial RPM release
