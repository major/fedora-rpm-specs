Name:           amsynth
Version:        1.13.4
Release:        2%{?dist}
Summary:        A classic synthesizer with dual oscillators

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://amsynth.github.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/release-%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lash-devel
BuildRequires:  mesa-libGL-devel mesa-libEGL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  intltool
BuildRequires:  pandoc
BuildRequires:  lv2-devel
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

%description
Amsynth is a software synthesis that provides a
classic subtractive synthesizer topology, with:

- Dual oscillators with classic waveforms - sine / saw / square / noise
- 12/24 dB/octave low/high/band-pass resonant filter
- Independent ADSR envelopes for filter and amplitude
- LFO which can modulate the oscillators, filter, and amplitude
- Distortion
- Reverb

%package data
BuildArch: noarch
Summary: Data files for amsynth
%description data
Sound banks and skins used in amsynth

%package -n lv2-amsynth-plugin
Summary: Amsynth lv2 plugin
Requires: lv2
Requires: %{name}-data = %{version}-%{release}
Obsoletes: lv2-amsynth-plugins < 1.6.0

%description -n lv2-amsynth-plugin
Amsynth plugin for the lv2 audio standard


%package -n dssi-amsynth-plugin
Summary: Amsynth dssi plugin
BuildRequires: dssi-devel liblo liblo-devel
BuildRequires: make
Requires:      dssi
Requires: %{name}-data = %{version}-%{release}
Obsoletes: dssi-amsynth-plugins < 1.6.0

%description -n dssi-amsynth-plugin
Amsynth plugin for the dssi audio API

%package -n vst-amsynth-plugin
Summary: Amsynth vst plugin
Requires: %{name}-data = %{version}-%{release}
Obsoletes: vst-amsynth-plugins < 1.6.0

%description -n vst-amsynth-plugin
Amsynth plugin for the vst protocl


%prep
%autosetup -p1

%build
%configure --with-jack --with-alsa --with-sndfile --with-lash --with-dssi
%make_build V=1


%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*%{name}.*.xml

%find_lang %{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/de/man1/amsynth.1*
%{_mandir}/fr/man1/amsynth.1*
%{_mandir}/man1/amsynth.1*


%files data -f %{name}.lang
%doc README AUTHORS
%license COPYING
%{_datadir}/%{name}

%files -n lv2-amsynth-plugin
%{_libdir}/lv2/%{name}.lv2/
%{_datadir}/appdata/lv2-%{name}-plugin.metainfo.xml

%files -n dssi-amsynth-plugin
%{_libdir}/dssi/%{name}_dssi.so
%{_libdir}/dssi/%{name}_dssi/
%{_datadir}/appdata/dssi-%{name}-plugin.metainfo.xml

%files -n vst-amsynth-plugin
%{_libdir}/vst/%{name}_vst.so
%{_datadir}/appdata/vst-%{name}-plugin.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Guido Aulisi <guido.aulisi@inps.it> - 1.13.4-1
- Update to 1.13.4

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.13.2-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Guido Aulisi <guido.aulisi@gmail.com> - 1.13.2-1
- Update to 1.13.2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Guido Aulisi <guido.aulisi@gmail.com> - 1.13.0-1
- Update to 1.13.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Guido Aulisi <guido.aulisi@gmail.com> - 1.12.4-1
- Update to 1.12.4
- Add BR lv2-devel

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 08:20:42 CET 2020 Guido Aulisi <guido.aulisi@gmail.com> - 1.12.2-1
- Update to 1.12.2
- Fix #1911367

* Mon Nov 16 2020 Guido Aulisi <guido.aulisi@gmail.com> - 1.12.1-1
- Update to 1.12.1

* Sun Oct 04 2020 Guido Aulisi <guido.aulisi@gmail.com> - 1.11.0-1
- Update to 1.11.0

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Guido Aulisi <guido.aulisi@gmail.com> - 1.10.0-1
- Update to 1.10.0
- Some spec cleanup

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Guido Aulisi <guido.aulisi@gmail.com> - 1.9.0-1
- Update to 1.9.0
- Patch a format string overflow
- Minor spec tuning

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Guido Aulisi <guido.aulisi@gmail.com> - 1.8.0-5
- Fix FTBFS with new Automake: patch Makefile.in, not Makefile.am

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.0-4
- Remove obsolete scriptlets

* Tue Aug 01 2017 Alexandre Moine <nobrakal@cthugha.org> - 1.8.0-3
- Fix RHBGZ #1476525
- Spec cleanup

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Alexandre Moine <nobrakal@cthugha.org> - 1.8.0-1
- New upstream release
- Drop dependency on gtkmm
- Add man page

* Fri Mar 17 2017 Alexandre Moine <nobrakal@gmail.com> - 1.7.1-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Alexandre Moine <nobrakal@gmail.com> 1.7.0-1
- Update to new upstream 1.7.0
- Add support for translation
- Move icon from pixmaps to hicolor

* Tue Apr 19 2016 Alexandre Moine <nobrakal@gmail.com> 1.6.4-1
- Update to new maintenance upstream 1.6.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 1 2015 Alexandre Moine <nobrakal@gmail.com> 1.6.3-1
- Update to new maintenance upstream 1.6.3

* Mon Oct 26 2015 Alexandre Moine <nobrakal@gmail.com> 1.6.2-1
- Update to new maintenance upstream 1.6.2

* Sun Oct 11 2015 Alexandre Moine <nobrakal@gmail.com> 1.6.1-1
- Update to new maintenance upstream 1.6.1

* Mon Sep 28 2015 Alexandre Moine <nobrakal@gmail.com> 1.6.0-1
- Update to new upstream 1.6.0
- Add the new vst plugin in a new sub-package.
- Remove ugly plurals of "plugins". There is only one.
- Fix build with new gtkmm24

* Mon Sep 07 2015 Richard Hughes <richard@hughsie.com> 1.5.1-6
- Remove the invalid ZERO WIDTH SPACE chars from the metainfo files.

* Sat Sep 05 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-5
- Move license files to the -data subpackage.
- Use fully versioned dependency in subpackages.
- Update the description of -the data subpackage.
- Add the skins/README as a doc file.

* Thu Sep 03 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-4
- Each plugins have now their licenses files and docs.
- Data subpackae for data files required by plugins.

* Thu Jun 04 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-3
- CHange the name of the dssi subckage to dssi-amsytnh-plugins.

* Tue Jun 02 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-2
- Add the support of alsa, lash and dssi. Can now export with libsndfile.
- New subpackage for dssi's plugins.
- Use now the right license: GPLv2+

* Sat May 30 2015 Alexandre Moine <nobrakal@gmail.com> 1.5.1-1
- Initial spec

