%global repo dde-account-faces

Name:           deepin-account-faces
Version:        1.0.12
Release:        %autorelease
Summary:        Account faces for Linux Deepin
License:        GPLv2+
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
