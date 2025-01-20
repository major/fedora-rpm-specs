%global commit bf7b41c2ff3f24a2031193b62aa76d35e8842b5a
%global snapdate 20240518

Name: qoi
Version: 0^%{snapdate}
Release: 3%{?dist}
Summary: The "Quite OK Image Format" for fast, lossless image compression

License: MIT
URL: https://github.com/phoboslab/qoi
Source0: %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: gcc
BuildRequires: libpng-devel
BuildRequires: stb_image-devel
BuildRequires: stb_image_write-devel
BuildRequires: make

%description
The "Quite OK Image Format" for fast, lossless image compression.

%package tools
Summary: Tools for %{name}

%description tools
Tools for fast, lossless image compression using the "Quite OK Image Format".

%package devel
Summary: Development files for %{name}
BuildArch: noarch
Provides: qoi-static = %{version}-%{release}

%description devel
Headers for fast, lossless image compression using the "Quite OK Image Format".

%prep
%autosetup -n qoi-%{commit}

%build
%make_build bench conv

%install
install -d %{buildroot}/%{_bindir} %{buildroot}/%{_includedir}
install -p qoibench qoiconv %{buildroot}/%{_bindir}
install -p qoi.h %{buildroot}/%{_includedir}

%files tools
%license LICENSE
%doc README.md
%{_bindir}/qoibench
%{_bindir}/qoiconv

%files devel
%license LICENSE
%{_includedir}/qoi.h

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20240518-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20240518-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 28 2024 ErrorNoInternet <errornointernet@envs.net> - 0^20240518-1
- Bump commit to bf7b41c2ff3f24a2031193b62aa76d35e8842b5a.
- Remove Makefile-ldflags patch as LDFLAGS are now included upstream.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20230911-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20230911-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 14 2023 ErrorNoInternet <errornointernet@envs.net> - 0^20230911-2
- Add `Provides: qoi-static` to the -devel package

* Tue Oct 10 2023 ErrorNoInternet <errornointernet@envs.net> - 0^20230911-1
- Use caret versioning
- Remove `Requires` from the -devel and -tools package
- Add LICENSE to -devel package

* Thu Aug 31 2023 ErrorNoInternet <errornointernet@envs.net> - 20230828git41e8f84-1
- Bump package version
- Split package into -tools and -devel

* Sun Jul 16 2023 ErrorNoInternet <errornointernet@envs.net> - 20230615git36190eb-3
- Add Makefile-ldflags patch (now includes Fedora's LDFLAGS)
- devel package now requires base package

* Fri Jul 14 2023 ErrorNoInternet <errornointernet@envs.net> - 20230615git36190eb-2
- Merge qoi-devel into qoi

* Fri Jul 14 2023 ErrorNoInternet <errornointernet@envs.net> - 20230615git36190eb-1
- Hello, world!
