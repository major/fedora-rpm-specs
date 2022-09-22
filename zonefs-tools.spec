Name:		zonefs-tools
Version:	1.5.2
Release:	4%{?dist}
Summary:	Provides user utilities for the zonefs file system

License:	GPLv2+
URL:		https://github.com/westerndigitalcorporation/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	libblkid-devel
BuildRequires:	libuuid-devel
BuildRequires:	autoconf
BuildRequires:	autoconf-archive
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc

%description
This package provides the mkzonefs (and mkfs.zonefs) user utility
to format zoned block devices for use with the zonefs file system.

%prep
%autosetup

%build
sh autogen.sh
%configure
%make_build

%install
%make_install

%files
%{_sbindir}/*
%{_mandir}/man8/*

%license COPYING.GPL
%doc README.md CONTRIBUTING

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Damien Le Moal <damien.lemoal@wdc.com> 1.5.2-1
- Version 1.5.2 initial package
