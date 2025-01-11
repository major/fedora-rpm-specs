Name:           lovelock-backgrounds
Version:        14.91.1
Release:        28%{?dist}
Summary:        Lovelock desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F14_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}


%description
This package contains desktop backgrounds for the Lovelock theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Lovelock Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Lovelock Backgrounds

#%package        animated
#Summary:        Images for Time of Day animation for Lovelock Backgrounds
#Group:          Applications/Multimedia
#License:        CC-BY-SA-4.0
#Requires:       %{name}-single = %{version}-%{release}

#%description    animated
#This package contains single screen images for Time of Day animation for 
#Lovelock Backgrounds

#%package        animated-gnome
#Summary:        Time of Day animation for Lovelock Backgrounds for Gnome
#Group:          Applications/Multimedia
#License:        CC-BY-SA-4.0
#Requires:       %{name}-animated = %{version}-%{release}

#%description    animated-gnome
#This package contains Time of Day animated wallpaper for Gnome dekstop for
#the Lovelock theme.

%package        kde 
Summary:        Lovelock Wallpapers for KDE 

Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    kde 
This package contains KDE desktop wallpapers for the Lovelock theme.

%package        gnome 
Summary:        Lovelock Wallpapers for Gnome 

Requires:       %{name}-single = %{version}-%{release} 

%description    gnome 
This package contains Gnome desktop wallpapers for the Lovelock theme.

%package        xfce 
Summary:        Lovelock Wallpapers for XFCE4 

Requires:       %{name}-single = %{version}-%{release} 
Requires:       xfdesktop

%description    xfce 
This package contains XFCE4 desktop wallpapers for the Lovelock theme.

%package        stripes-single
Summary:        Single screen images for Lovelock Stripes Backgrounds
License:        CC-BY-SA-4.0

%description    stripes-single
This package contains single screen images for Lovelock Stripes Backgrounds

#%package        stripes-animated
#Summary:        Images for Time of Day animation for Lovelock Stripes Backgrounds
#Group:          Applications/Multimedia
#Requires:       %{name}-stripes-single = %{version}-%{release}

#%description    stripes-animated
#This package contains single screen images for Time of Day animation for 
#Lovelock Stripes Backgrounds

#%package        stripes-animated-gnome
#Summary:        Time of Day animation for Lovelock Stripes Backgrounds for Gnome
#Group:          Applications/Multimedia
#Requires:       %{name}-stripes-animated = %{version}-%{release}

#%description    stripes-animated-gnome
#This package contains Time of Day animated wallpaper for Gnome dekstop for
#the Lovelock Stripes theme.

%package        stripes-kde 
Summary:        Lovelock Stripes Wallpapers for KDE 

Requires:       %{name}-stripes-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    stripes-kde 
This package contains KDE desktop wallpapers for the Lovelock Stripes theme.

%package        stripes-gnome 
Summary:        Lovelock Stripes Wallpapers for Gnome 

Requires:       %{name}-stripes-single = %{version}-%{release} 

%description    stripes-gnome 
This package contains Gnome desktop wallpapers for the Lovelock Stripes
theme.

%package        stripes-xfce 
Summary:        Lovelock Stripes Wallpapers for XFCE4 

Requires:       %{name}-stripes-single = %{version}-%{release} 
Requires:       xfdesktop

%description    stripes-xfce 
This package contains XFCE4 desktop wallpapers for the Lovelock Stripes
theme.


#%package        extras-single
#Summary:        Single screen images for Lovelock Extras Backrounds
#Group:          Applications/Multimedia
#License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

#%description    extras-single
#This package contains single screen images for Lovelock supplemental wallpapers

#%package        extras-gnome
#Summary:        Extra Lovelock Wallpapers for Gnome
#Group:          Applications/Multimedia

#Requires:       %{name}-extras-single

#%description    extras-gnome
#This package contains Lovelock supplemental wallpapers for Gnome

#%package        extras-kde
#Summary:        Extra Lovelock Wallpapers for KDE
#Group:          Applications/Multimedia

