%global backgrounds_kde_version 18.90.0

Name:		schroedinger-cat-kde-theme
Version:	18.91.6
Release:	17%{?dist}
Summary:	Schrödinger's Cat KDE Theme

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	schroedinger-cat-backgrounds-kde >= %{backgrounds_kde_version}

Provides:	schroedinger-cat-kdm-theme = %{version}-%{release}
Provides:	schroedinger-cat-ksplash-theme = %{version}-%{release}
Provides:	schroedinger-cat-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 19
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Schrödinger's Cat KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Schroedinger_Cat/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Schroedinger_Cat-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd {buildroot}{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/SchroedingerCat/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/SchroedingerCat/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/SchroedingerCat/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/schroedinger-cat/default/standard/schroedinger-cat.jpg \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/1920x1200/
ln -s ../../../../../../backgrounds/schroedinger-cat/default/wide/schroedinger-cat.jpg \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/1920x1200/Schroedinger_Cat.jpg
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/1280x1024/
ln -s ../../../../../../backgrounds/schroedinger-cat/default/normalish/schroedinger-cat.jpg \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/1280x1024/Schroedinger_Cat.jpg
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/2048x1536/logo.png


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Schroedinger_Cat/
%{_kde4_appsdir}/desktoptheme/Schroedinger_Cat-netbook/
%{_kde4_appsdir}/kdm/themes/SchroedingerCat/
%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.91.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.91.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 10 2013 Jaroslav Reznik <jreznik@redhat.com> 18.91.6-2
- set exclusive Fedora 19 theme

* Mon Aug 05 2013 Martin Briza <mbriza@redhat.com> 18.91.6-1
- moved and extended the area for the caps lock warning (#901822)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.91.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Martin Briza <mbriza@redhat.com> 18.91.5-1
- fixed default wallpaper file suffix

* Thu Mar 28 2013 Martin Briza <mbriza@redhat.com> 18.91.4-1
- removed unneeded sections from the spec
- fixed version dependency on backgrounds_kde

* Thu Mar 28 2013 Martin Briza <mbriza@redhat.com> 18.91.3-1
- fixed an undefined macro warning from rpmlint

* Thu Mar 28 2013 Martin Briza <mbriza@redhat.com> 18.91.2-1
- fixed the ksplash preview

* Wed Mar 27 2013 Martin Briza <mbriza@redhat.com> 18.91.1-1
- fixed the preview screenshots

* Wed Mar 27 2013 Martin Briza <mbriza@redhat.com> 18.91.0-1
- initial package
