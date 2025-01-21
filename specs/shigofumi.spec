Name:           shigofumi
Version:        0.9
Release:        13%{?dist}
Summary:        Command line client for accessing the Czech Data Boxes
# COPYING:          GPL-3.0 text
# README:           GPL-3.0-or-later
# src/gettext.h:    LGPL-2.1-or-later
# src/shigofumi.c:  GPL-3.0-or-later
## Not in the binary packages
# aclocal.m4:       GPL-2.0-or-later WITH Autoconf-exception-generic AND FSFULLRWD
# compile:          GPL-2.0-or-later WITH Autoconf-exception-generic
# config.sub:       GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config.guess:     GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# config.rpath:     FSFULLR
# configure:        FSFUL
# depcomp:          GPL-2.0-or-later WITH Autoconf-exception-generic
# doc/Makefile.in:  FSFULLRWD
# doc/po/cs/Makefile.in:    FSFULLRWD
# doc/po/Makefile.in:       FSFULLRWD
# install-sh:       X11 AND LicenseRef-Fedora-Public-Domain
# m4/gettext.m4:    FSFULLR
# m4/host-cpu-c-abi.m4: FSFULLR
# m4/iconv.m4:      FSFULLR
# m4/intlmacosx.m4: FSFULLR
# m4/lib-ld.m4:     FSFULLR
# m4/lib-link.m4:   FSFULLR
# m4/lib-prefix.m4: FSFULLR
# m4/nls.m4:        FSFULLR
# m4/po.m4:         FSFULLR
# m4/progtest.m4:   FSFULLR
# m4/readline.m4:   GPL-1.0-or-later WITH Autoconf-exception-generic
# Makefile.in:      FSFULLRWD
# missing:          GPL-2.0-or-later WITH Autoconf-exception-generic
# po/insert-header.sin: FSFUL
# po/Makefile.in.in:    FSFAP
# po/remove-potcdate.sin:   FSFAP
# po/Rules-quot:    FSFUL
# src/Makefile.in:  FSFULLRWD
# test/Makefile.in: FSFULLRWD
# test-driver:      GPL-2.0-or-later WITH Autoconf-exception-generic
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-1.0-or-later WITH Autoconf-exception-generic AND X11 AND FSFULLRWD AND FSFULLR AND FSFUL AND FSFAP AND LicenseRef-Fedora-Public-Domain
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}dist/%{name}-%{version}.tar.xz
Source1:        %{url}dist/%{name}-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
# Fix building with GCC 12, in upstream after 0.9
Patch0:         shigofumi-0.9-Fix-building-with-GCC-12.patch
# Fix use-after-frees when handling XML ISDS documents, in upstream after 0.9
Patch1:         shigofumi-0.9-Fix-two-use-after-frees-when-handling-XML-ISDS-docum.patch
# Adapt to changes in libxml2-2.12.0, in upstream after 0.9
Patch2:         shigofumi-0.9-Fix-building-with-libxml2-2.12.0.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  file-devel
BuildRequires:  gettext-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libisds) >= 0.10.7
BuildRequires:  readline-devel

%description
This is Shigofumi, an ISDS (Informační systém datových schránek / Data Box
Information System) client.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi

%build
%configure \
    --disable-debug \
    --enable-doc \
    --enable-fatalwarnings \
    --enable-largefile \
    --enable-nls \
    --disable-rpath \
    --enable-xattr
%{make_build}

%install
%{make_install}
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS TODO ChangeLog
%{_bindir}/shigofumi
%{_mandir}/man1/shigofumi.*
%{_mandir}/*/man1/shigofumi.*
%{_mandir}/man5/shigofumirc.*
%{_mandir}/*/man5/shigofumirc.*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 05 2024 Petr Pisar <ppisar@redhat.com> - 0.9-12
- Convert license tag to SPDX

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 24 2023 Petr Pisar <ppisar@redhat.com> - 0.9-8
- Adapt to changes in libxml2-2.12.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Petr Pisar <ppisar@redhat.com> - 0.9-4
- Fix use-after-frees when handling XML ISDS documents

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Petr Pisar <ppisar@redhat.com> - 0.9-3
- Fix building with GCC 12

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Petr Pisar <ppisar@redhat.com> - 0.9-1
- 0.9 bump (a license changed to "GPLv3+ and LGPLv2+")

* Wed Feb 24 2021 Petr Pisar <ppisar@redhat.com> - 0.8-17
- Adapt to Autoconf 2.71

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Petr Pisar <ppisar@redhat.com> - 0.8-13
- Fix building with GCC 10

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 0.8-12
- Fix argument to zfree call in tokenize

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8-10
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Petr Pisar <ppisar@redhat.com> - 0.8-7
- Adapt to attr-2.4.48

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Petr Pisar <ppisar@redhat.com> - 0.8-5
- Rebuild against libconfuse-3.2.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.8-2
- libconfuse rebuild.

* Fri Feb 17 2017 Petr Pisar <ppisar@redhat.com> - 0.8-1
- 0.8 bump

* Tue Feb 14 2017 Petr Pisar <ppisar@redhat.com> - 0.7-1
- 0.7 bump
- License corrected to "GPLv3+ and GPLv2+"

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6-5
- Rebuild for readline 7.x

* Wed Jun 15 2016 Petr Pisar <ppisar@redhat.com> - 0.6-4
- Rebuild against libconfuse-3.0
- Specify more dependencies

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Petr Pisar <ppisar@redhat.com> - 0.6-1
- 0.6 bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 01 2014 Petr Pisar <ppisar@redhat.com> - 0.5-1
- 0.5 bump
- Use _DEFAULT_SOURCE where _SVID_SOURCE macro presents to satisfy
  glibc-2.19.90

* Mon Oct 21 2013 Petr Pisar <ppisar@redhat.com> - 0.4-1
- 0.4 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Petr Pisar <ppisar@redhat.com> - 0.3-3
- Update config.sub to support aarch64 (bug #926524)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Petr Pisar <ppisar@redhat.com> - 0.3-1
- 0.3 bump

* Tue Oct 30 2012 Petr Pisar <ppisar@redhat.com> - 0.2-1
- 0.2 bump

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 03 2011 Petr Pisar <ppisar@redhat.com> - 0.1-6
- Rebuild against libisds-0.5

* Fri Feb 11 2011 Petr Pisar <ppisar@redhat.com> - 0.1-5
- Remove set but unread variable
- Remove BuildRoot stuff

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Petr Pisar <ppisar@redhat.com> - 0.1-3
- Rebuild against libisds-0.4

* Fri Nov 05 2010 Petr Pisar <ppisar@redhat.com> - 0.1-2
- Rebuild against new libxml2

* Thu Jul  8 2010 Petr Pisar <ppisar@redhat.com> - 0.1-1
- 0.1 import
