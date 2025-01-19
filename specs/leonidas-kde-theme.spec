Name:		leonidas-kde-theme
Version:	11.0.3
Release:	28%{?dist}
Summary:	Leonidas KDE Theme

# Automatically converted from old format: GPLv2+ and CC-BY-SA and CC-BY - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-CC-BY

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	leonidas-backgrounds-common >= 11.0.0-1
Requires:	leonidas-backgrounds-kdm >= 11.0.0-1



%description
This is Leonidas KDE Theme Artwork containing KSplash theme, KDM theme and
wallpapers theme. 

%prep
%setup -q


%package lion
Summary:	Leonidas Lion KDE Theme
Requires:	leonidas-backgrounds-lion >= 11.0.0-1

%description lion
This is an optional Leonidas Lion KDE wallpaper theme.


%package landscape
Summary:	Leonidas Landscape KDE Theme
Requires:	leonidas-backgrounds-landscape >= 11.0.0-1

%description landscape
This is an optional Leonidas Landscape KDE wallpaper theme.


%build
# blank

%install
rm -rf %{buildroot}

# wallpapers
# no more wallpapers links in wallpapers directory which causes all wp in list,
# not only theme
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers

# KDM
# for KDM and splash we use PNG wallpaper from leonidas-kdm package
# thus only one aspect ratio

mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/leonidas/ %{buildroot}/%{_kde4_appsdir}/kdm/themes/
(cd %{buildroot}/%{_kde4_appsdir}/kdm/themes/leonidas/
ln -s ../../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.png leonidas.png
)

mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/pics/users
cp -rp kdm/users %{buildroot}/%{_kde4_appsdir}/kdm/pics

# KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Leonidas/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/leonidas.png

# KDE 4 wallpapers theme
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers/leonidas/contents/images
cp -rp wallpapers/leonidas/metadata.desktop %{buildroot}%{_kde4_datadir}/wallpapers/leonidas
cp -rp wallpapers/leonidas/screenshot.png %{buildroot}%{_kde4_datadir}/wallpapers/leonidas/contents
(cd %{buildroot}%{_kde4_datadir}/wallpapers/leonidas/contents/images
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 640x480.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 800x480.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 800x600.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1024x600.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1024x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1152x720.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1152x864.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1200x900.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1280x720.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1280x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1280x800.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1280x960.jpg
ln -s ../../../../backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon.jpg 1280x1024.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1366x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1440x900.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1440x1080.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1600x1200.jpg
ln -s ../../../../backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon.jpg 1600x1280.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1680x1050.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1920x1080.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1920x1200.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1920x1440.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 2048x1536.jpg
)

# KDE 4 wallpapers theme lion
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-lion/contents/images
cp -rp wallpapers/leonidas-lion/metadata.desktop %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-lion
cp -rp wallpapers/leonidas-lion/screenshot.png %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-lion/contents
(cd %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-lion/contents/images
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 640x480.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 800x480.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 800x600.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1024x600.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1024x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1152x720.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1152x864.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1200x900.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1280x720.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1280x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1280x800.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1280x960.jpg
ln -s ../../../../backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon_right.jpg 1280x1024.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1366x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1440x900.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1440x1080.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1600x1200.jpg
ln -s ../../../../backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon_right.jpg 1600x1280.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1680x1050.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1920x1080.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1920x1200.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1920x1440.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 2048x1536.jpg
)

# KDE 4 wallpapers theme landscape
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-landscape/contents/images
cp -rp wallpapers/leonidas-landscape/metadata.desktop %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-landscape
cp -rp wallpapers/leonidas-landscape/screenshot.png %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-landscape/contents
(cd %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-landscape/contents/images
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 800x480.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1024x600.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1024x768.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1152x720.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1152x864.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1280x768.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1280x800.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1280x960.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1280x1024.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1366x768.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1440x900.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1440x1080.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1600x1200.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1600x1280.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1920x1080.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1920x1200.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1920x1440.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 2048x1536.png
)


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/kdm/themes/leonidas/
%{_kde4_appsdir}/ksplash/Themes/Leonidas/
%{_kde4_datadir}/wallpapers/leonidas/
%{_kde4_appsdir}/kdm/pics/users/default_leonidas.png

%files lion
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_datadir}/wallpapers/leonidas-lion/

%files landscape
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_datadir}/wallpapers/leonidas-landscape/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 11.0.3-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 26 2009 Jaroslav Reznik <jreznik@redhat.com> 11.0.3-1
- fix ksplash background on dual head (bz#519392)

* Tue Aug 04 2009 Rex Dieter <rdieter@fedoraproject.org> 11.0.2-1
- fixup theme metadata for KDE-4.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 12 2009 Jaroslav Reznik <jreznik@redhat.com> 11.0.1-1
- reenable icon labels

* Tue May 12 2009 Jaroslav Reznik <jreznik@redhat.com> 11.0.0-1
- synchronize versioning with leonidas-backgrounds
- leonidas lion and landscape theme

* Mon May 11 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.5-1
- text overflow (bz#498630)

* Sat May 09 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.4-3
- wallpaper symlinks fixed (bz#496379)

* Thu Apr 23 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.4-2
- tarball respin

* Thu Apr 23 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.4-1
- default face (original by K. Peirce, CC-BY)

* Thu Apr 23 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.3-1
- new KDM theme design

* Wed Apr 22 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.2-4
- our own logos for both fedora and generic version

* Tue Apr 21 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.2-3
- fix dist tag

* Tue Apr 21 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.2-2
- tarball respin

* Tue Apr 21 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.2-1
- wallpaper screenshot
- fixes

* Fri Apr 17 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.1-1
- use KDM PNG for KDM, KSplash, JPGs for wallpaper
- does not link wallpapers to wallpapers directory

* Wed Apr 15 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.0-2
- fix license
- upstream url + source url 
 
* Tue Apr 7 2009 Jaroslav Reznik <jreznik@redhat.com> 0.2.0-1
- updated to lion theme

* Tue Mar 17 2009 Jaroslav Reznik <jreznik@redhat.com> 0.1.0-1
- initial package
