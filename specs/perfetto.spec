%global forgeurl https://android.googlesource.com/platform/external/perfetto

%global common_description %{expand:
Perfetto is a production-grade open-source stack for performance
instrumentation and trace analysis. It offers services and libraries and for
recording system-level and app-level traces, native plus Java heap profiling, a
library for analyzing traces using SQL and a web-based UI to visualize and
explore multi-GB traces.}

Name:           perfetto
Version:        49.0
Release:        %autorelease
Summary:        System profiling, app tracing and trace analysis

License:        Apache-2.0
URL:            https://perfetto.dev/
Source0:        %{forgeurl}/+archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        perfetto.tmpfiles
Source2:        perfetto.sysusers

BuildRequires:  binutils-gold
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  gn
BuildRequires:  ninja-build
BuildRequires:  pandoc
BuildRequires:  protobuf-compiler
BuildRequires:  systemd-rpm-macros

BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# Upstream only supports these architectures
ExclusiveArch:  aarch64 x86_64

%description    %{common_description}

%package        libs
Summary:        Libraries for %{name}

%description    libs %{common_description}

This package contains shared libraries for %{name}.

%package        sdk
Summary:        Perfetto Tracing SDK
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    sdk %{common_description}

This package contains the Perfetto Tracing SDK, a C++17 library that allows
userspace applications to emit trace events and add more app-specific context
to a Perfetto trace.

%prep
%autosetup -c -p1

%build
gn gen build --args="\
  is_debug=false \
  use_custom_libcxx=false \
  is_hermetic_clang=false \
  is_system_compiler=true \
  is_clang=false \
  skip_buildtools_check=true \
  enable_perfetto_integration_tests=false \
  enable_perfetto_unittests=false \
  perfetto_use_system_protobuf=true \
  perfetto_use_system_zlib=true \
  perfetto_enable_git_rev_version_header=false \
  extra_cflags=\"${CFLAGS}\" \
  extra_cxxflags=\"${CXXFLAGS}\" \
  extra_ldflags=\"${LDFLAGS}\" \
  cc=\"${CC}\" \
  cxx=\"${CXX}\" \
  "
  
%ninja_build -C build perfetto traced traced_probes
pandoc docs/reference/perfetto-cli.md -s -t man --shift-heading-level-by=-1 \
  > perfetto.1

# Fix bogus rpath
chrpath -d build/{perfetto,traced,traced_probes}

%install
install -Dpm0755 -t %{buildroot}%{_libdir} build/libperfetto.so
install -Dpm0755 -t %{buildroot}%{_sbindir} build/traced build/traced_probes
install -Dpm0755 -t %{buildroot}%{_bindir} build/perfetto
install -Dpm0644 -t %{buildroot}%{_unitdir} debian/{traced,traced-probes}.service
install -Dpm0664 -t %{buildroot}%{_mandir}/man1 perfetto.1

install -Ddpm0755 %{buildroot}/run/perfetto
install -Dpm0644 %SOURCE1 %{buildroot}%{_tmpfilesdir}/perfetto.conf
install -Dpm0644 %SOURCE2 %{buildroot}%{_sysusersdir}/perfetto.conf

install -Dpm0644 -t %{buildroot}%{_datadir}/%{name}/configs test/configs/*.cfg
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name}/sdk sdk/perfetto.{h,cc}

%post
%systemd_post traced.service traced-probes.service

%pre
%sysusers_create_compat %{SOURCE2}

%preun
%systemd_preun traced.service traced-probes.service

%postun
%systemd_postun_with_restart traced.service traced-probes.service

%files
%doc CHANGELOG README.md
%attr(0755,traced,traced) %dir /run/%{name}
%{_bindir}/perfetto
%{_datadir}/%{name}/configs/
%{_mandir}/man1/perfetto.1*
%{_sbindir}/traced
%{_sbindir}/traced_probes
%{_sysusersdir}/perfetto.conf
%{_tmpfilesdir}/perfetto.conf
%{_unitdir}/traced.service
%{_unitdir}/traced-probes.service

%files libs
%license LICENSE
%{_libdir}/libperfetto.so
%dir %{_datadir}/%{name}

%files sdk
%{_datadir}/%{name}/sdk/

%changelog
%autochangelog
