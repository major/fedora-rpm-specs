%global pname   skinenigmang
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-%{pname}
Version:        0.1.5
Release:        2%{?dist}
Summary:        A skin for VDR based on the Enigma text2skin add on

License:        GPL-1.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-skinenigmang
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Source1:        http://andreas.vdr-developer.org/enigmang/download/skinenigmang-logos-xpm-hi-20070702.tgz
Source2:        %{name}.conf
Patch0:         %{name}-config.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  freetype-devel
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
VDR plugin: %{pname} - %{summary}
 
%prep
%autosetup -p1 -n vdr-plugin-skinenigmang-%{version} -a 1
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README
mv skinenigmang/HISTORY HISTORY.logos
mv skinenigmang/README README.logos

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" \
   HAVE_IMAGEMAGICK=GRAPHICS

%install
install -dm 755 $RPM_BUILD_ROOT%{vdr_plugindir}
install -pm 755 libvdr-%{pname}.so \
    $RPM_BUILD_ROOT%{vdr_plugindir}/libvdr-%{pname}.so.%{vdr_apiversion}

# skinenigmang.conf
install -Dpm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

# themes
install -dm 755 $RPM_BUILD_ROOT%{vdr_vardir}/themes
install -pm 644 themes/*.theme $RPM_BUILD_ROOT%{vdr_vardir}/themes

# flags,icons
install -dm 755 $RPM_BUILD_ROOT%{vdr_resdir}
cp -a skinenigmang/{flags,icons} $RPM_BUILD_ROOT%{vdr_resdir}

%files
%doc HISTORY* README*
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/EnigmaNG-*.theme
%{vdr_resdir}/flags
%{vdr_resdir}/icons

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.1.5-1
- Rebuilt for new VDR API version 2.7.2
- Update to 0.1.5

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-11
- Rebuilt for new VDR API version 2.6.9

* Thu Jul 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-10
- Rebuilt for new VDR API version 2.6.8

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.4-9
- convert license to SPDX

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-8
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-7
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-6
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-3
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org>  - 0.1.4-2
- Rebuilt for new VDR API version

* Mon Oct 10 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-1
- Update to new URL
- Update to 0.1.4

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-23.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-22.20180501git995b108
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-21.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-20.20180501git995b108
- Rebuilt for new VDR API version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-19.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-18.20180501git995b108
- Rebuilt for new VDR API version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-17.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-16.20180501git995b108
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-15.20180501git995b108
- Rebuilt for new VDR API version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-14.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-12.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-11.20180501git995b108
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-10.20180501git995b108
- Add BR gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9.20180501git995b108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-8.20150920git3362ab0
- Rebuilt for vdr-2.4.0
- Add %%{name}-0.1.3-min.patch

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7.20150920git3362ab0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6.20150920git3362ab0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5.20150920git3362ab0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4.20150920git3362ab0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3.20150920git3362ab0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 04 2015 Rex Dieter <rdieter@fedoraproject.org> 0.1.3-2.git
- rebuild (GraphicsMagick)

* Sun Sep 20 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.3-1.20150920git3362ab0
- update for new git snapshot

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.2-26
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr 06 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-25
- Rebuild (vdr)

* Mon Mar 09 2015 Rex Dieter <rdieter@fedoraproject.org> 0.1.2-24
- rebuild (GraphicsMagick)

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-23
- Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-20
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-19
- Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-17
- Rebuild.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-16
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-15
- Rebuild.

* Sun Mar 03 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-14
- Rebuild.

* Mon Feb 18 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-13
- Rebuild.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 22 2012 Martin Gansser <martinkg@fedoraproject.org> - 0.1.2-11
- Rebuild.

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-10
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-9
- Adapt to VDR 1.7.30.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.1.2-8
- Rebuild.

* Fri Jun 29 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.2-7
- fixed corrupt osd-signal-information.patch

* Thu Jun 28 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.2-6
- Rebuild
- added OSD patch for signal information
- added patch for Main menu info area with VDR 1.7.28+
- added patch to display free video disk space with VDR 1.7.28+  

* Sun Jun 17 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.2-5
- fixed wrong url
- changed license type from GPLv2+ to GPL+

* Thu Jun 14 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.2-4
- more spec file cleanups
- fixed copying of source file to build dir

* Tue Jun 12 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.2-3
- added config patch
- added flag and icons in file section
- spec file cleanup

* Sat Jun 2 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.2-2
- added patch for GraphicsMagick support
- added patch for disappearing symbols

* Mon Apr 30 2012 Martin Gansser <linux4martin@gmx.de> - 0.1.2-1
- spec cleanup

* Tue Sep 20 2011 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-2
- spec cleanup

* Sat Sep 17 2011 Sebastian Vahl <fedora@deadbabylon.de> - 0.1.1-1
- initial release
