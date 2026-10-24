%global realname certifi

Name:     erlang-%{realname}
Version:  2.18.0
Release:  %autorelease
BuildArch:noarch
Summary:  Dummy certifi (certificate bundle) package for erlang
License:  BSD-3-Clause
URL:      https://github.com/%{realname}/erlang-%{realname}
VCS:      git:%{url}.git
Source:   %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:    erlang-certifi-0001-Enforce-Fedora-CA-bundle.patch
Patch:    erlang-certifi-0002-Adapt-tests-to-the-system-CA-bundle.patch
BuildRequires: erlang-parse_trans
BuildSystem:   rebar3

%description
Upstream certifi provides a custom CA bundle to erlang. Since custom CA bundles
cannot be packaged in Fedora, this 'dummy' package patches certifi to point to
the default Fedora CA bundle.

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
