Name:           chromium-bsu
Version:        0.9.16.1
Release:        22%{?dist}
Summary:        Fast paced, arcade-style, top-scrolling space shooter
# Automatically converted from old format: Artistic clarified - review is highly recommended.
License:        ClArtistic
URL:            http://chromium-bsu.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# Do not forget to save LDFLAGS (fixed in upstream autoconf-archive)
Patch0:         ax_check_gl_m4.patch
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils SDL2-devel alsa-lib-devel libvorbis-devel
BuildRequires:  SDL2_image-devel libpng-devel libglpng-devel quesoglc-devel
BuildRequires:  pkgconfig(gl) pkgconfig(glu) openal-soft-devel freealut-devel >= 1.1.0-10
BuildRequires:  libappstream-glib gettext
BuildRequires:  make autoconf automake gettext-devel
Requires:       hicolor-icon-theme

%description
You are captain of the cargo ship Chromium B.S.U., responsible for delivering
supplies to our troops on the front line. Your ship has a small fleet of
robotic fighters which you control from the relative safety of the Chromium
vessel. This is an OpenGL-based shoot 'em up game with fine graphics.


%prep
%autosetup -p1
# https://www.gnu.org/software/gettext/manual/html_node/autopoint-Invocation.html
sed -i -e 's|AM_GNU_GETTEXT_VERSION|AM_GNU_GETTEXT_REQUIRE_VERSION|' configure.ac
autoreconf -fiv


%build
%configure
make %{?_smp_mflags}


%install
%make_install
%find_lang %{name}
cp -a AUTHORS README NEWS $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc %{_docdir}/%{name}
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_mandir}/man6/%{name}.6.gz


%changelog
* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.16.1-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Hans de Goede <hdegoede@redhat.com> - 0.9.16.1-8
- Rebuilt for new GLEW

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.16.1-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Hans de Goede <hdegoede@redhat.com> - 0.9.16.1-1
- New upstream bug-fix release 0.9.16.1 (rhbz#1397801)

* Sat Feb 20 2016 Hans de Goede <hdegoede@redhat.com> - 0.9.15.1-9
- Change gcc6 patch to not change game behavior

* Sat Feb 20 2016 Hans de Goede <hdegoede@redhat.com> - 0.9.15.1-8
- Fix FTBFS (rhbz#1307377)
- Add appdata

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.15.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.15.1-1
- New upstream release 0.9.15.1

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.15-6
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Wed May  1 2013 Hans de Goede <hdegoede@redhat.com> - 0.9.15-5
- run autoreconf for aarch64 support (rhbz#925222)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 14 2011 Hans de Goede <hdegoede@redhat.com> - 0.9.15-1
- New upstream release 0.9.15

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jun 21 2010 Hans de Goede <hdegoede@redhat.com> 0.9.14.1-1
- New upstream release 0.9.14.1
- Drop Fedora specific README.license (upstream has fixed the included license)
- This fixes the FTBFS of the previous version (#599832)

* Fri Oct  9 2009 Hans de Goede <hdegoede@redhat.com> 0.9.14-6
- Switch to quesoglc instead of ftgl (glc is the upstream default)
- This fixes chromium-bsu not finding its font, as quesoglc properly uses
  fontconfig instead of using a hardcoded path to the font (#526995)

* Sun Aug 16 2009 Hans de Goede <hdegoede@redhat.com> 0.9.14-5
- Switch to openal-soft

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 27 2009 Hans de Goede <hdegoede@redhat.com> 0.9.14-3
- Fix build errors (#502191)

* Fri May 22 2009 Hans de Goede <hdegoede@redhat.com> 0.9.14-2
- Minor packaging cleanups from review (#502191)

* Sun May 17 2009 Hans de Goede <hdegoede@redhat.com> 0.9.14-1
- Initial Fedora package
