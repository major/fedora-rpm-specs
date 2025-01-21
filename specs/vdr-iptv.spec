# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-iptv
Version:        2.4.0
Release:        33%{?dist}
Summary:        IPTV plugin for VDR
License:        GPL-2.0-or-later
URL:            https://github.com/rofafor/vdr-plugin-iptv
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  gettext
BuildRequires:  libcurl-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin integrates multicast IPTV transport streams seamlessly into
VDR. You can use any IPTV channel like any other normal DVB channel for
live viewing, recording, etc. The plugin also features full section
filtering capabilities which allow for example EIT information to be
extracted from the incoming stream.

%prep
%setup -q -n vdr-plugin-iptv-%{version}

# Fix paths in plugin scripts as defined by Fedora
sed -i "s|^CHANNELS_CONF=.*|CHANNELS_CONF=%{vdr_configdir}/channels.conf|; \
        s|^CHANNEL_SETTINGS_DIR=.*/iptv|CHANNEL_SETTINGS_DIR=%{vdr_configdir}/plugins/%{vdr_plugin}|" \
        iptv/vlc2iptv

%build
%make_install CFLAGS="%{optflags} -fPIC" CXXFLAGS="-std=gnu++14 %{optflags} -fPIC" STRIP=:

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY README
%license COPYING
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%dir %{vdr_configdir}/plugins/iptv
%config(noreplace) %{vdr_resdir}/plugins/iptv/*.sh
%config(noreplace) %{vdr_resdir}/plugins/iptv/vlc2iptv

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-32
- Rebuilt for new VDR API version 2.7.2

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-31
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-29
- Rebuilt for new VDR API version 2.6.9

* Fri Jul 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-28
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-27
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-26
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-25
- Rebuilt for new VDR API version

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-22
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-21
- Rebuilt for new VDR API version

* Thu Aug 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-20
- Update to new github address

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-18
- Rebuilt for new VDR API version

* Sat Jan 29 2022 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-17
- Add %%undefine _package_note_flags to vdr main package
- rebuild for rawhide

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-15
- Rebuilt for new VDR API version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-13
- Rebuilt for new VDR API version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-11
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-10
- Rebuilt for new VDR API version

* Wed Aug 19 2020 Jeff Law <law@redhat.com> - 2.4.0-9
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-5
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-3
- Rebuilt

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-5
- Patch to fix build with -std=c++11

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr 06 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
- Mark license files as %%license where available

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-12
- Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-9
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-8
- Rebuild

* Sat Feb 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-7
- added STRIP to get a usefull debuginfo package

* Wed Feb 12 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-6
- added %%dir for %%{vdr_configdir}/plugins/iptv

* Wed Feb 12 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-5
- added noreplace to prevent config files to be overwritten

* Mon Feb 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-4
- replaced gettext-devel by gettext in BuildRequires
- dropped iptv.conf file

* Mon Feb 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-3
- added compiler flags in build section
- fixed paths in plugin scripts for channels.conf

* Tue Jan 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-2
- corrected discription in vdr-iptv.conf file

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-1
- Initial build

