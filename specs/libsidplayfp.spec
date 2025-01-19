Name:           libsidplayfp
Version:        2.12.0
Release:        2%{?dist}
Summary:        SID chip music module playing library
# Zlib (src/utils/MD5/), GPL-2.0-only (src/builders/exsid-builder/) and GPL-2.0-or-later (the rest)
License:        GPL-2.0-or-later AND GPL-2.0-only AND Zlib
URL:            https://github.com/libsidplayfp
Source0:        https://github.com/libsidplayfp/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc gcc-c++ libtool doxygen
BuildRequires:  libftdi-c++-devel libgcrypt-devel
BuildRequires:  make
Provides:       bundled(md5-deutsch-c++)

%description
This library provides support for playing SID music modules originally
created on Commodore 64 and compatibles. It contains a processing engine
for MOS 6510 machine code and MOS 6581 Sound Interface Device (SID)
chip output. It is used by music player programs like SIDPLAY and
several plug-ins for versatile audio players.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
These are the files needed for compiling programs that use %{name}.


%package devel-doc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description devel-doc
This package contains API documentation for %{name}.


%prep
%setup -q
# Regenerate autofoo stuff, it is better to always build this from source
rm -r aclocal.m4 build-aux
autoreconf -ivf


%build
%configure --disable-static
make %{_smp_mflags} all doc


%install
%make_install INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_libdir}/libsidplayfp.so.6*
%{_libdir}/libstilview.so.0*

