%global pname   tvguide
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-tvguide
Version:        1.3.9
Release:        2%{?dist}
Summary:        TvGuide is a highly customizable 2D EPG viewer plugin
License:        GPL-2.0-or-later
URL:            https://gitlab.com/kamel5/tvguide
Source0:        https://gitlab.com/kamel5/%{pname}/-/archive/v%{version}/%{pname}-v%{version}.tar.bz2
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
VDR plugin: tvguide - %{summary}

%prep
%autosetup -p1 -n %{pname}-v%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" IMAGELIB=graphicsmagick

%install
# make install would install the themes under /etc, let's not use that
make install-lib install-i18n install-icons DESTDIR=%{buildroot}
# install the themes to the custom location used in Fedora
install -dm 755 %{buildroot}%{vdr_vardir}/themes
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/

# tvguide.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/tvguide.conf

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING HISTORY* README*
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/tvguide.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/tvguide-*.theme
%{vdr_resdir}/plugins/tvguide/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.9-1
- Rebuilt for new VDR API version 2.7.2
- Update to 1.3.9

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.8-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.8-6
- Rebuilt for new VDR API version 2.6.9

* Thu Jul 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.8-5
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.8-4
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.8-3
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.3.8-2
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Wed Nov 22 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.8-1
- Update to 1.3.8

* Sat Aug 26 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.7-1
- Update to 1.3.7

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.3.6-5
- Rebuilt against graphicsmagick due new ImageMagick 7

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.3.6-4
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.3.6-3
- Rebuilt for new VDR API version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.3.6-1
- Update to 1.3.6

* Mon May 02 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.3.5-7
- Add Fixed-possible-segfault-when-showing-scrollbar.patch

* Sat Feb 05 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.3.5-6
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.3.5-4
- Rebuilt for new VDR API version

* Fri Nov 26 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.5-1.1
- rebuild for new ImageMagick

* Sat Oct 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.3.5-3
- Rebuilt due FTI in rawhide

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.3.5-1
- Update to 1.3.5

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.3.4-3
- Rebuilt for new VDR API version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.3.3-5
- Rebuilt for new VDR API version

* Sat Nov 14 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.3-4
- Use Imagemagick due segfault with Graphicsmagick fix (BZ#1897776)

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.3-3
- Rebuilt for new VDR API version

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1.3.3-2
- Force C++14 as this code is not C++17 ready

* Fri Aug 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.3-1
- Update to 1.3.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Sun Mar 08 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Tue Feb 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.17-1
- Update to 1.2.17

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-1
- Update to 1.2.16

* Mon Nov 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.15-1
- Update to 1.2.15

* Sun Oct 20 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.14-1
- Update to 1.2.14

* Tue Oct 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.13-1
- Update to 1.2.13

* Mon Oct 14 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12

* Wed Sep 11 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.11-1
- Update to 1.2.11
- Use Graphicsmagick again, fixed segfault with graphicsmagick > 1.3.31

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.10-1
- Update to 1.2.10

* Fri Jul 05 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9

* Tue Jul 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.8-2
- Use Imagemagick due segfault with Graphicsmagick

* Sat Jun 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8
- Spec file cleanup

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-18
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-16
- Fix FTBFS due missing BR gcc (RHBZ#1606892)
- Add vdr-2.3.1-tvguide.diff
- Add vdr-2.3.5-tvguide.diff
- Add vdr-2.3.7-tvguide.diff

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 04 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-9
- rebuild(GraphicsMagick)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.2-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr 06 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.2.2-6
- Rebuild (vdr)

* Mon Mar 09 2015 Rex Dieter <rdieter@fedoraproject.org> 1.2.2-5
- rebuild (GraphicsMagick)

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.2.2-4
- Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.2.1-3
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.2.1-2
- Rebuild

* Sat Feb 08 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Mon Feb 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-2
- removed BuildRequires on freetype-devel

* Sat Feb 01 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- rebuild for new release
- replaced ImageMagick as requirement due big dependencies through GraphicsMagick

* Wed Jan 29 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-11
- reverted back to stable branch
- added ImageMagick-c++-devel package
- spec file cleanup

* Mon Jan 27 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-10.20140126git5eabb6e
- rebuild for new git release
- added correct license tag
- removed data subpackage
- removed ImageMagick-c++-devel package
- added GraphicsMagick-c++-devel package
- added CXXFLAGS and -fPIC build flag

* Wed Jan 22 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-9.20140122git0d3d2ef
- rebuild for new git release
- removed GraphicsMagick patch

* Wed Jan 22 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-8.20140117git662a17d
- replaced ImageMagick as requirement due big dependencies through GraphicsMagick
- added Patch to compile with GraphicsMagick
- replaced RPM_BUILD_ROOT macro through %%{buildroot}

* Sun Jan 19 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-7.20140119gita65fca4
- rebuild for new git release
- added vdr-tvguide-data as requirement
- corrected tarball download instructions

* Wed Jan 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-6.20140114gitd0651a4
- installed themes and themeconfigs to the custom location used in Fedora
- added gitdate for fedora naming schema
- added tarball download instructions

* Tue Jan 14 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-5.a8b7c95
- rebuild for new git release

* Sun Jan 12 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-4.d0651a4
- rebuild for new git release

* Sat Jan 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-3.3121910
- rebuild for new git release
- added themes and themeconfigs file
- added compiler flags in build section
- removed additional localization install section
- corrected path to README in skinnopacity.conf
- added icons directory to noarch sub-package

* Sat Jan 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-2.15dbae6
- rebuild for new git release

* Sun Sep 15 2013 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1
- rebuild for new release

* Fri Jul 12 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.0.6-1
- rebuild for new release

* Sun Jun 02 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.0.5-1
- rebuild for new release

* Fri May 24 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-1
- rebuild for new git version

* Sun Mar 31 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.0.2-1
- rebuild.

