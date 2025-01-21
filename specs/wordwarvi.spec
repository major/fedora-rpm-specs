%global commit 6beed311c2ecb3f9662f35ecc06948bd89ed9455
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wordwarvi
Version:        1.1
Release:        22.git%{shortcommit}%{?dist}
Summary:        Side-scrolling shoot 'em up '80s style arcade game
# Automatically converted from old format: GPLv2+ and CC-BY and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-CC-BY-SA
URL:            https://smcameron.github.io/wordwarvi/
# The 1.1 release never got a tag in git, so we use the commit-id
Source0:        https://github.com/smcameron/wordwarvi/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gtk2-devel portaudio-devel libvorbis-devel
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
Word War vi is your basic side-scrolling shoot 'em up '80s style arcade game.
You pilot your "vi"per craft through core memory, rescuing lost .swp files,
avoiding OS defenses, and wiping out those memory hogging emacs processes.
When all the lost .swp files are rescued, head for the socket which will take
you to the next node in the cluster.

Note: Obviously, emacs is a fine editor and this is all very tongue in cheek,
so don't be getting all bent out of shape because you like emacs better than
vi, mmm-kay?


%prep
%setup -qn %{name}-%{commit}


%build
make %{?_smp_mflags} PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS"


%install
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS COPYING README changelog.txt sounds/Attribution.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-21.git6beed31
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-19.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-6.git6beed31
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2.git6beed31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Hans de Goede <hdegoede@redhat.com> - 1.1-1.git6beed31
- Upstream has moved to github
- New upstream release 1.1
- Add appdata

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.25-8
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.25-5
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Hans de Goede <hdegoede@redhat.com> 0.25-1
- New upstream release 0.25

* Tue Dec 16 2008 Hans de Goede <hdegoede@redhat.com> 0.24-1
- New upstream release 0.24
- Drop upstreamed patches

* Mon Dec  8 2008 Hans de Goede <hdegoede@redhat.com> 0.23-2
- Fix wordwarvi crashing when used with a portaudio which has been patched to
  work with pulseaudio (rh 445644)

* Sun Nov 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.23-1
- New upstream release 0.23 (The xmas release)

* Thu Jul 31 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.21-1
- New upstream release 0.21

* Sun Jul 20 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.20-1
- New upstream release 0.20

* Wed Jul 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.19-1
- New upstream release 0.19

* Mon Jul  7 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.18-1
- New upstream release 0.18

* Mon Jun 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.17-1
- New upstream release 0.17

* Mon Jun 23 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.16-1
- New upstream release 0.16

* Mon Jun 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.15-1
- New upstream release 0.15

* Mon Jun  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.13-1
- New upstream release 0.13

* Mon May 26 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.12-1
- New upstream release 0.12
- Drop upstream merged patches

* Wed May 21 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.11-1
- New upstream release 0.11

* Mon May  5 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.09-1
- New upstream release 0.09

* Sat May  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.08-1
- New upstream release 0.08

* Thu May  1 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.07-1
- New upstream release 0.07
- Drop upstream merged patches

* Mon Apr 14 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.06-1
- New upstream release 0.06
- Drop upstream merged patches

* Fri Apr 11 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.05-1
- Initial Fedora Extras package
