Name: libcli
Version: 1.10.7
Release: 10%{?dist}
Summary: A shared library for a Cisco-like cli
License: LGPL-2.1-or-later
URL: http://sites.dparrish.com/libcli
Source0: https://github.com/dparrish/libcli/archive/V%{version}/%{name}-%{version}.tar.gz

# https://github.com/dparrish/libcli/pull/93
Patch0: calloc.patch

%package devel
Summary: Development files for libcli
Requires: %{name}%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
BuildRequires: make
%description
Libcli provides a shared library for including a Cisco-like command-line 
interface into other software. It's a telnet interface which supports 
command-line editing, history, authentication and callbacks for a 
user-definable function tree. 

%description devel
Libcli provides a shared library for including a Cisco-like command-line 
interface into other software. It's a telnet interface which supports 
command-line editing, history, authentication and callbacks for a 
user-definable function tree. 

These are the development files.

%prep
%setup -q

%patch -P 0 -p0

%build

make %{?_smp_mflags}

%install
install -d -p %{buildroot}%{_includedir}
install -p -m 644 libcli*.h %{buildroot}%{_includedir}/
install -d -p %{buildroot}%{_libdir}
install -p -m 755 libcli.so.%{version} %{buildroot}%{_libdir}/
ln -s %{_libdir}/libcli.so.%{version} %{buildroot}%{_libdir}/libcli.so.1.10
ln -s %{_libdir}/libcli.so.1.10 %{buildroot}%{_libdir}/libcli.so

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/*.so.1.10*

%files devel
%doc README.md
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.10.7-8
- Patch for calloc parameter order.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.10.7-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.10.7-1
- 1.10.7

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160141gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160140gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160139gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160138gite60d4cc
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160137gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160136gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160135gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160134gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.9.7-0.20160133gite60d4cc
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160132gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160131gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.9.7-0.20160130gite60d4cc
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160129gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160128gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160127gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-0.20160126gite60d4cc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jason Taylor <jtfas90@gmail.com> - 1.9.7-0
- Updated to latest upstream stable commit
- Updates to spec file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Jon Ciesla <limburgher@gmail.com> - 1.9.6-1
- Latest upstream.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Jon Ciesla <limb@jcomserv.net> - 1.9.5-3
- Corrected buildroot tag.

* Wed Nov 23 2011 Jon Ciesla <limb@jcomserv.net> - 1.9.5-2
- Added isa for -devel requires.
- Dropped setting of PREFIX from build section.
- Added README to -devel.

* Mon Oct 17 2011 Jon Ciesla <limb@jcomserv.net> - 1.9.5-1
- create.
