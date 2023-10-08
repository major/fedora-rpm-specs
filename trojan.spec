Name:       trojan
Version:    1.16.0
Release:    %autorelease
Summary:    An unidentifiable mechanism that helps you avoid censorship

#GPLv3+ with opelssl exceptions
License:    GPLv3+
URL:        https://github.com/trojan-gfw/%{name}
Source0:    %{URL}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# signature from release page
Source1:    %{URL}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
# keyid obtained from upstream auther's GitHub profile
Source2:    https://pgp.key-server.io/0xA1DDD486533B0112

# see: https://github.com/trojan-gfw/trojan/pull/473
# Changes/CMake to do out-of-source builds F33 make tests fail
# this is a workaround
Patch0:     0001-Avoid-a-race-condition-that-makes-the-test-to-fail.patch

# for build
BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    make
BuildRequires:    cmake >= 3.7.2
BuildRequires:    boost-devel >= 1.66.0
BuildRequires:    openssl-devel >= 1.1.0
BuildRequires:    mariadb-connector-c-devel
%if 0%{?fedora} >= 30
BuildRequires:    systemd-rpm-macros
%else
BuildRequires:    systemd
%endif
# for test
BuildRequires:    python3
BuildRequires:    nmap-ncat
BuildRequires:    curl
BuildRequires:    openssl
#for verifying the tarball
BuildRequires:    gnupg2


%description
An unidentifiable mechanism that helps you avoid censorship.

Trojan features multiple protocols over TLS to avoid both 
active/passive detection and ISP QoS limitations.

Trojan is not a fixed program or protocol. It's an idea, 
an idea that imitating the most common service, 
to an extent that it behaves identically, 
could help you get across the Great FireWall permanently, 
without being identified ever.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
# change cipher list in shipped configuration file&example into PROFILE=SYSTEM
sed -i '/"cipher"/c\        "cipher": "PROFILE=SYSTEM",' examples/*.json-example
sed -i '/"cipher_tls13"/c\        "cipher_tls13": "PROFILE=SYSTEM",' examples/*.json-example
sed -e '/User=nobody/ s/^#*/# /;/User=nobody/i # User=nobody is not recommended\n# You can use systemctl edit trojan to re-enable this\n# While DynamicUser=yes is suggested\n#' -i examples/trojan.service-example

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%{_bindir}/%{name}
%license LICENSE
%dir %{_sysconfdir}/%{name}
%dir %{_pkgdocdir}
%config(noreplace) %{_sysconfdir}/%{name}/config.json
%{_mandir}/man1/%{name}.1.*
%{_pkgdocdir}/*
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service


%changelog
%autochangelog