%files devel
%{_libdir}/libsidplayfp.so
%{_libdir}/libstilview.so
%{_includedir}/sidplayfp/
%{_includedir}/stilview/
%{_libdir}/pkgconfig/*.pc

%files devel-doc
%doc docs/html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 13 2024 Karel Volný <kvolny@redhat.com> - 2.12.0-1
- Update to 2.12.0 (rhbz#2329741)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Mon Nov 04 2024 Karel Volný <kvolny@redhat.com> - 2.11.0-1
- Update to 2.11.0 (rhbz#2323581)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Thu Oct 31 2024 Karel Volný <kvolny@redhat.com> - 2.10.1-1
- Update to 2.10.1 (rhbz#2316762)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Tue Aug 13 2024 Karel Volný <kvolny@redhat.com> - 2.9.0-1
- Update to 2.9.0 (rhbz#2304188)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.8.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Karel Volný <kvolny@redhat.com> - 2.8.0-1
- Update to 2.8.0 (rhbz#2291131)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Wed Jun 05 2024 Karel Volný <kvolny@redhat.com> - 2.7.1-1
- Update to 2.7.1 (rhbz#2281508)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Wed Apr 03 2024 Karel Volný <kvolny@redhat.com> - 2.7.0-1
- Update to 2.7.0 (rhbz#2272301)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Karel Volný <kvolny@redhat.com> - 2.6.0-1
- Update to 2.6.0 (rhbz#2255750)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Thu Dec 21 2023 Karel Volný <kvolny@redhat.com> - 2.5.0-1
- Update to 2.5.0 (rhbz#2185981)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Karel Volný <kvolny@redhat.com> - 2.4.2-1
- Update to 2.4.2 (rhbz#2165655)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Karel Volný <kvolny@redhat.com> - 2.4.1-1
- Update to 2.4.1 (rhbz#2144216)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Mon Nov 07 2022 Karel Volný <kvolny@redhat.com> - 2.4.0-1
- Update to 2.4.0 (rhbz#2140451)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Karel Volný <kvolny@redhat.com> - 2.3.1-1
- Update to 2.3.1 (rhbz#2030177)
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Fri Sep 24 2021 Karel Volný <kvolny@redhat.com> - 2.3.0-1
- Update to 2.3.0 (rhbz#2004943)
- Updated URLs to point to GitHub
- See the upstream changes at https://github.com/libsidplayfp/libsidplayfp/releases

* Mon Aug 09 2021 Karel Volný <kvolny@redhat.com> - 2.2.2-1
- Update to 2.2.2 (rhbz#1991097)
- See the upstream changes at https://sourceforge.net/p/sidplay-residfp/news/

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Karel Volný <kvolny@redhat.com> - 2.2.1-1
- Update to 2.2.1 (rhbz#1983475)
- See the upstream changes at https://sourceforge.net/p/sidplay-residfp/news/

* Tue May 25 2021 Karel Volný <kvolny@redhat.com> - 2.2.0-1
- Update to 2.2.0 (rhbz#1963441)
- See the upstream changes at https://sourceforge.net/p/sidplay-residfp/news/

* Mon Apr 19 2021 Karel Volný <kvolny@redhat.com> - 2.1.2-1
- Update to 2.1.2 (rhbz#1951193)
- See the upstream changes at https://sourceforge.net/p/sidplay-residfp/news/

* Wed Apr 14 2021 Karel Volný <kvolny@redhat.com> - 2.1.1-1
- Update to 2.1.1 (rhbz#1933405)
- See the upstream changes at https://sourceforge.net/p/sidplay-residfp/news/

* Thu Feb 18 2021 Karel Volný <kvolny@redhat.com> - 2.1.0-1
- Update to 2.1.0, soname bump (rhbz#1891224)
- See the upstream changes at https://sourceforge.net/p/sidplay-residfp/news/

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Hans de Goede <hdegoede@redhat.com> - 2.0.4-1
- Update to 2.0.4
- Fixes rhbz#1849704

* Tue May 19 2020 Karel Volný <kvolny@redhat.com> - 2.0.3-1
- Update to 2.0.3 (rhbz#1836331)

* Thu Apr 30 2020 Hans de Goede <hdegoede@redhat.com> - 2.0.2-1
- Update to 2.0.2 (rhbz#1827919)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Karel Volný <kvolny@redhat.com> - 2.0.1-1
- Update to 2.0.1 (rhbz#1750026)

* Tue Aug 27 2019 Karel Volný <kvolny@redhat.com> - 2.0.0-2
- Add dependency on libftdi-c++-devel to enable exsid (rhbz#1723876#c9)

* Wed Aug 21 2019 Karel Volný <kvolny@redhat.com> - 2.0.0-1
- Update to 2.0.0 (rhbz#1723876)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Hans de Goede <hdegoede@redhat.com> - 1.8.8-1
- Update to 1.8.8
- Fix FTBFS (rhbz#1604666)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Karel Volný <kvolny@redhat.com> - 1.8.7-1
- Update to 1.8.7 (#1370763)

* Mon Apr 18 2016 Hans de Goede <hdegoede@redhat.com> - 1.8.6-1
- Update to 1.8.6 (#1327802)

* Tue Apr 12 2016 Hans de Goede <hdegoede@redhat.com> - 1.8.5-1
- Update to 1.8.5 (#1325581)

* Tue Feb 23 2016 Hans de Goede <hdegoede@redhat.com> - 1.8.4-1
- Update to 1.8.4 (#1310477)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Hans de Goede <hdegoede@redhat.com> - 1.8.3-1
- Update to 1.8.3 (#1294551)

* Mon Oct 12 2015 Hans de Goede <hdegoede@redhat.com> - 1.8.2-1
- Update to 1.8.2 (#1270549)

* Fri Aug 14 2015 Hans de Goede <hdegoede@redhat.com> - 1.8.1-1
- Update to 1.8.1 (#1251735)

* Fri Jul 10 2015 Hans de Goede <hdegoede@redhat.com> - 1.8.0-1
- Update to 1.8.0 (#1241728)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Hans de Goede <hdegoede@redhat.com> - 1.7.2-1
- New upstream release 1.7.2 (rhbz#1220146)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Apr  2 2015 Hans de Goede <hdegoede@redhat.com> - 1.7.1-1
- New upstream release 1.7.1 (rhbz#1207460)

* Fri Feb 20 2015 Michael Schwendt <mschwendt@fedoraproject.org> - 1.7.0-2
- Rebuild for GCC 5 C++ ABI changes.

* Thu Jan 29 2015 Hans de Goede <hdegoede@redhat.com> - 1.7.0-1
- New upstream release 1.7.0 (rhbz#1186218)

* Thu Dec 18 2014 Hans de Goede <hdegoede@redhat.com> - 1.6.2-1
- New upstream release 1.6.2 (rhbz#1175174)

* Mon Dec  8 2014 Hans de Goede <hdegoede@redhat.com> - 1.6.1-1
- New upstream release 1.6.1 (rhbz#1170985)

* Thu Oct 16 2014 Hans de Goede <hdegoede@redhat.com> - 1.6.0-1
- New upstream release 1.6.0 (rhbz#1152070)

* Thu Sep 11 2014 Hans de Goede <hdegoede@redhat.com> - 1.5.3-1
- New upstream release 1.5.3 (rhbz#1138944)

* Mon Sep  1 2014 Hans de Goede <hdegoede@redhat.com> - 1.5.2-1
- New upstream release 1.5.2 (rhbz#1133504)

* Tue Aug 26 2014 Hans de Goede <hdegoede@redhat.com> - 1.5.1-1
- New upstream release 1.5.1 (rhbz#1133504)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Hans de Goede <hdegoede@redhat.com> - 1.5.0-1
- New upstream release 1.5.0 (rhbz#1089970)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr  6 2014 Hans de Goede <hdegoede@redhat.com> - 1.4.0-1
- New upstream release 1.4.0 (rhbz#1083942)

* Sat Mar  8 2014 Hans de Goede <hdegoede@redhat.com> - 1.3.0-1
- New upstream release 1.3.0 (rhbz#1026204)

* Wed Dec  4 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1.0-2
- Add "Provides: bundled(md5-deutsch-c++)" as per FPC #361.

* Sun Sep 29 2013 Hans de Goede <hdegoede@redhat.com> - 1.1.0-1
- New upstream release 1.1.0 (rhbz#1001099)

* Wed Aug 21 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.3-1
- New upstream release 1.0.3 (rhbz#999016)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May  1 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.1-4
- Also Obsoletes/Provides the old sidplay1 based libsidplay

* Mon Apr 29 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.1-3
- Add Obsoletes/Provides sidplay-libs[-devel]

* Thu Apr 11 2013 Hans de Goede <hdegoede@redhat.com> - 1.0.1-2
- Some minor style changes
- Fix rpmlint warnings about executable files in debuginfo sub-package
- Add a -devel-doc sub-package

* Mon Apr  8 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.0.1-1
- Initial RPM packaging for Fedora.
