Name:    dnf-plugin-cow
Version: 0.2.0
Release: %autorelease
Summary: DNF plugin to enable Copy on Write in RPM
URL:     https://github.com/facebookincubator/dnf-plugin-cow
License: MIT

Source:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libdnf5)

%description
Source package for DNF plugin to enable Copy on Write in DNF and RPM.

%package -n libdnf5-plugin-cow
Summary: DNF5 plugin to enable Copy on Write in RPM
# Using recommends to allow the plugin to be installed even if the requirements
# are not packaged/available yet.
Recommends: /usr/lib/rpm/rpm2extents
Recommends: rpm-plugin-reflink
# Drop once F45 is EOL
Obsoletes:  python3-dnf-plugin-cow < 0.2.0-1

%description -n libdnf5-plugin-cow
Installing this package enables a libdnf5 plugin which changes the behaviour
of librepo. Instead of downloading rpm files directly into cache before
installation they will be "transcoded" into "extent based" rpms which contain
all the constituent files of the rpm already uncompressed. This package
depends on a version of rpm which includes /usr/bin/rpm2extents and the
sub-package rpm-plugin-reflink which understands these "extent based" rpms
and can install files without copying the underlying data.

This package broadly assumes the root filesystem supports copy on write /
reflink'ing. Today this means btrfs or xfs.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n libdnf5-plugin-cow
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/reflink.conf
%{_libdir}/libdnf5/plugins/reflink.so

%changelog
%autochangelog
