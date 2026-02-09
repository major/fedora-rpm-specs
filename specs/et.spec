%ifnarch s390x
%bcond_without tests
%else
%if 0%{?el8}
# ConnectionTest fails
%bcond_with    tests
%else
%bcond_without tests
%endif
%endif

%ifarch s390x
# UniversalStackTrace fails with undefined references
%bcond_with    unwind
%else
%bcond_without unwind
%endif

%global _firewalld_dir %{_prefix}/lib/firewalld

Name:           et
Version:        6.2.11
Release:        %autorelease
Summary:        Remote shell that survives IP roaming and disconnect

License:        Apache-2.0
URL:            https://mistertea.github.io/EternalTerminal/
Source0:        https://github.com/MisterTea/EternalTerminal/archive/et-v%{version}/EternalTerminal-%{version}.tar.gz
Source1:        et.xml
Patch0:         et-use-system-dependency.patch

ExcludeArch: %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  firewalld-filesystem
# -static BR required for tracking of header-only libraries
BuildRequires:  cpp-httplib-devel
BuildRequires:  cpp-httplib-static
BuildRequires:  cxxopts-devel
BuildRequires:  cxxopts-static
BuildRequires:  easyloggingpp-devel
BuildRequires:  easyloggingpp-static
BuildRequires:  catch-devel
BuildRequires:  gflags-devel
BuildRequires:  json-devel
BuildRequires:  json-static
BuildRequires:  simpleini-devel
BuildRequires:  libatomic
BuildRequires:  libcurl-devel
BuildRequires:  libsodium-devel
%if %{with unwind}
BuildRequires:  libunwind-devel
%endif
BuildRequires:  libutempter-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-lite-devel
BuildRequires:  libselinux-devel
BuildRequires:  systemd

# Bundled libraries
# cat .gitmodules | grep submodule | sort
# for tarball, s/external/external_imported
Provides:       bundled(base64) = 0
# external_imported/cotire/CMake/cotire.cmake
Provides:       bundled(cotire) = 1.8.0
# external/msgpack-c/include/msgpack/version_master.h
Provides:       bundled(msgpack) = 3.3.0
# external/PlatformFolders/CMakeLists.txt
Provides:       bundled(PlatformFolders) = 4.0.0
# sanitizers-cmake is only used when building
%ifnarch ppc64le s390x
# external/sentry-native/include/sentry.h
Provides:       bundled(sentry-native) = 0.6.0
%endif
# https://github.com/r-lyeh-archived/sole
Provides:       bundled(sole) = 1.0.1
Provides:       bundled(ThreadPool) = 0
# external/UniversalStacktrace/CMakeLists.txt
Provides:       bundled(UniversalStacktrace) = 0.0.1
# vcpkg is disabled

%{?systemd_requires}

%description
Eternal Terminal (ET) is a remote shell that automatically reconnects without
interrupting the session.


%prep
%autosetup -p1 -n EternalTerminal-et-v%{version}
# use this if we have patches we need to apply by hand
# %%setup -q -n EternalTerminal-et-v%%{version}

# Remove bundled Catch2 test framework
rm -rf external_imported/Catch2

# Unbundle cpp-httplib
rm -rf external_imported/cpp-httplib

# Unbundle cxxopts
rm -rf external_imported/cxxopts

# Unbundle easyloggingpp
mkdir -p external_imported/easyloggingpp/src
ln -sf %{_includedir} external_imported/easyloggingpp/src

# Unbundle “JSON for Modern C++”
rm -rf external_imported/json
# both /usr/share/cmake/nlohmann_json/nlohmann_jsonConfig.cmake
# and /usr/share/pkgconfig/nlohmann_json.pc are wrong
# so we can't use find_package / pkg_check_module without further hacks anyway
#sed -r -i 's@\$\{.*\}/json/include@%{_includedir}/nlohmann@' \
#    CMakeLists.txt

# Unbundle simpleini
rm -rf external_imported/simpleini

%build
%cmake \
%ifarch ppc64le s390x
  -DDISABLE_SENTRY=ON \
%endif
  -DDISABLE_VCPKG=ON
%cmake_build


%install
%cmake_install
mkdir -p \
  %{buildroot}%{_unitdir} \
  %{buildroot}%{_sysconfdir} \
  %{buildroot}%{_firewalld_dir}/services
install -m 0644 -p systemctl/et.service %{buildroot}%{_unitdir}/et.service
install -m 0644 -p etc/et.cfg %{buildroot}%{_sysconfdir}/et.cfg
install -m 0644 %{SOURCE1} %{buildroot}%{_firewalld_dir}/services/et.xml

rm -vf %{buildroot}%{_bindir}/crashpad_handler
rm -rf %{buildroot}%{_libdir}/cmake/sentry
rm -vf %{buildroot}%{_libdir}/*.a

%if %{with tests}
%check
%if 0%{?fedora}
%ctest
%else
%ctest --verbose
%endif
%endif


%post
%systemd_post et.service
%firewalld_reload

%preun
%systemd_preun et.service

%postun
%systemd_postun_with_restart et.service
%firewalld_reload


%files
%license LICENSE
%doc README.md
%{_bindir}/et
%{_bindir}/etserver
%{_bindir}/etterminal
%{_bindir}/htm
%{_bindir}/htmd
%dir %{_firewalld_dir}
%dir %{_firewalld_dir}/services
%{_firewalld_dir}/services/et.xml
%config(noreplace) %{_sysconfdir}/et.cfg
%{_unitdir}/et.service


%changelog
%autochangelog
