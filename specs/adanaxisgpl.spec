Summary:        Action game in four spatial dimensions
Name:           adanaxisgpl
Version:        1.2.5
Release:        51%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.mushware.com/
Source0:        http://www.mushware.com/files/%{name}-1.2.5.tar.gz
Patch0:         adanaxisgpl-1.2.5-const.patch
Patch1:         adanaxisgpl-1.2.5-gcc47.patch
Patch2:         adanaxisgpl-1.2.5-xdg-open.patch
Patch3:         adanaxisgpl-gcc11.patch
Patch4:         adanaxisgpl-gcc12.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  freeglut-devel
BuildRequires:  expat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pcre-devel
BuildRequires:  SDL_mixer-devel
BuildRequires: make
BuildRequires: libxcrypt-devel

%description
Adanaxis is a fast-moving first person shooter set in deep space, where the
fundamentals of space itself are changed.  By adding another dimension to
space this game provides an environment with movement in four directions
and six planes of rotation.  Initially the game explains the 4D control
system via a graphical sequence, before moving on to 30 levels of gameplay
with numerous enemy, ally, weapon and mission types.  Features include
simulated 4D texturing, mouse and joystick control, and original music.
Screenshots, movies and further information are available at
http://www.mushware.com/.

Hardware-accelerated 3D is recommended, ideally with support for OpenGL
Shading Language.


%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}

# Build .desktop files
cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=Adanaxis GPL
Comment=An action game in four spatial dimensions
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ActionGame;
EOF


%install
%make_install INSTALL="install -p" CPPROG="cp -p"

# Install desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop

# Icons
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 x11/icons/%{name}-16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 x11/icons/%{name}-32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 x11/icons/%{name}-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%files
%doc README ChangeLog AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_mandir}/man6/%{name}*.6*


%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1.2.5-51
- Add explicit BR: libxcrypt-devel

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.5-49
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar  7 2022 Hans de Goede <hdegoede@redhat.com> - 1.2.5-42
- Fix FTBFS (#2045188)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Jeff Law <law@redhat.com> - 1.2.5-38
- Re-enable LTO

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-37
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Jeff Law <law@redhat.com> - 1.2.5-35
- Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.5-31
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.2.5-28
- Rebuilt for switch to libxcrypt

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.5-27
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.5-20
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 1.2.5-16
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support
- Remove vendor prefix from desktop files in F19+
- Drop recovery .desktop file, this just clutters the menu, and can be done
  from the cmdline if needed

* Mon Apr 29 2013 Hans de Goede <hdegoede@redhat.com> - 1.2.5-15
- Run autoreconf for aarch64 support (rhbz#924970)
- Use xdg-open to open game manual

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.2.5-13
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.2.5-12
- rebuild against new libjpeg

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.2.5-10
- Rebuild against PCRE 8.30

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.2.5-9
- Rebuild against PCRE 8.30

* Thu Jan 12 2012 Hans de Goede <hdegoede@redhat.com> - 1.2.5-8
- Various specfile cleanups
- Fix building with gcc-4.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.5-4
- constify strchr

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.5-2
- Autorebuild for GCC 4.3

* Sun Feb 17 2008 Andy Southgate <andy.southgate@mushware.com> 1.2.5-1
- Sync to upstream to pick up gcc 4.3 compatibility fixes

* Thu Oct 25 2007 Andy Southgate <andy.southgate@mushware.com> 1.2.4-1
- Updates following further review (bugzilla #309061)

* Wed Oct 17 2007 Andy Southgate <andy.southgate@mushware.com> 1.2.3-1
- Updates following review (bugzilla #309061)

* Thu Sep 27 2007 Andy Southgate <andy.southgate@mushware.com> 1.2.1-1
- Created from Mandriva .spec
