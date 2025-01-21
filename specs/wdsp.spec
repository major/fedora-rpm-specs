# git ls-remote git://github.com/g0orx/wdsp.git
%global git_commit c55342c5b15354a9ac2b8b16eb8748d5518f723c
%global git_date 20210705

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		wdsp
Version:	0
Release:	0.10.%{git_suffix}%{?dist}
Summary:	DSP library for LinHPSDR
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/g0orx/%{name}
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	fftw-devel
BuildRequires:	pkgconfig(gtk+-3.0)
# https://github.com/g0orx/wdsp/pull/15
Patch0:		wdsp-0-distro-makefile.patch
# Encouraged upstream to add SONAME (https://github.com/g0orx/wdsp/pull/15)
Patch1:		wdsp-0-soname-add.patch

%description
DSP library for LinHPSDR.

%package devel
Summary:	Development files for wdsp
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for wdsp.

%prep
%autosetup -n %{name}-%{git_commit} -p1

# unbundle fftw
rm -f fftw/*
rmdir fftw

%build
%make_build OPTIONS="-fPIC -D _GNU_SOURCE" CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" GTK_INCLUDE=GTK

%install
%make_install LIBDIR="%{buildroot}%{_libdir}" INCLUDEDIR="%{buildroot}%{_includedir}"

%files
%doc README.md
%license COPYING
%{_libdir}/libwdsp.so.0*

%files devel
%{_includedir}/wdsp.h
%{_libdir}/libwdsp.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20210705gitc55342c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.9.20210705gitc55342c5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20210705gitc55342c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20210705gitc55342c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20210705gitc55342c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20210705gitc55342c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20210705gitc55342c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20210705gitc55342c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jul 19 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.2.20210705gitc55342c5
- Fixed according to the package review
  Resolves: rhbz#1979403

* Mon Jul  5 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20210705gitc55342c5
- Initial release
