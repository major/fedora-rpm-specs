Name: coeurl
Version: 0.3.0
Release: 5%{?dist}

License: MIT
URL: https://nheko.im/nheko-reborn/%{name}
Summary: Simple async wrapper around CURL for C++
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# https://nheko.im/nheko-reborn/coeurl/-/commit/831e2ee8e9cf08ea1ee9736cde8370f9d0312abc
Patch100: %{name}-0.3.0-fmt10-fix.patch

BuildRequires: fmt-devel
BuildRequires: gcc-c++
BuildRequires: libcurl-devel
BuildRequires: libevent-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: spdlog-devel

%description
Simple library to do http requests asynchronously via CURL in C++.

Based on the CURL-libevent example.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson \
    -Dwerror=false \
    -Dtests=false \
    -Dexamples=false
%meson_build

%install
%meson_install

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-4
- Rebuilt due to spdlog 1.12 update.

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-3
- Rebuilt due to fmt 10 update.
- Backported upstream patch with fmt 10 build fix.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1
- Updated to version 0.3.0.

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.1-2
- Rebuilt due to spdlog update.

* Sat Jul 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.1-1
- Updated to version 0.2.1.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 16 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-3
- Rebuilt due to fmt library update.

* Sat Apr 30 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-2
- Rebuilt due to spdlog update.

* Thu Mar 10 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-1
- Updated to version 0.2.0.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.1-1
- Updated to version 0.1.1.

* Fri Nov 19 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-1
- Updated to version 0.1.0.

* Fri Aug 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20210813git22f5892
- Initial release.
