Name:		serialdv
Version:	1.1.4
Release:	8%{?dist}
Summary:	C++ minimal interface to encode/decode audio with AMBE3000 based devices
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/f4exb/serialdv
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	make

%description
C++ minimal interface to encode and decode audio with AMBE3000 based devices
in packet mode over a serial link.

%package devel
Summary:	Development files for serialdv
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for serialdv.

%prep
%autosetup -n serialDV-%{version} -p1

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc Readme.md
%{_bindir}/dvtest
%{_libdir}/libserialdv.so.1*

%files devel
%{_includedir}/*
%{_libdir}/libserialdv.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.4-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jan 25 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 1.1.4-1
- Initial release
