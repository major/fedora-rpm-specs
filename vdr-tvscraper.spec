%global pname   tvscraper
# version we want build against
%global vdr_version 2.4.0
%if 0%{?fedora} >= 36
%global vdr_version 2.6.1
%endif
%if 0%{?fedora} == 35
%global vdr_version 2.4.7
%endif

Name:           vdr-%{pname}
Version:        1.1.6
Release:        1%{?dist}
Summary:        Collects metadata for all available EPG events
# The entire source code is GPLv2+ except tools/curlfuncs.* which is BSD (3 clause)
License:        GPL-2.0-or-later AND MIT
URL:            https://github.com/MarkusEh/vdr-plugin-tvscraper
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  sqlite-devel
BuildRequires:  libcurl-devel
# BuildRequires:  libxml2-devel
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
%autosetup -p0 -n vdr-plugin-%{pname}-%{version}

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
%doc HISTORY
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%dir %{vdr_configdir}/plugins/%{pname}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/tvscraper.conf
%config(noreplace) %{vdr_configdir}/plugins/%{pname}/override.conf
%attr(-,%{vdr_user},root) %dir %{vdr_cachedir}/%{pname}/

%changelog
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
