Name: curlftpfs
Version: 0.9.2
Release: 40%{?dist}
Summary: CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and libcurl
URL: http://curlftpfs.sourceforge.net/
# Code does not specify a version of the license.
License: GPL-1.0-or-later
Requires: fuse
Source: http://downloads.sourceforge.net/curlftpfs/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: curl-devel >= 7.15.2 fuse-devel glib2-devel
BuildRequires: make
# https://bugzilla.redhat.com/show_bug.cgi?id=831417
Patch1: curlftpfs-0.9.2-offset_64_another.patch
# https://code.google.com/p/curlftpfs/issues/detail?id=6 (bz#962015)
Patch2: curlftpfs-0.9.2-create-fix.patch
# Aarch64 support, Fedora-specific. bz#925209
Patch3: curlftpfs-0.9.2-aarch64.patch

# Fix memleaks 2 patches (one upstream report: https://code.google.com/p/curlftpfs/issues/detail?id=10)
Patch4: curlftpfs-0.9.2-memleak#591298.patch
Patch5: curlftpfs-0.9.2-memleak-cached#591299.patch
Patch6: curlftpfs-c99.patch

%description
CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and
libcurl. It features SSL support, connecting through tunneling HTTP
proxies, and automatically reconnecting if the server times out.

%prep
%setup -q
%patch -P1 -p1 -b .offset
%patch -P2 -p1 -b .create-fix
%patch -P3 -p1 -b .aarch64
%patch -P4 -p1 -b .memleak
%patch -P5 -p1 -b .memleak-cached
%patch -P6 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/curlftpfs
%{_mandir}/*/curlftpfs.*
%doc README
%doc COPYING

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.2-38
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Florian Weimer <fweimer@redhat.com> - 0.9.2-35
- Fix C compatibility issue

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-14
- Apply patch to support aarch64 (Thanks to Dennis Gilmore) - bz#925209.
- Apply Patch4: curlftpfs-0.9.2-memleak#591298.patch and
	Patch5: curlftpfs-0.9.2-memleak-cached#591299.patch to fix memleaks. Thanks to Jérôme Benoit.

* Sun May 12 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-13
- Made Patch2: curlftpfs-0.9.2-create-fix.patch to fix file create issue bz#962015.
- Some cleanup, as it is not intended to be build on EPEL5.
- Reintroduce Patch1 by Debian (http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=556012) (bz#962015).
- Add patch2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 6 2012 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-11
- Replace patch0 (offset 64 fix) by more correct (bz#831417).

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-7
- Fix bz#671204, thanks to Viktor for the patch.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 12 2010 Pavel Alexeev <Pahan@Hubbitus.info> - 0.9.2-7
- New version 0.9.2

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> - 0.9.1-6
- Rebuild with new fuse

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.1-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-2
- Autorebuild for GCC 4.3

* Thu Apr 05 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 0.9.1-1
- 0.9.1

* Wed Mar 28 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 0.9-5
- Explicit dependency on fuse (bz#234349)

* Mon Jan 08 2007 David Anderson <fedora-packaging@dw-perspective.org.uk> 0.9-3
- Bump release number

* Tue Dec 12 2006 David Anderson <fedora-packaging@dw-perspective.org.uk> 0.9-1
- Initial package
