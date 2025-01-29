Name:    buildbox
Version: 1.2.43
Release: %autorelease
Summary: Building blocks to execute actions conforming to the Remote Execution API

License: Apache-2.0
URL:     https://buildgrid.gitlab.io/buildbox/buildbox-home/
Source0: https://gitlab.com/BuildGrid/buildbox/buildbox/-/archive/%{version}/buildbox-%{version}.tar.bz2

ExcludeArch: %{ix86}

BuildRequires: attr
BuildRequires: cmake
BuildRequires: fuse3
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: net-tools
BuildRequires: ninja-build
BuildRequires: pkgconfig(benchmark)
BuildRequires: pkgconfig(fuse3)
BuildRequires: pkgconfig(gmock_main)
BuildRequires: pkgconfig(grpc)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(libcares)
BuildRequires: pkgconfig(libglog)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(tomlplusplus)
BuildRequires: pkgconfig(uuid)

Requires: bubblewrap

%description
buildbox provides a set of building blocks to execute actions conforming to the
Remote Execution API, also supporting the Remote Worker API.

%prep
%autosetup -p1

%build
%cmake -GNinja \
       -DCMAKE_CXX_FLAGS="%{optflags} -Wno-format-security"
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_bindir}/buildbox-casd
%{_bindir}/buildbox-fuse
%{_bindir}/buildbox-run
%{_bindir}/buildbox-run-bubblewrap
%{_bindir}/buildbox-run-hosttools
%{_bindir}/buildbox-run-oci
%{_bindir}/buildbox-run-userchroot
%{_bindir}/buildbox-worker
%{_bindir}/casdownload
%{_bindir}/casupload
%{_bindir}/logstreamreceiver
%{_bindir}/logstreamtail
%{_bindir}/outputstreamer
%{_bindir}/recc
%{_bindir}/rexplorer
%{_bindir}/rumba
%{_bindir}/rumbad
%{_bindir}/trexe

%changelog
%autochangelog
