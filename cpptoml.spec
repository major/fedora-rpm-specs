# cpptoml is header only, so there's no debuginfo
%global debug_package %{nil}

Name:           cpptoml
Version:        0.1.1
Release:        8%{?dist}
Summary:        Header-only C++ TOML library 

License:        MIT
URL:            https://github.com/skystrife/cpptoml
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Modify-build-to-use-GNUInstallDirs.patch

BuildRequires:  cmake >= 3.1.0
BuildRequires:	make
BuildRequires:  gcc-c++

%description
A header-only library for parsing TOML configuration files.

Supports TOML v0.5.0.

This includes support for the new DateTime format, inline tables, multi-line
basic and raw strings, digit separators, hexadecimal integers, octal integers,
binary integers, and float special values.


%package devel
Summary:	Header files for cpptoml


%description devel
Header files to develop applications that use the TOML format.

Supports TOML v0.5.0.

This includes support for the new DateTime format, inline tables, multi-line
basic and raw strings, digit separators, hexadecimal integers, octal integers,
binary integers, and float special values.


%prep
%autosetup -p1


%build
%cmake -B builddir -DCPPTOML_BUILD_EXAMPLES=OFF


%install
%make_install -C builddir


%files devel
%license LICENSE
%doc README.md
%{_includedir}/cpptoml.h
%{_libdir}/cmake/cpptoml/


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 2020 Dakota Williams <raineforest@raineforest.me> - 0.1.1-5
- Rebuilt for f33 and f34

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Dakota Williams <raineforest@raineforest.me> 0.1.1-1
- Initial packaging 
