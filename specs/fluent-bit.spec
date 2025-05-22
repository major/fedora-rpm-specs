Name: fluent-bit
Version: 3.2.8
Release: %autorelease
Summary: Fluent Bit is a super fast, lightweight, and highly scalable logging and metrics processor and forwarder.
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/fluent/fluent-bit
Source0: https://github.com/fluent/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0: fluent-bit-cmake-c99.patch
Patch1: fluent-bit-cmake-c99-2.patch
Patch3: 0002-Bypass-incompatible-pointer-types-for-Kubernetes-Eve.patch
Patch4: librdkafka-no-openssl-engine.patch
# avoid issue due to two incompatible copies of zstd
# https://github.com/fluent/fluent-bit/issues/10139
# lightly tweaked to make changes to CMakeLists.txt apply
# from upstream commit 5f409f55ec667b525716be4afd54b5485c9d55c1
Patch5: 0001-build-use-the-system-provided-libzstd-if-found.patch


BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: cmake
BuildRequires: systemd-rpm-macros
# systemd-devel BR is needed for systemd input plugin
BuildRequires: systemd-devel
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libpq-devel
BuildRequires: zlib-devel
BuildRequires: gnutls-devel
BuildRequires: openssl-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: libyaml-devel
BuildRequires: libzstd-devel
BuildRequires: openssl

%if 0%{?rhel} <= 9
BuildRequires: netcat
%endif

%if 0%{?fedora} >= 41
BuildRequires: openssl-devel-engine
BuildRequires: netcat
%endif

%{?systemd_requires}

# Exclude armv7hl temporarily because of failing runtime tests
# https://github.com/fluent/fluent-bit/issues/4395
ExclusiveArch: x86_64 aarch64

%description
Fluent Bit is a high performance and multi-platform log forwarder.

%prep
%autosetup -p1

%build
%cmake\
    -DCMAKE_BUILD_TYPE=RelWithDebInfo\
    -DCMAKE_C_STANDARD=17\
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}\
    -DFLB_DEBUG=Off\
    -DFLB_EXAMPLES=Off\
    -DFLB_HTTP_SERVER=On\
    -DFLB_IN_PODMAN_METRICS=On\
    -DFLB_IN_SYSTEMD=On\
    -DFLB_OUT_ES=On\
    -DFLB_OUT_SLACK=Off\
    -DFLB_OUT_TD=Off\
    -DFLB_PREFER_SYSTEM_LIB_ZSTD=On\
    -DFLB_RELEASE=On\
    -DFLB_SHARED_LIB=Off\
    -DFLB_TESTS_INTERNAL=Off\
    -DFLB_TESTS_RUNTIME=Off\
    -DFLB_TLS=On\
    -DSYSTEMD_UNITDIR=%{_unitdir}\
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build

%install
%cmake_install
# We don't ship headers and shared library for plugins (yet)
rm -rvf %{buildroot}%{_includedir}

%check
%ctest

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md MAINTAINERS.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOLANG_OUTPUT_PLUGIN.md GOVERNANCE.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%exclude /usr/bin/luajit
%exclude /usr/lib64/libluajit.a

%changelog
%autochangelog
