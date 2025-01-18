%global minorver 1

Name:		ftplib
Version:	4.0
Release:	24%{?dist}
Summary:	Library of FTP routines
License:	LGPLv2+
URL:		http://nbpfaus.net/~pfau/ftplib-4/
Source0:	http://nbpfaus.net/~pfau/ftplib-4/%{name}-%{version}-%{minorver}.tar.gz
Patch0:		ftplib-3.1-1-modernize.patch
BuildRequires:	gcc
BuildRequires: make

%description
ftplib is a set of routines that implement the FTP protocol. They allow 
applications to create and access remote files through function calls 
instead of needing to fork and exec an interactive ftp client program.

%package devel
Summary:	Development files for ftplib
Requires:	ftplib = %{version}-%{release}

%description devel
Development libraries and headers for ftplib.

%package -n qftp
Summary:	Simple ftp client application
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later

%description -n qftp
Command line driven ftp file transfer program using ftplib.

%prep
%setup -q -n %{name}-%{version}-%{minorver}
%patch -P0 -p1 -b .modern

%build
cd src/
make %{?_smp_mflags} DEBUG="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cd src/
make DESTDIR=$RPM_BUILD_ROOT LIBDIR="%{_libdir}" install

cd ${RPM_BUILD_ROOT}%{_libdir}
chmod +x libftp.so.4.0
ln -sf libftp.so.4.0 libftp.so.4
ln -sf libftp.so.4 libftp.so

cd ${RPM_BUILD_ROOT}%{_bindir}
for f in ftpdir ftpget ftplist ftprm ftpsend; do
	ln -s qftp $f
done

%ldconfig_scriptlets

%files
%doc CHANGES
%license LICENSE
%{_libdir}/libftp*.so.*

%files devel
%doc additional_rfcs README.ftplib* RFC959.txt html/
%{_includedir}/ftplib.h
%{_libdir}/libftp*.so

%files -n qftp
%doc README.qftp
%{_bindir}/ftpdir
%{_bindir}/ftpget
%{_bindir}/ftplist
%{_bindir}/ftprm
%{_bindir}/ftpsend
%{_bindir}/qftp

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.0-23
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 4.0-9
- add BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 23 2016 Tom Callaway <spot@fedoraproject.org> - 4.0-3
- update to 4.0-1 sources

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Tom Callaway <spot@fedoraproject.org> - 4.0-1
- update to 4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1-4
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.1-3
- fix licensing (v2+)
- rebuild for BuildID (F-8)

* Mon Jun  4 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.1-2
- fix licensing (libs LGPL, qftp GPL)

* Mon Jun  4 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.1-1
- initial build for Fedora
