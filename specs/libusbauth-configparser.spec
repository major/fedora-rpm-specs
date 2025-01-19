#
# spec file for package libusbauth-configparser
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 Stefan Koch <stefan.koch10@gmail.com>
# Copyright (c) 2015 SUSE LLC. All Rights Reserved.
# Author: Stefan Koch <skoch@suse.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libusbauth-configparser
Version:        1.0.5
Summary:        Library for USB Firewall including flex/bison parser
URL:            https://github.com/kochstefan/usbauth-all/tree/master/libusbauth-configparser
Source:         https://github.com/kochstefan/usbauth-all/archive/v%{version}.tar.gz

Release:        8%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2

BuildRequires:  pkgconfig(libudev)
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool

%description
Library to read usbauth config file into data structures


%package devel
Summary:        Development part of library for USB Firewall including flex/bison parser
Requires:       libusbauth-configparser%{?_isa} = %{version}-%{release}

%description devel
Development part of library to read usbauth config file into data structures

%prep
%autosetup -n usbauth-all-%{version} -p1

%build
pushd %{name}/
autoreconf -f -i
%configure
%make_build
popd

%install
pushd %{name}/
%make_install
popd

%files
%license %{name}/COPYING
%doc %{name}/README
%_libdir/lib*.so.1*

%files devel
%license %{name}/COPYING
%doc %{name}/README
%doc %_mandir/*/*
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/*

%ldconfig_post

%ldconfig_postun

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.5-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 11 2023 stefan.koch10@gmail.com - 1.0.5-2
- Improve deps

* Sat Mar 04 2023 stefan.koch10@gmail.com - 1.0.5-1
- update to v1.0.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 22 2019 stefan.koch10@gmail.com - 1.0.1-1
- initial package for library to read usbauth config file
