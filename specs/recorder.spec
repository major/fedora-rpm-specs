Name:           recorder
Version:        1.2.2
Release:        10%{?dist}
Summary:        Lock-free, real-time flight recorder for C or C++ programs
License:        LGPLv2+
Url:            https://github.com/tao-3D/%{name}
Source:         https://github.com/tao-3D/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make >= 3.82
BuildRequires:  make-it-quick >= 0.3.2
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Flight recorder for C and C++ programs using printf-like 'record' statements.

%package devel
Summary:        Development files for recorder library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the flight recorder library.

%package scope
Summary:        A real-time graphing tool for data collected by recorder library
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtcharts-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description scope
Instrumentation that draws real-time charts, processes or saves data
collected by the flight_recorder library.

%prep
%autosetup -n %{name}-%{version}

%build
%configure

%make_build COLORIZE= TARGET=release V=1
(cd scope &&                            \
 %{qmake_qt6}                           \
        INSTALL_BINDIR=%{_bindir}       \
        INSTALL_LIBDIR=%{_libdir}       \
        INSTALL_DATADIR=%{_datadir}     \
        INSTALL_MANDIR=%{_mandir} &&    \
 make)

%check
%make_build COLORIZE= TARGET=release V=1 check

%install
%make_install COLORIZE= TARGET=release DOC_INSTALL=
%make_install -C scope TARGET=release INSTALL_ROOT=%{buildroot}

%files
%license COPYING
%doc README.md
%doc AUTHORS
%doc NEWS
%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_libdir}/lib%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_datadir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.*

%files scope
%{_bindir}/recorder_scope
%{_mandir}/man1/*.1.*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 16 2024 Jan Grulich <jgrulich@redhat.com> - 1.2.2-9
- Rebuild (qt6)

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.2-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 03 2024 Jan Grulich <jgrulich@redhat.com> - 1.2.2-6
- Rebuild (qt6)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 2 2022 Christophe de Dinechin <dinechin@redhat.com> - 1.2.2-1
- Upstream release 1.2.2, deal with errors showing in Koji

* Mon Aug 1 2022 Christophe de Dinechin <dinechin@redhat.com> - 1.2.1-1
- Upstream release 1.2.1, fixing configure script

* Mon Aug 1 2022 Christophe de Dinechin <dinechin@redhat.com> - 1.2.0-1
- Upstream release 1.2.0
- Add support for qt6
- Fix build failures

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 9 2021 Christophe de Dinechin <dinechin@redhat.com> - 1.1.0-1
- Add support for indentation

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.0.12-2
- Updated NEWS in sources, fix Qt5-Charts dependency

* Wed Jul 29 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.0.12-1
- Add support for disabling recording
- Switch to tao-3D organization rather than personal repository

* Wed Jul 29 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.0.11-1
- Add support for prefix - in trace specifications, e.g. -foo

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 6  2020 Christophe de Dinechin <dinechin@redhat.com> - 1.0.10-2
- Update BUildRequires to make-it-quick 0.2.6 to fix pkgconfig issue

* Fri Jun 26  2020 Christophe de Dinechin <dinechin@redhat.com> - 1.0.10-1
- Release 1.0.10, Add _Bool support

* Tue Jun 23 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.0.9-1
- Release 1.0.9, compatibility with Fedora 33

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 3 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.0.8-1
- Adjust Fedora package to address review comments

* Fri Apr 26 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.0.7-1
- Initial Fedora package from upstream release
