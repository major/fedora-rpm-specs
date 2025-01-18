%ifarch aarch64
# ext/termios currently crashing:
# Testing termios ...
# *** ERROR: A string containing NUL character is not allowed: #**"\xb0;\xfd;\xbb;\xa3;\xff;\xff;\0"
#     While loading "././test.scm" at line 162
%bcond_with tests
%else
%bcond_without tests
%endif

%define abi_version 0.98

Name:			gauche
Version:		0.9.12
Release:		8%{?dist}
Summary:		Scheme script interpreter with multibyte character handling

License:		BSD-3-Clause AND MIT
URL:			http://practical-scheme.net/gauche
Source0:		https://github.com/shirok/Gauche/releases/download/release0_9_12/Gauche-%{version}.tgz

Patch0:			%{name}-ext-ldflags.patch
Patch1:			%{name}-xz-info.patch

ExcludeArch:	armv7hl

BuildRequires:	gcc
BuildRequires:	gdbm-devel
BuildRequires:	make
BuildRequires:	mbedtls-devel
BuildRequires:	openssl
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:		lib%{name}%{?_isa} = %{version}-%{release}
Recommends:		slib


%description
Gauche is a Scheme interpreter conforming Revised^5 Report on
Algorithmic Language Scheme. It is designed for rapid development of
daily tools like system management and text processing. It can handle
multibyte character strings natively.


%package -n lib%{name}
Summary: Gauche runtime shared library

%description -n lib%{name}
This package contains Gauche runtime shared library


%package -n lib%{name}-static
Summary: Statically linked library for Gauce
Requires:	lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-static
This package contains statically linked library for Gauce.
Most users should *not* install this.


%package devel
Summary: Development files for Gauche
Requires:	lib%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for Gauche.


%package doc
Summary: Documentation files for Gauche

%description doc
This package contains info documents of the reference manual of Gauche
(English, Japanese).


%prep
%autosetup -n Gauche-%{version} -p1


%build
%configure --with-rpath=no --enable-threads=pthreads --enable-multibyte=utf-8 --with-slib=%{_datadir}/slib --enable-ipv6
LD_LIBRARY_PATH=`pwd`/src %make_build


%install
LD_LIBRARY_PATH=`pwd`/src %make_install

# correct permissions
chmod -R u+w %{buildroot}
# make .c files readable for debuginfo
find -name '*.c' | xargs chmod 0644


%if %{with tests}
%check
LD_LIBRARY_PATH=`pwd`/src make check
%endif


%post
# creates slib catalog, if possible.
/usr/bin/gosh -u slib -e "(require 'logical)" -e "(exit 0)" > /dev/null 2>&1 || echo


