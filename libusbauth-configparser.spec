#
# spec file for package libusbauth-configparser
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libusbauth-configparser
Version:        1.0.1
Summary:        Library for USB Firewall including flex/bison parser
Url:            https://github.com/kochstefan/usbauth-all/tree/master/libusbauth-configparser

Release:        8%{?dist}
License:        LGPLv2

# Generate a source tarball:
# git clone https://github.com/kochstefan/usbauth-all.git
# cd usbauth-all
# git checkout vVERSION
# tar cvfj libusbauth-configparser-VERSION.tar.bz2 libusbauth-configparser
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires: make

%description
Library to read usbauth config file into data structures


%package devel
Summary:        Development part of library for USB Firewall including flex/bison parser
Requires:       libusbauth-configparser%{?_isa} = %{version}-%{release}

%description devel
Development part of library to read usbauth config file into data structures

%prep
%setup -q -n %{name}

%build
autoreconf -f -i
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%_libdir/lib*.so.1*

%files devel
%license COPYING
%doc README
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/*
%_mandir/*/*

%ldconfig_post

%ldconfig_postun

%changelog
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
