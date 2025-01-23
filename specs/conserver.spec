# rhel 8+ do not ship tcp_wrappers
%if 0%{?rhel} == 7
  %bcond_without libwrap
%else
  %bcond_with libwrap
%endif

Name:           conserver
Version:        8.2.7
Release:        11%{?dist}
Summary:        Serial console server daemon/client

License:        BSD-3-Clause AND Zlib
URL:            https://www.%{name}.com

Source0:        https://github.com/bstansell/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/bstansell/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
# gpg --keyserver pgp.mit.edu --recv-key D8D14B91ACAF41E231F8686728E4B7253029E7F6
# gpg --output bstansell-gpg-key.asc --armor --export bryan@conserver.com
Source2:        bstansell-gpg-key.asc

# Additional sources
Source3:        %{name}.service

Patch0:         %{name}-no-exampledir.patch
Patch1:         %{name}-8.2.7-buffer-overflow.patch
# Fix FTBFS with GCC 15 in C23 mode
# https://github.com/bstansell/conserver/commit/84fc79a459e00dbc87b8cfc943c5045bfcc7aeeb
Patch2:         %{name}-gcc15-c23.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freeipmi-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
%if %{with libwrap}
BuildRequires:  tcp_wrappers-devel
%endif

%description
Conserver is an application that allows multiple users to watch a serial
console at the same time.  It can log the data, allows users to take
write-access of a console (one at a time), and has a variety of bells
and whistles to accentuate that basic functionality.

%package client
Summary: Serial console client

%description client
This is the client package needed to interact with a Conserver daemon.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# disable stripping of binaries
find . -name Makefile.in -exec \
       sed -i 's/@INSTALL_PROGRAM@ -s/@INSTALL_PROGRAM@/g' {} \;

%build
%configure --with-freeipmi   \
           --with-gssapi     \
%if %{with libwrap}
           --with-libwrap    \
%endif
           --with-openssl    \
           --with-pam        \
           --with-port=782   \
           --with-striprealm
%make_build

%install
%make_install

# put commented copies of the sample configure files in the
# system configuration directory
mkdir -p %{buildroot}%{_sysconfdir}
for cfg in conserver.{cf,passwd}; do
  sed -e 's/^/#/' "conserver.cf/$cfg" > "%{buildroot}%{_sysconfdir}/$cfg"
done

# install copy of systemd service
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/conserver.service

%check
%make_build test

%post
%systemd_post conserver.service

%preun
%systemd_preun conserver.service

%postun
%systemd_postun_with_restart conserver.service

%files
%doc CHANGES FAQ PROTOCOL README.md
%doc conserver.cf/{conserver.{cf,passwd},samples/}
%license LICENSE
%config(noreplace) %{_sysconfdir}/conserver.*
%{_unitdir}/conserver.service
%{_libdir}/conserver
%{_mandir}/man5/conserver.cf.5*
%{_mandir}/man5/conserver.passwd.5*
%{_mandir}/man8/conserver.8*
%{_sbindir}/conserver

%files client
%license LICENSE
%{_bindir}/console
%{_mandir}/man1/console.1*

