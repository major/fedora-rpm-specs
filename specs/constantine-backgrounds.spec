Name:           constantine-backgrounds
Version:        12.1.1
Release:        29%{?dist}
Summary:        Constantine desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F12_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.lzma

BuildArch:      noarch

#BuildRequires:  inkscape
# for %%_kde4_* macros
BuildRequires:	kde4-filesystem
BuildRequires: make
Requires:       %{name}-single = %{version}-%{release}

%if 0%{?fedora} == 12
Provides: system-backgrounds
%endif

%description
This package contains desktop backgrounds for the Constantine theme.

%package        single
Summary:        Single screen images for Constantine Backgrounds
Conflicts:      %{name} < 12.0.0

%description    single
This package contains Single screen images for Constantine Backgrounds

%package        extras
Summary:        Extra Constantine Backgrounds

%description    extras
This package contains aditional desktop backgrounds for the Constantine theme.

%package        kde 
Summary:        Constantine Wallpapers for KDE 
Obsoletes:      constantine-kde-theme <= 11.90.0
%if 0%{?fedora} == 12
Provides:       system-backgrounds-kde
%endif

Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    kde 
This package contains KDE desktop wallpapers for the Constantine theme.

%package        extras-kde
Summary:        Extra Constantine Wallpapers for KDE 

Requires:       %{name}-extras = %{version}-%{release}

%description    extras-kde
This package contains aditional KDE desktop wallpapers for the Constantine theme.



%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc
%{_datadir}/backgrounds/constantine/default/standard.dual
%{_datadir}/backgrounds/constantine/default/wide.dual
%{_datadir}/backgrounds/constantine/default/normalish.dual
%{_datadir}/backgrounds/constantine/default/constantine.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-constantine.xml

%files single
%doc COPYING Credits
%dir %{_datadir}/backgrounds/constantine
%dir %{_datadir}/backgrounds/constantine/default
%{_datadir}/backgrounds/constantine/default/standard
%{_datadir}/backgrounds/constantine/default/wide
%{_datadir}/backgrounds/constantine/default/normalish

%files extras
%doc COPYING Credits
%dir %{_datadir}/backgrounds/constantine
%{_datadir}/backgrounds/constantine/extras
%{_datadir}/gnome-background-properties/desktop-backgrounds-constantine-extras.xml

%files kde
%{_kde4_datadir}/wallpapers/Constantine/

%files extras-kde
%{_kde4_datadir}/wallpapers/Constantine_mosaico/
%{_kde4_datadir}/wallpapers/Constantine_4flowers/
%{_kde4_datadir}/wallpapers/Constantine_constantine/
%{_kde4_datadir}/wallpapers/Constantine_pruebas/
%{_kde4_datadir}/wallpapers/Constantine_rose/
%{_kde4_datadir}/wallpapers/Constantine_rain/


%changelog
* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 12.1.1-29
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 12.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 18 2010 Martin Sourada <mso@fedoraproject.org> - 12.1.1-3
- Prepare for the comming of goddard-backgrounds into >= f13

* Wed Nov 18 2009 Jaroslav Reznik <jreznik@redhat.com> - 12.1.1-2
- Extras-kde subpackage requires -extras subpackage (rhbz #538354)

* Wed Nov 11 2009 Martin Sourada <mso@fedoraproject.org> - 12.1.1-1
- Rose wallpapers should be all jpgs (rhbz #533605)

* Tue Oct 27 2009 Martin Sourada <mso@fedoraproject.org> - 12.1.0-1
- New default, final extras selection, start building extras-kde subpackage

* Tue Oct 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 12.0.0-2
- Provides: system-backgrounds(-kde) for F-12+ (until something else does)

* Wed Sep 30 2009 Martin Sourada <mso@fedoraproject.org> - 12.0.0-1
- Update default and 4flowers, adds dual screen versions for default
  => split single screen versions into -single subpackage

* Sat Aug 22 2009 Martin Sourada <mso@feodraproject.org> - 11.90.2.1-1
- Extras slideshow bugfix respin

* Fri Aug 21 2009 Martin Sourada <mso@fedoraproject.org> - 11.90.2-2
- Forgot to BR: inkscape

* Fri Aug 21 2009 Martin Sourada <mso@fedoraproject.org> - 11.90.2-1
- First wallpaper respin

* Thu Aug 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 11.90.1-3
- Provides: system-backgrounds(-kde) (F-12 only)

* Tue Aug 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 11.90.1-2
- -kde subpkg, CamelCase themes (with feeling)

* Wed Aug 05 2009 Martin Sourada <mso@fedoraproject.org> - 11.90.1-1
- Move Constantin Statue from extras to default per frequent requests

* Tue Aug 04 2009 Martin Sourada <mso@fedoraproject.org> - 11.90.0-2
- We now have space on fedorahosted -> source tarball is available there

* Tue Aug 04 2009 Martin Sourada <mso@fedoraproject.org> - 11.90.0-1
- Initial RPM packaging
