# * no tests available
%bcond check 0
%global watcher_name aw-awatcher

%global aw_server_rust_commit a0cdef90cf86cd8d2cc89723f5751c1123ae7e2b
%global aw_server_rust_short_commit %(c=%{aw_server_rust_commit}; echo ${c:0:7})

Name:           awatcher
Version:        0.3.2
Release:        %autorelease
Summary:        A window activity and idle watcher
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
License:        Apache-2.0 AND BSL-1.0 AND BSD-3-Clause AND (Apache-2.0 WITH LLVM-exception) AND ISC AND MIT AND Unicode-DFS-2016 AND Unicode-3.0 AND MPL-2.0 AND Unlicense
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/2e3s/awatcher
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/ActivityWatch/aw-server-rust/archive/%{aw_server_rust_commit}/aw-server-rust-%{aw_server_rust_short_commit}.tar.gz

Patch0:         0001-Use-locally-downloaded-aw-server-rust.patch
Patch1:         0002-Fix-dependencies-to-the-one-used-in-Fedora.patch
# Remove due to a missing dependency.
Patch2:         0003-Remove-cosmic-watcher.patch
Patch3:         0004-Remove-unneeded-dev-dependencies.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  systemd-rpm-macros
BuildRequires:  help2man

%description
%{summary}.

%package     -n %{watcher_name}
Requires:       aw-server-rust
Summary:        %{summary}
# Hopefuly one day it will be a part of aw-server-rust
# https://github.com/ActivityWatch/activitywatch/issues/92#issuecomment-1583938452
Provides:       bundled(aw-server-rust)

%description -n %{watcher_name}
%{summary}.

%prep
%autosetup -n %{name}-%{version} -N
tar -xf %{SOURCE1} --strip-components 1 aw-server-rust-%{aw_server_rust_commit}/{aw-client-rust,aw-models}
%autopatch -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
# prefix with aw- in order to be detected as a watcher in aw-qt
install -Dm 0755 target/release/%{name} %{buildroot}%{_bindir}/%{watcher_name}
mkdir -p %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{watcher_name} -o %{buildroot}%{_mandir}/man1/%{watcher_name}.1
install -Dm 0644 config/%{watcher_name}.service -t %{buildroot}%{_userunitdir}

%if %{with check}
%check
%cargo_test
%endif

%post -n %{watcher_name}
%systemd_user_post %{watcher_name}.service

%preun -n %{watcher_name}
%systemd_user_preun %{watcher_name}.service

%postun -n %{watcher_name}
%systemd_user_postun_with_restart %{watcher_name}.service

%files -n %{watcher_name}
%doc README.md
%license LICENSE LICENSE.dependencies
%{_mandir}/man1/%{watcher_name}.1*
%{_bindir}/%{watcher_name}
%{_userunitdir}/%{watcher_name}.service

%changelog
%autochangelog
