
#%%global dev rc1

%global githubname prometheus-cpp
%global tarball %{githubname}

Name:           libprometheus-cpp
Summary:        Prometheus Client Library for Modern C++
Version:        1.1.0
Release:        1%{?dev:%{dev}}%{?dist}
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
    -DENABLE_TESTING:BOOL=ON

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
* Mon Mar 6 2023 Kaleb S. KEITHLEY <kkeithle at redhat.com> - 1.1.0-1
- prometheus-cpp 1.1.0 GA

