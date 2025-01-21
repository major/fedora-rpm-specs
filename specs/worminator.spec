Name:           worminator
Version:        3.0R2.1
Release:        45%{?dist}
Summary:        Sidescrolling platform and shoot'em up action-game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/worminator/
Source0:        http://downloads.sourceforge.net/worminator/worminator-%{version}.tar.gz
Source1:        worminator.png
Source2:        worminator.desktop
Source3:        %{name}.appdata.xml
Patch0:         worminator-3.0R2.1-speed.patch
Patch1:         worminator-3.0R2.1-format-security.patch
Patch2:         worminator-3.0R2.1-c99.patch
BuildRequires:  gcc
BuildRequires:  allegro-devel desktop-file-utils libappstream-glib
Requires:       worminator-data >= 3.0R2.1-2, hicolor-icon-theme

%description
You play as The Worminator and fight your way through many levels of madness
and mayhem. Worminator features nine unique weapons, visible character damage,
full screen scrolling, sound and music, and much more!


%prep
%autosetup -p1
sed -i 's/\r//' ReadMe.txt


%build
gcc $RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations \
  -Wno-char-subscripts -DALLEGRO_FIX_ALIASES \
  -DDATADIR=\"%{_datadir}/%{name}/\" -o %{name} \
  Worminator.c `allegro-config --libs` -lm


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                           \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
        $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc ReadMe.txt changes.unix
%license license.txt license-change.txt
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/worminator.desktop
%{_datadir}/icons/hicolor/64x64/apps/worminator.png


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0R2.1-44
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Peter Fordham <peter.fordham@gmail.com> - 3.0R2.1-39
- Add a missing int for C99 compliance.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Hans de Goede <hdegoede@redhat.com> - 3.0R2.1-30
- Fix FTBFS (rhbz#1606823)
- Add appdata

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0R2.1-27
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0R2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Hans de Goede <hdegoede@redhat.com> 3.0R2.1-20
- Fix FTBFS (rhbz#1037387)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 3.0R2.1-17
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Hans de Goede <hdegoede@redhat.com> - 3.0R2.1-14
- Rebuild for new allegro-4.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 22 2010 Hans de Goede <hdegoede@redhat.com> 3.0R2.1-12
- Limit max framerate to 30 fps (fixes some sound issues)
- Fix FTBFS (#564902)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0R2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 3.0R2.1-9
- Fix Patch0:/%%patch mismatch.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0R2.1-8
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-7
- Rebuild for buildId

* Sun Aug 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-6
- Update License tag for new Licensing Guidelines compliance
- Fix invalid desktop file (fix building with latest desktop-file-utils)

* Tue Aug 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-5
- FE6 Rebuild

* Thu Jul  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-4
- Rebuild against new allegro to remove executable stack requirement caused
  by previous versions of allegro.

* Mon Apr 24 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-3
- Limit the framerate to 80 instead of trying to reach 160 fps,
  hopefully this fixes bug 188337.

* Tue Mar 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-2
- move worminator data dir from /usr/share/games to just /usr/share to match
  the games-SIG guidelines. Sorry about the somewhat large download for
  effectivly no changes, but I wanted to make this change before FC5 release.

* Sat Mar  4 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 3.0R2.1-1
- initial Fedora Extras package
- loosely based on the SRPM from Cru:
  http://naturidentisch.de/packages/fc4/worminator/
