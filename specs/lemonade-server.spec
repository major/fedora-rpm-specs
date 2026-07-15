Name:           lemonade-server
Version:        10.9.0
Release:        %autorelease
Summary:        Local LLM serving with GPU and NPU acceleration

# Apache-2.0: Main project license (LICENSE.md file)
# GPL-2.0-only WITH Linux-syscall-note: src/cpp/include/lemon/amdxdna_accel.h (kernel UAPI header)
# MIT: src/cpp/include/lemon/utils/aixlog.hpp (bundled C++ logging library)
License:        Apache-2.0 AND GPL-2.0-only WITH Linux-syscall-note AND MIT
URL:            https://github.com/lemonade-sdk/lemonade
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

# aixlog is a header-only library not available as a package in Fedora
Provides:       bundled(aixlog) = 1.5.0

# Disabled by default, requires GPU hardware
%bcond_with check

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros
BuildRequires:  libdrm-devel

BuildRequires:  libzstd-devel
BuildRequires:  libcurl-devel
BuildRequires:  brotli-devel

BuildRequires:  nlohmann-json-devel
BuildRequires:  cli11-devel
BuildRequires:  cpp-httplib-devel
BuildRequires:  zlib-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  mbedtls-devel

Requires:       llama-cpp

%if %{with check}
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-openai
%endif

%description
Lemonade helps users discover and run local AI apps by serving optimized
LLMs right from their own GPUs and NPUs. It supports GGUF, FLM, and
ONNX models.

%prep
%autosetup -n lemonade-%{version} -p1

# Removing hidden upstream directories not needed for the build
rm -rf .github .circleci .gitlab-ci

# Removing Debian packaging directory (not used, makes license scanning easier)
rm -rf contrib

# Force CMake to use system-provided httplib instead of attempting 
##  to download and vendor it via FetchContent during offline build.
sed -i 's/FetchContent_MakeAvailable(httplib)/find_package(httplib REQUIRED)/g' CMakeLists.txt

%build
%cmake -DBUILD_WEB_APP=OFF
%cmake_build

%install
%cmake_install

# Install tmpfiles.d config to create /var/lib/lemonade
install -Dpm 0644 /dev/stdin %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d /var/lib/lemonade 0755 lemonade lemonade -
EOF

# Create directory for the buildroot
install -dm 0755 %{buildroot}%{_sharedstatedir}/lemonade

%if %{with check}
%check
# Upstream tests are integration tests that require a running lemonade-server instance
# and GPU hardware for inference. These cannot run within a build environment.
cd test
python3 -m pytest -v
%endif

# Lemonade systemd service file
%post
%systemd_post lemond.service
%systemd_user_post lemond.service
# This is to make sure that /var/lib/lemonade is created immediately after install and not after a reboot
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf 2>/dev/null || :

%preun
%systemd_preun lemond.service
%systemd_user_preun lemond.service

%postun
%systemd_postun_with_restart lemond.service
%systemd_user_postun_with_restart lemond.service

%files
%license LICENSE
%doc README.md
%{_bindir}/lemonade
%{_bindir}/lemond
%{_datadir}/lemonade-server/
%{_datadir}/lemonade/

%{_mandir}/man1/lemonade*.1*
%{_mandir}/man1/lemond.1*

%{_tmpfilesdir}/%{name}.conf
%dir %{_sysconfdir}/lemonade
%dir %{_sysconfdir}/lemonade/conf.d
%dir %attr(0755, lemonade, lemonade) %{_sharedstatedir}/lemonade
# Restrict secrets file to be readable only by root and the lemonade service group
%attr(0640, root, lemonade) %config(noreplace) %{_sysconfdir}/lemonade/conf.d/zz-secrets.conf

%{_unitdir}/lemond.service
%{_userunitdir}/lemond.service
%{_sysusersdir}/lemonade.conf

%changelog
%autochangelog
