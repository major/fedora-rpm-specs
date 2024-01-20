Summary: IrcII chat client
Name: BitchX
Version: 1.2.1
Release: 34%{?dist}
License: BSD and GPLv2+
URL: http://www.bitchx.org
Source0: http://www.bitchx.ca/%{name}-%{version}.tar.gz
#RHBZ 1037000
Patch0: format-security.patch
Patch1: configure_openssl_SSLeay.patch
Patch2: remove-duplicate-symbols.patch
Patch3: expr2_static_inline.patch
Patch4: BitchX-configure-c99.patch
Patch5: BitchX-aim-c99.patch
Patch6: BitchX-arcfourc-c99.patch
Patch7: BitchX-possum-c99.patch
BuildRequires:  gcc
BuildRequires: ncurses-devel openssl-devel glib2-devel libxcrypt-devel
BuildRequires: make

# Some plugins rely on int-conversion and incompatible-pointer-types.
# <https://bugzilla.redhat.com/show_bug.cgi?id=2148940>
%global build_type_safety_c 1

%description
BitchX: The ultimate IRC client

%prep
%setup -q -n %{name}-%{version} 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%configure --with-plugins --with-ssl --enable-ipv6
gmake V=1

%install
make DESTDIR=%{buildroot} install

%files
%doc Changelog COPYRIGHT README README-1.1
%{_bindir}/BitchX
%{_bindir}/BitchX-1.2.1
%{_bindir}/scr-bx
%{_libdir}/bx/
%{_mandir}/man1/*

%changelog
* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Florian Weimer <fweimer@redhat.com> - 1.2.1-33
- Downgrade C type safety level to 1 (#2148940)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Florian Weimer <fweimer@redhat.com> - 1.2.1-30
- Fixes for building in strict(er) C99 mode (#2148940)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.2.1-27
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Kevin Easton <kme@fedoraproject.org> - 1.2.1-23
- Add patch to mark all inline functions in expr2.c static, fixing build on s390

* Wed Jan 29 2020 Kevin Easton <kme@fedoraproject.org> - 1.2.1-22
- Add patch to remove duplicate symbols, fixing build on gcc 10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.1-18
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Kevin Easton <kme@fedoraproject.org> - 1.2.1-16
- Update package URL (#1462340)
- Add libxcrypt-devel to BuildRequires for switch to libxcrypt

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.2.1-14
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Kevin Easton <kme@fedoraproject.org> - 1.2.1-11
- Patch configure to check for ERR_get_error in -lcrypto instead of SSLeay (RHBZ #1423242)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 20 2016 Kevin Easton <kme@fedoraproject.org> - 1.2.1-9
- Switch to non-parallel build until next upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.2.1-4
- Fix RHBZ #1037000 to enable "-Werror=format-security".

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 01 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.2.1-2
- Bump release version

* Mon Apr 01 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.2.1-1
- Remove patent encumbered mp3 files.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 31 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.2-20
- Update to BitchX 1.2-final release.

* Tue Nov 13 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.2-19
- Bugfix release

* Thu Nov 01 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.2-18
- Update to upstream version 1.2c02 which fixes quit msgs in SSL mode.

* Sat Aug 04 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.2-17
- Updated bindir macro for BitchX binary.

* Mon Jul 23 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.2-16
- Remove unncessery debian folder, add SASL support.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-14

* Thu Jun 14 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-13
-Update to latest source code (svn rev 207)

* Sun Jun 03 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-12
-Updated to latest source code (svn rev 204)

* Tue May 29 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-11
-Updated to latest source code (svn rev 199)

* Sat May 19 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-10
-Updated to latest source code (svn rev 192)
-Various bugfixes

* Tue May 15 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-9
-Updated to latest source code (svn rev 189)
-Various bugfixes

* Mon May 14 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-8
-Updated to latest source code (svn rev 181)

* Thu May 10 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-7
-Various bugfixes and update to the latest BitchX source code (svn rev 180)

* Thu May 10 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-6
-Bugfix release

* Mon Apr 30 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-5
-New BitchX release to fix /detach and scr-bx with ipv6 support enabled

* Thu Apr 19 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-4
-Updated spec file, removed .o files in source tarball and source RPM
-Updated release versions in change log

* Tue Apr 17 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-3
-Updated spec file per rdieter's rpm package review.

* Mon Apr 16 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-2
-Received .patch from spot to patch Makefile to respect DESTDIR
-Received sponsorship from rdieter for submission review to Fedora.

* Sun Apr 08 2012 Dan Mashal <vicodan@fedoraproject.org> 1.2-1
- First rpm build
