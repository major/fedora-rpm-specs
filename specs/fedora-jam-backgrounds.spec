Name:           fedora-jam-backgrounds
Version:        2.0.0
Release:        13%{?dist}
Summary:        Fedora Jam desktop backgrounds

# Automatically converted from old format: CC0 - review is highly recommended.
License:        CC0-1.0
URL:            https://fedoraproject.org/wiki/Fedora_jam
Source0:        https://pagure.io/%name/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}


%description
This package contains desktop backgrounds for the Fedora Jam theme.
Pulls in both Gnome and KDE themes.

%package        single
Summary:        Single screen images for Fedora Jam Backgrounds

%description    single
This package contains single screen images for Fedora Jam
Backgrounds.

%package        kde
Summary:        Fedora Jam Wallpapers for KDE

Requires:       %{name}-single = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Fedora Jam
theme.

%package        gnome
Summary:        Fedora Jam Wallpapers for Gnome

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Fedora Jam
theme.

%package        xfce
Summary:        Fedora Jam Wallpapers for XFCE4

Requires:       %{name}-single = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Fedora Jam
theme.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files single
%doc CC0* Attribution 
#Attribution
%dir %{_datadir}/backgrounds/fedora-jam
%dir %{_datadir}/backgrounds/fedora-jam/default
%{_datadir}/backgrounds/fedora-jam/default/normalish
%{_datadir}/backgrounds/fedora-jam/default/standard
%{_datadir}/backgrounds/fedora-jam/default/wide

%files kde
%{_kde4_datadir}/wallpapers/Fedora_Jam/

%files gnome
%{_datadir}/backgrounds/fedora-jam/default/fedora-jam.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-fedora-jam.xml

%files xfce
%{_datadir}/xfce4/backdrops/fedora-jam.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Adam Williamson <awilliam@redhat.com> - 2.0.0-4
- Rebuild for unretirement, for F35 and F36

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.0-1
- New background

* Fri Feb 21 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.0.1-0.15
- Project moved to pagure

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.14.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.13.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.12.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.11.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.10.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.9.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.8.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.7.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.6.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.5.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.4.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-0.3.git8db10f1
- Correct space in %%doc

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.git8db10f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 11 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.1-0.1.git8db10f1
- New 1.0.1

* Wed Oct 31 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.0-0.2.git1e1137e
- Add Attribution

* Wed Oct 31 2012 Brendan Jones <brendan.jones.it@gmail.com> 1.0.0-0.1.git1e1137e
- New release

* Mon Jul 30 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-2.2.git569af19fa
- Remove License line for single package

* Mon Jul 30 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-2.1.git569af19fa
- add tarball script
- remove clean sections

* Mon Jul 30 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-2
- Remove clean sections

* Sun Jul 29 2012 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-1
- Create package template
