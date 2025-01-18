Name:		goddard-kde-theme
Version:	13.1.1
Release:	22%{?dist}
Summary:	Goddard KDE Theme

License:	GPL-2.0-or-later AND CC-BY-SA-1.0

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	goddard-backgrounds-kde >= 13.0.0 

Provides:	goddard-kdm-theme = %{version}-%{release}
Provides:	goddard-ksplash-theme = %{version}-%{release}
Provides:       goddard-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 13
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:       system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Goddard KDE Theme Artwork containing
KDM theme, KSplash theme, Plasma desktop, and Plasma netbook theme.


%prep
%setup -q


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Goddard/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Goddard-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Goddard/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Goddard/
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-640x480.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-800x480.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-800x600.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1024x600.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1024x768.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1152x720.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1152x864.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1200x900.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1280x720.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1280x768.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1280x800.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1280x960.jpg
ln -s ../../../../../backgrounds/goddard/default/normalish/goddard.jpg goddard-1280x1024.jpg

# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1366x768.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1440x900.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1440x1080.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1600x1200.jpg
ln -s ../../../../../backgrounds/goddard/default/normalish/goddard.jpg goddard-1600x1280.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1680x1050.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1920x1080.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1920x1200.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1920x1440.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-2048x1536.jpg
# KDM falls back to this one if there's no match
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard.jpg
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Goddard/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
# goddard.png is not provided by goddard-backgrounds and is now embedded in the ksplash theme, no need for symlinks
#ln -s ../../../../../../backgrounds/goddard/default/standard/goddard.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Goddard/1400x1050/goddard.png
#mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Goddard/1280x800/
#ln -s ../../../../../../backgrounds/goddard/default/wide/goddard.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Goddard/1280x800/goddard.png

# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Goddard/1400x1050/logo.png



%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Goddard/
%{_kde4_appsdir}/desktoptheme/Goddard-netbook/
%{_kde4_appsdir}/kdm/themes/Goddard/
%{_kde4_appsdir}/ksplash/Themes/Goddard/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Than Ngo <than@redhat.com> - 13.1.1-17
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Martin Briza <mbriza@redhat.com> 13.1.1-1
- Moved and extended the area for the caps lock warning

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Rex Dieter <rdieter@fedoraproject.org> 13.1.0-1
- include Goddard,Goddard plasma desktoptheme

* Mon Aug 02 2010 Jaroslav Reznik <jreznik@redhat.com> 13.0.1-2
- provide system theme only for F-13

* Fri Apr 23 2010 Rex Dieter <rdieter@fedoraproject.org> 13.0.1-1
- scrub fedora logo from preview/screenshots

* Thu Apr 22 2010 Rex Dieter <rdieter@fedoraproject.org> 13.0.0-1
- artwork refresh

* Mon Feb 22 2010 Jaroslav Reznik <jreznik@redhat.com> 12.91.1-1
- Provides for system-kde-theme

* Fri Feb 19 2010 Jaroslav Reznik <jreznik@redhat.com> 12.91.0-1
- Update to new wallpapers

* Mon Feb 15 2010 Jaroslav Reznik <jreznik@redhat.com> 12.90.0-1
- initial package
