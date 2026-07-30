# spec file for package innoextract
#
# Copyright (c) 2012-2015 Daniel Scharrer <daniel@constexpr.org>
#               2015 Alexandre Detiste <alexandre@detiste.be>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           innoextract
Version:        1.9
Release:        %autorelease
License:        Zlib
Summary:        Tool to extract installers created by Inno Setup
Url:            https://constexpr.org/innoextract/
Source:         %{url}/files/%{name}-%{version}.tar.gz
Patch0:         innoextract-boost190.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  xz-devel

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

%prep
%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2380652)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DUSE_LDGOLD=FALSE
%cmake_build

%install
%cmake_install

%check
%{buildroot}%{_bindir}/innoextract --version

%files
%license LICENSE
%doc README.md CHANGELOG VERSION
%{_bindir}/innoextract
%{_mandir}/man1/innoextract.1*

%changelog
%autochangelog
