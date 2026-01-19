# git ls-remote git://github.com/jimahlstrom/wdsp
%global git_commit 18782be8d7e75bf7e41e1f23e912640de8d6ce58
%global git_date 20250922

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		wdsp
Version:	0
Release:	0.13.%{git_suffix}%{?dist}
Summary:	DSP library for LinHPSDR
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/jimahlstrom/%{name}
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	fftw-devel
BuildRequires:	pkgconfig(gtk+-3.0)
Patch0:		wdsp-0-soname-add.patch

%description
DSP library for LinHPSDR.

%package devel
Summary:	Development files for wdsp
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for wdsp.

%package doc
Summary:	Documentation files for wdsp
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation files for wdsp.

%prep
%autosetup -n %{name}-%{git_commit} -p1

%build
cd build_shared
%make_build CFLAGS="%{build_cflags} -fPIC -D _GNU_SOURCE" LDFLAGS="%{build_ldflags}"

%install
install -Dpm 0775 -t %{buildroot}%{_libdir} ./libwdsp.so.0.*
cp ./libwdsp.so "%{buildroot}%{_libdir}/libwdsp.so"
install -Dpm 0664 src/wdsp.h "%{buildroot}%{_includedir}/wdsp.h"
install -Dpm 0664 "WDSP Guide, Rev 1.25.pdf" %{buildroot}/%{_docdir}/%{name}/"WDSP Guide, Rev 1.25.pdf"

%files
%doc README.md
%license GNU_GENERAL_PUBLIC_LICENSE.txt
%{_libdir}/libwdsp.so.0*

%files devel
%{_includedir}/wdsp.h
%{_libdir}/libwdsp.so

%files doc
%{_docdir}/%{name}/WDSP\ Guide\,\ Rev\ 1.25.pdf

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20250922git18782be8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Sep 22 2025 Jaroslav Škarvada  <jskarvad@redhat.com> - 0-0.12.20250922git18782be8
- Switched to new upstream

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20210705gitc55342c5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

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
