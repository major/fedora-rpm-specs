Summary:        FUSE and libmtp based filesystem for accessing MTP devices
Name:           jmtpfs
Version:        0.5
Release:        12%{?dist}
License:        GPL-3.0-only
URL:            https://github.com/JasonFerrara/jmtpfs/
Source0:        https://github.com/JasonFerrara/jmtpfs/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        jmtpfs.1
Patch0:         https://github.com/JasonFerrara/jmtpfs/commit/840db07c39d95415c493170bf6513db4cd46490b.patch#/jmtpfs-0.5-exception.patch
Requires:       %{_bindir}/fusermount
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  fuse-devel >= 2.6
BuildRequires:  file-devel
BuildRequires:  libmtp-devel >= 1.1.0

%description
jmtpfs is a FUSE and libmtp based filesystem for accessing MTP (Media
Transfer Protocol) devices. It was specifically designed for exchanging
files between Linux systems and newer Android devices that support MTP
but not USB Mass Storage.

The goal is to create a well behaved filesystem, allowing tools like
find and rsync to work as expected. MTP file types are set automatically
based on file type detection using libmagic. Setting the file appears to
be necessary for some Android apps, like Gallery, to be able to find and
use the files.

Since it is meant as an Android file transfer utility, the playlists and
other non-file based data are not supported.

%prep
%setup -q
%patch -P0 -p1 -b .exception

%build
%configure
%make_build

%install
%make_install

install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Robert Scheck <robert@fedoraproject.org> 0.5-2
- Added patch to avoid MtpErrorCantOpenDevice crash (#1871442)

* Tue Jan 05 2021 Robert Scheck <robert@fedoraproject.org> 0.5-1
- Upgrade to 0.5 (#1913015)
- Added man page for jmtpfs from Debian (#1687358)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Robert Scheck <robert@fedoraproject.org> 0.4-2
- Use libmtp11 on RHEL 6
- Added patch by Chris Caron to build with fuse on RHEL 6

* Thu Mar 14 2013 Robert Scheck <robert@fedoraproject.org> 0.4-1
- Upgrade to 0.4
- Initial spec file for Fedora and Red Hat Enterprise Linux
