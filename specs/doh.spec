%global commit      8654bc94ddbfaeec33e3403c6424e2dec8e86c30
%global shortcommit %{sub %{commit} 1 7}

Name:           doh
Version:        0.1^1.%{shortcommit}
Release:        %autorelease
Summary:        Application for DNS-over-HTTPS name resolves and lookups
License:        MIT
URL:            https://github.com/curl/doh
Source:         %{url}/archive/%{commit}/doh-%{shortcommit}.tar.gz
# https://github.com/curl/doh/pull/45
Patch:          0001-Makefile-install-manpage-to-DESTDIR.patch
Patch:          0002-Makefile-install-manpage-without-execute-permission.patch
Patch:          0003-Makefile-create-manpage-directory-structure.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libcurl-devel


%description
A libcurl-using application that resolves a host name using DNS-over-HTTPS
(DoH).  This code uses POST requests unconditionally for this.


%prep
%autosetup -p 1 -n doh-%{commit}


%build
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/doh
%{_mandir}/man1/doh.1*


%changelog
%autochangelog
