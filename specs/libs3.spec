%global commit 287e4bee6fd430ffb52604049de80a27a77ff6b4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		libs3
Version:	4.1
Release:	0.22.20190408git%{shortcommit}%{?dist}
Summary:	C Library and Tools for Amazon S3 Access

License:	LGPL-3.0-or-later OR GPL-2.0-or-later
URL:		https://github.com/bji/libs3
Source0:	%{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
#		Fix compilation with openssl 3.0
#		https://github.com/bji/libs3/pull/112
Patch0:		libs3-openssl3.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel

%description
This package includes the libs3 shared object library, needed to run
applications compiled against libs3, and additionally contains the s3
utility for accessing Amazon S3.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1

%build
sed -e 's!^CFLAGS +=!& %{build_cflags}!' \
    -e 's!^LDFLAGS =!& %{build_ldflags}!' \
    -e 's!$(INSTALL) -Dps!$(INSTALL) -Dp!' \
    -i GNUmakefile

%make_build exported

%install
%make_install DESTDIR=%{buildroot}%{_prefix} LIBDIR=%{buildroot}%{_libdir}
rm %{buildroot}%{_libdir}/libs3.a
chmod 755 %{buildroot}%{_libdir}/libs3.so.4.1

%check
%make_build test

%files
%{_bindir}/s3
%{_libdir}/libs3.so.*
%license COPYING-LGPLv3 COPYING-GPLv2 LICENSE

%files devel
%{_includedir}/libs3.h
%{_libdir}/libs3.so

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.22.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.21.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.20.20190408git287e4be
- Update License tags (SPDX)
- Eliminate use of obsolete patchN syntax

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.19.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.18.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.17.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.16.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.15.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.14.20190408git287e4be
- Move makefile modification from prep to build section
  Workaround for breakage caused by broken redhat-rpm-config update

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.13.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.1-0.12.20190408git287e4be
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.11.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.10.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.9.20190408git287e4be
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.8.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.7.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.6.20190408git287e4be
- New github snapshot

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.5.20181203git111dc30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.4.20181203git111dc30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.3.20181203git111dc30
- New github snapshot
- Drop patch libs3-curl-7.62.patch (merged upstream)
- Update License tag

* Thu Nov 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.2.20180821gita4d873f
- Support curl >= 7.62

* Fri Aug 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.1.20180821gita4d873f
- New github snapshot

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.0-0.6.20170206git208bcba
- Add BuildRequires on gcc
- Packaging updates
  - Remove Group and BuildRoot tags
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Install license in licensedir
  - Use new ldconfig scriptlets macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.5.20170206git208bcba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.4.20170206git208bcba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.3.20170206git208bcba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.2.20170206git208bcba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.0-0.1.20170206git208bcba
- New github snapshot

* Thu Dec 01 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.5.20161104gita052a00
- New github snapshot
- Drop fix for old nice lib on EPEL 5 (fixed upstream)

* Fri May 20 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.4.20160322git0759f1d
- New github snapshot
- Drop patch libs3-format.patch (accepted upstream)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.3.20150902git247ba1b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.2.20150902git247ba1b
- Fix compilation on 32 bit archs

* Wed Sep 09 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.1.20150902git247ba1b
- Initial package
