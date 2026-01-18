# Upstream is not tagging releases on their gihub site
# Use a relevant git commit to grab what we are interested in
%global commit_long     795a815363a4401a30a1c0ef94f3381186172843

Name: dymo-cups-drivers-lw5xx
Version: 2.0.0.0
Release: 2%{?dist}
Summary: DYMO LabelWriter 5xx Drivers for CUPS
License: GPL-2.0-or-later
URL: https://github.com/dymosoftware/Drivers

Source0: %{url}/archive/%{commit_long}.tar.gz#/Drivers-%{commit_long}.tar.gz

Patch0: dymo-cups-drivers-fix-fsf-address.patch
Patch1: dymo-cups-drivers-include-ctime.patch
Patch2: dymo-cups-drivers-replace-boolean-or-with-bitwise.patch
Patch3: dymo-cups-drivers-replace-deprecated-type.patch
Patch4: dymo-cups-drivers-append-cxxflags-dont-overwrite.patch
Patch5: dymo-cups-drivers-fprintf-format-specifier.patch

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: boost-devel
BuildRequires: cairo-devel
BuildRequires: cups-devel
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: sed
BuildRequires: make

Requires: cups

%description
This package contains DYMO LabelWriter 5xx series drivers for CUPS.
For LabelWriter 4xx and 3xx series drivers, please use the older
dymo-cups-drivers package.

%prep
%autosetup -p 1 -n Drivers-%{commit_long}

# Remove unwanted subfolders
rm -rf "LW4xx Linux"
rm -rf LW5xx_218_Beta
rm -rf LW5xx_Linux/src/boost

# move the subfolder we will build from up to the root
mv LW5xx_Linux/* ./
rmdir LW5xx_Linux

%build
autoupdate
autoreconf --force --install

chmod +x configure
%configure

%make_build

%install
%make_install

%check
# Upstream has not updated the tests to reflect the newer v2 api
#make_build check

%files
%license LICENSE
%doc AUTHORS ChangeLog README
%{_cups_serverbin}/filter/*
%{_datadir}/cups/model/*

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Oct 23 2025 Andrew Bauer <zonexpertconsulting@outlook.com> - 2.0.0.0-1
- Initial specfile
