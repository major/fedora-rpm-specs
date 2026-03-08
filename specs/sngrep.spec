Name:           sngrep
Version:        1.8.3
Release:        %autorelease
Summary:        Ncurses SIP Messages flow viewer
License:        GPL-3.0-or-later WITH cryptsetup-OpenSSL-exception
URL:            https://github.com/irontec/sngrep
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/v%{version}.tar.gz.asc
Source2:        69100FFB90E87A320DF8643CBEC39009E8321A61.gpg
Patch:          b84f0663e47de6f238d9f81eed67612a9ab616ef.patch
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(zlib)

%description
sngrep is a tool for displaying SIP calls message flows from terminal. It
supports live capture to display realtime SIP packets and can also be used as
PCAP viewer.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
rm -f README.md
cp -f README README.md

%build
%cmake -DWITH_OPENSSL=ON -DWITH_PCRE2=ON -DWITH_ZLIB=ON -DWITH_NCURSES=ON -DWITH_UNICODE=ON -DUSE_IPV6=ON -DUSE_EEP=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE LICENSE.OpenSSL
%exclude %{_pkgdocdir}/*
%doc AUTHORS README.md
%config %{_sysconfdir}/sngreprc
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog
