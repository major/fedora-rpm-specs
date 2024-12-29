%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global fontfile %{_datadir}/fonts/bitstream-vera-sans-fonts/VeraBd.ttf
%else
%global fontfile %{_datadir}/fonts/bitstream-vera/VeraBd.ttf
%endif

Name:           setBfree
Version:        0.8.13
Release:        3%{?dist}
Summary:        A DSP Tonewheel Organ emulator

# Automatically converted from old format: GPLv2+ and GPLv3+ and ISC - review is highly recommended.
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND ISC
URL:            https://setbfree.org
# Not present in releases, but tagged on GitHub
Source0:        https://github.com/pantherb/setBfree/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        x42-whirl.desktop
Source3:        %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  ftgl-devel
BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cairo-devel
BuildRequires:  pango-devel

Requires:       bitstream-vera-sans-fonts
Requires:       hicolor-icon-theme

%package -n lv2-setBfree-plugins
Summary:        A DSP Tonewheel Organ emulator. LV2 version
Requires:       lv2 >= 1.8.1
Requires:       bitstream-vera-sans-fonts

%description
setBfree is a MIDI-controlled, software synthesizer designed to imitate the
sound and properties of the electromechanical organs and sound modification
devices that brought world-wide fame to the names and products of Laurens
Hammond and Don Leslie.
This is the Jack version.

%description -n lv2-setBfree-plugins
setBfree is a MIDI-controlled, software synthesizer designed to imitate the
sound and properties of the electromechanical organs and sound modification
devices that brought world-wide fame to the names and products of Laurens
Hammond and Don Leslie.
This is the LV2 version.

%prep
%autosetup -p 1

%build

# This package does not build on all arches with upstream build flags,
# so upstream build flags are split.
# This is a realtime app, so we need the fastest possible math,
# flags for x86_64 are set to be compatible with most AMD and Intel CPUs,
# and to use the best possible SIMD instruction set.
flags=" -ffast-math -fno-finite-math-only"

%ifarch %{ix86}
flags+=" -msse -mfpmath=sse"
%endif

%ifarch x86_64
flags+=" -msse2 -mfpmath=sse"
%endif

CC=gcc; export CC
%set_build_flags

%make_build OPTIMIZATIONS="%{optflags} ${flags}" \
 PREFIX=%{_prefix} FONTFILE=%{fontfile} \
 lv2dir=%{_libdir}/lv2

%install
%make_install PREFIX=%{_prefix} \
 FONTFILE=%{fontfile} lv2dir=%{_libdir}/lv2

# install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
 %{SOURCE1} %{SOURCE2}

# install appdata file
install -d -m755 %{buildroot}%{_metainfodir}
install -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}

# validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# install icon file
install -d -m755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m644 doc/%{name}.png doc/x42-whirl.png \
 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps

# install man pages
install -d -m755 %{buildroot}%{_mandir}/man1
install -p -m644 doc/jboverdrive.1 doc/setBfree.1 doc/setBfreeUI.1 doc/x42-whirl.1 \
 %{buildroot}%{_mandir}/man1

%files
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/x42-whirl.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/x42-whirl.png
%{_metainfodir}/*
%doc AUTHORS ChangeLog README.md
%license COPYING

%files -n lv2-setBfree-plugins
%{_libdir}/lv2/*
%doc AUTHORS ChangeLog README.md
%license COPYING

%changelog
* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.13-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.13-1
- Version 0.8.13

* Sat Feb 03 2024 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.12-1
- Version 0.8.12

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Nils Philippsen <nils@tiptoe.de> - 0.8.11-5
- Use correct font path in Fedora >= 32

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.11-1
- Version 0.8.11

* Mon Nov 04 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.10-1
- Version 0.8.10

* Mon Sep 09 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.9-1
- Version 0.8.9
- Minor spec cleanup

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.8-4
- Fix FTBFS due to undefined reference to symbol g_object_unref

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.8-2
- Fix FTBFS with new Mesa libraries

* Mon Aug 27 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.8-1
- Version 0.8.8

* Sun Aug 05 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.7-1
- Version 0.8.7
- Patch to fix sprintf warnings by GCC

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.5-4
- Fix AppData directory

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.5-2
- Remove obsolete scriptlets

* Tue Aug 22 2017 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.5-1
- Version 0.8.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.4-4
- Do not use AVX instruction set in x86_64 builds (#1436871)
- Use hardened LDFLAGS

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.4-1
- Version 0.8.4
- Added missing Requires to LV2 package

* Tue Jan 03 2017 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.3-1
- Version 0.8.3
- Patched a possible buffer overflow

* Fri Dec 30 2016 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.2-5
- Use hardened LDFLAGS
- Drop unneeded Patch0

* Thu Dec 29 2016 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.2-4
- Added BRs for whirl/leslie GUI

* Tue Nov 01 2016 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.2-3
- Removed common package

* Fri Sep 09 2016 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.2-2
- Correct some rpmlint warnings

* Mon Sep 05 2016 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.2-1
- Version 0.8.2
