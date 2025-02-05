Name:		sdrangel
Version:	7.22.5
Release:	3%{?dist}
Summary:	Software defined radio (SDR) and signal analyzer frontend to various hardware
License:	GPL-3.0-or-later
URL:		https://github.com/f4exb/sdrangel
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	org.sdrangel.SDRangel.metainfo.xml
ExclusiveArch:	%{qt5_qtwebengine_arches}

Provides:	bundled(jrtplib) = 3.11.1
Provides:	bundled(qthid)
Provides:	bundled(QtWebApp)
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	pkgconf-pkg-config
BuildRequires:	codec2-devel
BuildRequires:	airspyone_host-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	hackrf-devel
BuildRequires:	uhd-devel
BuildRequires:	rtl-sdr-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtwebsockets-devel
BuildRequires:	qt5-qtwebengine-devel
BuildRequires:	qt5-qtmultimedia-devel
# qtpositioning
BuildRequires:	qt5-qtlocation-devel
BuildRequires:	qt5-qtcharts-devel
BuildRequires:	qt5-qtserialport-devel
BuildRequires:	qt5-qtspeech-devel
BuildRequires:	qt5-qtbase-private-devel
BuildRequires:	qt5-qtgamepad-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	boost-devel
BuildRequires:	gr-osmosdr-devel
BuildRequires:	fftw-devel
BuildRequires:	libusbx-devel
BuildRequires:	zlib-devel
#BuildRequires:	faad2-devel
BuildRequires:	opencv-devel
BuildRequires:	serialdv-devel
BuildRequires:	opus-devel
BuildRequires:	libiio-devel
#BuildRequires:	ffmpeg-devel
BuildRequires:	hidapi-devel
BuildRequires:	flac-devel
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme

%description
SDRangel uses sample source plugins to collect I/Q samples from a hardware
device. Then in the passband returned possibly decimated one or more channel
Rx plugins can be used to demodulate, decode or analyze some part of this
spectrum.

Conversely SDRangel uses sample sink plugins to send I/Q samples to a
hardware device. One or more channel Tx plugins can be used to produce
modulated samples that are mixed into a transmission passband with possible
subsequent interpolation before being sent to the device or written to file.

More information is available on the project Wiki:
https://github.com/f4exb/sdrangel/wiki/Quick-start

%prep
%autosetup -p1

%build
%cmake -DARCH_OPT=""
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/

# drop duplicate readme file, already installed as the doc
rm -f %{buildroot}%{_datadir}/%{name}/Readme.md

%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/sdrangel.desktop

appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/org.sdrangel.SDRangel.metainfo.xml

%files
%license LICENSE
%doc CHANGELOG Readme.md
%{_bindir}/sdrangel
%{_bindir}/sdrangelbench
%{_bindir}/sdrangelsrv
%{_libdir}/sdrangel
%{_datadir}/applications/sdrangel.desktop
%{_datadir}/icons/hicolor/scalable/apps/sdrangel_icon.svg
%{_metainfodir}/org.sdrangel.SDRangel.metainfo.xml

%changelog
* Tue Feb 04 2025 Sérgio Basto <sergio@serjux.com> - 7.22.5-3
- Rebuild for opencv-4.11.0

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.22.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec  5 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.22.5-1
- New version
  Resolves: rhbz#2330485

* Sat Nov 16 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.22.4-1
- New version
  Resolves: rhbz#2325025

* Tue Oct 22 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.22.2-1
- New version
  Resolves: rhbz#2320051

* Thu Oct 10 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.22.1-1
- New version
  Resolves: rhbz#2316878

* Thu Aug 15 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.22.0-1
- New version
  Resolves: rhbz#2305090

* Thu Jul 25 2024 Sérgio Basto <sergio@serjux.com> - 7.21.4-4
- Rebuild for opencv 4.10.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.21.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.21.4-2
- Rebuilt for new uhd

* Mon Jul 15 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.21.4-1
- New version
  Resolves: rhbz#2295724

* Tue Jun 18 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.21.3-1
- New version
  Resolves: rhbz#2292861

* Mon Jun 10 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.21.2-1
- New version
  Resolves: rhbz#2290997

* Mon May 27 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.21.1-1
- New version
  Resolves: rhbz#2283179

* Wed Apr 17 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.20.0-1
- New version
  Resolves: rhbz#2275094

* Tue Apr  9 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.19.1-2
- Rebuilt for new rtl-sdr

* Tue Mar 19 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.19.1-1
- New version
  Resolves: rhbz#2270201

* Mon Mar 18 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.19.0-1
- New version
  Resolves: rhbz#2268689

* Mon Feb 26 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.18.1-1
- New version
  Resolves: rhbz#2265576
- Converted license tag to SPDX

* Mon Feb 19 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.18.0-1
- New version
  Resolves: rhbz#2264781

* Mon Feb 05 2024 Sérgio Basto <sergio@serjux.com> - 7.17.3-3
- Rebuild for opencv 4.9.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.17.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 7.17.3-1
- New version
  Resolves: rhbz#2256347

