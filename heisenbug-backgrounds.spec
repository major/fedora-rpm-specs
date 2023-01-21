%global bgname heisenbug
%global Bg_Name Heisenbug

Name:           %{bgname}-backgrounds
Version:        20.0.0
Release:        17%{?dist}
Summary:        Heisenbug desktop backgrounds

License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/F20_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the Heisenbug theme.
Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Heisenbug Backgrounds
License:        CC-BY-SA

%description    base
This package contains base images for Heisenbug Backgrounds.

# TOD animation will be enabled later
#~ %package        animated
#~ Summary:        Time of day images for Heisenbug Backgrounds
#~ Group:          Applications/Multimedia
#~
#~ Requires:       %{name}-base = %{version}-%{release}
#~
#~ %description    animated
#~ This package contains the time of day images for Heisenbug
#~ Backgrounds.

%package        kde
Summary:        Heisenbug Wallpapers for KDE

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Heisenbug
theme.

%package        gnome
Summary:        Heisenbug Wallpapers for Gnome and Cinnamon

Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpapers for the
Heisenbug theme.

%package        mate
Summary:        Heisenbug Wallpapers for Mate

Requires:       %{name}-base = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpapers for the Heisenbug
theme.

%package        xfce
Summary:        Heisenbug Wallpapers for XFCE4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Heisenbug
theme.

# Extras will be enabled later
%package        extras-base
Summary:        Base images for Heisenbug Extras Backrounds
License:        CC-BY and CC-BY-SA

%description    extras-base
This package contains base images for Heisenbug supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra Heisenbug Wallpapers for Gnome and Cinnamon

Requires:       %{name}-extras-base

%description    extras-gnome
This package contains Heisenbug supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra Heisenbug Wallpapers for Mate

Requires:       %{name}-extras-base

%description    extras-mate
This package contains Heisenbug supplemental wallpapers for Mate

%package        extras-kde
Summary:        Extra Heisenbug Wallpapers for KDE

Requires:       %{name}-extras-base

%description    extras-kde
This package contains Heisenbug supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra Heisenbug Wallpapers for XFCE

Requires:       %{name}-extras-base

%description    extras-xfce
This package contains Heisenbug supplemental wallpapers for XFCE


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files base
%doc CC-BY-SA-3.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/normalish
%{_datadir}/backgrounds/%{bgname}/default/standard
%{_datadir}/backgrounds/%{bgname}/default/wide
%{_datadir}/backgrounds/%{bgname}/default/tv-wide
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}.xml

#~ %files animated
#~ %dir %{_datadir}/backgrounds/%{bgname}/default-animated
#~ %{_datadir}/backgrounds/%{bgname}/default-animated/normalish
#~ %{_datadir}/backgrounds/%{bgname}/default-animated/standard
#~ %{_datadir}/backgrounds/%{bgname}/default-animated/wide
#~ %{_datadir}/backgrounds/%{bgname}/default-animated/%{bgname}.xml

%files kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%files extras-base
%doc CC-BY-SA-3.0 CC-BY-2.0 CC0-1.0 Attribution-Extras
%{_datadir}/backgrounds/%{bgname}/extras/*.jpg
%{_datadir}/backgrounds/%{bgname}/extras/*.png
%{_datadir}/backgrounds/%{bgname}/extras/%{bgname}-extras.xml

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}_*/

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg
%{_datadir}/xfce4/backdrops/*.png

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 17 2013 Martin Sourada <mso@fedoraproject.org> - 20.0.0-1
- Add extras

* Mon Sep 09 2013 Martin Sourada <mso@fedoraproject.org> - 19.90.0-1
- Initial rpm release
