
#%%global dev rc1

%global githubname prometheus-cpp
%global tarball %{githubname}

Name:           libprometheus-cpp
Summary:        Prometheus Client Library for Modern C++
Version:        1.2.4
Release:        4%{?dev:%{dev}}%{?dist}
License:        MIT AND 0BSD
Url:            https://github.com/jupp0r/%{githubname}
Source:         %{url}/archive/v%{version}/%{tarball}-%{version}.tar.gz
Requires:       libxcrypt
BuildRequires:  cmake gcc-c++
BuildRequires:  civetweb-devel
BuildRequires:  zlib-devel
BuildRequires:  libcurl-devel
BuildRequires:  gmock-devel

%description
This library aims to enable Metrics-Driven Development for C++ services. It
implements the Prometheus Data Model, a powerful abstraction on which to
collect and expose metrics. We offer the possibility for metrics to be
collected by Prometheus, but other push/pull collections can be added as
plugins.

%package devel
Summary:        Prometheus Client Library C++ header files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for prometheus-cpp library.

%prep
%setup -q -n %{tarball}-%{version}

%build
%{cmake} \
    -DCMAKE_BUILD_TYPE=RelWithDebugInfo \
    -DBUILD_CONFIG=rpmbuild \
    -DUSE_THIRDPARTY_LIBRARIES:BOOL=OFF \
    -DENABLE_TESTING:BOOL=OFF

export GCC_COLORS=
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}-*.so.1*

%files devel
%{_includedir}/prometheus/
%{_libdir}/%{name}-*.so
%{_libdir}/cmake/%{githubname}/
%{_libdir}/pkgconfig/%{githubname}-*.pc

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 1.2.4-1
- prometheus-cpp 1.2.4 GA

* Thu Feb 8 2024 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 1.2.3-1
- prometheus-cpp 1.2.3 GA

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 1.2.1-1
- prometheus-cpp 1.2.1 GA

* Tue Jan 2 2024 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 1.2.0-1
- prometheus-cpp 1.2.0 GA

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 6 2023 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 1.1.0-1
- prometheus-cpp 1.1.0 GA

