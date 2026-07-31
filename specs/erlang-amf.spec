%global realname amf
%global git_commit 8fea004e61c746c16271476c190a9c01e398a2d5
%global git_date 20170825

Name:		erlang-%{realname}
Version:	0
Release:	%autorelease -p -s %{git_date}git%{sub %git_commit 0 7}
BuildArch:	noarch
Summary:	Erlang Action Message Format Library
License:	BSD-2-Clause
URL:		https://github.com/abuibrahim/erlang-%{realname}
VCS:		git:%{url}.git
Source:		%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
Patch:		erlang-amf-0001-Fix-gb_trees-iterator-exhaustion-for-OTP-27.patch
BuildSystem:	rebar3

%description
%{summary}.

%files
%license LICENSE
%doc README doc
%{erlang_appdir}/

%changelog
%autochangelog
