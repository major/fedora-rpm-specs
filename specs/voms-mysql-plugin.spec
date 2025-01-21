Name:		voms-mysql-plugin
Version:	3.1.7
Release:	24%{?dist}
Summary:	VOMS server plugin for MySQL

License:	Apache-2.0
URL:		https://italiangrid.github.io/voms/
Source:		https://github.com/italiangrid/%{name}/archive/v%{version}.tar.gz

Provides:	voms-mysql = %{version}-%{release}
Obsoletes:	voms-mysql < 3.1.6
Requires:	voms-server%{?_isa}

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	libtool
%if %{?fedora}%{!?fedora:0} >= 28 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	mariadb-connector-c-devel
%else
BuildRequires:	mysql-devel
%endif
BuildRequires:	openssl-devel

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package offers the MySQL implementation for the VOMS server.

%prep
%setup -q
./autogen.sh

%build
%configure --libdir=%{_libdir}/voms --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/voms/libvomsmysql.la

%files
%{_datadir}/voms/voms-mysql.data
%{_datadir}/voms/voms-mysql-compat.data
%dir %{_libdir}/voms
%{_libdir}/voms/libvomsmysql.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.7-23
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.1.7-16
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.7-13
- Add BuildRequires on make

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.7-8
- Add BuildRequires on gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.7-5
- Build using mariadb-connector-c for Fedora 28+
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 11 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.1.7-1
- Update to version 3.1.7

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.6-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.6-5
- Use non-isa build deps

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.6-1
- Update to version 3.1.6 (EMI 2 version)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 31 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.5.1-1
- Update to version 3.1.5.1

* Wed Mar 23 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.3.2-3
- Rebuild for mysql 5.5.10

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jun 06 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.3.2-1
- Update to version 3.1.3.2
- Drop all patches (accepted upstream)

* Thu Dec 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.3.1-1
- Update to version 3.1.3.1

* Sat Aug 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.1-1
- Update to version 3.1.1

* Tue Jun 30 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1.0-1
- First build
