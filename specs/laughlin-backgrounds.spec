Name:           laughlin-backgrounds
Version:        14.1.0
Release:        30%{?dist}
Summary:        Laughlin desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F14_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.lzma

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}


%description
This package contains desktop backgrounds for the Laughlin theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Laughlin Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Laughlin Backgrounds

%package        animated
Summary:        Images for Time of Day animation for Laughlin Backgrounds
License:        CC-BY-SA-4.0
Requires:       %{name}-single = %{version}-%{release}

%description    animated
This package contains single screen images for Time of Day animation for 
Laughlin Backgrounds

%package        animated-gnome
Summary:        Time of Day animation for Laughlin Backgrounds for Gnome
License:        CC-BY-SA-4.0
Requires:       %{name}-animated = %{version}-%{release}

%description    animated-gnome
This package contains Time of Day animated wallpaper for Gnome dekstop for
the Laughlin theme.

%package        kde 
Summary:        Laughlin Wallpapers for KDE 
%if 0%{?fedora} == 14
Provides:       system-backgrounds-kde = %{version}-%{release}
%endif

Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    kde 
This package contains KDE desktop wallpapers for the Laughlin theme.

%package        gnome 
Summary:        Laughlin Wallpapers for Gnome 

Requires:       %{name}-single = %{version}-%{release} 
%if 0%{?fedora} == 14
Provides:        system-backgrounds-gnome = %{version}-%{release}
%endif

%description    gnome 
This package contains Gnome desktop wallpapers for the Laughlin theme.

%package        extras-single
Summary:        Single screen images for Laughlin Extras Backrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-single
This package contains single screen images for Laughlin supplemental wallpapers

%package        extras-gnome
Summary:        Extra Laughlin Wallpapers for Gnome
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-gnome
This package contains Laughlin supplemental wallpapers for Gnome

%package        extras-kde
Summary:        Extra Laughlin Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-kde
This package contains Laughlin supplemental wallpapers for Gnome


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
#There'll be also dual wallpapers in dual subpackage in the future, hence the 
# %%dir ownership is treated separately
%dir %{_datadir}/backgrounds/laughlin
%dir %{_datadir}/backgrounds/laughlin/default
%{_datadir}/backgrounds/laughlin/default/normalish
%{_datadir}/backgrounds/laughlin/default/standard
%{_datadir}/backgrounds/laughlin/default/wide

%files animated
%dir %{_datadir}/backgrounds/laughlin/default-tod
%{_datadir}/backgrounds/laughlin/default-tod/normalish
%{_datadir}/backgrounds/laughlin/default-tod/standard
%{_datadir}/backgrounds/laughlin/default-tod/wide

%files animated-gnome
%{_datadir}/backgrounds/laughlin/default-tod/laughlin.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-laughlin-animated.xml

%files kde
%{_kde4_datadir}/wallpapers/Laughlin/

%files gnome
%{_datadir}/backgrounds/laughlin/default/laughlin.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-laughlin.xml

%files extras-single
%doc CC-BY?2.0 CC-BY-SA?2.0 CC-BY-SA?3.0 Attribution
%defattr(-,root,root,-)
%{_datadir}/backgrounds/laughlin/extras/*.jpg

%files extras-gnome
%{_datadir}/backgrounds/laughlin/extras/laughlin-extras.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-laughlin-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/Laughlin_*/


%changelog
* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 14.1.0-30
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 21 2013 Martin Sourada <mso@fedoraproject.org> - 14.1.0-8
- Fix mistake in %%changelog

* Thu Feb 21 2013 Martin Sourada <mso@fedoraproject.org> - 14.1.0-7
- Fix build

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Martin Sourada <mso@fedoraproject.org> - 14.1.0-2
- New default wallpaper for F15

* Sun Oct 17 2010 Martin Sourada <mso@fedoraproject.org> - 14.1.0-1
- New upstream release
  - Split animated backgrounds out of main gnome package (animated background 
    are too big for some spins)
  - Fix a typo in animated wallpaper xml (it should start at 7am not 6am)
  

* Wed Oct 13 2010 Martin Sourada <mso@fedoraproject.org> - 14.0.0-1
- New upstream release
  - Adds Time of Day wallpaper for Gnome
  - Fix some attributions
  - Fixes 634328

* Tue Sep 14 2010 Martin Sourada <mso@fedoraproject.org> - 13.92.0-1
- New upstream release
  - Add extras wallpapers

* Tue Jul 27 2010 Martin Sourada <mso@fedoraproject.org> - 13.91.0-1
- Initial backgrounds package for F14 Laughlin

