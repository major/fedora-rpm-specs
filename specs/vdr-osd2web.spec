## This macro activates/deactivates debug option
%bcond_with debug
%global pname   osd2web
%global rname   vdr-plugin-osd2web
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-%{pname}
Version:        0.3.2
Release:        12%{?dist}
Summary:        VDR skin interface for the browser
License:        GPL-2.0-or-later
URL:            https://github.com/horchi/vdr-plugin-osd2web
Source0:        https://github.com/horchi/vdr-plugin-osd2web/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  libwebsockets-devel
BuildRequires:  zlib-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  jansson-devel
BuildRequires:  libexif-devel
BuildRequires:  libuuid-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
osd2web is a VDR skin interface for the browser, which displays the OSD
and allows all interactions which are possible on the OSD.

%prep
%autosetup -n %{rname}-%{version}

## Optimization flags in 'Make.config' file
sed -i \
    -e 's|PREFIX   = /usr/local|PREFIX   =  %{_prefix}|' \
    -e 's|CXXFLAGS += -O3|CXXFLAGS += %{optflags}|' \
    -e 's|@@OPTFLAGS | %{optflags}|' \
    Make.config

%if %{without debug}
sed -i -e 's|DEBUG = 1||' Make.config
%endif

%build
%make_build

%install
%make_install

install -Dpm 644 %{SOURCE1} \
  %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{name}.conf

# fix the perm due W: unstripped-binary-or-object
chmod 0755 %{buildroot}/%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

# install executable to %%{vdr_plugindir} due E: executable-marked-as-config-file
rm -rf %{buildroot}/%{vdr_configdir}/plugins/osd2web/startBrowser.sh
install -Dpm 755 scripts/startBrowser.sh %{buildroot}%{vdr_plugindir}/bin/startBrowser.sh

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE COPYING
%doc README
%dir %{vdr_configdir}/plugins/osd2web/
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{name}.conf
%{vdr_plugindir}/libvdr-%{pname}.so.%{vdr_apiversion}
%config(noreplace) %{vdr_configdir}/plugins/osd2web/*
%{vdr_plugindir}/bin/startBrowser.sh

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.3.2-11
- rebuild for tinyxml2

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 0.3.2-10
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-9
- Rebuilt for new VDR API version 2.7.2

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.2-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-6
- Rebuilt for new VDR API version 2.6.9

* Fri Jul 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-5
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-4
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-3
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-2
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Mon Oct 23 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Wed Oct 18 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Wed Oct 11 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.2.58-1
- Update to 0.2.58

* Sun Mar 12 2023 Martin Gansser <martinkg@fedoraproject.org> - 0.2.56-1
- Update to 0.2.56

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.54-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-16
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-15
- Rebuilt for new VDR API version

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 0.2.54-14
- Rebuild for tinyxml2-9.0.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.54-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-12
- Rebuilt due an SONAME bump of libwebsockets to 4.3.1

* Fri Feb 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-11
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.54-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-9
- Rebuilt for new VDR API version

* Thu Aug 26 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-8
- Rebuilt due an SONAME bump of libwebsockets to 4.2.0

* Fri Jul 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-7
- Add %%{name}-ambiguous.patch fixes (BZ#1988033)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-5
- Rebuilt for new VDR API version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-3
- Rebuilt for new VDR API version

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-2
- Rebuilt for new VDR API version

* Sun Sep 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-1
- Rebuilt for new libwebsockets
- Update to 0.2.54

* Sun Aug 02 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.52-1
- Update to 0.2.52
- Rebuilt for new VDR API version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.50-1
- Update to 0.2.50
- Rebuilt due an SONAME bump of libwebsockets to 4.0.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.49-4
- Rebuilt for new libwebsocket version 

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.49-2
- Rebuilt for new VDR API version

* Fri May 31 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.49-1
- Update to 0.2.49

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.48-3
- Rebuilt for new libwebsockets

* Fri Nov 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.2.48-2
- Use %%{version} for SOURCE tag
- Use %%bcond_with/without for debugging flag
- Mark COPYING as %%license file
- Use korrekt license GPLv2+
- take ownership of unowned directory %%{vdr_configdir}/plugins/osd2web/

* Wed Nov 07 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.2.48-1
- Initial build
