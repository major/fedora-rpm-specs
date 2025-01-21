%{!?tcl_version: %global tcl_version %((echo '8.6'; echo 'puts $tcl_version' | tclsh 2>/dev/null) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

%define real_name mysqltcl

Summary:        MySQL interface for Tcl
Name:           tcl-mysqltcl
Version:        3.052
Release:        24%{?dist}

License:        MIT
Source:         http://www.xdobry.de/mysqltcl/%{real_name}-%{version}.tar.gz
URL:            http://www.xdobry.de/mysqltcl

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  tcl-devel
Requires:       tcl(abi) = %{tcl_version}
Provides:       %{real_name} = %{version}-%{release}

%description
Mysqltcl is an extension to the Tool Command Language (Tcl) that
provides high-level access to a MySQL database server.


%prep
%setup -q -n mysqltcl-%{version}
chmod -x generic/mysqltcl.c
chmod 644 README ChangeLog COPYING AUTHORS README-msqltcl doc/mysqltcl.html

%build
%configure --with-tcl=%{_libdir} \
           --with-mysql-lib=%{_libdir} \
           --enable-threads \
           --enable-symbols
make %{?_smp_mflags}


%install
rm -Rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{tcl_sitearch}
mv $RPM_BUILD_ROOT%{_libdir}/%{real_name}-%{version} $RPM_BUILD_ROOT%{tcl_sitearch}/%{real_name}-%{version}


%files
%doc README ChangeLog COPYING AUTHORS README-msqltcl doc/mysqltcl.html
%{tcl_sitearch}/%{real_name}-%{version}
%{_mandir}/mann/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Rene Plötz <reneploetz@gmx.de> - 3.052-17
- Refactor build according to current package guidelines

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Rene Plötz <reneploetz@gmx.de> - 3.052-8
- Update to change path of mariadb client library

* Wed Nov 01 2017 Rene Plötz <reneploetz@gmx.de> - 3.052-7
- Rebuilt using mariadb-connector-c-devel (RHBZ#1493660)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Rene Ploetz <RenePloetz@gmx.de> - 3.052-4
- Rebuild against MariaDB 10.2 (RHBZ#1467667)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.052-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Rene Ploetz <RenePloetz@gmx.de> - 3.052-1
- update to upstream release 3.052

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.05-17
- Changed requires to require tcl-8.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.05-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 3.05-11
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Wed Mar 23 2011 Rene Ploetz <RenePloetz@gmx.de> - 3.05-10
- Rebuilt against newer libmysqlclient

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 27 2009 Rene Ploetz <RenePloetz@gmx.de> 3.05-8
- split spec file versions for EL-4 and EL-5 from those of Fedora

* Wed Oct 27 2009 Rene Ploetz <RenePloetz@gmx.de> 3.05-7
- fix tcl version on EL-4 and EL-5

* Wed Oct 08 2009 Rene Ploetz <RenePloetz@gmx.de> 3.05-6
- synchronize the spec file version for all branches

* Wed Oct 07 2009 Rene Ploetz <RenePloetz@gmx.de> 3.05-5
- Fix build on EL-4

* Sat Oct 03 2009 Rene Ploetz <RenePloetz@gmx.de> 3.05-4
- Removed unnecessary Obsoletes tag

* Tue Sep 21 2009 Rene Ploetz <RenePloetz@gmx.de> 3.05-3
- Updated spec file according to bz #466047 comments 17-19

* Thu Oct 30 2008 Rene Ploetz <RenePloetz@gmx.de> 3.05-2
- Updated spec file

* Thu Oct 7 2008 Rene Ploetz <RenePloetz@gmx.de> 3.05-1
- Initial mysqltcl
