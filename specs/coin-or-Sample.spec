%global		module		Sample

Name:		coin-or-%{module}
Summary:	Coin-or Sample data files
Version:	1.2.13
Release:	%autorelease
License:	LicenseRef-Not-Copyrightable
URL:		https://github.com/coin-or-tools/Data-Sample
Source0:	%{url}/archive/releases/%{version}/Data-%{module}-%{version}.tar.gz
Source1:	%{name}-COPYING
BuildArch:	noarch

BuildRequires:	make

%description
Coin-or Sample data files.

%prep
%autosetup -n Data-%{module}-releases-%{version}
cp -p %{SOURCE1} ./COPYING

%build
%configure
%make_build

%install
%make_install pkgconfiglibdir=%{_datadir}/pkgconfig

%files
%{_datadir}/coin/
%{_datadir}/pkgconfig/*
%license COPYING

%changelog
%autochangelog
