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
Version:        7.1.1
Release:        %autorelease
Summary:        Remote shell that survives IP roaming and disconnect

# Apache-2.0: et, UniversalStacktrace
# MIT: base64, easyloggingpp, libvterm, PlatformFolders
# Zlib: sole, ThreadPool
License:        Apache-2.0 AND MIT AND Zlib
URL:            https://mistertea.github.io/EternalTerminal/
Source0:        https://github.com/MisterTea/EternalTerminal/archive/et-v%{version}/EternalTerminal-%{version}.tar.gz
Source1:        et.xml
Patch0:         et-use-system-dependency.patch
# Upstream builds with -Werror; fix the warnings Fedora's -Wall enables
# https://github.com/MisterTea/EternalTerminal/pull/920
Patch1:         et-pr920-gcc-wall-warnings.patch
# Reject pipe paths too long for sun_path instead of leaving it
# unterminated (also fixes -Wstringop-truncation); backported to 7.1.1
# https://github.com/MisterTea/EternalTerminal/pull/921
Patch2:         et-pr921-pipe-path-length.patch
# Raise the soft open file limit in the FD_SETSIZE poller test; Koji's
# soft limit of 1024 makes F_DUPFD(FD_SETSIZE) fail
# https://github.com/MisterTea/EternalTerminal/pull/922
Patch3:         et-pr922-fdpoller-nofile-limit.patch

ExcludeArch: %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  firewalld-filesystem
# -static BR required for tracking of header-only libraries
BuildRequires:  catch-devel
BuildRequires:  cpp-httplib-devel
BuildRequires:  cpp-httplib-static
BuildRequires:  cxxopts-devel
BuildRequires:  cxxopts-static
BuildRequires:  json-devel
BuildRequires:  json-static
BuildRequires:  libatomic
BuildRequires:  libselinux-devel
BuildRequires:  libsodium-devel
%if %{with unwind}
BuildRequires:  libunwind-devel
%endif
BuildRequires:  libutempter-devel
BuildRequires:  openssl-devel
%if %{with tests}
# pgrep, pkill and ps, used by the htm end-to-end tests
BuildRequires:  procps-ng
%endif
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-lite-devel
BuildRequires:  simpleini-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel

# Bundled libraries
# Versions are those of the submodule commits pinned at the release tag
# (external/ in the upstream git repository). The tarball carries them
# in external_imported/; the prep section checks that only the
# directories listed here remain, so a newly bundled library fails the
# build.
# https://github.com/tkislan/base64
Provides:       bundled(base64) = 0^20200731git6780d5b
# MisterTea fork of https://github.com/abumusamq/easyloggingpp
Provides:       bundled(easyloggingpp) = 9.97.0^20210202git8489989
# Vendored copy (not a submodule) of libvterm 0.3.3 plus later changes;
# et needs vterm_screen_callbacks_has_pushline4(), which the released
# 0.3.3 shipped as libvterm-devel does not have
Provides:       bundled(libvterm) = 0.3.3
# https://github.com/sago007/PlatformFolders
Provides:       bundled(PlatformFolders) = 4.3.0
# https://github.com/r-lyeh-archived/sole
Provides:       bundled(sole) = 1.0.1^20200819git424b969
# https://github.com/progschj/ThreadPool
Provides:       bundled(ThreadPool) = 0^20140926git9a42ec1
# https://github.com/MisterTea/UniversalStacktrace
Provides:       bundled(UniversalStacktrace) = 0^20260918gitfc5ade8
# Not shipped: sanitizers-cmake (build only). Removed in prep: Catch2,
# cotire, cpp-httplib, cxxopts, json, msgpack-c, sentry-native,
# simpleini, vcpkg

%{?systemd_requires}

%description
Eternal Terminal (ET) is a remote shell that automatically reconnects without
interrupting the session.


%prep
%autosetup -p1 -n EternalTerminal-et-v%{version}

# Unbundle: Catch2, cpp-httplib, cxxopts, json, simpleini
# Unused: cotire, msgpack-c, vcpkg; sentry-native (telemetry disabled)
for d in Catch2 cotire cpp-httplib cxxopts json msgpack-c sentry-native simpleini vcpkg; do
  rm -r external_imported/$d
done

# Fail if upstream bundles something new; update the bundled() Provides
# and License when this list changes
expected="base64 easyloggingpp libvterm PlatformFolders sanitizers-cmake sole ThreadPool UniversalStacktrace"
actual=$(ls external_imported | LC_ALL=C sort -f | xargs)
if [ "$actual" != "$expected" ]; then
  echo "external_imported changed: expected '$expected', got '$actual'" >&2
  exit 1
fi

# Telemetry is compiled out (DISABLE_TELEMETRY); do not suggest otherwise
sed -i 's/^telemetry = true$/telemetry = false/' etc/et.cfg


%build
# DISABLE_TELEMETRY also disables sentry; without it, logs are sent to
# Datadog unless ET_NO_TELEMETRY is set
%cmake \
  -DDISABLE_TELEMETRY=ON \
  -DDISABLE_VCPKG=ON \
  -DBASH_COMPLETION_COMPLETIONSDIR=%{bash_completions_dir} \
  -DZSH_COMPLETIONS_DIR=%{zsh_completions_dir}
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

# Windows wrapper for et1
rm %{buildroot}%{_bindir}/et1.cmd

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
%{_bindir}/et1
%{_bindir}/etctl
%{_bindir}/etserver
%{_bindir}/etterminal
%{_bindir}/htm
%{_bindir}/htmd
%dir %{_firewalld_dir}
%dir %{_firewalld_dir}/services
%{_firewalld_dir}/services/et.xml
%config(noreplace) %{_sysconfdir}/et.cfg
%{_unitdir}/et.service
%{bash_completions_dir}/et
%{zsh_completions_dir}/_et


%changelog
%autochangelog
