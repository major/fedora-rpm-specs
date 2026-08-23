%global forgeurl https://github.com/google/perfetto
%global tag         v%{version}
%global soname_suffix 0.1

%global common_description %{expand:
Perfetto is a production-grade open-source stack for performance
instrumentation and trace analysis. It offers services and libraries and for
recording system-level and app-level traces, native plus Java heap profiling, a
library for analyzing traces using SQL and a web-based UI to visualize and
explore multi-GB traces.}

Name:           perfetto
Version:        57.2
Release:        %autorelease
Summary:        System profiling, app tracing and trace analysis

License:        Apache-2.0 AND BSD-2-Clause
URL:            https://perfetto.dev/
%forgemeta
Source0:        %{forgesource}
Source1:        perfetto.tmpfiles
Source2:        perfetto.sysusers
Source3:        %{forgeurl}/releases/download/%{tag}/perfetto-cpp-sdk-src.zip#/%{name}-cpp-sdk-src-%{tag}.zip
Source4:        perfetto-traced.service
Source5:        perfetto-traced-probes.service

# system re2
Patch0:         perfetto-system-re2.patch
# system gtest
Patch1:         perfetto-system-gtest.patch
# versioned SONAME; bump it when abi-compliance-checker reports a break.
Patch2:         perfetto-versioned-soname.patch

BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gn
BuildRequires:  gtest-devel
BuildRequires:  ninja-build
BuildRequires:  pandoc
BuildRequires:  pkgconf-pkg-config
BuildRequires:  protobuf-compiler
BuildRequires:  systemd-rpm-macros
BuildRequires:  unzip

BuildRequires:  protobuf-devel
BuildRequires:  re2-devel
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
BuildArch:      noarch
Requires:       %{name}-libs = %{version}-%{release}

%description    sdk %{common_description}

This package contains the Perfetto Tracing SDK, a C++17 library that allows
userspace applications to emit trace events and add more app-specific context
to a Perfetto trace.

%prep
%autosetup %{forgesetupargs} -p1
unzip -q -o %{SOURCE3} -d sdk/

%build
gn gen build --args="\
  is_debug=false \
  use_custom_libcxx=false \
  is_hermetic_clang=false \
  is_system_compiler=true \
  is_clang=false \
  skip_buildtools_check=true \
  enable_perfetto_integration_tests=false \
  perfetto_use_pkgconfig=true \
  perfetto_use_system_gtest=true \
  perfetto_use_system_protobuf=true \
  perfetto_use_system_re2=true \
  perfetto_use_system_zlib=true \
  perfetto_enable_git_rev_version_header=false \
  perfetto_shared_lib_soname_suffix=\"%{soname_suffix}\" \
  extra_cflags=\"${CFLAGS}\" \
  extra_cxxflags=\"${CXXFLAGS} -Wno-error=array-bounds\" \
  extra_ldflags=\"${LDFLAGS}\" \
  cc=\"${CC}\" \
  cxx=\"${CXX}\" \
  "

%ninja_build -C build perfetto traced traced_probes tracebox \
  perfetto_base_unittests perfetto_tracing_unittests
pandoc docs/reference/perfetto-cli.md -s -t man --shift-heading-level-by=-1 \
  > perfetto.1
pandoc docs/reference/tracebox.md -s -t man --shift-heading-level-by=-1 \
  > tracebox.1
for man in traced traced_probes; do
  pandoc docs/reference/${man}.md -s -t man --shift-heading-level-by=-1 \
    -V section=8 > ${man}.8
done

# Fix bogus rpath
chrpath -d build/{perfetto,tracebox,traced,traced_probes}

# The SONAME must be versioned: it is in the default library path and is
# linked against by traced/traced_probes rather than dlopen()ed.
test "$(objdump -p build/libperfetto.so.%{soname_suffix} | awk '/SONAME/{print $2}')" \
  = "libperfetto.so.%{soname_suffix}"

%install
install -Dpm0755 -t %{buildroot}%{_libdir} build/libperfetto.so.%{soname_suffix}
install -Dpm0755 -t %{buildroot}%{_sbindir} build/traced build/traced_probes
install -Dpm0755 -t %{buildroot}%{_bindir} build/perfetto build/tracebox
install -Dpm0644 %{SOURCE4} %{buildroot}%{_unitdir}/traced.service
install -Dpm0644 %{SOURCE5} %{buildroot}%{_unitdir}/traced-probes.service
install -Dpm0664 -t %{buildroot}%{_mandir}/man1 perfetto.1 tracebox.1
install -Dpm0664 -t %{buildroot}%{_mandir}/man8 traced.8 traced_probes.8

install -Dpm0644 %SOURCE1 %{buildroot}%{_tmpfilesdir}/perfetto.conf
install -Dpm0644 %SOURCE2 %{buildroot}%{_sysusersdir}/perfetto.conf

install -Dpm0644 -t %{buildroot}%{_datadir}/%{name}/configs test/configs/*.cfg
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name}/sdk sdk/perfetto.{h,cc}

%check
for bin in perfetto tracebox traced traced_probes; do
  LD_LIBRARY_PATH=build build/${bin} --version
done
build/perfetto_base_unittests
build/perfetto_tracing_unittests

%post
%tmpfiles_create_package %{name} %{SOURCE1}
%systemd_post traced.service traced-probes.service


%preun
%systemd_preun traced.service traced-probes.service

%postun
%systemd_postun_with_restart traced.service traced-probes.service

%files
%doc CHANGELOG README.md
%ghost %attr(0755,traced,traced) %dir /run/%{name}
%{_bindir}/perfetto
%{_bindir}/tracebox
%{_datadir}/%{name}/configs/
%{_mandir}/man1/perfetto.1*
%{_mandir}/man1/tracebox.1*
%{_mandir}/man8/traced.8*
%{_mandir}/man8/traced_probes.8*
%{_sbindir}/traced
%{_sbindir}/traced_probes
%{_sysusersdir}/perfetto.conf
%{_tmpfilesdir}/perfetto.conf
%{_unitdir}/traced.service
%{_unitdir}/traced-probes.service

%files libs
%license LICENSE
%{_libdir}/libperfetto.so.%{soname_suffix}
%dir %{_datadir}/%{name}

%files sdk
%doc docs/instrumentation/tracing-sdk.md
%{_datadir}/%{name}/sdk/

%changelog
%autochangelog
