Summary:         Utility to access BitLocker encrypted volumes
Name:            dislocker
Version:         0.7.3
Release:         18%{?dist}
License:         GPL-2.0-or-later
URL:             https://github.com/Aorimn/dislocker
Source0:         https://github.com/Aorimn/dislocker/archive/v%{version}/%{name}-%{version}.tar.gz
# Upstream changes since last release
Patch0:          https://github.com/Aorimn/dislocker/compare/v0.7.3...3e7aea196eaa176c38296a9bc75c0201df0a3679.patch#/dislocker-0.7.3-upstream-changes.patch
# Multibyte character support in passwords, see https://github.com/Aorimn/dislocker/pull/118
Patch1:          https://github.com/Aorimn/dislocker/pull/333.patch#/dislocker-0.7.3-multibyte-support.patch
Requires:        %{name}-libs%{?_isa} = %{version}-%{release}
Requires:        ruby(release)
Requires:        ruby(runtime_executable)
Requires(post):  %{?el8:/usr/sbin/}alternatives
Requires(preun): %{?el8:/usr/sbin/}alternatives
Provides:        %{_bindir}/%{name}
BuildRequires:   cmake
BuildRequires:   gcc
BuildRequires:   mbedtls-devel
BuildRequires:   ruby-devel
BuildRequires:   %{_bindir}/ruby

%description
Dislocker has been designed to read BitLocker encrypted partitions ("drives")
under a Linux system. The driver has the capability to read/write partitions
encrypted using Microsoft Windows Vista, 7, 8, 8.1 and 10 (AES-CBC, AES-XTS,
128 or 256 bits, with or without the Elephant diffuser, encrypted partitions);
BitLocker-To-Go encrypted partitions (USB/FAT32 partitions).

The file name where the BitLocker encrypted partition will be decrypted needs
to be given. This may take a long time, depending on the size of the encrypted
partition. But afterward, once the partition is decrypted, the access to the
NTFS partition will be faster than with FUSE. Another thing to think about is
the size of the disk (same size as the volume that is tried to be decrypted).
Nevertheless, once the partition is decrypted, the file can be mounted as any
NTFS partition and won't have any link to the original BitLocker partition.

%package libs
Summary:         Libraries for applications using dislocker

%description libs
The dislocker-libs package provides the essential shared libraries for any
dislocker client program or interface.

%package -n fuse-dislocker
Summary:         FUSE filesystem to access BitLocker encrypted volumes
Provides:        %{_bindir}/%{name}
Provides:        dislocker-fuse = %{version}-%{release}
Provides:        dislocker-fuse%{?_isa} = %{version}-%{release}
Requires:        %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post):  %{?el8:/usr/sbin/}alternatives
Requires(preun): %{?el8:/usr/sbin/}alternatives
BuildRequires:   fuse-devel

%description -n fuse-dislocker
Dislocker has been designed to read BitLocker encrypted partitions ("drives")
under a Linux system. The driver has the capability to read/write partitions
encrypted using Microsoft Windows Vista, 7, 8, 8.1 and 10 (AES-CBC, AES-XTS,
128 or 256 bits, with or without the Elephant diffuser, encrypted partitions);
BitLocker-To-Go encrypted partitions (USB/FAT32 partitions).

A mount point needs to be given to dislocker-fuse. Once keys are decrypted, a
file named 'dislocker-file' appears into this provided mount point. This file
is a virtual NTFS partition, it can be mounted as any NTFS partition and then
reading from it or writing to it is possible.

%prep
%autosetup -p1

%build
%cmake -D WARN_FLAGS="-Wall -Wno-error -Wextra"
%cmake_build

%install
%cmake_install

# Remove standard symlinks due to alternatives
rm -f $RPM_BUILD_ROOT{%{_bindir}/%{name},%{_mandir}/man1/%{name}.1*}

# Clean up files for later usage in documentation
for file in *.md; do mv -f $file ${file%.md}; done
for file in *.txt; do mv -f $file ${file%.txt}; done

%post
alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-file 60

%preun
if [ $1 -eq 0 ]; then
  alternatives --remove %{name} %{_bindir}/%{name}-file
fi

%ldconfig_scriptlets libs

%post -n fuse-dislocker
alternatives --install %{_bindir}/%{name} %{name} %{_bindir}/%{name}-fuse 80

%preun -n fuse-dislocker
if [ $1 -eq 0 ]; then
  alternatives --remove %{name} %{_bindir}/%{name}-fuse
fi

%files
%{_bindir}/%{name}-bek
%{_bindir}/%{name}-file
%{_bindir}/%{name}-find
%{_bindir}/%{name}-metadata
%{_mandir}/man1/%{name}-file.1*
%{_mandir}/man1/%{name}-find.1*

