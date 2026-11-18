Name:          libpisp
Version:       1.8.0
Release:       1%{?dist}
Summary:       A helper library for the Raspberry Pi ISP (PiSP)
URL:           https://github.com/raspberrypi/libpisp
# The entire source is BSD-3-Clause, except that the following are
# GPL-2.0-only WITH Linux-syscall-note:
#  src/libpisp/*/*.h
# The header-only json/nlohmann_json dependency is (MIT AND CC0-1.0)
License: %{shrink:
	BSD-3-Clause
	AND GPL-2.0-only WITH Linux-syscall-note
	AND MIT
	AND CC0-1.0
}

Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/raspberrypi/libpisp/pull/79
Patch0:        libpisp-drop-unused-license-files.patch

ExclusiveArch: %{arm64}
BuildRequires: boost-devel
BuildRequires: gcc gcc-c++
BuildRequires: json-static
BuildRequires: meson

%description
A helper library to generate run-time configuration for the Raspberry Pi
ISP (PiSP), consisting of the Frontend and Backend hardware components.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.


%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSES/*
%{_libdir}/libpisp.so.1*
%{_datadir}/libpisp/

%files devel
%{_includedir}/libpisp/
%{_libdir}/libpisp.so
%{_libdir}/pkgconfig/libpisp.pc

%changelog
* Thu Nov 05 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sat Oct 10 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.0-2
- Updates for review

* Fri Aug 07 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Sat Jul 18 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.0-2
- Upstream patch to fix license issues

* Tue Jul 14 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Feb 18 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Thu Sep 11 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1
- Updates for license verification

* Fri Apr 04 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.0-1
- Initial package
