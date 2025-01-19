%global prerelease 20240611

Name:           lv2-x42-plugins
Version:        0.20.0
Release:        0.4.%{prerelease}%{?dist}
Summary:        A number of LV2 plugins

# files in balance.lv2/pugl are ISC, the rest are GPLv2+
# Automatically converted from old format: GPLv2+ and ISC - review is highly recommended.
License:        GPL-2.0-or-later AND ISC
URL:            https://github.com/x42/x42-plugins
# A tarball is now provided at http://gareus.org/misc/x42-plugins.php
Source0:        http://gareus.org/misc/x42-plugins/x42-plugins-%{prerelease}.tar.xz
Source1:        README.md

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  zita-convolver-devel >= 3.1.0
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libltc-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  fftw3-devel
BuildRequires:  gtk2-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  ftgl-devel
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  mesa-libEGL-devel
Requires:       lv2 >= 1.8.1
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
Requires:       gnu-free-mono-fonts

%description
A number of lv2 plugins including stereo balance, midi filter, delay,
convolver, fader, parametric equalizer, auto-tune.

%prep
%setup -q -n x42-plugins-%{prerelease}
cp -p %{SOURCE1} .

%build
%set_build_flags
export FONTFILE="/usr/share/fonts/gnu-free/FreeSansBold.ttf"
export STRIP=/bin/true
export PKG_CONFIG=pkgconf
export OPTIMIZATIONS="%{optflags}"
%make_build LIBDIR=%{_libdir} LV2DIR=%{_libdir}/lv2 PREFIX=%{_prefix}

%install
%make_install LIBDIR=%{_libdir} LV2DIR=%{_libdir}/lv2 PREFIX=%{_prefix}

%files
# all plugins share the same license
%license balance.lv2/COPYING
%doc plugin.versions plugin.list README.md
%{_libdir}/lv2/*.lv2
%{_bindir}/x42*
%{_mandir}/man1/x42*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-0.4.20240611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20.0-0.3.20240611
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-0.2.20240611
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Guido Aulisi <guido.aulisi@gmail.com> - 0.20.0-0.1.20240611
- Update to 20240611
- zeroconvolv replaces convoLV2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-0.3.20230915
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-0.2.20230915
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.19.0-0.1.20230915
- Update to 20230915

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-0.4.20220327
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-0.3.20220327
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-0.2.20220327
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Guido Aulisi <guido.aulisi@gmail.com> - 0.18.0-0.1.20220327
- Update to 20220327

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-0.2.20211016
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 20 2021 Guido Aulisi <guido.aulisi@gmail.com> - 0.17.0-0.1.20210114
- Update to 20211016

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-0.2.20210114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 05 2021 Guido Aulisi <guido.aulisi@gmail.com> - 0.16.0-0.1.20210114
- Update to 20210114

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-0.2.20200714
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.15.0-0.1.20200114
- Update to 20200714
- Some spec cleanup

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-0.3.20200114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-0.2.20200114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.14.0-0.1.20200114
- Update to 20200114

* Thu Nov 07 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.13.0-0.1.20191013
- Update to 20191013

* Mon Sep 09 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.12.0-0.1.20190714
- Update to 20190820

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-0.2.20190714
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.11.0-0.1.20190714
- Update to 20190714

* Mon Jun 24 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.0-0.2.20190507
- Rebuilt for zita-convolver upgrade

* Mon Jun 03 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.10.0-0.1.20190507
- Update to 20190507

* Tue Apr 30 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.0-0.1.20190413
- Update to 20190413
- Minor spec cleanup

* Sun Feb 03 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.0-0.3.20190124
- Fix FTBFS due to undefined reference to symbol g_object_unref

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.2.20190124
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.8.0-0.1.20190124
- Update to 20190124

* Mon Jan 21 2019 Guido Aulisi <guido.aulisi@gmail.com> - 0.7.0-0.1.20190105
- Update to 20190105

* Sat Nov 17 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.6.0-0.1.20181103
- Update to 20181103

* Tue Aug 07 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.5.0-0.1.20180803
- Update to 20180803
- New dpl plugin

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-0.2.20180320
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.4.0-0.1.20180320
- Update to 20180320

* Tue Feb 13 2018 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.0-0.5.20170428
- Fix FTBS with glibc 2.27 and gcc 8

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.4.20170428
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.3.20170428
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-0.2.20170428
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.0-0.1.20170428
- Update to 20170428
- New plugins
- Use hardened LDFLAGS
- Remove deprecated Group tag
- Use license macro

* Thu Feb 16 2017 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.2.0-0.4.20150608git3e40bc9
- Added BR: libltc-devel jack-audio-connection-kit-devel
- Do not strip binaries

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.3.20150608git3e40bc9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.2.20150608git3e40bc9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Brendan Jones <brendan.jones.it@gmail.com> 0.2.0-0.1.20150608git3e40bc9
- Update to 20150608 

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-0.7.20131005git7db99d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.1-0.6.20131005git7db99d5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-0.5.20131005git7db99d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-0.4.20131005git7db99d5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 06 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.1.1-0.3.20131005git7db99d5
- Specify font and UI BR's

* Sat Oct 05 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.1.1-0.2.20131005git7db99d5
- New upstream commit, adds meters.lv2

* Sat Sep 14 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.1.1-0.1.20130615git7153e34
- Correct prelease release syntax
- Correct FSF address
- Use %%make_install macro

* Mon Sep 02 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.0.1-1
- Initial build

