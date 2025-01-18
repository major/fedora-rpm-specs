#%%global _default_patch_fuzz 2

%global bootstrap 1

%global shortversion 5.3.0
%global libver 11

Name:           chicken
Version:        %{shortversion}
Release:        9%{?dist}
Summary:        A practical and portable Scheme system

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://call-cc.org
Source0:        http://code.call-cc.org/releases/%{shortversion}/%{name}-%{version}.tar.gz
Patch0:         make_cflags_work.patch
BuildRequires:  gcc
BuildRequires:  chrpath
Requires:       chicken-libs%{?_isa} = %{version}-%{release}

# Old docs subpackage, which is no longer a subpackage
Obsoletes:      chicken-doc < 4.8.0.5-3
Provides:       chicken-doc = %{version}-%{release}

%if 0%{?rhel}
BuildRequires:  net-tools
%else
BuildRequires:  hostname
%endif

%if %{bootstrap} == 0
BuildRequires:  chicken
%endif
BuildRequires: make

%package libs
Summary:        Chicken Scheme runtime library

%description libs
The Chicken Scheme runtime library, linked to by programs compiled with
Chicken.

%package static
Summary:	Static library for Chicken
Requires:	chicken%{?_isa} = %{version}-%{release}

%description static
The Chicken Scheme runtime library, as a static library for users
to link against

%description
CHICKEN is a compiler for the Scheme programming language.
CHICKEN produces portable, efficient C, supports almost all of the R5RS
Scheme language standard, and includes many enhancements and extensions.

%prep
%autosetup -n %{name}-%{version}

%build
%if %{bootstrap} == 0

# This removes all C code from the repo, and leaves us only with Scheme code.
# Otherwise, it will try to compile C, defeating the point of bootstrapping.
make PLATFORM=linux spotless

# The above command nukes a necessary buildtag file, and there's no way that
# I can find to regenerate it - so instead we just generate it ourselves.
echo "#define C_BUILD_TAG \"compiled $(date '+%Y-%m-%d') on $(hostname)\"" > buildtag.h

%endif

# Chicken's build system is freaking horrible.
# So, Fedora requires that we use optflags here - makes sense, they contain
# some security related flags, etc. The issue is that Chicken uses the same
# flags that it was compiled with when it compiles code for the end-user.
# So if we pass -Wall here, it'll give the user a bunch of warnings when they
# compile anything at all with `csc`. So that's lovely. -codeblock

# Can't even use %%{make_build} or anything, since everything breaks... -sham1
make CFLAGS="$(echo "%{optflags}" | sed 's/-Wall//') -Wformat" \
     PREFIX=%{_prefix} \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     DATADIR=%{_datadir}/chicken \
     INCLUDEDIR=%{_includedir} \
     INFODIR=%{_infodir}/chicken \
     TOPMANDIR=%{_mandir} \
     DOCDIR=%{_docdir}/chicken \
     PLATFORM=linux

%install
make CFLAGS="$(echo "%{optflags}" | sed 's/-Wall//') -Wformat" \
     PREFIX=%{_prefix} \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     DATADIR=%{_datadir}/chicken \
     INCLUDEDIR=%{_includedir} \
     INFODIR=%{_infodir}/chicken \
     TOPMANDIR=%{_mandir} \
     DOCDIR=%{_docdir}/chicken \
     DESTDIR=%{buildroot} \
     PLATFORM=linux install

rm -f %{buildroot}/%{_docdir}/%{name}/LICENSE %{buildroot}/%{_docdir}/%{name}/README

find %{buildroot} -name \*.so -exec chrpath --delete \{\} \;
chrpath --delete %{buildroot}/%{_bindir}/chicken*
chrpath --delete %{buildroot}/%{_bindir}/csc
chrpath --delete %{buildroot}/%{_bindir}/csi

%check
make PLATFORM=linux check

%ldconfig_scriptlets libs

