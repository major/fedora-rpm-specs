%global commit b4ba3c8030b22e8a8c59dcb538642a29bd6a7085
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           usbsniff
Version:        0
Release:        24.20170624git%{shortcommit}%{?dist}
Summary:        USB traffic capture and replay tools

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/vdudouyt/usbsniff
Source0:        https://github.com/vdudouyt/usbsniff/archive/%{commit}/usbsniff-%{shortcommit}.tar.gz
Patch0:         usbsniff-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  flex-devel
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig(libusb-1.0)

%description
Tools to capture USB traffic, store the capture results and replay them against
the device. Useful for debugging USB devices or reverse-engineering protocols.


%prep
%autosetup -p1 -n usbsniff-%{commit}


%build
# Parallel make broken, missing deps
make LIBS="$(pkg-config --libs libusb-1.0) -lpcap -ll" \
        CFLAGS="$(pkg-config --cflags libusb-1.0) -DLINUX %{optflags}"


%install
mkdir -p %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot}


%files
%{_bindir}/*
%doc LICENSE README.md


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0-23.20170624gitb4ba3c8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-21.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Florian Weimer <fweimer@redhat.com> - 0-18.20170624gitb4ba3c8
- Port to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20170624gitb4ba3c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 01 2020 Lubomir Rintel <lkundrak@v3.sk> - 0-12.20170624gitb4ba3c8
- Update to a newer snapshot

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.20141209git079747e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 09 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-2.20141209git079747e
- Fix BR
- Update to a later snapshot

* Fri Nov 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 0-1.20140421gitdf4293f
- Initial packaging
