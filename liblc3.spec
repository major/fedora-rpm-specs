Name:          liblc3
Version:       1.0.4
Release:       2%{?dist}
Summary:       Low Complexity Communication Codec (LC3)

License:       Apache-2.0
URL:           https://github.com/google/liblc3
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson

%description
The Low Complexity Communication Codec (LC3) is used by
Bluetooth as the codec for LE Audio. It enables high
quality audio over the low bandwidth connections provided
by Bluetooth LE.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package utils
Summary: Utility package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Uitlities for command line use of and testing
the %{name} library.

%prep
%autosetup -p1

%build
%meson -Dtools=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%{_libdir}/liblc3.so.1{,.*}

%files devel
%{_includedir}/lc3*
%{_libdir}/pkgconfig/lc3.pc
%{_libdir}/liblc3.so

%files utils
%{_bindir}/dlc3
%{_bindir}/elc3

%changelog
* Mon Nov 13 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.4-2
- Review fixes

* Fri Aug 04 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- Review updates
- Split utils out to subpackage

* Thu Jun 22 2023 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.3-1
- Initial package
