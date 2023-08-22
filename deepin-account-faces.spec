%global repo dde-account-faces

Name:           deepin-account-faces
Version:        1.0.14
Release:        %autorelease
Summary:        Account faces for Linux Deepin
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-account-faces
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
Requires:       accountsservice

%description
Account faces for Linux Deepin

%prep
%setup -q -n %{repo}-%{version}

%build

%install
%make_install

%files
%{_sharedstatedir}/AccountsService/icons/*

%changelog
%autochangelog