%files
%license COPYING
%doc ChangeLog AUTHORS README.adoc VERSION
%{_bindir}/gauche-cesconv
%{_bindir}/gosh
%{_datadir}/gauche-%{abi_version}
%{_libdir}/gauche-%{abi_version}
%{_mandir}/man*/gauche-cesconv.*
%{_mandir}/man*/gosh.*
%exclude %{_libdir}/gauche-%{abi_version}/%{version}/include
%exclude %{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-%{abi_version}.so*
%exclude %{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-static-%{abi_version}.a
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/aclocal.m4
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/lib/build-standalone
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/lib/gencomp
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/lib/genstub
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/lib/precomp
%exclude %{_datadir}/gauche-%{abi_version}/%{version}/package-templates
%exclude %{_libdir}/libgauche-%{abi_version}.so.*
%exclude %{_libdir}/libgauche-static-%{abi_version}.a


%files devel
%doc HACKING.adoc
%{_bindir}/gauche-config
%{_bindir}/gauche-install
%{_bindir}/gauche-package
%{_datadir}/aclocal/gauche.m4
%{_datadir}/gauche-%{abi_version}/%{version}/aclocal.m4
%{_datadir}/gauche-%{abi_version}/%{version}/lib/build-standalone
%{_datadir}/gauche-%{abi_version}/%{version}/lib/gencomp
%{_datadir}/gauche-%{abi_version}/%{version}/lib/genstub
%{_datadir}/gauche-%{abi_version}/%{version}/lib/precomp
%{_datadir}/gauche-%{abi_version}/%{version}/package-templates
%{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-%{abi_version}.so
%{_libdir}/libgauche-%{abi_version}.so
%{_libdir}/gauche-%{abi_version}/%{version}/include
%{_mandir}/man*/gauche-config*
%{_mandir}/man*/gauche-install.*
%{_mandir}/man*/gauche-package.*


%files doc
%{_infodir}/gauche-*


%files -n lib%{name}
%{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-%{abi_version}.so.*
%{_libdir}/libgauche-%{abi_version}.so.*


%files -n lib%{name}-static
%{_libdir}/gauche-%{abi_version}/%{version}/*/libgauche-static-%{abi_version}.a
%{_libdir}/libgauche-static-%{abi_version}.a


%ldconfig_scriptlets -n lib%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Morten Stevens <mstevens@fedoraproject.org> - 0.9.12-7
- Rebuilt for mbedTLS 3.6.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 2 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.9.11-2
- armv7hl excluded due to qemu compilation issue (rhbz#2044282)

* Tue Mar 29 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.9.11-1
- Update to 0.9.11 and IPv6 option enabled

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.10-1
- Update to 0.9.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.9-1
- Update to 0.9.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.9.5-8
- Rebuilt for new freeglut

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.5-5
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jan 03 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.5-4
- Use sequential make, fixes FTBFS (#1604051)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.5-1
- Update to 0.9.5

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.4-8
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.4-2
- Drop ExcludeArch for ppc64

* Wed Dec  3 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9.4-1
- Update to 0.9.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.3.3-1
- Update to 0.9.3.3

* Sun May 13 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.3.2-1
- Update to 0.9.3.2

* Fri May 11 2012 Michel Salim <salimma@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3
- Update URL field
- Spec clean-ups

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Sun Feb  6 2011 Gérard Milmeister <gemi@bluewin.ch> - 0.9.1-1
- new release 0.9.1

* Sat Jul 25 2009 Gerard Milmeister <gemi@bluewin.ch> - 0.8.14-3
- patch for setting target arch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Gerard Milmeister <gemi@bluewin.ch> - 0.8.14-1
- new release 0.8.14

* Mon Apr 14 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.8.13-2
- set correct path to slib

* Thu Feb 14 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.8.13-1
- new release 0.8.13

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.8.11-2
- exclude arch ppc64

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.8.11-1
- new release 0.8.11

* Fri Apr 20 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.8.10-1
- new version 0.8.10

* Thu Jan 18 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.8.9-1
- new version 0.8.9

* Mon Nov 13 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.8.8-2
- new version 0.8.8

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.8.7-6
- Rebuild for FE6

* Thu May  4 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.8.7-5
- added patch for consistent arch directories (gauche-arch.patch)

* Fri Apr 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.8.7-3
- added %%check
- included COPYING file in %%doc

* Thu Apr 27 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.8.7-2
- fixes permissions
- patch to fix jp problem in texinfo file

* Fri Apr 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.8.7-1
- new version 0.8.7

* Sun Nov  6 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.8.6-1
- New Version 0.8.6

* Fri Jul  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.8.5-1
- New Version 0.8.5

* Wed Feb 23 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:0.8.3-1
- New Version 0.8.3

* Sat Aug  7 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.8.1-0.fdr.1
- New Version 0.8.1

* Sun May 23 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.8-0.fdr.1
- New Version 0.8

* Fri Mar 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.7.4.2-0.fdr.1
- New Version 0.7.4.2

* Fri Mar 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.7.4.1-0.fdr.1
- New Version 0.7.4.1

* Sun Nov  9 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:0.7.2-0.fdr.1
- First Fedora release