%files
%doc README LICENSE
%dir %{_datadir}/chicken
%{_datadir}/chicken/setup.defaults
%{_bindir}/chicken*
%{_bindir}/csc
%{_bindir}/csi
%{_bindir}/feathers
%dir %{_includedir}/chicken
%{_includedir}/chicken/chicken-config.h
%{_includedir}/chicken/chicken.h
%{_datarootdir}/chicken/feathers.tcl
%dir %{_libdir}/chicken
%dir %{_libdir}/chicken/%{libver}
%{_libdir}/chicken/%{libver}/*
%{_mandir}/man1/*
%{_docdir}/chicken

%files libs
%{_libdir}/libchicken.so*

%files static
%{_libdir}/libchicken.a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.3.0-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 10 2022 Jani Juhani Sinervo <jani@sinervo.fi> - 5.3.0-1
- Update to latest upstream version (RHBZ#2024501)
- Add -static subpackage for users to link against (RHBZ#2083300)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 28 2021 Jani Juhani Sinervo <jani@sinervo.fi> - 5.2.0-1
- Update to latest upstream release
- Fix a bunch of bugs

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Rick Elrod <relrod@redhat.com> - 5.0.0-2
- Build from the bootstrap.

* Fri Mar 15 2019 Rick Elrod <relrod@redhat.com> - 5.0.0-1
- Bump for latest release
- Drop CVE patches
- Bump libver.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Ricky Elrod <relrod@redhat.com> - 4.12.0-3
- Fix for CVE-2017-11343

* Thu May 11 2017 Ricky Elrod <relrod@redhat.com> - 4.12.0-2
- And use the bootstrap.

* Thu May 11 2017 Ricky Elrod <relrod@redhat.com> - 4.12.0-1
- Latest upstream release.
- Bootstrap for el7 aarch64.

* Tue Mar 21 2017 Ricky Elrod <relrod@redhat.com> - 4.11.0-5
- Fix for CVE-2017-6949

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 23 2016 Ricky Elrod <relrod@redhat.com> - 4.11.0-3
- Patch around CVE-2016-6830 and CVE-2016-6831

* Fri Jul 08 2016 Ricky Elrod <relrod@redhat.com> - 4.11.0-2
- Rebuild.

* Tue Jul 05 2016 Ricky Elrod <relrod@redhat.com> - 4.11.0-1
- Latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Ricky Elrod <relrod@redhat.com> - 4.10.0-1
- Latest upstream release.
- Drop former patches.

* Mon Jun 15 2015 Ricky Elrod <relrod@redhat.com> - 4.9.0.1-4
- Apply patch to work around out of bounds bug:
  https://bugzilla.redhat.com/show_bug.cgi?id=1231871

* Tue Jan 13 2015 Ricky Elrod <relrod@redhat.com> - 4.9.0.1-3
- Apply patch to work around buffer overrun:
  https://bugzilla.redhat.com/show_bug.cgi?id=1181483

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Ricky Elrod <relrod@redhat.com> - 4.9.0.1-1
- Latest upstream release.

* Sat Jun 07 2014 Ricky Elrod <relrod@redhat.com> - 4.9.0-4
- Rebuild from previous bootstrap.

* Sat Jun 07 2014 Ricky Elrod <relrod@redhat.com> - 4.9.0-3
- Bootstrap for el7.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Ricky Elrod <codeblock@fedoraproject.org> - 4.9.0-1
- Latest upstream release.

* Tue May 20 2014 Ricky Elrod <codeblock@fedoraproject.org> - 4.8.0.6-2
- Patch for CVE-2014-3776.

* Thu Apr 24 2014 Ricky Elrod <codeblock@fedoraproject.org> - 4.8.0.6-1
- Upstream 4.8.0.6.

* Sat Dec 14 2013 Ricky Elrod <codeblock@fedoraproject.org> - 4.8.0.5-3
- Get rid of docs subpackage.
- Add a -libs subpackage for the runtime library.

* Sun Dec 8 2013 Ricky Elrod <codeblock@fedoraproject.org> - 4.8.0.5-2
- Add -Wformat for BZ #1037013.

* Sun Nov 24 2013 Ricky Elrod <codeblock@fedoraproject.org> - 4.8.0.5-1
- Upstream 4.8.0.5.

* Fri Sep 27 2013 Ricky Elrod <codeblock@fedoraproject.org> - 4.8.0.4-4
- Add upstream patch for CVE-2013-4385, until 4.8.0.5 is released.
  http://code.call-cc.org/cgi-bin/gitweb.cgi?p=chicken-core.git;a=commitdiff;h=cd1b9775005ebe220ba11265dbf5396142e65f26

* Mon Sep 02 2013 Ricky Elrod <codeblock@fedoraproject.org> - 4.8.0.4-3
- Nuke -Wall from optflags.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Ricky Elrod <codeblock@fedoraproject.org> 4.8.0.4-1
- Upstream 4.8.0.4.

* Sat May 11 2013 Ricky Elrod <codeblock@fedoraproject.org> 4.8.0.3-4
- Bootstrap again, with working CFLAGS.

* Wed May 08 2013 Ricky Elrod <codeblock@fedoraproject.org> 4.8.0.3-3
- Bootstrap.

* Wed May 08 2013 Ricky Elrod <codeblock@fedoraproject.org> 4.8.0.3-2
- Fix BuildRequires for RHEL building.

* Sun May 05 2013 Ricky Elrod <codeblock@fedoraproject.org> 4.8.0.3-1
- Clean spec file up a lot.
- Bump to latest upstream release.

* Thu May 03 2012 J R Jones <fedora@zaniyah.org> 4.7.0-2
- Separated into separate sub-packages

* Thu May 03 2012 J R Jones <fedora@zaniyah.org> 4.7.0-1
- Specfile created.
