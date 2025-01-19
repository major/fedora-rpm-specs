%global project_owner MapServer
%global project_name mapcache

%global maj 1
%global min 14
%global micro 1

ExcludeArch: i686

Name:           mod_mapcache
Version:        %{maj}.%{min}.%{micro}
Release:        3%{?dist}
Summary:        Caching server for WMS layers

# mapcache-1.14.0/lib/hmac-sha.c - bsd-3
# mapcache-1.14.0/lib/strptime.c - bsd-3
License:        MIT AND BSD-3-Clause
URL:            http://mapserver.org/mapcache/

Source:         https://github.com/%{project_owner}/%{project_name}/releases/download/rel-%{maj}-%{min}-%{micro}/mapcache-%{version}.tar.gz
Source:         mapcache.sysusers

Source:         https://salsa.debian.org/debian-gis-team/mapcache/-/raw/master/debian/man/mapcache_detail.1.xml
Source:         https://salsa.debian.org/debian-gis-team/mapcache/-/raw/master/debian/man/mapcache_seed.1.xml

Requires:       httpd
Requires:       libmapcache%{?_isa} = %{version}-%{release}

BuildRequires: chrpath
BuildRequires: cmake
BuildRequires: fcgi-devel
BuildRequires: gcc
BuildRequires: gdal-devel
BuildRequires: geos-devel
BuildRequires: httpd-devel
BuildRequires: libcurl-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libmemcached-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: lmdb-devel
BuildRequires: pixman-devel
BuildRequires: proj-devel
BuildRequires: sqlite-devel
BuildRequires: systemd-rpm-macros
BuildRequires: xmltoman

%global _description %{expand:
MapCache is a server that implements tile caching to speed up access to WMS
layers.  The primary objectives are to be fast and easily deployable, while
offering the  essential features (and more!) expected from a tile caching
solution.}

%description %{_description}
This is the MapCache module for the Apache web server implementing OGC web
services. An alternative mapcache FastCGI program is available in
libmapcache-fcgi.

%pre
%sysusers_create_compat %{SOURCE1}

%package -n libmapcache
Summary: The shared library for mapcache
Requires: mapserver%{?_isa}

%description -n libmapcache %{_description}
The shared library files for libmapcache

%package -n libmapcache-devel
Summary: Development files for mapcache

%description -n libmapcache-devel %{_description}
Development files for mapcache; these files are needed when building binary
packages against libmapcache.

%package -n libmapcache-doc
Summary: Documentation files for mapcache
BuildArch: noarch

%description -n libmapcache-doc %{_description}
Documentation files for mapcache.

%package -n libmapcache-fcgi
Summary: An fcgi implementation for mapcache
Requires: libmapcache%{?_isa} = %{version}-%{release}

%description -n libmapcache-fcgi %{_description}
This package contains the mapcache FastCGI program, as alternative to the
 Apache module available in mod_mapcache.

%package -n libmapcache-tools
Summary: Tools for mapcache

%description -n libmapcache-tools %{_description}
Provides command-line utilities for mapcache

%prep
%autosetup -n %{project_name}-%{version}

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DWITH_MEMCACHE=1 -DCMAKE_SKIP_BUILD_RPATH=TRUE . 
%cmake_build

%install
%cmake_install

for f in \
  %{buildroot}%{_bindir}/{mapcache_seed,mapcache.fcgi,mapcache_detail} \
  %{buildroot}%{_libdir}/libmapcache.so* \
  %{buildroot}%{_libdir}/httpd/modules/mod_mapcache.so;
do
 chrpath --delete $f 
done

install -p -D -m 0644 mapcache.xml %{buildroot}%{_sysconfdir}/mapcache.xml
install -p -D -m 0644 mapcache.xml.sample %{buildroot}%{_datadir}/mapcache/mapcache.xml.sample

pushd include
for f in *.h; do
  install -p -D -m 0644 $f %{buildroot}%{_includedir}/libmapcache/$f;
done
popd

install -p -D -d -m 0755 %{buildroot}%{_localstatedir}/cache/mapcache/

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/mapcache.conf


install -p -D -d -m 0755 %{buildroot}%{_mandir}/man1

xmltoman %{SOURCE2} > %{buildroot}%{_mandir}/man1/mapcache_detail.1
xmltoman %{SOURCE3} > %{buildroot}%{_mandir}/man1/mapcache_seed.1

%files
%license LICENSE.md
%{_libdir}/httpd/modules/mod_mapcache.so
%config(noreplace) %{_sysconfdir}/mapcache.xml
%dir %{_datadir}/mapcache
%{_datadir}/mapcache/mapcache.xml.sample

%files -n libmapcache
%{_libdir}/libmapcache.so.%{version}
%{_libdir}/libmapcache.so.1
%dir %{_localstatedir}/cache/mapcache
%{_sysusersdir}/mapcache.conf

%files -n libmapcache-doc
%doc INSTALL.md README.md
%{_mandir}/man1/mapcache_seed.1*
%{_mandir}/man1/mapcache_detail.1*

%files -n libmapcache-devel
%{_libdir}/libmapcache.so
%dir %{_includedir}/libmapcache/
%{_includedir}/libmapcache/*.h

%files -n libmapcache-fcgi
%{_bindir}/mapcache.fcgi

%files -n libmapcache-tools
%{_bindir}/mapcache_detail
%{_bindir}/mapcache_seed


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 10 2024 Neil Hanlon <neil@rockylinux.org> - 1.14.1-2
- rebuild for mapserver 8.2.2

* Mon Aug 19 2024 Neil Hanlon <neil@shrug.pw> - 1.14.1-1
- update to 1.14.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Neil Hanlon <neil@shrug.pw - 1.14.0-1
- address review comments for initial package release

* Tue Mar 26 2024 Neil Hanlon <neil@shrug.pw> - 1.14.0-1
- add mapcache header files
- add Requires on libmapcache to mapserver

* Mon Mar 11 2024 Neil Hanlon <neil@shrug.pw> - 1.14.0-1
- Include mapcache.xml
- split into subpackages following debian as a guide

* Thu Feb 29 2024 Neil Hanlon <neil@shrug.pw> - 1.14.0-0
- Initial package based on work from ElNinijo