%files libs
%license LICENSE
%doc CHANGELOG README
%{_libdir}/libdislocker.so.*
# dislocker-find (ruby) fails without this symlink (#1583480)
%{_libdir}/libdislocker.so

%files -n fuse-dislocker
%{_bindir}/%{name}-fuse
%{_mandir}/man1/%{name}-fuse.1*

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.3-18
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Sun Jan 05 2025 Robert Scheck <robert@fedoraproject.org> 0.7.3-17
- Add patch with upstream changes, fixes and mbedTLS 3.x support
- Add updated patch for multibyte character support in passwords

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> - 0.7.3-16
- Rebuilt for mbedTLS 3.6.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.3-12
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.3-9
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Sat Jan 22 2022 Morten Stevens <mstevens@fedoraproject.org> - 0.7.3-6
- Rebuilt for mbedTLS 2.28.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.3-2
- F-34: rebuild against ruby 3.0
- Fix for build with ruby 3.0

* Sun Dec 13 2020 Robert Scheck <robert@fedoraproject.org> 0.7.3-1
- Spec file cleanup
- Upgrade to 0.7.3 (#1876804, thanks to Eshin Kunishima)

* Tue Aug 04 2020 Robert Scheck <robert@fedoraproject.org> 0.7.1-17
- Work around CMake out-of-source builds on all branches (#1863427)
- Add libdislocker.so symlink for dislocker-find (#1659733, #1583480)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-14
- F-32: rebuild against ruby27

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Vít Ondruch <vondruch@redhat.com> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Thu Sep 27 2018 Morten Stevens <mstevens@fedoraproject.org> - 0.7.1-10
- Rebuilt for mbed TLS 2.13.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Robert Scheck <robert@fedoraproject.org> 0.7.1-8
- Rebuilt for mbed TLS 2.7.3/2.9.0 (libmbedcrypto.so.2)

* Mon Feb 19 2018 Robert Scheck <robert@fedoraproject.org> 0.7.1-7
- Rebuilt for mbed TLS 2.7.0

* Sun Feb 18 2018 Robert Scheck <robert@fedoraproject.org> 0.7.1-6
- Rebuilt for mbed TLS 2.7.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-4
- F-28: rebuild for ruby25

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Robert Scheck <robert@fedoraproject.org> 0.7.1-1
- Upgrade to 0.7.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-5
- F-26: rebuild for ruby24

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Vít Ondruch <vondruch@redhat.com> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Mon Jan 11 2016 Robert Scheck <robert@fedoraproject.org> 0.5.1-2
- Build ruby extension and ship dislocker-find

* Wed Jan 06 2016 Robert Scheck <robert@fedoraproject.org> 0.5.1-1
- Upgrade to 0.5.1

* Sat Jul 25 2015 Robert Scheck <robert@fedoraproject.org> 0.4.1-5
- Rebuilt for mbed TLS 2.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Robert Scheck <robert@fedoraproject.org> 0.4.1-3
- Rebuilt for mbed TLS 1.3.11

* Mon Jun 01 2015 Robert Scheck <robert@fedoraproject.org> 0.4.1-2
- Rebuilt for mbed TLS 1.3.10

* Sat May 30 2015 Robert Scheck <robert@fedoraproject.org> 0.4.1-1
- Upgrade to 0.4.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6.20140423git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Robert Scheck <robert@fedoraproject.org> 0.3.1-5.20140423git
- Rebuild for PolarSSL 1.3.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4.20140423git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 01 2014 Robert Scheck <robert@fedoraproject.org> 0.3.1-3.20140423git
- Rebuild for PolarSSL 1.3.6

* Wed Apr 23 2014 Robert Scheck <robert@fedoraproject.org> 0.3.1-2.20140423git
- Upgrade to GIT 20140423 (#991689 #c15)
- Added %%{?__global_ldflags} for make (#991689 #c16)

* Mon Nov 25 2013 Robert Scheck <robert@fedoraproject.org> 0.3.1-1.20131102git
- Upgrade to GIT 20131102 (#991689 #c8)

* Mon Nov 25 2013 Robert Scheck <robert@fedoraproject.org> 0.2.3-2.20130131git
- Changed PolarSSL patch to support PolarSSL 1.2 and 1.3 (#991689 #c5)
- Added the missing Group tag on fuse-dislocker sub-package (#991689 #c5)

* Wed May 08 2013 Robert Scheck <robert@fedoraproject.org> 0.2.3-1.20130131git
- Upgrade to GIT 20130131
- Initial spec file for Fedora and Red Hat Enterprise Linux
