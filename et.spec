%if 0%{?el8} || 0%{?fc34}
%ifarch s390x
# ConnectionTest fails
%bcond_with tests
%else
%bcond_without tests
%endif
%else
%bcond_without tests
%endif

%global _firewalld_dir %{_prefix}/lib/firewalld

Name:           et
Version:        6.2.1
Release:        %autorelease
Summary:        Remote shell that survives IP roaming and disconnect

License:        ASL 2.0
URL:            https://mistertea.github.io/EternalTerminal/
Source0:        https://github.com/MisterTea/EternalTerminal/archive/et-v%{version}.tar.gz
Source1:        et.xml

BuildRequires:  boost-devel
BuildRequires:  cmake3
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc-c++
BuildRequires:  catch-devel
# -static BR required for tracking of header-only libraries
BuildRequires:  cxxopts-devel
BuildRequires:  cxxopts-static
BuildRequires:  easyloggingpp-devel
BuildRequires:  easyloggingpp-static
BuildRequires:  gflags-devel
BuildRequires:  json-devel
BuildRequires:  json-static
BuildRequires:  libatomic
BuildRequires:  libcurl-devel
BuildRequires:  libsodium-devel
BuildRequires:  libutempter-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-lite-devel
BuildRequires:  systemd

# Bundled libraries
# cat .gitmodules | grep submodule | sort
# for tarball, s/external/external_imported
Provides:       bundled(base64) = 0
# external_imported/cotire/CMake/cotire.cmake
Provides:       bundled(cotire) = 1.8.0
# grep User-Agent external/cpp-httlib/httplib.h
# cross-check with the git checkout for specific version
Provides:       bundled(cpp-httplib) = 0.7.18
# external/msgpack-c/include/msgpack/version_master.h
Provides:       bundled(msgpack) = 3.3.0
# external/PlatformFolders/CMakeLists.txt
Provides:       bundled(PlatformFolders) = 4.0.0
# sanitizers-cmake is only used when building
%ifnarch ppc64le s390x
Provides:       bundled(sentry-native) = 0.4.7
%endif
# external/simpleini/SimpleIni.h
Provides:       bundled(simpleini) = 4.17
# https://github.com/r-lyeh-archived/sole
Provides:       bundled(sole) = 1.0.1
Provides:       bundled(ThreadPool) = 0
Provides:       bundled(UniversalStacktrace) = 0
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
sed -r -i '/\$\{EXTERNAL_DIR\}\/Catch2\/single_include/d' CMakeLists.txt

# Unbundle cxxopts
rm -rf external_imported/cxxopts
sed -r -i '/\$\{.*\}\/cxxopts\/include/d' CMakeLists.txt

# Unbundle easyloggingpp
rm -rf external_imported/easyloggingpp
# The easylogging++.cc source file is treated as a strangely-named header; see
# notes in the easyloggingpp spec file.
sed -r -i \
    -e 's@\$\{.*\}/easyloggingpp/src/(easylogging.*)@%{_includedir}/\1@' \
    -e '/easyloggingpp\/src\/?$/d' \
    CMakeLists.txt

# Unbundle “JSON for Modern C++”
rm -rf external_imported/json
sed -r -i 's@\$\{.*\}/json/single_include/nlohmann@%{_includedir}/nlohmann@' \
    CMakeLists.txt


%build
%cmake \
%ifarch ppc64le s390x
  -DDISABLE_SENTRY=TRUE \
%endif
  -DDISABLE_VCPKG=TRUE
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
