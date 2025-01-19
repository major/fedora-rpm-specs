%global major	1
%if 0%{?fedora}
%global with_docs	0
%else
%global with_docs	0
%endif

Name:		libircclient
Summary:	C library to create IRC clients
Version:	1.10
Release:	2%{?dist}
License:	LGPL-3.0-or-later
URL:		https://www.ulduzsoft.com/libircclient/
Source0:	https://downloads.sourceforge.net/libircclient/%{name}-%{version}.tar.gz
BuildRequires: make
%if %{with_docs}
BuildRequires:	doxygen
%endif
BuildRequires:	openssl-devel
%if %{with_docs}
BuildRequires:	python-sphinx
BuildRequires:	rst2pdf
%endif
BuildRequires:	gcc-c++
# Add rfc include to main header to avoid build failures of packages using it
# example: error: 'LIBIRC_RFC_RPL_ENDOFNAMES' was not declared in this scope
Patch0:		libircclient-rfc.patch
Patch1:		libircclient-1.8-nostrip.patch

%description
libircclient is a small but extremely powerful library which implements
the IRC protocol. It is designed to be small, fast, portable and compatible
with the RFC standards as well as non-standard but popular features.
It is perfect for building the IRC clients and bots.

%package	devel
Summary:	Development files for libircclient
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains development files for libircclient.

%prep
%setup -q
# Correct use of deprecated function to detect ssl
sed -e 's/SSL_library_init/SSL_CTX_new/g' -i configure
rm -rvf cocoa
%patch -P0 -p1
%patch -P1 -p1

%build
%configure --enable-shared --enable-threads --enable-openssl --enable-ipv6
make %{?_smp_mflags}
%if %{with_docs}
make -C doc html
%endif

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p man/%{name}.1 %{buildroot}%{_mandir}/man1

%ldconfig_scriptlets

%files
%if 0%{?fedora}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changelog
%doc THANKS
%{_libdir}/*.so.%{major}

%files		devel
%if %{with_docs}
%doc doc/_build/html/*
%endif
%{_libdir}/libircclient.so
%{_includedir}/libirc*.h
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Sérgio Basto <sergio@serjux.com> - 1.10-1
- Update libircclient to 1.10

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8-27
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.8-20
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Adam Huffman <bloch@verdurin.com> - 1.8-13
- Add BR for gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8-10
- Correct FTBFS in rawhide (#1423856)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.8-4
- Don't strip binaries too early

* Mon Apr 13 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8-3
- Do not build requires doxygen if not building docs
- Do not use the license macro on non fedora

* Mon Apr 13 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8-2
- Do not regenerate documentation on epel

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8-1
- Update to latest upstream release
- Remove patches already in upstream
- Switch to doxygen an python-sphinx documentation build

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-3
- Add Changelog, LICENSE, and THANKS files to main package.

* Fri May 4 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-2
- Add patch to create a shared library.
- Add documentation to devel package.

* Sat Apr 28 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-1
- Initial libircclient spec.
