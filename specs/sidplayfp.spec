Name:           sidplayfp
Version:        2.12.0
Release:        2%{?dist}
Summary:        SID chip music module player
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/libsidplayfp
Source0:        https://github.com/libsidplayfp/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libsidplayfp-devel >= 2.0
BuildRequires:  alsa-lib-devel pulseaudio-libs-devel libtool
BuildRequires:  gettext-devel

%description
A player for playing SID music modules originally created on the Commodore 64
and compatibles.


%prep
%setup -q
# Regenerate autofoo stuff, it is better to always build this from source
#the following does't work because rpm can't cope with the exclamation mark:
# rm aclocal.m4 build-aux/!(config.rpath)
rm aclocal.m4 build-aux/*
#so recreate fake config.rpath - see https://lists.gnu.org/archive/html/bug-gettext/2011-10/msg00012.html
touch build-aux/config.rpath
autoreconf -ivf


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc AUTHORS README
%license COPYING
%{_bindir}/sidplayfp
%{_bindir}/stilview
%{_mandir}/man?/sidplayfp.*
%{_mandir}/man1/stilview.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 13 2024 Karel Volný <kvolny@redhat.com> - 2.12.0-1
- Update to 2.12.0 (rhbz#2329755)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Mon Nov 11 2024 Karel Volný <kvolny@redhat.com> - 2.11.0-1
- Update to 2.11.0 (rhbz#2323726)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Thu Oct 31 2024 Karel Volný <kvolny@redhat.com> - 2.10.0-1
- Update to 2.10.0 (rhbz#2316879)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Tue Aug 13 2024 Karel Volný <kvolny@redhat.com> - 2.9.0-1
- Update to 2.9.0 (rhbz#2304308)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.8.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Karel Volný <kvolny@redhat.com> - 2.8.0-1
- Update to 2.8.0 (rhbz#2291233)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Wed Apr 03 2024 Karel Volný <kvolny@redhat.com> - 2.7.0-1
- Update to 2.7.0 (rhbz#2272265)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Karel Volný <kvolny@redhat.com> - 2.6.2-1
- Update to 2.6.2 (rhbz#2258031)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Tue Jan 09 2024 Karel Volný <kvolny@redhat.com> - 2.6.1-1
- Update to 2.6.1 (rhbz#2185665)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Karel Volný <kvolny@redhat.com> - 2.4.1-1
- Update to 2.4.1 (rhbz#2179662)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 08 2022 Karel Volný <kvolny@redhat.com> - 2.4.0-1
- Update to 2.4.0 (rhbz#2140720)
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 16 2022 Karel Volný <kvolny@redhat.com> - 2.2.3-1
- Update to 2.2.3
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 26 2021 Karel Volný <kvolny@redhat.com> - 2.2.2-1
- Update to 2.2.2
- Updated URLs to point to GitHub
- See the upstream changes at https://github.com/libsidplayfp/sidplayfp/releases

* Mon Aug 09 2021 Karel Volný <kvolny@redhat.com> - 2.2.1-1
- Update to 2.2.1
- See the upstream changes at https://sourceforge.net/p/sidplay-residfp/news/

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Karel Volný <kvolny@redhat.com> - 2.2.0-1
- Update to 2.2.0
- Add BuildRequires gettext-devel because of AM_ICONV usage

* Wed Apr 14 2021 Karel Volný <kvolny@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Sun Feb 21 2021 Karel Volný <kvolny@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Hans de Goede <hdegoede@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Karel Volný <kvolny@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Sat Aug 31 2019 Hans de Goede <hdegoede@redhat.com> - 2.0.0-1
- Update to 2.0.0 upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Hans de Goede <hdegoede@redhat.com> - 1.4.4-1
- Update to 1.4.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 10 2015 Hans de Goede <hdegoede@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 20 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1.3.0-3
- Rebuild for GCC 5 rebuilt libsidplayfp.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Hans de Goede <hdegoede@redhat.com> - 1.3.0-1
- New upstream release 1.3.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr  6 2014 Hans de Goede <hdegoede@redhat.com> - 1.2.0-1
- New upstream release 1.2.0
- Drop our patches (merged upstream)

* Mon Sep 30 2013 Hans de Goede <hdegoede@redhat.com> - 1.1.0-1
- New upstream release 1.1.0
- Drop our patches (merged upstream)

* Wed Aug 21 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.3-1
- New upstream release 1.0.3

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.1-1
- Initial RPM packaging for Fedora
