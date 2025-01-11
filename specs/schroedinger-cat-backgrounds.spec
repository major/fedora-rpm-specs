Name:           schroedinger-cat-backgrounds
Version:        18.91.0
Release:        22%{?dist}
Summary:        Schrödinger's Cat desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F19_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires: make
BuildRequires:  kde4-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the Schrödinger's Cat theme.
Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Schrödinger's Cat Backgrounds
License:        CC-BY-SA-4.0

%description    base
This package contains base images for Schrödinger's Cat Backgrounds.

%package        animated
Summary:        Time of day images for Schrödinger's Cat Backgrounds

Requires:       %{name}-base = %{version}-%{release}

%description    animated
This package contains the time of day images for Schrödinger's Cat
Backgrounds.

%package        kde
Summary:        Schrödinger's Cat Wallpapers for KDE

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Schrödinger's Cat
theme.

%package        gnome
Summary:        Schrödinger's Cat Wallpapers for Gnome and Cinnamon

Requires:       %{name}-animated = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpapers for the
Schrödinger's Cat theme.

%package        mate
Summary:        Schrödinger's Cat Wallpapers for Mate

Requires:       %{name}-animated = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpapers for the Schrödinger's Cat
theme.

%package        xfce
Summary:        Schrödinger's Cat Wallpapers for XFCE4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Schrödinger's Cat
theme.

%package        extras-base
Summary:        Base images for Schrödinger's Cat Extras Backrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-base
This package contains base images for Schrödinger's Cat supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra Schrödinger's Cat Wallpapers for Gnome and Cinnamon
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base

%description    extras-gnome
This package contains Schrödinger's Cat supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra Schrödinger's Cat Wallpapers for Mate
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base

%description    extras-mate
This package contains Schrödinger's Cat supplemental wallpapers for Mate

%package        extras-kde
Summary:        Extra Schrödinger's Cat Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base

%description    extras-kde
This package contains Schrödinger's Cat supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra Schrödinger's Cat Wallpapers for XFCE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base

%description    extras-xfce
This package contains Schrödinger's Cat supplemental wallpapers for XFCE


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
%dir %{_datadir}/backgrounds/schroedinger-cat
%dir %{_datadir}/backgrounds/schroedinger-cat/default
%{_datadir}/backgrounds/schroedinger-cat/default/normalish
%{_datadir}/backgrounds/schroedinger-cat/default/standard
%{_datadir}/backgrounds/schroedinger-cat/default/wide
%{_datadir}/backgrounds/schroedinger-cat/default/schroedinger-cat.xml

%files animated
%dir %{_datadir}/backgrounds/schroedinger-cat/default-animated
%{_datadir}/backgrounds/schroedinger-cat/default-animated/normalish
%{_datadir}/backgrounds/schroedinger-cat/default-animated/standard
%{_datadir}/backgrounds/schroedinger-cat/default-animated/wide
%{_datadir}/backgrounds/schroedinger-cat/default-animated/schroedinger-cat.xml

%files kde
%{_kde4_datadir}/wallpapers/Schroedinger_Cat/

%files gnome
%{_datadir}/gnome-background-properties/schroedinger-cat-animated.xml

%files mate
%{_datadir}/mate-background-properties/schroedinger-cat-animated.xml

%files xfce
%{_datadir}/xfce4/backdrops/schroedinger-cat.jpg

%files extras-base
%doc CC-BY-SA-3.0 CC-BY-3.0 Attribution-Extras
%{_datadir}/backgrounds/schroedinger-cat/extras/*.jpg
%{_datadir}/backgrounds/schroedinger-cat/extras/*.png
%{_datadir}/backgrounds/schroedinger-cat/extras/schroedinger-cat-extras.xml

%files extras-gnome
%{_datadir}/gnome-background-properties/schroedinger-cat-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/Schroedinger_Cat_*/

%files extras-mate
%{_datadir}/mate-background-properties/schroedinger-cat-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg
%{_datadir}/xfce4/backdrops/*.png

%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 18.91.0-22
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 18.91.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.91.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.91.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.91.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Martin Sourada <mso@fedoraproject.org> - 18.91.0-1
- New release. 
  - Adds supplemental wallpapers.
  - Switches non-animated default from night to dawn (rhbz 962952)

* Sun Mar 03 2013 Martin Sourada <mso@fedoraproject.org> - 18.90.0-1
- Initial rpm release
