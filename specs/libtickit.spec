%global libname tickit
%global libtickit_ver  v0.4

# Unibilium by default, otherwise ncurses
%bcond_without unibilium

Name:           lib%{libname}
Version:        0.4.4
Release:        5%{?dist}
Summary:        Terminal Interface Construction Kit

License:        MIT
URL:            https://launchpad.net/%{name}
Source0:        %{url}/trunk/%{libtickit_ver}/+download/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Convert::Color)
BuildRequires:  perl(Convert::Color::XTerm)
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(termkey)
%if %{with unibilium}
BuildRequires:  pkgconfig(unibilium) >= 1.1.0
%else
BuildRequires:  ncurses-devel
%endif
# Tests
BuildRequires:  %{_bindir}/prove

%description
This library provides an abstracted mechanism for building interactive
full-screen terminal programs. It provides a full set of output drawing
functions, and handles keyboard and mouse input events.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libtermkey-devel%{?_isa}
%if %{with unibilium}
Requires:       unibilium-devel%{?_isa}
%endif

%description devel
%{summary}.

%prep
%autosetup
rm -f src/linechars.inc src/xterm-palette.inc

%build
CFLAGS="%{__global_cflags}" LDFLAGS="%{__global_ldflags}" %{make_build} VERBOSE=1

%install
%{make_install} PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
CFLAGS="%{__global_cflags} -D_XOPEN_SOURCE" LDFLAGS="%{__global_ldflags}" make test VERBOSE=1
make examples

%files
%license LICENSE
%doc CHANGES examples README.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}.h
%{_includedir}/%{libname}-*.h
%{_libdir}/pkgconfig/%{libname}.pc
%{_mandir}/man3/%{libname}_*.3*
%{_mandir}/man7/%{libname}.7*
%{_mandir}/man7/%{libname}_*.7*

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.4-1
- 0.4.4 bump (rhbz#2245228)
- Update URL and Source0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.3-1
- 0.4.3 bump

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.2a-1
- 0.4.2a bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.1-1
- 0.4.1 bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.2-2
- Add unibilium to run-require for libtickit-devel

* Tue Jul 23 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.2-1
- Initial release
