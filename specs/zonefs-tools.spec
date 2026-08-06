%global forgeurl https://github.com/westerndigitalcorporation/zonefs-tools
Version:        1.7.0
%forgemeta

Name:           zonefs-tools
Release:        %autorelease
Summary:        Provides user utilities for the zonefs file system

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libblkid-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make

%description
This package provides the mkzonefs (and mkfs.zonefs) user utility
to format zoned block devices for use with the zonefs file system.

%prep
%autosetup %{forgesetupargs}


%build
sh autogen.sh
%configure
%make_build

%install
%make_install

%check
%{buildroot}%{_sbindir}/mkzonefs --version

%files
%{_sbindir}/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%license COPYING.GPL
%doc README.md CONTRIBUTING


%changelog
%autochangelog
