Name:           beefy-miracle-backgrounds
Version:        16.91.0
Release:        28%{?dist}
Summary:        Beefy Miracle desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F17_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}


%description
This package contains desktop backgrounds for the Beefy Miracle theme.
Pulls in both Gnome and KDE themes.

%package        single
Summary:        Single screen images for Beefy Miracle Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Beefy Miracle
Backgrounds.

%package        kde
Summary:        Beefy Miracle Wallpapers for KDE

Requires:       %{name}-single = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Beefy Miracle
theme.

%package        gnome
Summary:        Beefy Miracle Wallpapers for Gnome

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Beefy Miracle
theme.

%package        xfce
Summary:        Beefy Miracle Wallpapers for XFCE4

Requires:       %{name}-single = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Beefy Miracle
theme.

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
%dir %{_datadir}/backgrounds/beefy-miracle
%dir %{_datadir}/backgrounds/beefy-miracle/default
%{_datadir}/backgrounds/beefy-miracle/default/normalish
%{_datadir}/backgrounds/beefy-miracle/default/standard
%{_datadir}/backgrounds/beefy-miracle/default/wide

%files kde
%{_kde4_datadir}/wallpapers/Beefy_Miracle/

%files gnome
%{_datadir}/backgrounds/beefy-miracle/default/beefy-miracle.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-beefy-miracle.xml

%files xfce
%{_datadir}/xfce4/backdrops/beefy-miracle.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 16.91.0-27
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16.91.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 21 2013 Martin Sourada <mso@fedoraproject.org> - 16.91.0-5
- Fix build

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.91.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Martin Sourada <mso@fedoraproject.org> - 16.91.0-2
- Fix a typo.
- Remove buildroot and defattr, not needed since rpm 4.4

* Wed Feb 01 2012 Martin Sourada <mso@fedoraproject.org> - 16.91.0-1
- Update to Alpha release.

* Sun Jan 29 2012 Martin Sourada <mso@fedoraproject.org> - 16.90.0-1
- First release (pre-alpha wallpaper)
