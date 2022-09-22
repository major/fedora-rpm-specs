
Name:		spherical-cow-kde-theme
Summary:        Spherical Cow KDE Theme
Version:	18.0.3
Release:	16%{?dist}

License:	GPLv2+ and CC-BY-SA
# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	spherical-cow-backgrounds-kde >= 18.0.0

Provides:	spherical-cow-kdm-theme = %{version}-%{release}
Provides:	spherical-cow-ksplash-theme = %{version}-%{release}
Provides:	spherical-cow-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 18
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Spherical Cow KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q


%build
# blank


%install
### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Spherical_Cow/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Spherical_Cow-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd %{buildroot}%{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/SphericalCow/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/SphericalCow/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/SphericalCow/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/spherical-cow/default/standard/spherical-cow.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/1920x1200/
ln -s ../../../../../../backgrounds/spherical-cow/default/wide/spherical-cow.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/1920x1200/Spherical_Cow.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/1280x1024/
ln -s ../../../../../../backgrounds/spherical-cow/default/normalish/spherical-cow.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/1280x1024/Spherical_Cow.png
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/2048x1536/logo.png


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Spherical_Cow/
%{_kde4_appsdir}/desktoptheme/Spherical_Cow-netbook/
%{_kde4_appsdir}/kdm/themes/SphericalCow/
%{_kde4_appsdir}/ksplash/Themes/SphericalCow/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Martin Briza <mbriza@redhat.com> 18.0.3-1
- moved and extended the area for the caps lock warning (#901822)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Martin Briza <mbriza@redhat.com> 18.0.2-1
- set as Fedora 18 only theme

* Thu Mar 07 2013 Martin Briza <mbriza@redhat.com> 18.0.1-1
- fix the ksplash preview

* Wed Mar 06 2013 Rex Dieter <rdieter@fedoraproject.org> 18.0.0-2
- drop mostly-useless backgrounds-kde-version macro (used only once)

* Mon Feb 25 2013 Rex Dieter <rdieter@fedoraproject.org> 18.0.0-1
- fix desktoptheme previews
- update fedora references to 18
- .spec cosmetics

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.91.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 20 2012 Martin Briza <mbriza@redhat.com> 17.91.1-1
- Fixed symlink locations
- Added a proper screenshot

* Wed Aug 15 2012 Martin Briza <mbriza@redhat.com> 17.91.0-1
- initial package
