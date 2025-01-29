%bcond check 1

%global commit a0cdef90cf86cd8d2cc89723f5751c1123ae7e2b
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           aw-server-rust
Version:        0.13.1^20241216.git%{short_commit}
Release:        %autorelease
Summary:        A re-implementation of aw-server in Rust
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR ISC OR MIT
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND MIT AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/ActivityWatch/aw-server-rust
Source:         %{url}/archive/%{commit}/%{name}-%{short_commit}.tar.gz

Patch0:         0001-Remove-vendored-openssl.patch
Patch1:         0002-Remove-Android-dependencies.patch
# jemallocator will not be packaged for Fedora, so remove it
Patch2:         0003-Remove-jemallocator.patch
# switch to dependency versions available in Fedora
Patch3:         0004-Fix-fern-dependency-to-the-one-used-in-Fedora.patch
Patch4:         0005-Fix-fancy-regex-dependency-to-the-one-used-in-Fedora.patch
Patch5:         0006-Fix-rusqlite-dependency-to-the-one-used-in-Fedora.patch
# drop an unused, benchmark-only criterion dev-dependency to speed up builds
Patch6:         0007-Remove-criterion.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  systemd-rpm-macros
BuildRequires:  help2man
BuildRequires:  nodejs-aw-webui

%description
%{summary}

%package     -n aw-sync-rust
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}

%description -n aw-sync-rust
%{summary}

%prep
%autosetup -n %{name}-%{commit} -p1

# append current commit to the version string for displaying in the UI
# similarily to what upstream Makefile setversion does
sed -ri 's/version = ("[[:alnum:]]+\.[[:alnum:]]+\.[[:alnum:]]+)/version = \1+%{short_commit}/' aw-server/Cargo.toml

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# no UI built without this
export AW_WEBUI_DIR="%{_datadir}/aw-webui/dist/"
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dm 0755 target/rpm/{aw-server,aw-sync} -t %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/aw-server -o %{buildroot}%{_mandir}/man1/aw-server.1
help2man %{buildroot}%{_bindir}/aw-sync -o %{buildroot}%{_mandir}/man1/aw-sync.1
install -Dm 0644 aw-server.service -t %{buildroot}%{_userunitdir}

%if %{with check}
%check
# tests report an error with EmbeddedAssets without this
export AW_WEBUI_DIR="%{_datadir}/aw-webui/dist/"
%cargo_test
%endif

%post
%systemd_user_post aw-server.service

%preun
%systemd_user_preun aw-server.service

%postun
%systemd_user_postun_with_restart aw-server.service

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%{_mandir}/man1/aw-server.1*
%{_bindir}/aw-server
%{_userunitdir}/aw-server.service

%files -n aw-sync-rust
%doc README.md
%license LICENSE LICENSE.dependencies
%{_mandir}/man1/aw-sync.1*
%{_bindir}/aw-sync

%changelog
%autochangelog
