# Don't build internal static libs as shared
%global _cmake_shared_libs %{nil}

Name:           warzone2100
Version:        4.5.5
Release:        1%{?dist}
Summary:        Innovative 3D real-time strategy

# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://wz2100.net/
Source0:        https://github.com/Warzone2100/warzone2100/releases/download/%{version}/warzone2100_src.tar.xz
Source1:        https://github.com/Warzone2100/wz-sequences/releases/download/v3/high-quality-en-sequences.wz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glslc
BuildRequires:  harfbuzz-devel
BuildRequires:  libcurl-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  p7zip
BuildRequires:  physfs-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  SDL2-devel
BuildRequires:  sqlite-devel
BuildRequires:  vulkan-devel

Requires: hicolor-icon-theme
Recommends: %{name}-sequences

%description
Warzone 2100 was an innovative 3D real-time strategy game back in 1999, and
most will agree it didn't enjoy the commercial success it should have had. The
game's source code was liberated on December 6th, 2004, under a GPL license
(see COPYING in this directory for details). Soon after that, the Warzone 2100
ReDev project was formed to take care of its future.

%package sequences
Summary:        Video file for %{name}
Requires:       %{name}
BuildArch:      noarch

%description sequences
Video file for %{name}.

%prep
%autosetup -n warzone2100 -p1

# Don't use -Werror for distro builds
sed -i -e '/^CONFIGURE_WZ_COMPILER_WARNINGS()$/d' CMakeLists.txt

%build
%cmake -DWZ_DISTRIBUTOR=Fedora
%cmake_build

%install
%cmake_install
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}
%find_lang %{name} --all-name
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/warzone2100/sequences.wz

# Fix icon install path
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mv $RPM_BUILD_ROOT%{_datadir}/icons/net.wz2100.warzone2100.png \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/net.wz2100.warzone2100.png

%files -f %{name}.lang
%license COPYING COPYING.NONGPL COPYING.README
%doc AUTHORS ChangeLog
%{_bindir}/warzone2100
%{_datadir}/applications/net.wz2100.warzone2100.desktop
%{_datadir}/icons/hicolor/128x128/apps/net.wz2100.warzone2100.png
%{_datadir}/metainfo/net.wz2100.warzone2100.metainfo.xml
%{_datadir}/warzone2100/
%exclude %{_datadir}/warzone2100/sequences.wz
%{_mandir}/man6/warzone2100.6*

%files sequences
%{_datadir}/warzone2100/sequences.wz

