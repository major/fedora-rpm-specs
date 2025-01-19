Name:           libu2f-host
Version:        1.1.10
Release:        18%{?dist}
Summary:        Yubico Universal 2nd Factor (U2F) Host C Library

License:        GPLv3 and LGPLv2
URL:            http://developers.yubico.com/%{name}/
Source0:        http://developers.yubico.com/%{name}/releases/%{name}-%{version}.tar.xz

# https://github.com/Yubico/libu2f-host/pull/146
Patch0001:      libu2f-host-1.1.10_add_support_for_upcoming_json_c_0_14_0.patch

BuildRequires:  gcc
BuildRequires:  json-c-devel hidapi-devel
BuildRequires: make

# Bundled gnulib https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(gnulib)

# People using libu2f-host are actually using Yubikeys and
# will want them to be set up properly by udev
Requires:       u2f-hidraw-policy

%description
libu2f-host provides a C library that implements the host-side of the
U2F protocol. There are APIs to talk to a U2F device and perform the U2F
Register and U2F Authenticate operations.

%package -n u2f-host
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Summary:        Command-line tool for U2F devices
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n u2f-host
u2f-host provides a command line tool that implements the host-side of the
U2F protocol.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files needed to develop applications that
use libu2f-host.

%global _hardened_build 1

%prep
%autosetup -p 1

%build
%configure --disable-rpath --disable-static

# --disable-rpath doesn't work.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%check
LD_LIBRARY_PATH="$(pwd)/u2f-host/.libs" make check

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING.LGPLv2
%doc README AUTHORS NEWS THANKS ChangeLog doc/*
%{_libdir}/*.so.*

%files -n u2f-host
%license COPYING
%{_bindir}/u2f-host
%{_mandir}/man1/u2f-host.1*

%files devel
%doc %{_datadir}/gtk-doc
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.10-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1.1.10-8
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.1.10-5
- Rebuild (json-c)

* Mon Apr 13 2020 Björn Esser <besser82@fedoraproject.org> - 1.1.10-4
- Add support for upcoming json-c 0.14.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Seth Jennings <sethdjennings@gmail.com> - 1.1.10-1
- Upstream release
- Fixes pam-u2f is no longer working after upgrade to F30 - bug #1706293

* Wed Mar 6 2019 Seth Jennings <sethdjennings@gmail.com> - 1.1.8-1
- Upstream release
- Fixes CVE-2019-9578 libu2f-host: leak of uninitialized stack in devs.c - bug #1685955

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Seth Jennings <sethdjennings@gmail.com> - 1.1.6-1
- Upstream release

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 1.1.4-3
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Seth Jennings <sethdjennings@gmail.com> - 1.1.4-1
- Upstream release

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-4
- Rebuilt for libjson-c.so.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Seth Jennings <sethdjennings@gmail.com> - 1.1.3-1
- Upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 4 2016 Seth Jennings <spartacus06@gmail.com> - 1.0.0-6
- disable signature verficiation due to gpgv2 bug

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.0-4
- Add u2f-hidraw-policy as Requires

* Wed Oct 28 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.0-3
- Removed unneeded systemd BuildRequires
- Be an owner of gtk-doc

* Mon Oct 26 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.0-2
- Add _hardened_build
- More specific devel gtk-doc path

* Tue Sep 1 2015 Seth Jennings <spartacus06@gmail.com> - 1.0.0-1
- Update to new release

* Fri Feb 13 2015 Andy Lutomirski <luto@mit.edu> - 0.0.4-1
- Update to new release
- Drop udev rules -- they should be a separate package IMO
- Mark COPYING as a license
- Improve manpage rule

* Fri Oct 31 2014 Andy Lutomirski <luto@mit.edu> - 0.0-5
- BR: systemd, for _udevrulesdir

* Fri Oct 31 2014 Andy Lutomirski <luto@mit.edu> - 0.0-4
- Update udev rules for the Plug-Up key
- Fix timestamp on the udev rules

* Wed Oct 29 2014 Andy Lutomirski <luto@mit.edu> - 0.0-3
- Use _udevrulesdir

* Mon Oct 27 2014 Andy Lutomirski <luto@mit.edu> - 0.0-2
- Add udev rules

* Wed Oct 22 2014 Andy Lutomirski <luto@mit.edu> - 0.0-1
- New package
