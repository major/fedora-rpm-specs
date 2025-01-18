Name:           CubicSDR
Version:        0.2.7
Release:        19%{?dist}.1
Summary:        Cross-Platform Software-Defined Radio Panadapter

# The primary license of CubicSDR is GPLv2+.
# There are multiple third party libraries bundled in the source of CubicSDR.
# external/loadpng/ and external/tinyxml/ use the zlib/libpng license
# external/rs232/, external/liquid-dsp/, src/util/DataTree* use the MIT/X11 (BSD like) license
# Note: external/hamlib/ and external/rtaudio/ are provided by the source, but at
#  build and run time we use system-provided copies of these libraries
# Automatically converted from old format: GPLv2+ and MIT and zlib - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-MIT AND Zlib
URL:            https://cubicsdr.com
Source0:        https://github.com/cjcliffe/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        CubicSDR
Source2:        com.cubicsdr.CubicSDR.metainfo.xml
Patch0:         gdk-backend-desktop.patch

ExcludeArch:    i686

# Upstream includes local copies of librs232 and tinyxml unfortunately.
#    https://github.com/cjcliffe/CubicSDR/issues/670
Provides: bundled(librs232) = 0.21
Provides: bundled(tinyxml) = 2.6.2
# Upstream includes local copy of lodepng not present in Fedora already
Provides: bundled(lodepng) = 20180809
BuildRequires:  cmake gcc-c++ desktop-file-utils
# Library dependencies
BuildRequires: SoapySDR-devel
BuildRequires: wxGTK-devel
BuildRequires: hamlib-devel
BuildRequires: fftw-devel
BuildRequires: rtaudio-devel
BuildRequires: liquid-dsp-devel >= 1.4.0
Requires: hicolor-icon-theme

%description
CubicSDR is a cross-platform Software-Defined Radio application which
allows you to navigate the radio spectrum and demodulate any signals
you might discover.  It currently includes several common analog
demodulation schemes such as AM and FM and will support digital modes
in the future.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake -Wno-dev -DCMAKE_BUILD_TYPE=Release -DUSE_HAMLIB=1 -DUSE_SYSTEM_RTAUDIO=1
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
# Move executable to libexecdir, leave CLI start script in bindir
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
mv %{buildroot}/%{_bindir}/CubicSDR %{buildroot}/%{_libexecdir}/%{name}/%{name}
install -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}
install -D -p -m644 src/CubicSDR.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
desktop-file-edit --set-key=Icon --set-value=%{name} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -p -m644 %{SOURCE2} %{buildroot}%{_metainfodir}/com.cubicsdr.CubicSDR.metainfo.xml


%files
%license LICENSE
%{_libexecdir}/*
%{_bindir}/*
# Upstream includes local copies of Bitstream Vera fonts
#    https://github.com/cjcliffe/CubicSDR/issues/669
%{_datadir}/cubicsdr/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_metainfodir}/com.cubicsdr.CubicSDR.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-19.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Richard Shaw <hobbes1069@gmail.com> - 0.2.7-18.1
- Rebuild for new rtaudio.

* Sun Oct 13 2024 Richard Shaw <hobbes1069@gmail.com> - 0.2.7-17.1
- Rebuild for liquid-dsp-1.6.0 now that it's in the repos.

* Sun Oct 13 2024 Richard Shaw <hobbes1069@gmail.com> - 0.2.7-17
- Rebuild for liquid-dsp-1.6.0.

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.7-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Daniel Rusek <mail@asciiwolf.com> - 0.2.7-10
- Add AppStream metadata, desktop icon to standard location

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Scott Talbert <swt@techie.net> - 0.2.7-8
- Rebuild due to wxGLCanvas ABI change

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 0.2.7-7
- Rebuild for hamlib 4.5.

* Mon Jul 25 2022 Scott Talbert <swt@techie.net> - 0.2.7-6
- Rebuild for wxGTK 3.2.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 10 2022 Scott Talbert <swt@techie.net> - 0.2.7-4
- Rebuild for wxGTK 3.1.7

* Tue Apr 12 2022 Scott Talbert <swt@techie.net> - 0.2.7-3
- Rebuild for wxGTK 3.1.6

* Mon Feb  7 2022 Matt Domsch <matt@domsch.com> - 0.2.7-2
- rebuild for liquid-dsp rebuild

* Sat Feb  5 2022 Matt Domsch <matt@domsch.com> - 0.2.7-1
- Upstream 0.2.7

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-22.20210814git0248e5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 0.2.5-21.20210814git0248e5a
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 0.2.5-19.20210814git0248e5a
- Rebuild for hamlib 4.4.

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 0.2.5-18.20210814git0248e5a
- Rebuild for hamlib 4.3.1.

* Tue Aug 17 2021 Matt Domsch <matt@domsch.com> - 0.2.5-17.20200824git4f1db55
- Upstream latest snapshot with hamlib 4.2 support
- exclude unneeded external/ files from git-generated tarball, reduces size
  from 36MB to 2MB.
- Rebuilt for SoapySDR 0.8.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-16.20200824git4f1db55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 0.2.5-15.20200824git4f1db55
- Rebuild for hamlib 4.2.

* Tue May 04 2021 Scott Talbert <swt@techie.net> - 0.2.5-14.20200824git4f1db55
- Rebuild for wxWidgets 3.1.5

* Sun Feb 07 2021 Richard Shaw <hobbes1069@gmail.com> - 0.2.5-13.20200824git4f1db55
- Rebuild for hamlib 4.1.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 0.2.5-12.20200824git4f1db55
- Rebuild for hamlib 4.1.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-11.20200824git4f1db55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Matt Domsch <matt@domsch.com> - 0.2.5-10.20200824git4f1db55
- upstream snapshot. Zero-to-right by SHIFT+Right Click on the frequency digits.

* Sun Aug 09 2020 Scott Talbert <swt@techie.net> - 0.2.5-9.20200226gitd2f9333
- Rebuild for wxWidgets 3.1.4 (for real)

* Sat Aug 08 2020 Scott Talbert <swt@techie.net> - 0.2.5-8.20200226gitd2f9333
- Rebuild for wxWidgets 3.1.4

* Sun Aug  2 2020 Matt Domsch <matt@domsch.com> - 0.2.5-7.20200226gitd2f9333
- F33 cmakes fixes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6.20200226gitd2f9333
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5.20200226gitd2f9333
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Matt Domsch <matt@domsch.com> 0.2.5-4.20200407gitd2f9333
- rebuild for hamlib-devel 4.0.0

* Thu Apr  9 2020 Matt Domsch <matt@domsch.com> 0.2.5-3.20200407gitd2f9333
- move executable to libexecdir
- delete unused external libraries source tarball
- address review comments, spec file cleanups

* Wed Apr  8 2020 Matt Domsch <matt@domsch.com> 0.2.5-2.20200407gitd2f9333
- move env GDK_BACKEND=x11 into the desktop start file

* Tue Apr  7 2020 Matt Domsch <matt@domsch.com> 0.2.5-1.20200407gitd2f9333
- Latest upstream plus newer liquid-dsp library

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4.20180806gita7e4d91
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3.20180806gita7e4d91
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2.20180806gita7e4d91
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug  7 2018 Matt Domsch <matt@domsch.com> 0.2.4-1.20180806gita7e4d91
- Initial Fedora packaging
