%bcond_without openssl
%bcond_without zlib

Name:           goaccess
Version:        1.12
Release:        %autorelease
Summary:        Real-time web log analyzer and interactive viewer
# Main code and khash.h are MIT
# src/tpl.{c,h} is BSD-1-Clause
# src/pdjson.{c,h} and src/bin2c.c are LicenseRef-Fedora-Public-Domain
# resources/js/hogan.min.js is ASL 2.0 (Apache-2.0)
# resources/js/d3.v7.min.js and resources/js/topojson.v3.min.js are ISC
# resources/css/bootstrap.min.css is MIT
License:        MIT AND BSD-1-Clause AND Apache-2.0 AND ISC AND LicenseRef-Fedora-Public-Domain
URL:            https://goaccess.io/
Source0:        https://tar.goaccess.io/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libmaxminddb-devel
BuildRequires:  ncurses-devel
BuildRequires:  gettext-devel
%if %{with openssl}
BuildRequires:  openssl-devel
%endif
%if %{with zlib}
BuildRequires:  zlib-ng-compat-devel
%endif
BuildRequires:  make

%description
GoAccess is a real-time web log analyzer and interactive viewer that runs in a
terminal in *nix systems. It provides fast and valuable HTTP statistics for
system administrators that require a visual server report on the fly.

Features:
GoAccess parses the specified web log file and outputs the data to terminal.

* General statistics, bandwidth, etc.
* Time taken to serve the request (useful to track pages that are slowing down
your site).
* Metrics for cumulative, average and slowest running requests.
* Top visitors.
* Requested files & static files.
* 404 or Not Found.
* Hosts, Reverse DNS, IP Location.
* Operating Systems.
* Browsers and Spiders.
* Referring Sites & URLs.
* Keyphrases.
* Geo Location - Continent/Country/City.
* Visitors Time Distribution.
* HTTP Status Codes.
* Ability to output JSON and CSV.
* Tailor GoAccess to suit your own color taste/schemes.
* Support for large datasets + data persistence.
* Support for IPv6.
* Output statistics to HTML. 
and more...

GoAccess allows any custom log format string. Predefined options include, but
not limited to:

* Amazon CloudFront (Download Distribution).
* AWS Elastic Load Balancing.
* Apache/Nginx Common/Combined + VHosts.
* Google Cloud Storage.
* W3C format (IIS).

%prep
%autosetup
# Prevent flags being overridden again and again.
#sed -i 's|-pthread|$CFLAGS \0|' configure.ac
sed -i '/-pthread/d' configure.ac

%build
autoreconf -fiv
# %%configure --enable-debug --enable-geoip --enable-utf8 --enable-tcb=btree --with-getline
%configure \
    --enable-debug \
    --enable-geoip=mmdb \
    --enable-utf8 \
    --with-getline \
    %{?with_openssl:--with-openssl} \
    %{?with_zlib:--with-zlib}
%make_build

%install
%make_install
%find_lang %{name}

%check
%{buildroot}%{_bindir}/%{name} --version

%files -f %{name}.lang
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/browsers.list
%config(noreplace) %{_sysconfdir}/%{name}/podcast.list
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