%changelog
* Tue Jan 21 2025 Lukáš Zaoral <lzaoral@redhat.com> - 8.2.7-11
- fix FTBFS with GCC 15 in C23 mode

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Lukáš Zaoral <lzaoral@redhat.com> - 8.2.7-6
- fix buffer-overflow caused by SIGHUP during SSH connections (rhbz#2256665)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 28 2023 Lukáš Zaoral <lzaoral@redhat.com> - 8.2.7-4
- Use %%{_mandir}/man1/foo.1* for manual pages as recommended by the packaging
  guidelines.
- Do not strip binaries during installation.
- Convert license to SPDX format.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Lukáš Zaoral <lzaoral@redhat.com> - 8.2.7-1
- Update to 8.2.7 (rhbz#2105250)
- Drop unused patches
- Fix incorrect license
  * BSD with advertising and zlib -> BSD and zlib
- Fix install-file-in-docs rpmlint warning
- Install license into correct destination
- Modernize and reformat the specfile
- Run upstream test suite
- Update URL to homepage and sources
- Verify sources signatures

* Mon Jul 11 2022 Lukáš Zaoral <lzaoral@redhat.com> - 8.2.6-6
- Implement conserver.service reloading (rhbz#1504194)
- Autorestart conserver.service on failure or after package upgrade

* Thu Jul  7 2022 Lukáš Zaoral <lzaoral@redhat.com> - 8.2.6-5
- Fix broken GSSAPI support

* Fri Jun 24 2022 Lukáš Zaoral <lzaoral@redhat.com> - 8.2.6-4
- Fix FTBFS in Rawhide and 36 (rhbz#2045276, rhbz#1999439, rhbz#1943012)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 8.2.6-2
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 31 2021 Jiri Kastner <jkastner@fedoraproject.org> - 8.2.6-1
- update to 8.2.6

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar  3 2020 Jiri Kastner <jkastner@fedoraproject.org> - 8.2.2-6
- fix systemd scriplets

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 8.2.2-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jan  4 2019 Jiri Kastner - 8.2.2-1
- update to 8.2.2
- fixes openssl-1.1 build

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 8.2.1-8
- Rebuilt for switch to libxcrypt

* Sun Dec 10 2017 Jiri Kastner - 8.2.1-7
- removed old systemd snippets and dependencies (BZ#850068)
- changed dependency on openssl to compat-openssl10 for newer fedoras (BZ#1423307)
- removed tcp_wrappers dependency (BZ#1518757)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Jiri Kastner <jkastner (at) redhat (dot) com> - 8.2.1-1
- updated to 8.2.1 (BZ#1225592)

* Mon Jan 12 2015 Jiri Kastner <jkastner (at) redhat (dot) com> - 8.2.0-2
- hardening build (BZ#955327)

* Wed Jan  7 2015 Jiri Kastner <jkastner (at) redhat (dot) com> - 8.2.0-1
- updated to new release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Jiri Kastner <jkastner (at) redhat (dot) com> - 8.1.20-1
- updated to new release
- added support for freeipmi (serial over lan)

* Mon Sep 16 2013 Jiri Kastner <jkastner (at) redhat (dot) com> - 8.1.18-9
- removed libgss*-devel build dependency

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Jon Ciesla <limburgher@gmail.com> - 8.1.18-5
- Migrate to systemd, BZ 771450.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.18-2
- Paolo Bonzini advises --with-uds would be a Bad Thing; removed (thanks!)

* Tue Jan 25 2011 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.18-1
- Updated to newer version for added Kerberos support (BZ#652688)
- Fixed BZ#466541
- Fixed broken tcp_wrappers support
- Enabled Unix Domain Socket support
- Removed upstream-adopted patches

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 8.1.16-9
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> 8.1.16-6
- rebuild with new openssl

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.16-5
- Bump-n-build for GCC 4.3

* Tue Dec 04 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.16-4
- Bump-n-build for openssl soname change

* Wed Aug 22 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.16-3
- License clarification

* Tue Aug 21 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.16-2
- Rebuild for BuildID

* Wed Apr 11 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.16-1
- New upstream release with "certainly important" bugfix
- Removed URLs from patch lines (it's all in CVS)
- Added patch to fix man page permissions (755 -> 644)
- rpmlint's "mixed-use-of-spaces-and-tabs" is mostly a false positive

* Wed Jan 03 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.15-1
- New upstream release
- Fix rpmlint warning about mixed spaces/tabs

* Mon Aug 28 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.14-4
- Rebuild for FC6

* Wed May 24 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 8.1.14-3
- Fix from Nate Straz: UDS support (pre-emptively fixed bug 192910)
- Fix from Nate Straz: krb detection

* Wed Apr 26 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 8.1.14-2
- Split 'console' out to -client subpackage, as suggested by Nate Straz

* Mon Apr 10 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 8.1.14-1
- Figures, two days after my initial Fedora Extras RPM, a new release...

* Fri Apr 07 2006 Patrick "Jima" Laughton <jima@auroralinux.org> 8.1.13-1
- Initial Fedora Extras RPM
- Added patch to disable /usr/share/examples/conserver -- non-standard
- Added patch to correct poorly written initscript
- Cleaned up what goes in /usr/share/doc/conserver-8.1.13/ (sloppy)
- Other .spec cleanups with lots of help from Dennis Gilmore (thanks!)
