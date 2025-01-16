# Not all test dependencies are packaged for fedora
%bcond check 0

Name:    newsboat
Version: 2.38
Release: %{autorelease}
Summary: RSS/Atom feed reader for the text console

License: MIT
URL:     https://www.newsboat.org
Source0: https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz
Source1: https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2: https://newsboat.org/newsboat.pgp

Patch:  0001-make-do-not-require-Cargo.lock.patch
Patch:  0002-libnewsboat-relax-requirements.patch
Patch:  0003-Do-not-build-http-test-server-by-default.patch
## # Following patches should be included in next release; prune when updating

# Source file verification
BuildRequires: make
BuildRequires: gnupg2

BuildRequires: asciidoctor
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: pkgconfig(json-c) >= 0.11
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(stfl)
# Rust parts
BuildRequires:  git
BuildRequires:  rust-packaging

Provides: podboat = %{version}-%{release}

%description
Newsboat is a fork of Newsbeuter, an RSS/Atom feed reader for the text console.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
# Note to self: do not use -S git_am for released builds, it messes up version string
%autosetup -p1
%cargo_prep

%generate_buildrequires
INTERNAL_CRATES=$'libnewsboat\nlibnewsboat-ffi\nregex-rs\nstrprintf'
cargo2rpm --path=Cargo.toml buildrequires --all-features %{?with_check:--with-check}|grep -vwe "${INTERNAL_CRATES}"

%build
# Respect RPM settings
%set_build_flags
# Do not fail build because our GCC emits different warnings
export CFLAGS="-Wno-error ${CFLAGS}" CXXFLAGS="-Wno-error ${CXXFLAGS}"
# CARGO_BUILD_FLAGS is used/appended to by this Makefile
export CARGO_BUILD_FLAGS="%{__cargo_common_opts}"

# Verify non-rust deps and setup LDFLAGS
sh config.sh

# Build the project
# Replace bare `cargo` with the one used by %%cargo_* macros
%make_build CARGO="%{__cargo}" all %{?with_check:test}

%install
%make_install prefix="%{_prefix}"
# Remove executable bit from example/contrib scripts
find %{buildroot}%{_pkgdocdir}/ -type f -exec chmod -x '{}' +

%find_lang %{name}

%check
%if %{with check}
# TMPDIR=%%{_tmppath} ./test/test  # Have issues with permission in tpmdir
%cargo_test
%endif
# Ensure that the proper release version is detected
%{buildroot}%{_bindir}/newsboat --version|sed 1q|grep -v dirty

%files -f %{name}.lang
%license LICENSE
%doc README.md

%{_bindir}/newsboat
%{_bindir}/podboat

%{_mandir}/man1/newsboat.1*
%{_mandir}/man1/podboat.1*
%{_pkgdocdir}
%{_datadir}/icons/hicolor/scalable/apps/newsboat.svg

%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/newsboat.fish

%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_newsboat

%changelog
%{autochangelog}
