%global pname     streamdev
# If this variable is set the spec file assumes it's building a git snapshot
# Also see info below on generating snapshots
%global gitver    b84b7d858cf4f6f3473ba72d456326c048946cb0
%global gitshort  %(echo %gitver | awk '{print substr($0,1,8)}')
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

%if 0%{?gitver:0}
  # Use vdr-streamdev-snapshot.sh contained in the source of the package to
  # generate new snapshots
  # You can also create snapshots for specific commit hashes
  # Example: sh vdr-streamdev-snapshot.sh b84b7d858cf4f6f3473ba72d456326c048946cb0
  %global srcfile   %{name}-%{gitshort}.tar.xz
  %global setuppath %{name}-%{gitshort}
%else
  # URL for original source file when not using git snapshots
  %global srcfile   https://github.com/vdr-projects/vdr-plugin-streamdev/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
  %global setuppath %{pname}-%{version}
%endif

Name:           vdr-%{pname}
Version:        0.6.4
%if 0%{?gitver:0}
Release:        0.44%{?gitver:.git%{gitshort}}%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        Streaming plug-in for VDR
License:        GPL-1.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-streamdev

Source0:        %{srcfile}
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}-server.conf
Source2:        %{name}-client.conf
# Script to generate git snapshots
# listed here so that it's pulled into the SRPM
Source3:        %{name}-snapshot.sh

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}

%description
The streamdev plug-in adds streaming capabilities to your VDR.

%package server
Summary:        Streaming server plug-in for VDR
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description server
Lets your VDR act as a streaming server for other clients.
This will let you watch TV or Recordings across the network.

%package client
Summary:        Streaming client plug-in for VDR
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description client
Lets your VDR in conjunction with a streamdev-server act as a streaming client.
VDR will then be able to work even without a DVB device.

%prep
%if 0%{?gitver:0}
%autosetup -p1 -n %{setuppath}
%else
%autosetup -p1 -n vdr-plugin-streamdev-%{version}
%endif

sed -i 's@$(VDRDIR)/device.h@%{_includedir}/vdr/device.h@' Makefile

for f in CONTRIBUTORS HISTORY; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install
install -dm 755 $RPM_BUILD_ROOT%{vdr_configdir}/plugins/streamdev-server
install -Dpm 644 streamdev-server/streamdevhosts.conf $RPM_BUILD_ROOT%{vdr_configdir}/plugins/streamdev-server/streamdevhosts.conf
install -Dpm 755 streamdev-server/externremux.sh $RPM_BUILD_ROOT%{_libdir}/vdr/bin/externremux.sh 
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-server.conf
install -Dpm 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-client.conf
%find_lang %{name}-server
%find_lang %{name}-client

%files server -f %{name}-server.lang
%doc CONTRIBUTORS COPYING HISTORY PROTOCOL README
%{vdr_plugindir}/libvdr-%{pname}-server.so.%{vdr_apiversion}
%{_libdir}/vdr/bin/externremux.sh
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-server.conf
%dir %{vdr_configdir}/plugins/streamdev-server
%config(noreplace) %{vdr_configdir}/plugins/streamdev-server/streamdevhosts.conf

%files client -f %{name}-client.lang
%doc CONTRIBUTORS COPYING HISTORY PROTOCOL README
%{vdr_plugindir}/libvdr-%{pname}-client.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}-client.conf

%changelog
* Thu Jan 02 2025 Martin Gansser <martinkg@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-14
- Rebuilt for new VDR API version 2.7.2

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.3-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-11
- Rebuilt for new VDR API version 2.6.9

* Thu Jul 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-10
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-9
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-8
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-7
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-4
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-3
- Rebuilt for new VDR API version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Sat Feb 05 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.33.gitb84b7d85
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.32.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.31.gitb84b7d85
- Rebuilt for new VDR API version
- Add streamdev-server-2.5.4-patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.30.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.29.gitb84b7d85
- Rebuilt for new VDR API version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.28.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.27.gitb84b7d85
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.26.gitb84b7d85
- Rebuilt for new VDR API version

* Fri Aug 14 2020 Jeff Law <law@redhat.com> - 0.6.1-0.25.gitb84b7d85
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.24.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.23.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.22.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.21.gitb84b7d85
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.20.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.19.gitb84b7d85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-0.18.gitb84b7d85
- Rebuild for vdr-2.4.0
- Update to 0.6.1-0.18.gitb84b7d8
- Add 0001-Fixed-compilation-for-vdr-2.3.7.diff

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.17.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.16.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.15.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.14.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-0.13.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-0.12.git84c6f6b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 07 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.6.1-0.11.git84c6f6b6
- fix compile for VDR 2.2 and F22+
- use make install

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-0.10.git10db11ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-0.9.git10db11ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.8.git10db11ac
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.7.git10db11ac
- Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-0.6.git10db11ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.5.git10db11ac
- Rebuild.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.4.git10db11ac
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.3.git10db11ac
- Rebuild.

* Sun Mar 03 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-0.2.git10db11ac
- Rebuild.

* Thu Feb 21 2013 Felix Kaechele <heffer@fedoraproject.org> - 0.6.1-0.1.git10db11ac
- update to latest git snapshot for VDR 1.7.38 support
- modified spec to easily support git snapshots
- cleanup spec: remove old macros and constructs

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-4
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-3
- Rebuild.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-2
- Make vdr(abi) deps arch qualified.

* Wed Jul 04 2012 Felix Kaechele <heffer@fedoraproject.org> - 0.6.0-1
- update to 0.6.0
- drop all patches as upstream includes them already

* Tue Mar 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-12
- Rebuild.

* Sun Mar 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-11
- Apply upstream VDR 1.7.26+ patches.

* Tue Mar  6 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-10
- Apply upstream VDR 1.7.25+ patches.

* Mon Feb 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-9
- Rebuild.

* Sun Jan 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-8
- Rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-6
- Rebuild.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-5
- Fix build with Liemikuutio patch 1.32.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-4
- Install locale files (#750084).

* Sun Oct 23 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.5.1-3
- own the configuration dir
- add patch to fix the GPL in COPYING and the FSF address in some source files

* Sat Oct 08 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.5.1-2
- move streamdevhosts.conf to the right directory

* Sat Feb 12 2011 Felix Kaechele <heffer@fedoraproject.org> - 0.5.1-1
- update to latest upstream release
- see HISTORY for full changelog

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 25 2010 Felix Kaechele <heffer@fedoraproject.org> - 0.5.0-1
- update to final 0.5.0 release

* Sat Jan 02 2010 Felix Kaechele <heffer@fedoraproject.org> - 0.5.0-0.2.pre20090706
- added missing BuildReq: gettext

* Fri Dec 18 2009 Felix Kaechele <heffer@fedoraproject.org> - 0.5.0-0.1.pre20090706
- update to latest version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 30 2008 Felix Kaechele <felix at fetzig dot org> - 0.3.4-2
- Incorporated fixes suggested in bug #454120
* Fri Jul  4 2008 Felix Kaechele <felix at fetzig dot org> - 0.3.4-1
- Initial Build