* Mon Dec 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.17.2-1
- New version
  Resolves: rhbz#2253626

* Mon Dec  4 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.17.1-1
- New version
  Resolves: rhbz#2252199

* Fri Nov 24 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.17.0-2
- Rebuilt for new uhd

* Tue Oct 31 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.17.0-1
- New version
  Resolves: rhbz#2246813

* Mon Sep 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.16.0-1
- New version
  Resolves: rhbz#2240192

* Tue Sep  5 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.15.4-1
- New version
  Resolves: rhbz#2237056

* Fri Aug 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.15.3-1
- New version
  Resolves: rhbz#2229367

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 7.15.1-4
- Rebuild for opencv 4.8.0

* Sat Aug 05 2023 Richard Shaw <hobbes1069@gmail.com> - 7.15.1-3
- Rebuild for codec2.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.15.1-1
- New version
  Resolves: rhbz#2222469

* Tue Jun 27 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.15.0-1
- New version
  Resolves: rhbz#2216071

* Thu Jun  1 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.14.2-1
- New version
  Resolves: rhbz#2210983

* Thu May 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.14.1-1
- New version
  Resolves: rhbz#2209844

* Thu Apr 13 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.13.0-1
- New version
  Related: rhbz#2183851

* Tue Apr 11 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.12.0-1
- New version
  Resolves: rhbz#2183851

* Thu Mar 23 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.11.0-1
- New version
  Resolves: rhbz#2179661

* Thu Mar  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.10.0-1
- New version
  Resolves: rhbz#2173033

* Thu Feb  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.9.0-1
- New version
  Resolves: rhbz#2166588

* Wed Feb  1 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.8.6-2
- Rebuilt for new uhd

* Thu Jan 19 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.8.6-1
- New version
  Resolves: rhbz#2160860

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 7.8.5-2
- Rebuild for opencv 4.7.0

* Mon Jan  2 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 7.8.5-1
- New version
  Resolves: rhbz#2154585

* Thu Dec  8 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.8.4-1
- New version
  Resolves: rhbz#2150464

* Sun Nov 13 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.8.2-1
- New version
  Resolves: rhbz#2139282

* Fri Oct 21 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.8.1-1
- New version
  Resolves: rhbz#2136733

* Mon Sep 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.7.0-1
- New version
  Resolves: rhbz#2125841

* Mon Sep  5 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.6.3-1
- New version
  Resolves: rhbz#2123922

* Sat Aug 20 2022 Daniel Rusek <mail@asciiwolf.com> - 7.6.2-2
- Added AppStream metadata

* Wed Aug 17 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.6.2-1
- New version
  Resolves: rhbz#2118207

* Thu Aug  4 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.6.1-1
- New version
  Resolves: rhbz#2115146

* Thu Aug  4 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.6.0-3
- Rebuilt for Qt
  Resolves: rhbz#2112956

* Sat Jul 30 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.6.0-2
- Rebuilt for new uhd

* Thu Jul 21 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.6.0-1
- New version
  Resolves: rhbz#2109506

* Tue Jul 19 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.5.1-1
- New version
  Resolves: rhbz#2108379

* Mon Jul 11 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.4.0-3
- Rebuilt for new airspyone_host

* Sat Jul 09 2022 Richard Shaw <hobbes1069@gmail.com> - 7.4.0-2
- Rebuild for codec2 1.0.4.

* Tue Jun 28 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.4.0-1
- New version
  Resolves: rhbz#2101173

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 7.3.2-2
- Rebuilt for opencv 4.6.0

* Tue Jun 14 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.3.2-1
- New version
  Resolves: rhbz#2096464

* Mon Jun  6 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.3.1-1
- New version
  Resolves: rhbz#2091481

* Fri May 27 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.2.1-1
- New version
  Resolves: rhbz#2090931

* Thu May 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.2.0-1
- New version
  Resolves: rhbz#2090518

* Mon May 23 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.1.0-1
- New version
  Resolves: rhbz#2088770

* Thu May 19 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 7.0.0-1
- New version
  Resolves: rhbz#2070713

* Wed Apr 27 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 6.20.2-4
- Used distro's optimization flags, not the -march=native

* Tue Apr 26 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 6.20.2-3
- Rebuilt for new uhd
  Resolves: rhbz#2077805

* Thu Apr  7 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 6.20.2-2
- Rebuilt for new QT
  Resolves: rhbz#2071950

* Thu Mar 31 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 6.20.2-1
- New version
  Resolves: rhbz#2070713

* Thu Mar 31 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 6.20.1-2
- Rebuilt for new QT5
  Resolves: rhbz#2070663

* Thu Mar 10 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 6.20.1-1
- New version
- Updated according to the Fedora review
  Related: rhbz#2045924

* Wed Feb 23 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 6.19.1-1
- New version
- Updated according to the Fedora review
  Related: rhbz#2045924

* Tue Jan 25 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 6.18.1-1
- Initial release
