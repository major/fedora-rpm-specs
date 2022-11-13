%global nagiospluginsdir %{_libdir}/nagios/plugins
Name:           nagios-plugins-ssl_cert
Version:        2.54.0
Release:        %autorelease
Summary:        Nagios Plugin - check_ssl_cert

License:        GPL-3.0-or-later
URL:            https://exchange.nagios.org/directory/Plugins/Network-Protocols/HTTP/check_ssl_cert/details
Source:         https://github.com/matteocorti/check_ssl_cert/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       /usr/bin/bash
Requires:       /usr/bin/bc
Requires:       /usr/bin/curl
Requires:       /usr/bin/date
Requires:       /usr/bin/openssl
Requires:       nagios-plugins
Requires:       perl(Date::Parse)

Recommends:     /usr/bin/dig
Recommends:     /usr/bin/expand
Recommends:     /usr/bin/timeout
Recommends:     /usr/sbin/ip

BuildRequires:  make

# The package does not contain any architecture-dependent things, but installs
# into an arch-dependent directory. Thus, it cannot be noarch, but it does not
# provide any debuginfo.
%global debug_package %{nil}

%description
A POSIX shell script (that can be used as a Nagios/Icinga plugin) to check an
SSL/TLS connection and certificate.

%prep
%autosetup -p1 -n check_ssl_cert-%{version}

%build
# Nothing to do here.

%install
%make_install DESTDIR=%{buildroot}/%{nagiospluginsdir} MANDIR=%{buildroot}/%{_mandir}

%check
# Do not run unit tests because they require internet access.

%files
%doc NEWS.md
%doc README.md
%doc SECURITY.md
%license COPYING.md
%{_mandir}/man1/check_ssl_cert.1*
%{nagiospluginsdir}/check_ssl_cert


%changelog
%autochangelog
