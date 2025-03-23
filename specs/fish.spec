%global version_base 4.0.1
%dnl %global version_pre beta.1
%dnl %global gitnum 1
%dnl %global githash b82d0fcbcc44eb259cf2209b04f7a41c1f324e27
%dnl %global githashshort %{lua:print(string.sub(rpm.expand('%{githash}'), 1, 11))}

# For forked pcre2 crate that includes https://github.com/BurntSushi/rust-pcre2/pull/38
%global rust_pcre2_fish_tag 0.2.9-utf32

Name:           fish
Version:        %{version_base}%{?version_pre:~%{version_pre}}%{?gitnum:^git%{gitnum}.%{githashshort}}
Release:        %autorelease
Summary:        Friendly interactive shell
# Non-code licenses, see also doc_src/license.rst
# MIT
#   - share/completions/grunt.fish
#   - share/tools/web_config/js/angular-route.js
#   - share/tools/web_config/js/angular-sanitize.js
#   - share/tools/web_config/js/angular.js
# PSF-2.0
#   - doc_src/python_docs_theme/,
# Code licenses, see LICENSE.dependencies for a full license breakdown
# Apache-2.0 OR MIT
# GPL-2.0-only AND LGPL-2.0-or-later AND MIT AND PSF-2.0
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
# WTFPL
# Zlib
License:        Apache-2.0 OR MIT and GPL-2.0-only AND LGPL-2.0-or-later AND MIT AND PSF-2.0 and Unlicense OR MIT and WTFPL and Zlib
URL:            https://fishshell.com
%if %{undefined gitnum}
Source0:        https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/fish-shell/fish-shell/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-003837986104878835FA516D7A67D962D88A709A.gpg
%else
Source0:        https://github.com/fish-shell/fish-shell/archive/%{githash}/%{name}-%{githash}.tar.gz
%endif

# For forked pcre2 crate that includes https://github.com/BurntSushi/rust-pcre2/pull/38
Source10:       https://github.com/fish-shell/rust-pcre2/archive/%{rust_pcre2_fish_tag}/rust-pcre2-%{rust_pcre2_fish_tag}.tar.gz

# Backports from upstream (0001~500)
## From: https://github.com/fish-shell/fish-shell/commit/a42c5b4025abfb0113af8c51c096795d47ef0802
Patch0001:      0001-Remove-fish.desktop-file-as-it-was-only-needed-for-A.patch
## From: https://github.com/fish-shell/fish-shell/commit/ef4fad763febfcd91f3d08c9c721047f82ea574f
Patch0002:      0002-Remove-fish.desktop-harder.patch

# Proposed upstream (501~1000)
Patch0501:      https://github.com/fish-shell/fish-shell/pull/11173.patch
# Proposed in a different form (with Cargo.lock changes) upstream: https://github.com/fish-shell/fish-shell/pull/11311
Patch0502:      0502-Update-lru-to-0.13.0.patch

# Downstream-only (1001+)
Patch1001:      1001-cargo-Use-internal-copy-of-rust-pcre2-instead-of-fet.patch
Patch1002:      1002-cmake-Use-rpm-profile-for-RelWithDebInfo.patch
## Already exists in a different form upstream: https://github.com/fish-shell/fish-shell/commit/0c9c5e3a341903a9820c26b04fc9d1c7ed6e4053
Patch1003:      1003-cargo-Bump-serial_test-to-v3.patch

# Patches for bundled dependencies (10000+)
## For forked pcre2 crate that includes https://github.com/BurntSushi/rust-pcre2/pull/38
Patch10001:     10001-rust-pcre2-cargo-Drop-workspace-definition.patch


BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake >= 3.5
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  python3-pexpect
BuildRequires:  procps-ng
BuildRequires:  rust
BuildRequires:  glibc-langpack-en
%global __python %{__python3}
BuildRequires:  /usr/bin/sphinx-build

# Needed to get terminfo
Requires:       ncurses-term

# tab completion wants man-db
Recommends:     man-db
Recommends:     man-pages
Recommends:     groff-base

# For the webconfig interface
Provides:       bundled(js-alpine)

# For forked pcre2 crate that includes https://github.com/BurntSushi/rust-pcre2/pull/38
Provides:       bundled(crate(pcre2)) = %{rust_pcre2_fish_tag}

# fish does not currently build on 32-bit architectures
ExcludeArch:    %{ix86} %{arm32}

%description
fish is a fully-equipped command line shell (like bash or zsh) that is
smart and user-friendly. fish supports powerful features like syntax
highlighting, autosuggestions, and tab completions that just work, with
nothing to learn or configure.

%prep
%if %{undefined gitnum}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -N %{?gitnum:-n fish-shell-%{githash}}

# For forked pcre2 crate that includes https://github.com/BurntSushi/rust-pcre2/pull/38
mkdir -p ./third-party-forks/rust-pcre2
tar -C ./third-party-forks/rust-pcre2 --strip-components=1 -xf %{SOURCE10}

%autopatch -p1

%if %{defined gitnum}
echo "%{version}" > version
%endif

# Change the bundled scripts to invoke the python binary directly.
for f in $(find share/tools -type f -name '*.py'); do
    sed -i -e '1{s@^#!.*@#!%{__python3}@}' "$f"
done
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires -t


%conf
%cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_DOCS=ON \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -Dextra_completionsdir=%{_datadir}/%{name}/vendor_completions.d \
    -Dextra_functionsdir=%{_datadir}/%{name}/vendor_functions.d \
    -Dextra_confdir=%{_datadir}/%{name}/vendor_conf.d


%build
export CARGO_NET_OFFLINE=true

# Cargo doesn't create this directory
mkdir -p %{_vpath_builddir}

%cmake_build -t all doc

# We still need to slightly manually adapt the pkgconfig file and remove
# some /usr/local/ references (RHBZ#1869376)
sed -i 's^/usr/local/^/usr/^g' %{_vpath_builddir}/*.pc

# Get Rust licensing data
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
%cmake_install

# No more automagic Python bytecompilation phase 3
# * https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/tools/

# Install docs from tarball root
cp -a README.rst %{buildroot}%{_pkgdocdir}
cp -a CONTRIBUTING.rst %{buildroot}%{_pkgdocdir}

%find_lang %{name}


%check
%cmake_build --target fish_run_tests


%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/fish" > %{_sysconfdir}/shells
    echo "/bin/fish" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/fish$" %{_sysconfdir}/shells || echo "%{_bindir}/fish" >> %{_sysconfdir}/shells
    grep -q "^/bin/fish$" %{_sysconfdir}/shells || echo "/bin/fish" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/fish$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/fish$!d' %{_sysconfdir}/shells
fi


%files -f %{name}.lang
%license COPYING
%license LICENSE.dependencies
%{_mandir}/man1/fish*.1*
%{_bindir}/fish*
%config(noreplace) %{_sysconfdir}/fish/
%{_datadir}/fish/
%{_datadir}/pkgconfig/fish.pc
%{_pkgdocdir}


%changelog
%autochangelog
