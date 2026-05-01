Name:      gnome-srpm-macros
Version:   1.0
Release:   %autorelease
Summary:   Helper SRPM macros common across GNOME hosted projects
License:   Zlib
URL:       https://www.gnome.org/
Source0:   macros.gnome
Source1:   LICENSE.txt
BuildArch: noarch

BuildRequires: coreutils

%description
%{name} contains declarations of SRPM macros common to
GNOME hosted projects.

%install
install -m 644 -D "%{SOURCE0}" "%{buildroot}%{_rpmconfigdir}/macros.d/macros.gnome"
install -m 644 -D "%{SOURCE1}" "%{buildroot}%{_datadir}/licenses/%{name}/LICENSE.txt"

%files
%license LICENSE.txt
%{_rpmconfigdir}/macros.d/macros.gnome

%changelog
%autochangelog
