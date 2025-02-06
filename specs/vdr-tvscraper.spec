%global pname   tvscraper
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-%{pname}
Version:        1.2.12
Release:        1%{?dist}
Summary:        Collects metadata for all available EPG events
# The entire source code is GPLv2+ except tools/curlfuncs.* which is BSD (3 clause)
License:        GPL-2.0-or-later AND MIT
URL:            https://github.com/MarkusEh/vdr-plugin-tvscraper
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/vdr-plugin-tvscraper-%{version}.tar.gz
Source1:        %{name}.conf

# Build for armv7hl failed
ExcludeArch:    armv7hl

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  sqlite-devel
BuildRequires:  libcurl-devel
BuildRequires:  jansson-devel
BuildRequires:  vdr-devel >= %{vdr_version} 
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
TVScraper runs in the background and collects metadata (posters,
banners, fanart, actor thumbs and roles, descriptions) for all
available EPG events on selectable channels and for recordings.
Additionally the plugin provides the collected metadata via the VDR
service interface to other plugins which deal with EPG information.

TVScraper uses the thetvdb.com API for collecting series metadata and
themoviedb.org API for movies. Check the websites of both services for
the terms of use.

Important: To avoid unnecessary traffic, only activate these channels
to be scrapped which are reasonable. After plugin installation all
channels are deactivated by default, so please consider this point when
you activate the channels you are interested in ;)

Additionally you are invited to contribute to the used web services with
providing missing data for your favorite movies and series.

%prep
%autosetup -p1 -n vdr-plugin-%{pname}-%{version}

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/tvscraper.conf
install -dm 755 %{buildroot}%{vdr_cachedir}/%{pname}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README.md
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%dir %{vdr_configdir}/plugins/%{pname}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/tvscraper.conf
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/override.conf
%config(noreplace) %{_datadir}/vdr/plugins/%{pname}/override_tvs.conf
%config(noreplace) %{_datadir}/vdr/plugins/%{pname}/networks.json
%attr(-,%{vdr_user},root) %dir %{vdr_cachedir}/%{pname}/

%changelog
* Tue Feb 04 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 25 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.11-1
- Update to 1.2.11

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2.10-2
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.10-1
- Rebuilt for new VDR API version 2.7.2
- Update to 1.2.10

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.9-4
- Rebuilt for new VDR API version 2.6.9

* Fri Jul 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.9-3
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.9-2
- Rebuilt for new VDR API version

* Wed Apr 10 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9

* Sun Jan 28 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.6-2
- Rebuilt for new VDR API version

* Thu Jan 04 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6

* Mon Nov 27 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Thu Sep 07 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Tue Aug 22 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Sat Aug 05 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 18 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sun Jun 11 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.1.13-1
- Update to 1.1.13

* Mon Mar 06 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.1.11-1
- Update to 1.1.11

* Sun Jan 29 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.1.10-1
- Update to 1.1.10

* Tue Jan 24 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.1.9-1
- Update to 1.1.9

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.8-3
- Rebuilt for new VDR API version

* Fri Dec 02 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.8-2
- Rebuilt for new VDR API version

* Fri Oct 28 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.8-1
- Update to 1.1.8-1

* Wed Oct 12 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.7-1
- Update to 1.1.7-1

* Sat Sep 24 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6-1

* Sat Sep 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5-1

* Fri Aug 19 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4-1

* Sat Aug 13 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3-1

* Thu Aug 11 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2-1
- Add %%{name}-f35.patch

* Tue Aug 09 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-2
- Update license tag to "GPL-2.0-or-later AND MIT"
- Add BR gettext

* Mon Aug 08 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-2
- Update to 1.1.1-1
- Added %%dir %%{vdr_configdir}/plugins/%%{pname} because it's owned by the package

* Tue Jun 21 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-1
- initial release
