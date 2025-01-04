%global relnum 26
%global Bg_Name F%{relnum}
%global bgname %(t="%{Bg_Name}";echo ${t,,})

# Enable Extras
%global with_extras 1

Name:           %{bgname}-backgrounds
Version:        %{relnum}.2.7
Release:        19%{?dist}
Summary:        Fedora %{relnum} default desktop background

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F%{relnum}_Artwork
Source0:        https://releases.pagure.org/design/%{name}-%{version}.tar.xz
# Plasma desktoptheme
Source1:        metadata.desktop

BuildArch:      noarch

BuildRequires: make

Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the Fedora %{relnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Fedora %{relnum} default background
License:        CC-BY-SA-4.0

%description    base
This package contains base images for Fedora %{relnum} default background.

%package        animated
Summary:        Time of day images for Fedora %{relnum} backgrounds

Requires:       %{name}-base = %{version}-%{release}
Recommends:	%{name}-gnome = %{version}-%{release}

%description    animated
This package contains the time of day images for Fedora %{relnum} 
Backgrounds.

%package        kde
Summary:        Fedora %{relnum} default wallpaper for KDE

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpaper for the Fedora %{relnum}
default theme.

%package        gnome
Summary:        Fedora %{relnum} default wallpaper for Gnome and Cinnamon

Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Fedora %{relnum} default theme.

%package        mate
Summary:        Fedora %{relnum} default wallpaper for Mate

Requires:       %{name}-base = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpaper for the Fedora %{relnum}
default theme.

%package        xfce
Summary:        Fedora %{relnum} default background for XFCE4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop background for the Fedora %{relnum}
default theme.

%if %{with_extras}
%package        extras-base
Summary:        Base images for F%{relnum} Extras Backrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-base
This package contains base images for F%{relnum} supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra F%{relnum} Wallpapers for Gnome and Cinnamon
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base = %{version}-%{release}

%description    extras-gnome
This package contains F%{relnum} supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra F%{relnum} Wallpapers for Mate
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base = %{version}-%{release}

%description    extras-mate
This package contains F%{relnum} supplemental wallpapers for Mate

%package        extras-kde
Summary:        Extra F%{relnum} Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base = %{version}-%{release}

%description    extras-kde
This package contains F%{relnum} supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra F%{relnum} Wallpapers for XFCE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base = %{version}-%{release}

%description    extras-xfce
This package contains F%{relnum} supplemental wallpapers for XFCE
%endif

%prep
%autosetup -n %{name}


%build
%make_build


%install
%make_install

install -D -p -m644 %{SOURCE1} \
%{buildroot}%{_datadir}/plasma/desktoptheme/%{Bg_Name}/metadata.desktop

%files
%doc

%files base
%license CC-BY-SA-4.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/normalish
%{_datadir}/backgrounds/%{bgname}/default/standard
%{_datadir}/backgrounds/%{bgname}/default/wide
%{_datadir}/backgrounds/%{bgname}/default/tv-wide
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}.xml

%files animated
%dir %{_datadir}/backgrounds/%{bgname}/default-animated
%{_datadir}/backgrounds/%{bgname}/default-animated/normalish
%{_datadir}/backgrounds/%{bgname}/default-animated/standard
%{_datadir}/backgrounds/%{bgname}/default-animated/wide
%{_datadir}/backgrounds/%{bgname}/default-animated/tv-wide
%{_datadir}/backgrounds/%{bgname}/default-animated/%{bgname}.xml

%files kde
%{_datadir}/wallpapers/%{Bg_Name}/
%dir %{_datadir}/plasma/
%dir %{_datadir}/plasma/desktoptheme/
%{_datadir}/plasma/desktoptheme/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml
%{_datadir}/gnome-background-properties/%{bgname}-animated.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml
%{_datadir}/mate-background-properties/%{bgname}-animated.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%if %{with_extras}
%files extras-base
%license CC-BY-SA-4.0 CC-BY-4.0 CC0-1.0 Attribution-Extras
%{_datadir}/backgrounds/%{bgname}/extras/*.jpg
%{_datadir}/backgrounds/%{bgname}/extras/*.png
%{_datadir}/backgrounds/%{bgname}/extras/%{bgname}-extras.xml

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-kde
%{_datadir}/wallpapers/%{Bg_Name}_*/

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg
%{_datadir}/xfce4/backdrops/*.png
%endif

%changelog
* Mon Dec 02 2024 David Auer <dreua@posteo.de> - 26.2.7-19
- Fix build on f40+

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 26.2.7-18
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.7-2
- Add weak dependency for animated default wallpaper

* Thu Jul 27 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.7-1
- Upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.6-1
- Upstream release with further improved jpg compression

* Mon Jul 03 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.5-1
- Upstream release restoring png default wallpaper

* Sat Jul 01 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.4-1
- Upstream release fixing missing default wallpaper

* Sat Jul 01 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.3-1
- Upstream release with default wallpaper in jpg format

* Thu May 18 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.2-1
- Upstream release with improved animated default wallpaper

* Mon May 08 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.1-1
- Bump upstream release due to corrupted upload

* Sat May 06 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.0-2
- Enable animated default wallpaper

* Fri May 05 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.2.0-1
- Upstream release with enabled animated default wallpaper

* Thu Apr 06 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.1.0-1
- Upstream release with selected supplemental wallpapers

* Fri Mar 31 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.0.2-1
- Enable extras with dark blue wallpaper as placeholder (#1437642)

* Sat Mar 25 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.0.1-1
- Upstream release fixing wrong version for Gnome desktop

* Tue Mar 21 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 26.0.0-1
- Initial release
