%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           tcl-thread
Version:        2.8.8
Release:        6%{?dist}
Summary:        Tcl Thread extension
License:        TCL
URL:            http://tcl.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/tcl/thread%{version}.tar.gz
Patch0:         tcl-thread-x86_64-build.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  tcl-devel
BuildRequires:  gdbm-devel
Requires:       tcl(abi) = 8.6

%description
Thread extension for the Tcl toolkit.  You can use this extension to gain
script level access to Tcl threading capabilities.

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Include files and mandatory libraries for development.

%prep
%autosetup -p0 -n thread%{version}

%build
%configure --with-gdbm --enable-64bit
%make_build

%install
%make_install
mkdir -p %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/thread%{version} %{buildroot}%{tcl_sitearch}/
chmod 755 %{buildroot}%{tcl_sitearch}/thread%{version}/libthread%{version}.so

%files
%doc README ChangeLog
%license license.terms
%{tcl_sitearch}/thread%{version}
%{_mandir}/mann/*

%files devel
%{_includedir}/tclThread.h

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.8-1
- Update to 2.8.8

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 2.8.5-1
- Update to 2.8.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Vasiliy N. Glazov <vascom2@gmail.com> 2.8.2-1
- Update to 2.8.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 - Wart <wart at kobold.org> 2.6.5-6
- Rebuild for gcc 4.3

* Fri Jan 4 2008 - jwboyer@jdub.homelinux.org 2.6.5-5
- Fix build problem caused by path mismatch on 64-bit platforms

* Fri Jan 4 2008 - jwboyer@jdub.homelinux.org 2.6.5-4
- Rebuild for Tcl 8.5

* Tue Aug 28 2007 - jwboyer@jdub.homelinux.org 2.6.5-3
- Rebuild for BuildID
- Correct license tag

* Fri Nov 3 2006 - jwboyer@jdub.homelinux.org 2.6.5-2
- Update for review comments
- Add patch to compile on x86_64

* Thu Oct 26 2006 - jwboyer@jdub.homelinux.org 2.6.5-1
- Initial tcl-threads
