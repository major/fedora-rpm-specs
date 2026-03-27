%global srcname eimp
%global p1_utils_ver 1.0.29

Name:    erlang-%{srcname}
Version: 1.0.27
Release: %autorelease
License: Apache-2.0
Summary: Erlang Image Manipulation Process
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-provider_asn1
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: gcc
BuildRequires: gd-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libwebp-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
eimp is an Erlang/Elixir application for manipulating graphic images
using external C libraries. It supports WebP, JPEG, PNG and GIF.

%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -f configure

%build
autoreconf -ivf
%configure
%{erlang3_compile}

%install
%{erlang3_install}
install -p -D -m 755 priv/bin/* --target-directory=%{buildroot}%{erlang_appdir}/priv/bin/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
