Name:		pam-ssh-auth-info
Version:	1.8.20230906
Release:	1%{?dist}
Summary:	PAM SSH Authentication Information Module
# GPL-3.0-or-later: * line_tokens_match_test.h
# LGPL-3.0-or-later: pam_*.c *.h
License:	GPL-3.0-or-later AND LGPL-3.0-or-later
URL:		https://github.eero.häkkinen.fi/%{name}/
Source0:	https://github.com/eehakkin/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	pam-devel
Requires:	pam%{?_isa}

%description
The pam_ssh_auth_info.so PAM module is designed to succeed or fail
authentication based on SSH authentication information consisting of a
list of successfully completed authentication methods and public
credentials (e.g. keys) used to authenticate the user. One use is to
select whether to load other modules based on this test.

%prep
%autosetup

%build
autoreconf --install
%configure
%make_build

%check
make check

%install
%make_install

%files
%doc README.md
%license COPYING
%license COPYING.LESSER
%{_libdir}/security/pam_ssh_auth_info.so
%{_mandir}/man8/pam_ssh_auth_info.8.gz

%changelog
* Tue Nov 14 2023 Jonathan McDowell <noodles@earth.li> - 1.8.20230906-1
- Initial packaging
