#
# Copyright (c) 2004-2015 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Summary: Volume rendering library for Coin
Name: SIMVoleon
Version: 2.1.0
Release: 8%{?dist}

# Older releases had been licensed GPLv2
License: BSD-3-Clause
URL: http://www.coin3d.org

Source: https://github.com/coin3d/simvoleon/releases/download/simvoleon-%{version}/simvoleon-%{version}-src.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: /usr/bin/iconv
BuildRequires: Coin4-devel
BuildRequires: SoQt-devel
BuildRequires: doxygen

Provides: Coin4-SIMVoleon = %{version}-%{release}

%description
A volume rendering library for Coin.

%package devel
Summary: Development files for SIMVoleon
Requires: %{name} = %{version}-%{release}
Requires: Coin4-devel

Provides: Coin4-SIMVoleon-devel = %{version}-%{release}

%description devel
Development files for SIMVoleon.


%prep
%setup -n simvoleon

# Some sources are ISO-8859-1 encoded
# We want doxygen to generate utf-8 encoded docs from them
for nonUTF8 in \
  lib/VolumeViz/readers/VRVolFileReader.cpp \
; do \
  %{_bindir}/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
  mv -f $nonUTF8.conv $nonUTF8
done

# No timestamps in doxygen generated docs!
sed -i -e 's,HTML_TIMESTAMP.*= YES,HTML_TIMESTAMP = NO,' \
  docs/simvoleon.doxygen.cmake.in


%build
mkdir -p build-%{_build_arch}
pushd build-%{_build_arch}
%cmake -DSIMVOLEON_BUILD_DOCUMENTATION=TRUE \
       -DSIMVOLEON_BUILD_TESTS=FALSE \
       -DSIMVOLEON_BUILD_DOC_MAN=TRUE \
       -S .. -B .

%make_build
popd

%install
pushd build-%{_build_arch}
%make_install

# Remove stray files
rm -rf %{buildroot}/usr/share/info/SIMVoleon2/
popd

%files
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_libdir}/libSIMVoleon*.so.*

%files devel
%{_docdir}/SIMVoleon/html/
%{_includedir}/VolumeViz/
%{_libdir}/libSIMVoleon.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}-%{version}/
%{_mandir}/man3/*.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-4
- Rebuild for Coin4.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 15 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.1.0-1
- Upgrade to 2.1.0.
- Convert license to SPDX.
- Remove bogusly installed /usr/share/info/SIMVoleon2.
- Fix broken handling of non-utf8 sources.
- Switch off HTML_TIMESTAMPs.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.3-5
- Work around cmake madness (F33FTBFS, RHBZ#1863119).

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-1
- Update to 2.0.3.
- Move from autotools to CMake based build.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 27 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-23
- Eliminate %%define.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-21
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 27 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-20
- Add Provides: Coin3-SIMVoleon, Coin3-SIMVoleon.

* Thu Feb 26 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-19
- Rebuild against Coin3.
- Modernise spec.
- Remove %%optflags and %%__global_ld_flags from *.cfg.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-15
- Modernize spec.
- Update config.{guess,sub} for aarch64 (RHBZ #926532).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 28 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.0.1-10
- Add SIMVoleon-2.0.1-pivy-hacks.diff, SIMVoleon-2.0.1-bash4.0.diff.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-8
- Rebuild for gcc43.
- Spec-file cosmetics.
- Update copyright.

* Wed Aug 22 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-7
- Mass rebuild.
- Update license tag.

* Tue Feb 20 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-6
- Install simvoleon-default.cfg into %%{_prefix}/%%{_lib}

* Mon Feb 19 2007 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-5
- Filter errant -L%%_libdir from soqt-config.cfg.
- Remove *.la.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-4
- Mass rebuild.

* Tue Feb 28  2006 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-3
- Rebuild.

* Mon Jan 16  2006 Ralf Corsépius <rc040203@freenet.de> - 2.0.1-2
- Rebuild.
- Add gcc4.1 patch.
- Spec cleanup.

* Sat May 21  2005 Ralf Corsepius <ralf@links2linux.de> - 2.0.1-1
- FE submission candidate.

* Mon Oct 11  2004 Ralf Corsepius <ralf@links2linux.de> - 0:2.0.0-0.fdr.1
- Upstream update.

* Tue Jul 27  2004 Ralf Corsepius <ralf@links2linux.de> - 0:1.0.0-0.fdr.1
- Initial Fedora RPM.
