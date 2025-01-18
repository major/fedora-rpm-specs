Name:		constantine-kde-theme
Version:	12.1.0
Release:	29%{?dist}
Summary:	Constantine KDE Theme

License:	GPL-2.0-or-later AND CC-BY-SA-1.0

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	constantine-backgrounds-kde >= 12.0.0

Provides:	constantine-kdm-theme = %{version}-%{release}
Provides:	constantine-ksplash-theme = %{version}-%{release}

%if 0%{?fedora} == 12
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
%endif

# replace it later for el6
%if 0%{?rhel} == 6
Provides:   system-kde-theme = %{version}-%{release}
Provides:   system-kdm-theme = %{version}-%{release}
Provides:   system-ksplash-theme = %{version}-%{release}
%endif

%description
This is Constantine KDE Theme Artwork containing
KDM, KSplash, and wallpaper theme.


%prep
%setup -q


%build
# blank

%install
rm -rf %{buildroot}

# KDM
mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Constantine/ %{buildroot}/%{_kde4_appsdir}/kdm/themes/
(cd %{buildroot}/%{_kde4_appsdir}/kdm/themes/Constantine/
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-800x480.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1024x600.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1024x768.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1152x720.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1152x864.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1280x768.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1280x800.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1280x960.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1366x768.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1440x900.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1440x1080.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1600x1200.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1920x1080.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1920x1200.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1920x1440.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-2048x1536.png
# KDM falls back to this one if there's no match
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine.png
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
)

#mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/pics/users
#cp -rp kdm/users %{buildroot}/%{_kde4_appsdir}/kdm/pics

# KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Constantine/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/constantine/default/standard/constantine.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Constantine/2048x1536/constantine.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Constantine/1920x1200/
ln -s ../../../../../../backgrounds/constantine/default/wide/constantine.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Constantine/1920x1200/constantine.png

# end finally drag logo
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Constantine/2048x1536/logo.png


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/kdm/themes/Constantine/
%{_kde4_appsdir}/ksplash/Themes/Constantine/
#%{_kde4_appsdir}/kdm/pics/users/default_constantine.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Than Ngo <than@redhat.com> - 12.1.0-24
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 22 2010 Jaroslav Reznik <jreznik@redhat.com> 12.1.0-2
- Provides system-k*-theme only for F12

* Wed Oct 28 2009 Jaroslav Reznik <jreznik@redhat.com> 12.1.0-1
- Constantine Smile KSplash Theme
- Constantine Loadme! login screen Theme

* Wed Oct 07 2009 Than Ngo <than@redhat.com> - 12.0.0-2
- fix deps

* Thu Oct 01 2009 Rex Dieter <rdieter@fedoraproject.org> 12.0.0-1
- fix deps, depend only on (newer) constantine-backgrounds-kde

* Fri Sep 25 2009 Than Ngo <than@redhat.com> - 11.90.3-4
- rhel cleanup

* Sat Sep 12 2009 Rex Dieter <rdieter@fedoraproject.org> 11.90.3-3
- Provides: system-kde-theme system-kdm-theme system-ksplash-theme (f12)
- Provides: constantine-kdm-theme constantine-ksplash-theme

* Tue Sep 09 2009 Jaroslav Reznik <jreznik@redhat.com> 11.90.3-1
- fixes widescreen background

* Sun Sep 06 2009 Jaroslav Reznik <jreznik@redhat.com> 11.90.2-2
- more resolutions for KDM theme
- c-b-kde BR, bumped version

* Fri Sep 04 2009 Jaroslav Reznik <jreznik@redhat.com> 11.90.2-1
- KDM theme

* Thu Sep 03 2009 Jaroslav Reznik <jreznik@redhat.com> 11.90.1-1
- wallpapers moved to backgrounds package
- ksplash theme

* Thu Aug 06 2009 Jaroslav Reznik <jreznik@redhat.com> 11.90.0-1
- initial package
