Name:           shntool
Version:        3.0.10
Release:        %autorelease
Summary:        A multi-purpose WAVE data processing and reporting utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://shnutils.freeshell.org/shntool/
Source0:        http://shnutils.freeshell.org/shntool/dist/src/%{name}-%{version}.tar.gz

# Patches are from Debian
# https://sources.debian.org/patches/shntool/3.0.10-1/
Patch0:         large-size.patch
Patch1:         large-times.patch
Patch2:         no-cdquality-check.patch
Patch3:         https://github.com/max619/shntool/commit/cfd06e4edecdca2013e0fe04db135fd110a68203.patch
Patch4:         0001-fix-valid-wavepack-header-versions.patch
Patch5:         gcc-15-fixes.patch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc

%description
A multi-purpose WAVE data processing and reporting utility. File
formats are abstracted from its core, so it can process any file that contains
WAVE data, compressed or not - provided there exists a format module to handle
that particular file type. 

%prep
%autosetup -p1
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README
%doc doc/*
%license COPYING
%{_bindir}/shn*
%{_mandir}/man1/%{name}.1.*


%changelog
%autochangelog
