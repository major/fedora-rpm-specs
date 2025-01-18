%global _hardened_build 1

Name:		fswatch
Version:	1.17.1
Release:	4%{?dist}
Summary:	A cross-platform file change monitor
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/emcrisostomo/fswatch
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++ gcc gettext-devel
BuildRequires: make

%description
%{name} is a cross-platform file change monitor.

%package devel
Summary:	Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and headers for lib%{name}.

%package static
Summary:	Static library for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static 
Static library (.a) of lib%{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build

%install
%make_install
mkdir $RPM_BUILD_ROOT%{_mandir}/man1/
mv $RPM_BUILD_ROOT%{_mandir}/man7/%{name}.7 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*

%find_lang %{name}

%check
make check

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md README.linux AUTHORS NEWS CONTRIBUTING.md ABOUT-NLS
%license COPYING
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files devel
%doc README.libfswatch.md AUTHORS.libfswatch NEWS.libfswatch
%{_libdir}/lib%{name}.so
%{_includedir}/lib%{name}/*
%{_libdir}/pkgconfig/libfswatch.pc

%files static
%{_libdir}/*.a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.17.1-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 06 2024 Darryl T. Agostinelli <dagostinelli@gmail.com> 1.17.1-1
- Update to version 1.17.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 08 2021 Darryl T. Agostinelli <dagostinelli@gmail.com 1.14.0-6
- Update for autoconf-2.71 upgrade

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Darryl T. Agostinelli <dagostinelli@gmail.com> 1.14.0-3
- Corrections made for package review process

* Sun May 03 2020 Darryl T. Agostinelli <dagostinelli@gmail.com> 1.14.0-2
- Corrections made for package review process

* Sat Apr 11 2020 Darryl T. Agostinelli <dagostinelli@gmail.com> 1.14.0-1
- Created the .spec file for version 1.14.0
