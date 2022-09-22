Name:		libavtp
Version:	0.2.0
Release:	2%{?dist}
Summary:	An AVTP protocol implementation

License:	BSD
URL:		https://github.com/Avnu/libavtp
Source0:	https://github.com/Avnu/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	libcmocka-devel
BuildRequires:	meson

%description
An open source implementation of Audio Video Transport
Protocol (AVTP) specified in IEEE 1722-2016 spec.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libavtp.so.*

%files devel
%doc CONTRIBUTING.md HACKING.md
%{_includedir}/avtp*
%{_libdir}/libavtp.so
%{_libdir}/pkgconfig/avtp.pc


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 12 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.0-1
- Initial package