#Requires:       %{name}-extras-single

#%description    extras-kde
#This package contains Lovelock supplemental wallpapers for Gnome


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
%dir %{_datadir}/backgrounds/lovelock
%dir %{_datadir}/backgrounds/lovelock/default
%{_datadir}/backgrounds/lovelock/default/normalish
%{_datadir}/backgrounds/lovelock/default/standard
%{_datadir}/backgrounds/lovelock/default/wide

#%files animated
#%defattr(-,root,root,-)
#%dir %{_datadir}/backgrounds/lovelock/default-tod
#%{_datadir}/backgrounds/lovelock/default-tod/normalish
#%{_datadir}/backgrounds/lovelock/default-tod/standard
#%{_datadir}/backgrounds/lovelock/default-tod/wide

#%files animated-gnome
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/lovelock/default-tod/lovelock.xml
#%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock-animated.xml

%files kde
%{_kde4_datadir}/wallpapers/Lovelock/

%files gnome
%{_datadir}/backgrounds/lovelock/default/lovelock.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock.xml

%files xfce
%{_datadir}/xfce4/backdrops/lovelock.png

%files stripes-single
%doc CC-BY-SA?3.0 Attribution-Stripes
%dir %{_datadir}/backgrounds/lovelock
%dir %{_datadir}/backgrounds/lovelock/default-stripes
%{_datadir}/backgrounds/lovelock/default-stripes/normalish
%{_datadir}/backgrounds/lovelock/default-stripes/standard
%{_datadir}/backgrounds/lovelock/default-stripes/wide

#%files stripes-animated
#%defattr(-,root,root,-)
#%dir %{_datadir}/backgrounds/lovelock/default-stripes-tod
#%{_datadir}/backgrounds/lovelock/default-stripes-tod/normalish
#%{_datadir}/backgrounds/lovelock/default-stripes-tod/standard
#%{_datadir}/backgrounds/lovelock/default-stripes-tod/wide

#%files stripes-animated-gnome
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/lovelock/default-stripes-tod/lovelock.xml
#%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock-stripes-animated.xml

%files stripes-kde
%{_kde4_datadir}/wallpapers/Lovelock_Stripes/

%files stripes-gnome
%{_datadir}/backgrounds/lovelock/default-stripes/lovelock.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock-stripes.xml

%files stripes-xfce
%{_datadir}/xfce4/backdrops/lovelock-stripes.png

#%files extras-single
#%doc CC-BY\ 2.0 CC-BY-SA\ 2.0 CC-BY-SA\ 3.0 Attribution
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/lovelock/extras/*.jpg

#%files extras-gnome
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/lovelock/extras/lovelock-extras.xml
#%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock-extras.xml

#%files extras-kde
#%defattr(-,root,root,-)
#%{_kde4_datadir}/wallpapers/Lovelock_*/


%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 14.91.1-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.91.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 21 2013 Martin Sourada <mso@fedoraproject.org> - 14.91.1-6
- Fix a mistake in %%changelog

* Thu Feb 21 2013 Martin Sourada <mso@fedoraproject.org> - 14.91.1-5
- Fix build

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 01 2011 Martin Sourada <mso@fedoraproject.org> - 14.91.1-1
- New release
  - Includes "Stripes" version of the wallpaper
    - Apropriate subpackages created

* Tue Mar 22 2011 Martin Sourada <mso@fedoraproject.org> - 14.91.0-1
- New release, includes beta artwork

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.90.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Martin Sourada <mso@fedoraproject.org> - 14.90.1-2
- Drop system-backgrounds* virtual provides. They're now provided by
  desktop-backgrounds-*.

* Fri Feb 04 2011 Martin Sourada <mso@fedoraproject.org> - 14.90.1-1
- New release
  - provides symlinks for use by XFCE4 (put into -xfce subpacakge)

* Wed Feb 02 2011 Martin Sourada <mso@fedoraproject.org> - 14.90.0-1
- Initial backgrounds package for F15 Lovelock

