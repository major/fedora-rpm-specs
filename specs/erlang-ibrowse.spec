%global realname ibrowse

Name:		erlang-%{realname}
Version:	4.4.2
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang HTTP client
License:	BSD-3-Clause OR LGPL-2.1-or-later
URL:		https://github.com/cmullaparthi/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-ibrowse-0001-use-is_ipv6_host-1-function-from-httpc.patch
Patch:		erlang-ibrowse-0002-use-ssl-handshake-2-function-for-erlang-otp-21.patch
BuildSystem:	rebar3

%description
%{summary}.

%install -a
install -D -p -m 0644 priv/%{realname}.conf %{buildroot}%{erlang_appdir}/priv/%{realname}.conf

%files
%license BSD_LICENSE LICENSE
%doc CHANGELOG CONTRIBUTORS README.md doc/
%{erlang_appdir}/

%changelog
%autochangelog
