Name:           verne-backgrounds
Version:        15.92.1
Release:        27%{?dist}
Summary:        Verne desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F16_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires: make
BuildRequires:  kde4-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}


%description
This package contains desktop backgrounds for the Verne theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Verne Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Verne Backgrounds

#%package        animated
#Summary:        Images for Time of Day animation for Verne Backgrounds
#Group:          Applications/Multimedia
#Requires:       %{name}-single = %{version}-%{release}

#%description    animated
#This package contains single screen images for Time of Day animation for
#Verne Backgrounds

#%package        animated-gnome
#Summary:        Time of Day animation for Verne Backgrounds for Gnome
#Group:          Applications/Multimedia
#Requires:       %{name}-animated = %{version}-%{release}

#%description    animated-gnome
#This package contains Time of Day animated wallpaper for Gnome dekstop for
#the Verne theme.

%package        kde
Summary:        Verne Wallpapers for KDE

Requires:       %{name}-single = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Verne theme.

%package        gnome
Summary:        Verne Wallpapers for Gnome

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Verne theme.

%package        xfce
Summary:        Verne Wallpapers for XFCE4

Requires:       %{name}-single = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Verne theme.

%package        extras-single
Summary:        Single screen images for Verne Extras Backrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-single
This package contains single screen images for Verne supplemental wallpapers

%package        extras-gnome
Summary:        Extra Verne Wallpapers for Gnome
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-gnome
This package contains Verne supplemental wallpapers for Gnome

%package        extras-kde
Summary:        Extra Verne Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-kde
This package contains Verne supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra Verne Wallpapers for XFCE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-xfce
This package contains Verne supplemental wallpapers for XFCE

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc

%files single
%doc CC-BY-SA?3.0 Attribution
%dir %{_datadir}/backgrounds/verne
%dir %{_datadir}/backgrounds/verne/default
%{_datadir}/backgrounds/verne/default/normalish
%{_datadir}/backgrounds/verne/default/standard
%{_datadir}/backgrounds/verne/default/wide

#%files animated
#%defattr(-,root,root,-)
#%dir %{_datadir}/backgrounds/verne/default-tod
#%{_datadir}/backgrounds/verne/default-tod/normalish
#%{_datadir}/backgrounds/verne/default-tod/standard
#%{_datadir}/backgrounds/verne/default-tod/wide

#%files animated-gnome
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/verne/default-tod/verne.xml
#%{_datadir}/gnome-background-properties/desktop-backgrounds-verne-animated.xml

%files kde
%{_kde4_datadir}/wallpapers/Verne/

%files gnome
%{_datadir}/backgrounds/verne/default/verne.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-verne.xml

%files xfce
%{_datadir}/xfce4/backdrops/verne.png

%files extras-single
%doc CC-BY-SA?3.0 Attribution-Extras
%defattr(-,root,root,-)
%{_datadir}/backgrounds/verne/extras/*.jpg

%files extras-gnome
%{_datadir}/backgrounds/verne/extras/verne-extras.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-verne-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/Verne_*/

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 15.92.1-27
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.92.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.92.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.92.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.92.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 21 2013 Martin Sourada <mso@fedoraproject.org> - 15.92.1-6
- Fix a mistake in %%changelog.

* Thu Feb 21 2013 Martin Sourada <mso@fedoraproject.org> - 15.92.1-5
- Fix build

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.92.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.92.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.92.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Martin Sourada <mso@fedoraproject.org> - 15.92.1-1
- Update default wallpaper to beta version

* Mon Sep 05 2011 Martin Sourada <mso@fedoraproject.org> - 15.92.0-1
- Update to newest version, include supplemental wallpapers

* Thu Jul 28 2011 Martin Sourada <mso@fedoraproject.org> - 15.91.0-1
- Initial backgrounds package for F16 Verne

