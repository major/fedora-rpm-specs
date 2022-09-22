Name:           qodem
Version:        1.0.1
Release:        1%{?dist}
Summary:        Terminal emulator and communications package

License:        GPLv2+
URL:            http://qodem.sourceforge.net/
Source0:        https://sourceforge.net/projects/%{name}/files/qodem/%{version}/%{name}-%{version}.tar.gz
Source100:      qodem.desktop
Source101:      qodem.appdata.xml

BuildRequires:  automake autoconf gcc desktop-file-utils libappstream-glib make
BuildRequires:  SDL-devel
BuildRequires:  ncurses-devel
BuildRequires:  gettext
BuildRequires:  glibc-devel
BuildRequires:  libssh2-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXt-devel
BuildRequires:  miniupnpc-devel

# Not in Fedora
Provides:       bundled(pdcurses) = 3.4.0

Requires:       terminus-fonts
Requires:       xterm


%description
Qodem is an open-source re-implementation of the Qmodem(tm)
shareware communications package, updated for more modern uses.
Major features include:
    * Unicode display: translation of CP437 (PC VGA), VT100 DEC
      Special Graphics characters, VT220 National Replacement
      Character sets, etc., to Unicode
    * Terminal interface conveniences: scrollback buffer, capture
      file, screen dump, dialing directory, keyboard macros, script
      support
    * Connection methods: serial, local shell, command line, telnet,
      ssh, rlogin, rsh
    * Emulations: ANSI.SYS (including "ANSI music"), Avatar, VT52,
      VT100/102, VT220, Linux, and XTerm
    * Transfer protocols: Xmodem, Ymodem, Zmodem, and Kermit


%prep
%autosetup -p1
# Remove bundled stuff
rm -f intl/gettext.c
rm -rf lib/{c,cryptlib,upnp}


%build
export CFLAGS="%{optflags} -Werror=format-security"
export LDFLAGS="-lm"
autoreconf -fi
%configure --enable-x11 

%make_build


%install
%make_install

# Upstream does not provide a desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install %{SOURCE100}

# install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{64x64,512x512,scalable}/apps
install -pm 0644 build/icons/qodem.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/
install -pm 0644 build/icons/qodem-512.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/qodem.png
install -pm 0644 build/icons/qodem.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/a

# Install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -p %{SOURCE101} %{buildroot}%{_datadir}/metainfo/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%doc ChangeLog CREDITS README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/*


%changelog
* Mon Sep 05 2022 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-1
- Update to 1.0.1.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Kalev Lember <klember@redhat.com> - 1.0.0-5
- Rebuilt for miniupnpc soname bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-2
- Add desktop and appdata file.

* Mon Mar 05 2018 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-1
- Update to 1.0.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Richard Shaw <hobbes1069@gmail.com> - 0.3.2-7
- Fix possible security bug with printf (BZ#1037294).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.2-6
- Patch for buffer overflow, Fixes BZ#978600.

* Sun May 26 2013 Richard Shaw <hobbes1069@gmail.com> - 0.3.2-5
- Add autoreconf to permit building for aarch64.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Richard Shaw <hobbes1069@gmail.com> - 0.3.2-1
- Rebuild for GC 4.7.0.

* Sat Jul 23 2011 Richard Shaw <hobbes1069@gmail.com> - 0.3.2-1
- Initial Release.
