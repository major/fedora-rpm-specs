%global backgrounds_kde_version 19.90.0

Name:		heisenbug-kde-theme
Version:	19.90.5
Release:	17%{?dist}
Summary:	Heisenbug KDE Theme

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	heisenbug-backgrounds-kde >= %{backgrounds_kde_version}

Provides:	heisenbug-kdm-theme = %{version}-%{release}
Provides:	heisenbug-ksplash-theme = %{version}-%{release}
Provides:	heisenbug-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 20
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Heisenbug KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Heisenbug/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Heisenbug-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd {buildroot}{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Heisenbug/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Heisenbug/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Heisenbug/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/heisenbug/default/standard/heisenbug.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/1920x1200/
ln -s ../../../../../../backgrounds/heisenbug/default/wide/heisenbug.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/1920x1200/Heisenbug.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/1280x1024/
ln -s ../../../../../../backgrounds/heisenbug/default/normalish/heisenbug.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/1280x1024/Heisenbug.png
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/2048x1536/logo.png


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Heisenbug/
%{_kde4_appsdir}/desktoptheme/Heisenbug-netbook/
%{_kde4_appsdir}/kdm/themes/Heisenbug/
%{_kde4_appsdir}/ksplash/Themes/Heisenbug/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 19.90.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19.90.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 02 2014 Rex Dieter <rdieter@fedoraproject.org> 19.90.5-3
- let f21-kde-theme be default for f21+

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19.90.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 19.90.5-1
- drop sddm theme (moved to sddm packaging)

* Tue Sep 10 2013 Martin Briza <mbriza@redhat.com> 19.90.4-1
- Fedora-brand the KDE theme, set it to username entry instead of user list (#1007065)

* Tue Sep 10 2013 Martin Briza <mbriza@redhat.com> 19.90.3-1
- fix the symlink to SDDM theme's background
- fix the screenshots
- fixed the wallpaper name in the KDM theme
- stopped linking the font in the SDDM theme'

* Tue Sep 10 2013 Jaroslav Reznik <jreznik@redhat.com> 19.90.2-1
- fix png suffix and version for desktop theme

* Mon Sep 09 2013 Jaroslav Reznik <jreznik@redhat.com> 19.90.1-1
- fix backgrounds suffix to match heisenbug-backgrounds
- fix screenshots

* Mon Sep 09 2013 Martin Briza <mbriza@redhat.com> 19.90.0-1
- initial package
