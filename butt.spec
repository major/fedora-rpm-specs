%global rdnn de.danielnoethen.butt

Name:           butt
Version:        0.1.36
Release:        2%{?dist}
Summary:        Broadcast using this tool
License:        GPLv2+
URL:            https://danielnoethen.de/butt/
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  gettext
BuildRequires:  gettext-devel

# https://danielnoethen.de/butt/manual.html#_install
BuildRequires:  fltk-devel
BuildRequires:  portaudio-devel
BuildRequires:  lame-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libogg-devel
BuildRequires:  flac-devel
BuildRequires:  opus-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  fdk-aac-free-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  openssl-devel
BuildRequires:  libX11-devel
BuildRequires:  libcurl-devel

# for desktop-file-install command
BuildRequires:  desktop-file-utils
# for appstream-util command
BuildRequires:  libappstream-glib
BuildRequires:  make

Requires:       hicolor-icon-theme


%description
butt (broadcast using this tool) is an easy to use, multi OS streaming tool.
It supports ShoutCast and IceCast and runs on Linux, MacOS and Windows.  The
main purpose of butt is to stream live audio data from your computers Mic or
Line input to an Shoutcast or Icecast server. Recording is also possible.  It
is NOT intended to be a server by itself or automatically stream a set of audio
files.


%prep
%autosetup -p 1


%build
autoreconf -ifv
%configure LIBS=-lX11
%make_build


%install
%make_install

# desktop file
install -Dpm 0644 usr/share/applications/butt.desktop %{buildroot}%{_datadir}/applications/%{rdnn}.desktop

# icons
for size in 16 22 24 32 48 64 96 128 256 512; do
    path=icons/hicolor/${size}x${size}/apps/butt.png
    install -Dpm 0644 usr/share/$path %{buildroot}%{_datadir}/$path
done
install -Dpm 0644 usr/share/icons/hicolor/scalable/apps/butt.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/butt.svg

# pixmaps
for size in 16 32; do
    path=pixmaps/butt$size.xpm
    install -Dpm 0644 usr/share/$path %{buildroot}%{_datadir}/$path
done

# appdata
install -Dpm 0644 usr/share/metainfo/%{rdnn}.metainfo.xml %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml

# locales
%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/butt
%{_datadir}/applications/%{rdnn}.desktop
%{_datadir}/icons/hicolor/*/apps/butt.*
%{_datadir}/pixmaps/butt*.xpm
%{_metainfodir}/%{rdnn}.metainfo.xml


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 03 2022 Carl George <carl@george.computer> - 0.1.36-1
- Latest upstream, resolves rhbz#2098461

* Tue Sep 13 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1.34-3
- Rebuilt for flac 1.4.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 21 2022 Carl George <carl@george.computer> - 0.1.34-1
- Latest upstream (resolves: rhbz#2018071)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.1.31-2
- Rebuilt with OpenSSL 3.0.0

* Sat Jul 24 2021 Carl George <carl@george.computer> - 0.1.31-1
- Latest upstream
- Resolves: rhbz#1981020

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Carl George <carl@george.computer> - 0.1.30-1
- Latest upstream
- Fixes: rhbz#1891773

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Carl George <carl@george.computer> - 0.1.24-1
- Latest upstream rhbz#1826467

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Carl George <carl@george.computer> - 0.1.19-1
- Latest upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Carl George <carl@george.computer> - 0.1.18-1
- Latest upstream

* Tue Apr 09 2019 Carl George <carl@george.computer> - 0.1.17-3
- Re-enable s390x via patch0

* Sun Apr 07 2019 Carl George <carl@george.computer> - 0.1.17-2
- Exclude s390x rhbz#1697142

* Fri Apr 05 2019 Carl George <carl@george.computer> - 0.1.17-1
- Initial package
