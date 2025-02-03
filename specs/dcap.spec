Name:		dcap
Version:	2.47.14
Release:	9%{?dist}
Summary:	Client Tools for dCache

#		plugins/gssapi/{base64.[ch],util.c} - BSD license
#		the rest - LGPLv2+ license
License:	LGPL-2.0-or-later AND BSD-3-Clause
URL:		https://www.dcache.org/manuals/libdcap.shtml
Source0:	https://github.com/dCache/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#		https://github.com/dCache/dcap/pull/28
Patch0:		0001-Add-missing-include-crypt.h.patch
#		https://github.com/dCache/dcap/pull/29
Patch1:		0001-Don-t-define-the-dc_xxx64-macros-while-compiling-dca.patch
#		https://github.com/dCache/dcap/pull/30
Patch2:		0001-Fix-spelling-errors.patch
Patch3:		0002-Avoid-format-errors-when-using-64-bit-time_t-on-32-b.patch

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:	globus-gssapi-gsi-devel
BuildRequires:	krb5-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	CUnit-devel
BuildRequires: libxcrypt-devel

%description
dCache is a distributed mass storage system.
This package contains the client tools.

%package libs
Summary:	Client Libraries for dCache
License:	LGPL-2.0-or-later

%description libs
dCache is a distributed mass storage system.
This package contains the client libraries.

%package devel
Summary:	Client Development Files for dCache
License:	LGPL-2.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
dCache is a distributed mass storage system.
This package contains the client development files.

%package tunnel-gsi
Summary:	GSI tunnel for dCache
License:	LGPL-2.0-or-later AND BSD-3-Clause
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-gsi
This package contains the gsi tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-krb
Summary:	Kerberos tunnel for dCache
License:	LGPL-2.0-or-later AND BSD-3-Clause
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-krb
This package contains the kerberos tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-ssl
Summary:	SSL tunnel for dCache
License:	LGPL-2.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-ssl
This package contains the ssl tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%package tunnel-telnet
Summary:	Telnet tunnel for dCache
License:	LGPL-2.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description tunnel-telnet
This package contains the telnet tunnel plugin library used by dcap-libs.
This library is dynamically loaded at runtime.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
./bootstrap.sh

%configure \
    --disable-static \
    --with-tunneldir=%{_libdir}/%{name} \
    --with-globus-include=%{_includedir}/globus \
    --with-globus-lib=/dummy
%make_build

%install
%make_install

# Remove libtool archive files
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/%{name}/*.la

# We are installing the docs in the files sections
rm -rf %{buildroot}/%{_docdir}

%check
%make_build check

%files
%{_bindir}/dccp
%{_mandir}/man1/dccp.1*

%files libs
%{_libdir}/libdcap.so.*
%{_libdir}/libpdcap.so.*
%dir %{_libdir}/%{name}
%license LICENSE COPYING.LIB AUTHORS

%files devel
%{_libdir}/libdcap.so
%{_libdir}/libpdcap.so
%{_includedir}/dc_hack.h
%{_includedir}/dcap.h
%{_includedir}/dcap_errno.h

%files tunnel-gsi
%{_libdir}/%{name}/libgsiTunnel.so
%license plugins/gssapi/Copyright

%files tunnel-krb
%{_libdir}/%{name}/libgssTunnel.so
%license plugins/gssapi/Copyright

%files tunnel-ssl
%{_libdir}/%{name}/libsslTunnel.so

%files tunnel-telnet
%{_libdir}/%{name}/libtelnetTunnel.so

%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 2.47.14-9
- Add explicit BR: libxcrypt-devel

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.14-7
- Backport accepted patches from upstream

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 13 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.14-3
- Add missing include crypt.h

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 01 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.14-1
- New upstream release

* Mon Jan 23 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.13-1
- New upstream release
- Drop patches accepted upstream

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.12-15
- Fix some compiler warnings and typos

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.47.12-13
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.47.12-6
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.12-4
- Fix an implicit declaration warning

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.47.12-2
- Rebuilt for switch to libxcrypt

* Sat Nov 18 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.12-1
- New upstream release

* Wed Oct 25 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.11-1
- New upstream release
- Drop patches (previously backported)
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Sat Aug 12 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.10-9
- Don't use deprecated TLSv1_client_method

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 15 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.10-5
- Rebuild for OpenSSL 1.1.0 (Fedora 26)
- Fix more compiler warnings

* Wed Sep 14 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.47.10-4
- Backport fixes from upstream

* Thu Mar 10 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.10-3
- Fix broken postun scriptlet in dcap-libs

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.47.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.10-1
- New upstream release
- Drop patch dcap-dlopen.patch - merged upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.9-1
- New upstream release
- Enable tests and add BR CUnit-devel (except EPEL 5)
- Adapt to new license packaging guidelines

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.8-1
- New upstream release
- Drop patch dcap-segfault.patch - merged upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.7-3
- Fix segfault

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.7-1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.6-2
- Remove encoding fixes

* Thu May 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.6-1
- New upstream release (EMI 2 release)
- Drop patches dcap-aliasing.patch and dcap-libs.patch implemented upstream

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 11 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.47.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 06 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.5-1
- New upstream release
- Drop dcap-docs.patch - implemented upstream
- Put CFLAGS back to default - the issue causing problem is fixed upstream

* Thu Jun 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.2-2
- Adjust CFLAGS so that the compiled program works correctly

* Wed Apr 07 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.47.2-1
- New upstream release
- Drop dcap-adler32.patch - implemented upstream

* Thu Mar 11 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.44.0-3
- Add missing build requires on autotools
- Fix configure to look for functions in the right libraries

* Wed Mar 10 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.44.0-2
- Use the adler32 function from zlib and drop the bundled source file
- Drop the zlib license tag again

* Wed Mar 10 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.44.0-1
- Major revision of spec file - upstream has started using autotools
- Add zlib license tag due to the adler32 source

* Sun Jan 03 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.44-2
- Porting to additional architectures
- Add BSD license tags for the tunnel-gsi and tunnel-krb sub packages

* Thu Dec 17 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.44-1
- Update to version 1.2.44 (svn tag 1.9.3-7)

* Thu Sep 17 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.42-2
- Update to new svn tag 1.9.3-3

* Thu Aug 13 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.42-1
- Initial Fedora package based on svn tag 1.9.3-1
