%global realname stdlib2

Name:		erlang-%{realname}
Version:	1.4.6
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang stdlib extensions
# Original sources seems to be licensed under BSD-2-Clause, the files added by
# Kivra are licensed under Apache-2.0
License:	BSD-2-Clause AND Apache-2.0
URL:		https://github.com/kivra/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-folsom
BuildSystem:	rebar3

%description
%{summary}.

%files
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
