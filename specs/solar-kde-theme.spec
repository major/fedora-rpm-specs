Name:		solar-kde-theme
Version:	0.1.19
Release:	27%{?dist}
Summary:	Solar KDE Theme

# Automatically converted from old format: GPLv2 and CC-BY-SA - review is highly recommended.
License:	GPL-2.0-only AND LicenseRef-Callaway-CC-BY-SA
# We are upstream for this package
URL:            https://fedorahosted.org/fedora-kde-artwork/
Source0:        https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	solar-backgrounds-common >= 0.91.0
%if 0%{?fedora} > 10
# for Leonidas system logo
Requires:	leonidas-kde-theme
%endif


%description
Solar KDE Theme based on Solar theme by Samuele Storari. This package
contains KDM Solar Mania theme, KSplash Solar Comet theme and Solar background.


%prep
%setup -q


%build
# blank


%install
rm -rf %{buildroot}

# wallpapers
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers
ln -sf ../backgrounds/solar/standard/2048x1536/solar-0-morn.png %{buildroot}%{_kde4_datadir}/wallpapers/solar.png
ln -sf ../backgrounds/solar/wide/1920x1200/solar-0-morn.png %{buildroot}%{_kde4_datadir}/wallpapers/solar_wide.png
ln -sf ../backgrounds/solar/normalish/1280x1024/solar-0-morn.png %{buildroot}%{_kde4_datadir}/wallpapers/solar_high.png

# KDM
mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/SolarMania/ %{buildroot}/%{_kde4_appsdir}/kdm/themes/
(cd %{buildroot}/%{_kde4_appsdir}/kdm/themes/SolarMania/
ln -s ../../../../../wallpapers/solar.png solar-640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-800x480.png
ln -s ../../../../../wallpapers/solar.png solar-800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1024x600.png
ln -s ../../../../../wallpapers/solar.png solar-1024x768.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1152x720.png
ln -s ../../../../../wallpapers/solar.png solar-1152x864.png
ln -s ../../../../../wallpapers/solar.png solar-1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1280x768.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1280x800.png
ln -s ../../../../../wallpapers/solar.png solar-1280x960.png
ln -s ../../../../../wallpapers/solar_high.png solar-1280x1024.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1366x768.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1440x900.png
ln -s ../../../../../wallpapers/solar.png solar-1440x1080.png
ln -s ../../../../../wallpapers/solar.png solar-1600x1200.png
ln -s ../../../../../wallpapers/solar_high.png solar-1600x1280.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1920x1080.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1920x1200.png
ln -s ../../../../../wallpapers/solar.png solar-1920x1440.png
ln -s ../../../../../wallpapers/solar.png solar-2048x1536.png
# KDM falls back to this one if there's no match
ln -s ../../../../../wallpapers/solar.png solar.png
)

mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/pics/users
cp -rp kdm/users %{buildroot}/%{_kde4_appsdir}/kdm/pics

# KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/SolarComet/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/2048x1536
ln -s ../../../../../../wallpapers/solar.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/2048x1536/solar.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/1920x1200
ln -s ../../../../../../wallpapers/solar_wide.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/1920x1200/solar.png
ln -s ../../../../../../wallpapers/solar_high.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/1280x1024/solar.png