%changelog
* Tue Jan 14 2025 Pete Walter <pwalter@fedoraproject.org> - 4.5.5-1
- Update to 4.5.5 (rhbz#2324276)

* Wed Oct 02 2024 Pete Walter <pwalter@fedoraproject.org> - 4.5.3-1
- Update to 4.5.3 (rhbz#2312053)

* Wed Sep  4 2024 Miroslav Suchý <msuchy@redhat.com> - 4.5.2-2
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.3.5-4
- Backport upstream patch for new vulkan header (#2242267)

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 4.3.5-3
- rebuild for new libsodium

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Pete Walter <pwalter@fedoraproject.org> - 4.3.5-1
- Update to 4.3.5 (rhbz#2182221)

* Sun Mar 12 2023 Pete Walter <pwalter@fedoraproject.org> - 4.3.3-4
- Fix FTBFS (rhbz#2171756)

* Fri Feb 03 2023 Pete Walter <pwalter@fedoraproject.org> - 4.3.3-3
- ExcludeArch i686 for https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Pete Walter <pwalter@fedoraproject.org> - 4.3.3-1
- Update to 4.3.3 (#2158024)

* Mon Nov 21 2022 Pete Walter <pwalter@fedoraproject.org> - 4.3.2-1
- Update to 4.3.2 (#2134915)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Pete Walter <pwalter@fedoraproject.org> - 4.2.7-1
- Update to 4.2.7

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Pete Walter <pwalter@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1
- Install high quality intro sequences
- Recommends sequences subpackage

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 3.3.0-7
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Jeff Law <law@redhat.org> - 3.3.0-5
- Fix missing #include for gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Pete Walter <pwalter@fedoraproject.org> - 3.3.0-2
- Install icons in hicolor icon theme

* Thu Sep 05 2019 Pete Walter <pwalter@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0 (#1748064)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.2.3-8
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Jan Synáček <jsynacek@redhat.com> - 3.2.3-5
- remove unnecessary build dependency on quesoglc-devel (#1533110)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Apr 24 2017 Jan Synáček <jsynacek@redhat.com> - 3.2.3-1
- Update to 3.2.3 (#1444681)

* Sun Mar 12 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.2-5
- Build with openssl 1.1 now fixed upstream

* Mon Feb 20 2017 Jan Synáček <jsynacek@redhat.com> - 3.2.2-4
- Fix FTBFS (#1424536)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 3.2.2-2
- Rebuild for glew 2.0.0

* Mon Dec  5 2016 Jan Synáček <jsynacek@redhat.com> - 3.2.2-1
- Update to 3.2.2 (#1401273)

* Sun Nov 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.1-2
- Rebuild against compat-openssl10

* Fri Jul 29 2016 Jan Synáček <jsynacek@redhat.com> - 3.2.1-1
- Update to 3.2.1 (#1361438)

* Tue Jul 12 2016 Jan Synáček <jsynacek@redhat.com> - 3.2.0-1
- Update to 3.2.0 (#1354227)

* Tue Apr 12 2016 Jan Synáček <jsynacek@redhat.com> - 3.1.5-1
- Update to 3.1.5 (#1325926)

* Tue Apr  5 2016 Jan Synáček <jsynacek@redhat.com> - 3.1.4-1
- Update to 3.1.4 (#1323678)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jan Synáček <jsynacek@redhat.com> - 3.1.3-1
- Update to 3.1.3 (#1301801)

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 3.1.2-5
- Rebuild for glew 1.13

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.1.2-2
- Add an AppData file for the software center

* Mon Jan  5 2015 Jan Synáček <jsynacek@redhat.com> - 3.1.2-1
- Update to 3.1.2 (#1178445)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Jan Synáček <jsynacek@redhat.com> - 3.1.1-1
- Update to 3.1.1 (#1040915)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 3.1.0-4
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 3.1.0-2
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Tue Jan 15 2013 Jan Synáček <jsynacek@redhat.com> - 3.1.0-1
- Update to 3.1.0

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 3.1-0.11.rc3
- Rebuild for glew 1.9.0

* Wed Oct 17 2012 Jan Synáček <jsynacek@redhat.com> - 3.1-0.10.rc3
- Update to rc3

* Mon Aug 27 2012 Jan Synáček <jsynacek@redhat.com> - 3.1-0.9.rc2
- Update to rc2
- Improve spec again

* Tue Jul 31 2012 Jan Synáček <jsynacek@redhat.com> - 3.1-0.7.beta11
- Rebuilt against new glew
- Make spec more fedora-review friendly

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-0.6.beta11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Jan Synáček <jsynacek@redhat.com> - 3.1-0.5.beta11
- Update to 3.1 beta 11

* Wed May 09 2012 Jan Synáček <jsynacek@redhat.com> - 3.1-0.4.beta9
- Update to 3.1 beta9
- Fix spec

* Wed Mar 21 2012 Jan Synáček <jsynacek@redhat.com> - 3.0-0.3.beta7
- Fix sources

* Wed Mar 21 2012 Jan Synáček <jsynacek@redhat.com> - 3.0-0.2.beta7
- Update to 3.1 beta7

* Thu Mar 15 2012 Jan Synáček <jsynacek@redhat.com> - 3.1-0.1.beta6
- Update to 3.1 beta6

* Thu Jan 05 2012 Jan Synáček <jsynacek@redhat.com> - 2.3.9-2
- Rebuilt for GCC 4.7

* Mon Jan 02 2012 Jan Synáček <jsynacek@redhat.com> - 2.3.9-1
- Update to v2.3.9

* Thu Dec 15 2011 Tom Callaway <spot@fedoraproject.org> - 2.3.7-3
- rebuild for physfs2

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.3.7-2
- Rebuild for new libpng

* Sun Feb 13 2011 Karol Trzcionka <karlik at fedoraproject.org> 2.3.7-1
-Update to v2.3.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 18 2010 Karol Trzcionka <karlikt at gmail.com> - 2.3.4-1
- Update to v2.3.4

* Tue Aug 03 2010 Karol Trzcionka <karlikt at gmail.com> - 2.3.3-1
- Update to v2.3.3
- Sequences in noarch RPM

* Mon Apr 26 2010 Karol Trzcionka <karlikt at gmail.com> - 2.3.0-1
- Update to v2.3.0

* Thu Jan 28 2010 Karol Trzcionka <karlikt at gmail.com> - 2.3-0.2.beta9
- Update to v2.3_beta9

* Sun Jan 10 2010 Karol Trzcionka <karlikt at gmail.com> - 2.3-0.1.beta6
- Update to v2.3_beta6

* Sat Aug 22 2009 Karol Trzcionka <karlikt at gmail.com> - 2.2.1-3
- Rebuilt with new physfs
- Rebuilt with openal-soft-devel instead of openal-devel

* Tue Aug 11 2009 Karol Trzcionka <karlikt at gmail.com> - 2.2.1-2
- Fix BuildRequires

* Tue Aug 11 2009 Karol Trzcionka <karlikt at gmail.com> - 2.2.1-1
- Update to v2.2.1
- Add sequences subpackage

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 Karol Trzcionka <karlikt at gmail.com> - 2.1.2-1
- Update to v2.1.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 06 2009 Karol Trzcionka <karlikt at gmail.com> - 2.1.1-1
- Update to v2.1.1
* Sun Dec 21 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-1
- Update to v2.1.0 stable
* Fri Dec 05 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-0.8.rc2
- Update to v2.1.0-rc2
* Sun Nov 16 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-0.7.rc1
- Update to v2.1.0-rc1
- Fix typo in changelog
- Update License tag
- Fix game-crash while saving and loading (svn revision 6283)
* Thu Oct 02 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-0.6.beta5
- Update to v2.1.0-beta5
* Tue Apr 22 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-0.5.beta2
- Update to v2.1.0-beta2
- Add requires
* Mon Mar 03 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-0.4.beta1
- Fix ppc build
* Sun Mar 02 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-0.3.beta1
- add translations
* Sun Mar 02 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-0.2.beta1
- Fix BRs
* Sun Mar 02 2008 Karol Trzcionka <karlikt at gmail.com> - 2.1.0-0.1.beta1
- Update to v2.1.0-beta1
- Remove ExcludeArch
* Sun Dec 30 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.10-1
- Update to v2.0.10
* Mon Dec 03 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.8-2
- Fix desktop-file for fedora 9
* Mon Dec 03 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.8-1
- Update to v2.0.8 and apply fixsound
* Mon Nov 19 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.8-0.1.rc1
- Update to v2.0.8_rc1
* Wed Oct 17 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.7-5
- Fix build on koji ppc (remove smp_flags)
- set ExcludeArch x86_64 ppc64 sparc64 alpha
* Wed Oct 17 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.7-4
- Merge data subpackage with core package
- Replace ExcludeArch with ExclusiveArch
* Sun Aug 19 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.7-3
- Apply upstream patch
* Sun Jun 24 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.7-2
- Add ppc64 to ExcludeArch
* Sun Jun 24 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.7-1
- Update to v2.0.7
* Sun Apr 08 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.6-2
- Fix build-problem in fedora 7
* Sat Apr 07 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.6-1
- Update to v2.0.6
* Fri Jan 26 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.5-4
- Update BRs for FC-5
* Tue Jan 16 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.5-3
- change ExclusiveArch: i386 to ExcludeArch: x86_64
* Tue Jan 09 2007 Karol Trzcionka <karlikt at gmail.com> - 2.0.5-2
- add an ExclusiveArch
* Sun Dec 31 2006 Karol Trzcionka <karlikt at gmail.com> - 2.0.5-1
- Initial Release
