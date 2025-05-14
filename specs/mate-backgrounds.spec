Name:          mate-backgrounds
Version:       1.28.0
Release:       %autorelease
Summary:       MATE Desktop backgrounds
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
Source1:       default-mate.xml

BuildArch:     noarch
BuildRequires: make
BuildRequires: mate-common

%description
Backgrounds for MATE Desktop

%prep
%autosetup -p1

%build
%configure

make %{?_smp_mflags} V=1


%install
%{make_install}

cp -f %{SOURCE1} %{buildroot}%{_datadir}/backgrounds/mate/default-mate.xml

%files
%doc AUTHORS COPYING README
%{_datadir}/mate-background-properties
%{_datadir}/backgrounds/mate


%changelog
%autochangelog