%if 0%{?fedora} > 10
# we have to drag Leonidas ksplash theme directory for F11
ln -s %{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/1280x1024/logo.png
%endif

# KDE 4 wallpapers theme
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers/Solar/contents/images
cp -rp wallpapers/Solar/metadata.desktop %{buildroot}%{_kde4_datadir}/wallpapers/Solar
cp -rp wallpapers/Solar/screenshot.png %{buildroot}%{_kde4_datadir}/wallpapers/Solar/contents
(cd %{buildroot}%{_kde4_datadir}/wallpapers/Solar/contents/images
ln -s ../../../solar.png 640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 800x480.png
ln -s ../../../solar.png 800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1024x600.png
ln -s ../../../solar.png 1024x768.png
ln -s ../../../solar_wide.png 1152x720.png
ln -s ../../../solar.png 1152x864.png
ln -s ../../../solar.png 1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1280x768.png
ln -s ../../../solar_wide.png 1280x800.png
ln -s ../../../solar.png 1280x960.png
ln -s ../../../solar_high.png 1280x1024.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1366x768.png
ln -s ../../../solar_wide.png 1440x900.png
ln -s ../../../solar.png 1440x1080.png
ln -s ../../../solar.png 1600x1200.png
ln -s ../../../solar_high.png 1600x1280.png
ln -s ../../../solar_wide.png 1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1920x1080.png
ln -s ../../../solar_wide.png 1920x1200.png
ln -s ../../../solar.png 1920x1440.png
ln -s ../../../solar.png 2048x1536.png
)



%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/kdm/themes/SolarMania/
%{_kde4_appsdir}/ksplash/Themes/SolarComet/
%{_kde4_datadir}/wallpapers/solar.png
%{_kde4_datadir}/wallpapers/solar_wide.png
%{_kde4_datadir}/wallpapers/solar_high.png
%{_kde4_datadir}/wallpapers/Solar/
%{_kde4_appsdir}/kdm/pics/users/default_solar.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.19-26
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 26 2009 Jaroslav Reznik <jreznik@redhat.com> 0.1.19-1
- correct NVR

* Wed Aug 26 2009 Jaroslav Reznik <jreznik@redhat.com> 0.1.19-1
- fix ksplash background on dual head

* Tue Aug 04 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.18-1.1
- don't require Leonidas on F10

* Tue Aug 04 2009 Rex Dieter <rdieter@fedoraproject.org> 0.1.18-1
- fixup theme metadata for KDE-4.3

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.1.17-5
- Link to F11 system logo

* Wed Apr 08 2009 Jesse Keating <jkeating@redhat.com> - 0.1.17-4
- Drop the version requirement on system-logos, causes problems
  with other logo packages.

* Mon Mar 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.1.17-3
- own %%_kde4_datadir/wallpapers/Solar

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Jaroslav Reznik <jreznik@redhat.com> 0.1.17-1
- screenshot resized to 200x150 px
- kdm theme authors are more compact 

* Thu Nov 13 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.16-2
- list 1920x1080, 1366x768 and 1280x720 (16:9/HDTV) as widescreen

* Mon Nov 10 2008 Than Ngo <than@redhat.com> 0.1.16-1
- uses hostname instead welcome-label
- fixes font issue

* Tue Nov 04 2008 Than Ngo <than@redhat.com> 0.1.15-1
- fix bz#469819, Username and password input fields overlaps each other

* Mon Nov 03 2008 Jaroslav Reznik <jreznik@redhat.com> 0.1.14-1
- revert clock label overflows changes (bz#469141) 

* Mon Nov 03 2008 Jaroslav Reznik <jreznik@redhat.com> 0.1.13-1
- fixes KDM clock label overflows the login box (bz#469141)

* Fri Oct 31 2008 Than Ngo <than@redhat.com> 0.1.12-1
- fix multihead issue
- fix topline/inputbox issue
- fix date string runs past the boundaries with DPI=120

* Thu Oct 30 2008 Jaroslav Reznik <jreznik@redhat.com> 0.1.11-1
- fixes full qualified host name runs past the boundaries (bz#469048)
- removes backgrounds from source tarball

* Thu Oct 30 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.10-3
- list 1200x900 (OLPC XO) for 4:3
- list 1280x768 (5:3) as widescreen (used by at least one netbook)

* Thu Oct 30 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.10-2
- use backgrounds from solar-backgrounds-common (>= 0.91.0, with the new look)
- support aspect ratios in the KDM theme
- add some more 4:3 and 8:5 resolutions to the symlink lists (KDM, wallpapers)
- use solar_wide.png for 800x480 and 1024x600 in KDM and wallpapers

* Mon Oct 27 2008 Than Ngo <than@redhat.com> 0.1.10-1
- fix layout issue

* Mon Oct 27 2008 Than Ngo <than@redhat.com> 0.1.9-2
- install screenshot in correct place

* Mon Oct 27 2008 Than Ngo <than@redhat.com> 0.1.9-1
- fix KDM/Wallpaper screenshot issue in KDM theme

* Sun Oct 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.8-2
- fix wallpaper symlinks in the KSplash theme

* Sun Oct 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.8-1
- use latest version of Solar wallpapers, includes 5:4 (1600x1280) image

* Sun Oct 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.7-1
- fix coordinates of KSplash animations not to segfault on small resolutions

* Sun Oct 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.1.6-1
- symlink all copies of wallpapers instead of hardlinking
- put wallpapers in directories with their actual resolution for KSplash
  (fixes ksplashx segfault)
- remove Fedora logo, add Requires: system-logos instead
- use bz2 instead of gz for the tarball

* Fri Oct 24 2008 Jaroslav Reznik <jreznik@redhat.com> 0.1.5-1
- KDM fixes
- normal/widescreen support for KSplash
- fixes default face path
- Plasma theme screenshot

* Thu Oct 23 2008 Jaroslav Reznik <jreznik@redhat.com> 0.1.4-1
- corrected licenses, README, COPYING and URL
- added default user face
- package description
- fixes KDM theme colors, positioning
- backgrounds theme

* Wed Oct 22 2008 Jaroslav Reznik <jreznik@redhat.com> 0.1.3-1
- generic Solar Comet splash screenshot
- fixes KDM theme layout problems

* Mon Oct 20 2008 Jaroslav Reznik <jreznik@redhat.com> 0.1.2-1
- final splash theme

* Sat Oct 18 2008 Rex Dieter <rdieter@fedoraproject.org> 0.1-1
- first try
