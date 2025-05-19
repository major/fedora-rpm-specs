%global branch 1.28

Name:          mate-icon-theme
Version:       %{branch}.0
Release:       %autorelease
Summary:       Icon theme for MATE Desktop
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildArch:     noarch

BuildRequires: make
BuildRequires: mate-common 
BuildRequires: icon-naming-utils

%description
Icon theme for MATE Desktop


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure  --enable-icon-mapping

make %{?_smp_mflags} V=1


%install
%{make_install}


%files
%doc AUTHORS COPYING README
%{_datadir}/icons/mate
%{_datadir}/icons/menta


%changelog
%autochangelog
