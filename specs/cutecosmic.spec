%global commit 1469fa3a8890b74a7189d10de737150678b57418
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251110

%global downloadref %{?commitdate:%{commit}}%{!?commitdate:v%{version}}
%global tarballref %{?commitdate:%{shortcommit}}%{!?commitdate:%{version}}

%global qt6_minver 6.9.0

Name:           cutecosmic
Version:        0.1%{?commitdate:^git%{commitdate}.%{shortcommit}}
Release:        3%{?dist}
Summary:        Qt platform plugins for the COSMIC desktop

# Main sources are GPL-3.0-or-later, rest are rust licenses
### BEGIN LICENSE SUMMARY ###
#
# (MIT OR Apache-2.0) AND Unicode-3.0
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-3-Clause
# BSD-3-Clause OR Apache-2.0
# BSL-1.0
# CC0-1.0
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR CC0-1.0
# MIT OR Apache-2.0 OR LGPL-2.1-or-later
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT
###  END LICENSE SUMMARY  ###
License:        GPL-3.0-or-later AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (BSD-3-Clause OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND ISC AND MIT AND (MIT OR Apache-2.0 OR CC0-1.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND ZLib
URL:            https://github.com/IgKh/cutecosmic
Source0:        %{url}/archive/%{downloadref}/%{name}-%{tarballref}.tar.gz
%dnl To create the below sources:
%dnl * git clone https://github.com/IgKh/cutecosmic at the specified commit
%dnl * cd bindings
%dnl * cargo vendor > %{name}-%{tarballref}-cargovendor-config.toml
%dnl * tar -pczf %{name}-%{tarballref}-cargovendor.tar.gz vendor
Source1:        %{name}-%{tarballref}-cargovendor.tar.gz
Source2:        %{name}-%{tarballref}-cargovendor-config.toml

BuildRequires:  cargo-rpm-macros >= 28
BuildRequires:  cmake >= 3.22
BuildRequires:  cmake(Corrosion) >= 0.5.2
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

%description
%{summary}.

%dnl ---------------------------------------------------------------------

%package qt6
Summary:        Qt 6 platform plugins for the COSMIC desktop
BuildRequires:  cmake(Qt6Core) >= %{qt6_minver}
BuildRequires:  cmake(Qt6CoreTools) >= %{qt6_minver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_minver}
BuildRequires:  cmake(Qt6GuiPrivate) >= %{qt6_minver}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_minver}
BuildRequires:  qt6-rpm-macros
Requires:       qt6-filesystem
Requires:       cosmic-icon-theme
Supplements:    (cosmic-session%{?_isa} and qt6-qtbase-gui%{?_isa})
Requires:       qt6qml(org.kde.desktop)
Requires:       breeze-icon-theme
Recommends:     plasma-breeze-qt6
Recommends:     qt6qml(org.kde.breeze)

%description qt6
This package provides the Qt platform plugins to integrate
Qt 6 applications into the COSMIC desktop.

%files qt6
%doc README.md
%license COPYING
%license bindings/LICENSE.dependencies
%license bindings/cargo-vendor.txt
%{_qt6_plugindir}/platformthemes/libcutecosmictheme.so

%dnl ---------------------------------------------------------------------


%prep
%autosetup -C
tar -xf %{SOURCE1} -C bindings
pushd bindings
%cargo_prep -N
%dnl Append the contents of %{SOURCE2} to .cargo/config.toml
cat %{SOURCE2} >> .cargo/config.toml
echo "Appended %{SOURCE2} to .cargo/config.toml"
popd


%conf
pushd bindings
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
popd
%cmake_qt6 -GNinja


%build
%cmake_build


%install
%cmake_install



%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1^git20251110.1469fa3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1^git20251110.1469fa3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Dec 19 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.1^git20251110.1469fa3-1
- Initial package
