%global		module		Data-Netlib
%global		giturl		https://github.com/coin-or-tools/Data-Netlib

Name:		coin-or-%{module}
Summary:	COIN-OR Netlib models
Version:	1.2.11
Release:	%autorelease
License:	EPL-1.0
URL:		https://www.coin-or.org/download/pkgsource/Data
VCS:		git:%{giturl}.git
Source:		%{giturl}/archive/releases/%{version}/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(zlib)

%description
This package contains the COmputational INfrastructure for Operations
Research (COIN-OR) models from netlib for testing.

%prep
%autosetup -n %{module}-releases-%{version}

%conf
# We cannot regenerate the configure script due to missing macro definitions.
# However, the existing configure script will soon stop working due to
# https://fedoraproject.org/wiki/Changes/PortingToModernC
# Munge the script for now until we can get upstream to fix the issue.
sed -i '/ctype\.h/i#include <stdlib.h>' configure

%build
%configure
%make_build

%install
%make_install pkgconfiglibdir=%{_datadir}/pkgconfig

%files
%{_datadir}/coin/
%{_datadir}/pkgconfig/coindatanetlib.pc

%changelog
%autochangelog
