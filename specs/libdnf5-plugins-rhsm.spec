Name:           libdnf5-plugins-rhsm
Version:        0.1.3
Release:        %autorelease
Summary:        Libdnf5 plugins for Red Hat Subscription Management
License:        GPL-3.0-only
URL:            https://github.com/candlepin/rhsm-dnf5-plugins
Source0:        https://github.com/candlepin/rhsm-dnf5-plugins/releases/download/%{version}/%{name}-%{version}.tar.gz

%bcond_with     clang
%bcond_without  tests
%bcond_without  productid_libdnf5_plugin
%bcond_without  rhsm_libdnf5_plugin

%if %{with clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++ >= 10.1
%endif
BuildRequires:  cmake >= 3.21
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  libdnf5-devel
BuildRequires:  jsoncpp-devel
%if %{with tests}
BuildRequires:  gtest-devel
%endif

%description
This package provides libdnf5 plugins to interact with repositories
and subscriptions from the Red Hat entitlement platform; contains
rhsm and product-id plugins.

%prep
%autosetup -p1

%build
%cmake \
    -DWITH_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
    \
    -DWITH_PLUGIN_PRODUCTID=%{?with_productid_libdnf5_plugin:ON}%{!?with_productid_libdnf5_plugin:OFF} \
    -DWITH_PLUGIN_RHSM=%{?with_rhsm_libdnf5_plugin:ON}%{!?with_rhsm_libdnf5_plugin:OFF}
%cmake_build

%install
%cmake_install
install -Dpm 0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%check
%if %{with tests}
    %ctest
%endif

%files
%license %{_licensedir}/%{name}/LICENSE
%{_libdir}/libdnf5/plugins/productid.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/productid.conf
%{_libdir}/libdnf5/plugins/rhsm.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/rhsm.conf

%changelog
%autochangelog
