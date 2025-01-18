%define prever pre2

Name:           atomorun
Version:        1.1
Release:        0.45.%{prever}%{?dist}
Summary:        Jump & Run game where you have to flee an exploding nuclear bomb
License:        GPL-1.0-or-later
URL:            http://atomorun.whosme.de/index.php
# the file seems to be gone from upstreams server so no URL
Source0:        %{name}-%{version}_%{prever}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         atomorun-1.1-missing-protos.patch
Patch1:         atomorun-1.1-fcommon-fix.patch
Patch2:         atomorun-1.1-warnings-fix.patch
Patch3:         atomorun-1.1-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  SDL_mixer-devel SDL_image-devel libtiff-devel libvorbis-devel
BuildRequires:  alsa-lib-devel desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Atomorun is a OpenGL Jump&Run game where you have to flee an exploding
nuclear bomb.


%prep
%autosetup -p1 -n %{name}-%{version}_%{prever}


%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign"
%configure
make %{?_smp_mflags}


%install
%make_install
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps/atomorun_winicon.ico
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pixmaps/%{name}_icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.45.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.44.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun  17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-0.43.pre2
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.42.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.41.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.40.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.39.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec  7 2022 Peter Fordham <peter.fordham@gmail.com> - 1.1-0.38.pre2
- Port configure script to C99

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.37.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.36.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.35.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.34.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.33.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar  4 2020 Hans de Goede <hdegoede@redhat.com> - 1.1-0.32.pre2
- Replace 128x128 icon with a better version
- Restore original 48x48 icon for cases where we need a lower res icon

* Sat Feb 15 2020 Hans de Goede <hdegoede@redhat.com> - 1.1-0.31.pre2
- Fix FTBFS (rhbz#1799176)
- Replace icon with 128x128 pixel version
- Add appdata

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.30.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.29.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.28.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.27.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.26.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-0.25.pre2
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.24.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.23.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.22.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.21.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.20.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.19.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.18.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.17.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 1.1-0.16.pre2
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Mon Apr 29 2013 Hans de Goede <hdegoede@redhat.com> - 1.1-0.15.pre2
- run autoreconf for aarch64 support (rhbz#925046)

* Sun Feb 10 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.1-0.14.pre2
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.13.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.12.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.11.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.10.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.9.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-0.8.pre2
- Fix missing prototype compiler warnings

* Mon Feb 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-0.7.pre2
- Use included png version of icon instead of running convert on .ico file

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1-0.6.pre2
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-0.5.pre2
- Fix broken Source0 URL

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-0.4.pre2
- Update License tag for new Licensing Guidelines compliance

* Sat Mar 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-0.3.pre2
- Fixup .desktop file categories for games-menus usage

* Sun Nov 26 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-0.2.pre2
- Add Requires hicolor-icon-theme (bz 217249)

* Sat Nov 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-0.1.pre2
- Initial FE package
