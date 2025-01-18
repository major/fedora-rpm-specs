Name:		beefy-miracle-kde-theme
Version:	16.91.0.3
Release:	23%{?dist}
Summary:	Beefy Miracle KDE Theme

License:	GPL-2.0-or-later AND CC-BY-SA-1.0

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	beefy-miracle-backgrounds-kde >= 16.91.0

Provides:	beefy-miracle-kdm-theme = %{version}-%{release}
Provides:	beefy-miracle-ksplash-theme = %{version}-%{release}
Provides:	beefy-miracle-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 17
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Beefy Miracle KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Beefy_Miracle/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Beefy_Miracle-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd %{buildroot}%{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/BeefyMiracle/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/BeefyMiracle/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/BeefyMiracle/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/beefy-miracle/default/standard/beefy-miracle.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/1920x1200/
ln -s ../../../../../../backgrounds/beefy-miracle/default/wide/beefy-miracle.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/1920x1200/beefy-miracle.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/1280x1024/
ln -s ../../../../../../backgrounds/beefy-miracle/default/normalish/beefy-miracle.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/1280x1024/
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/2048x1536/logo.png


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Beefy_Miracle/
%{_kde4_appsdir}/desktoptheme/Beefy_Miracle-netbook/
%{_kde4_appsdir}/kdm/themes/BeefyMiracle/
%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Than Ngo <than@redhat.com> - 16.91.0.3-18
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Martin Briza <mbriza@redhat.com> 16.91.0.3-1
- Moved and extended the area for the caps lock warning

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012 Rex Dieter <rdieter@fedoraproject.org> 16.91.0.1-4
- fix unexpanded macro (simplify by not using a macro)

* Tue Aug 21 2012 Martin Briza <mbriza@redhat.com - 16.91.0.1-3
- Set as a Fedora 17 exclusive theme

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Jaroslav Reznik <jreznik@redhat.com> 16.91.0.1-1
- fix Plasma Desktop theme - reference correct wps

* Thu Feb 09 2012 Jaroslav Reznik <jreznik@redhat.com> 16.91.0-2
- fix provides

* Thu Feb 09 2012 Jaroslav Reznik <jreznik@redhat.com> 16.91.0-1
- initial package
