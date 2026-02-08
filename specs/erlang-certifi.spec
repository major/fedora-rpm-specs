%global realname certifi

Name:     erlang-%{realname}
Version:  2.16.0
Release:  %autorelease
BuildArch:noarch
Summary:  Dummy certifi (certificate bundle) package for erlang
License:  BSD-3-Clause
URL:      https://github.com/%{realname}/erlang-%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:   erlang-certifi-0001-Enforce-Fedora-CA-bundle.patch
BuildRequires:  erlang-parse_trans
BuildRequires:  erlang-rebar3

%description
Upstream certifi provides a custom CA bundle to erlang. Since custom CA bundles
cannot be packaged in Fedora, this 'dummy' package patches certifi to point to
the default Fedora CA bundle.

%prep
%autosetup -p1 -n erlang-%{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# FIXME unfortunately we're using a different set of certificates (Fedora CA
# bundle) so all tests have to be adjusted accordingly.
#%%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
