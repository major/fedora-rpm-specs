%global realname goldrush

Name:		erlang-%{realname}
Version:	0.2.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Small, fast event processing and monitoring for Erlang/OTP applications
License:	MIT
URL:		https://github.com/DeadZen/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildSystem:	rebar3

%description
%{summary}.

%files
%license LICENSE
%doc README.org
%{erlang_appdir}/

%changelog
%autochangelog
