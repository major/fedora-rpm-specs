%bcond bundled_cxx 0

Name:           gn
# Upstream uses the number of commits in the git history as the version number.
# See gn --version, which outputs something like “1874 (2b683eff)”. The commit
# position and short commit hash in this string come from “git describe HEAD
# --match initial-commit”; see build/gen.py. This means that a complete git
# checkout is required to establish the version number; the information is not
# in the tarball! This is terribly inconvenient. See
# https://bugs.chromium.org/p/gn/issues/detail?id=3.
#
# As a result, it is necessary to use our custom update-version script,
# supplying the new full commit hash as the sole argument or providing no
# arguments to select the latest commit. This will:
#  1. Clone the git repository from the Internet (a substantial download)
#  2. Run build/gen.py to generate last_commit_position.h, the header with
#     version information, and copy it into the same directory as the script
#  3. Modify the commit and access macros and the Version field in this spec
#     file.
#  4. Download the source tarball (spectool -g)
#  5. Update the sources (fedpkg new-sources %%{commit}.tar.gz)
#  6. Stage all changes in git
#  7. Commit the changes
#
# See https://gn.googlesource.com/gn/+log for the latest changes.
%global commit 8d35b83847d1bf61bad0b8176a8aab6afc052ae1
%global access 20260708
%global shortcommit %{sub %{commit} 1 12}
%global position 2459
Version:        %{position}^%{access}.%{shortcommit}
Release:        %autorelease
Summary:        Meta-build system that generates build files for Ninja

# The entire source is BSD-3-Clause, except:
#
# - src/base/third_party/icu/ is (Unicode-DFS-2016 AND ICU); see
#   src/base/third_party/icu/LICENSE and also the header comment in
#   src/base/third_party/icu/icu_utf.h.
# - src/gn/starlark/vendor/cxx/include/cxx.h is (MIT OR Apache-2.0); per
#   src/gn/starlark/vendor/cxx/README.md, it is
#   https://github.com/dtolnay/cxx/blob/1.0.194/include/cxx.h.
%global bundled_cxx_version 1.0.194
#   The license texts for this are missing,
#   https://gn.issues.chromium.org/issues/529413117.
# - gn/src/util/test/gn_test.cc, gn/infra/recipes/gn.py, and
#   gn/infra/recipes.py are Apache-2.0. The first does not contribute to the
#   binary RPMs, only to the gn_unittests executable, which is not installed;
#   not installed; you may verify this with:
#     gdb -ex 'set pagination off' -ex 'info sources' gn | grep -F gn_test.cc
#   However, the two files from gn/infra/ are installed in the -doc subpackage.
#   The required Apache-2.0 license text is missing,
#   https://gn.issues.chromium.org/issues/529413117.
License:        %{shrink:
    BSD-3-Clause AND
    ICU AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT)
    }
SourceLicense:  %{license} AND Apache-2.0
URL:            https://gn.googlesource.com/gn
Source0:        %{url}/+archive/%{commit}.tar.gz#/gn-%{shortcommit}.tar.gz
# Generated using script update-version:
Source1:        last_commit_position.h
Source2:        update-version
# Missing Apache-2.0 license text for src/gn/starlark/vendor/cxx/include/cxx.h,
# gn/src/util/test/gn_test.cc, gn/infra/recipes/gn.py, and gn/infra/recipes.py.
# https://gn.issues.chromium.org/issues/529413117
Source3:        https://www.apache.org/licenses/LICENSE-2.0.txt
# Missing MIT license text for src/gn/starlark/vendor/cxx/include/cxx.h; the
# corresponding LICENSE-APACHE would be identical to LICENSE-2.0.txt, above, so
# we don’t need another copy.
# https://gn.issues.chromium.org/issues/529413117
Source4:        https://github.com/dtolnay/cxx/raw/refs/tags/%{bundled_cxx_version}/LICENSE-MIT

# Downstream-only: do not override optimization flags
#
# Stop overriding optimization flags; not sent upstream because this is
# intentional on their part.
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags
Patch:          0001-Downstream-only-do-not-override-optimization-flags.patch
# Downstream-only: do not build with -Wno-format
#
# This conflicts with -Werror=format-security.
Patch:          0002-Downstream-only-do-not-build-with-Wno-format.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  ninja-build
BuildRequires:  gcc-c++

# For RPM macros:
BuildRequires:  emacs-common

BuildRequires:  help2man
%if %{without bundled_cxx}
BuildRequires:  cargo-rpm-macros
# We express this as rust-cxx-devel rather than crate(cxx) because we don’t use
# the package as a Rust crate, only for the C++ header file it contains, and
# this better reflectes our intent.
BuildRequires:  (rust-cxx-devel >= 1.0.0 with rust-cxx-devel < 2.0.0~)
%endif

Requires:       vim-filesystem
Requires:       python3
Provides:       vim-gn = %{version}-%{release}

Requires:       emacs-filesystem >= %{_emacs_version}
Provides:       emacs-gn = %{version}-%{release}

# src/base/third_party/icu/icu_utf.h:
#
#   This file has the relevant components from ICU copied to handle basic
#   UTF8/16/32 conversions. Components are copied from umachine.h, utf.h,
#   utf8.h, and utf16.h into icu_utf.h.
#
# The forked, bundled ICU components are copied from Chromium. Because of the
# downstream changes (primarily, changing namespaces and symbol prefixes),
# there is no clear path to unbundling.
#
# See src/base/third_party/icu/README.chromium, from which the version number
# is taken.
Provides:       bundled(icu) = 60
%if %{with bundled_cxx}
# src/gn/starlark/vendor/cxx/include/cxx.h
Provides:       bundled(crate(cxx)) = %{bundled_cxx_version}
%endif

%description
GN is a meta-build system that generates build files for Ninja.


%package doc
Summary:        Documentation for GN
BuildArch:      noarch

# The entire source is BSD-3-Clause, except where otherwise noted in the
# comment above the base package’s License field.
#
# The -doc subpackage contains files that are Apache-2.0:
# gn/infra/recipes/gn.py and gn/infra/recipes.py.
License:        BSD-3-Clause AND Apache-2.0

%description doc
The gn-doc package contains detailed documentation for GN.


%prep
%autosetup -c -n gn-%{commit} -p1

# Use pre-generated last_commit_position.h.
mkdir ./out
cp --preserve '%{SOURCE1}' ./out/

# Copy and rename vim extensions readme for use in the main documentation
# directory.
cp --preserve misc/vim/README.md README-vim.md

# Fix shebangs in examples and such.
%py3_shebang_fix .

# Copy in missing license texts.
cp --preserve '%{SOURCE3}' '%{SOURCE4}' .
# Put the ICU license text somewhere it’s easy to install, with a unique name.
cp --preserve src/base/third_party/icu/LICENSE LICENSE-ICU

rm src/gn/starlark/Cargo.lock

%conf
%if %{without bundled_cxx}
# Unbundle this in %%conf rather than %%prep to ensure that the dependency we
# are trying to symlink is installed.
cxx_header='src/gn/starlark/vendor/cxx/include/cxx.h'
# Explicit removal asserts that we still have the right path, failing if the
# file does not exist.
rm "${cxx_header}"
system_cxx_header="$(
    rpm --query --list rust-cxx-devel | grep -E '/cxx\.h$' | head -n 1
)"
ln --symbolic --verbose "${system_cxx_header}" "${cxx_header}"
%endif

AR='gcc-ar'; export AR
# Treating warnings as errors is too strict for downstream builds.
#
# Both --use-icf and --use-lto add compiler flags that only work with clang++,
# not with g++. We do get LTO on Fedora anyway, since we respect the
# distribution’s build flags.
%{python3} build/gen.py \
    --allow-warnings \
    --no-last-commit-position \
    --no-strip \
    --no-static-libstdc++


%build
%ninja_build -C out

help2man \
    --name='%{summary}' \
    --version-string="gn $(./out/gn --version)" \
    --no-info \
    ./out/gn |
  # Clean up a couple of stray binary bytes in the help output
  tr --delete '\302\240' |
  # Format the entries within the sections as tagged paragraphs, and italicise
  # [placeholders in square brackets].
  sed --regexp-extended --expression='s/(^[[:alnum:]_]+:)/.TP\n.B \1\n/' \
      --expression='s/\[([^]]+)\]/\\fI[\1]\\fR/g' > out/gn.1


%install
install -D --preserve-timestamps --target='%{buildroot}%{_bindir}' out/gn

install --directory '%{buildroot}%{_datadir}/vim/vimfiles'
cp --verbose --recursive --preserve misc/vim/* \
    '%{buildroot}%{_datadir}/vim/vimfiles'
find '%{buildroot}%{_datadir}/vim/vimfiles' \
    -type f -name 'README.*' -print -delete
%py_byte_compile %{python3} '%{buildroot}%{_datadir}/vim/vimfiles/gn-format.py'

install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_emacs_sitestartdir}' misc/emacs/*.el

install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' out/gn.1


%check
out/gn_unittests

# Verify consistency of the version header with the spec file
grep --extended-regexp \
    '^#define[[:blank:]]+LAST_COMMIT_POSITION_NUM[[:blank:]]+'\
'%{position}[[:blank:]]*' \
    'out/last_commit_position.h' >/dev/null
grep --extended-regexp \
    '^#define[[:blank:]]+LAST_COMMIT_POSITION[[:blank:]]+'\
'"%{position} \(%{shortcommit}\)"[[:blank:]]*' \
    'out/last_commit_position.h' >/dev/null


%files
%license LICENSE LICENSE-ICU LICENSE-2.0.txt LICENSE-MIT
%{_bindir}/gn

%{_mandir}/man1/gn.1*

%{_datadir}/vim/vimfiles/gn-format.py
%{_datadir}/vim/vimfiles/autoload/gn.vim
%{_datadir}/vim/vimfiles/ftdetect/gnfiletype.vim
%{_datadir}/vim/vimfiles/ftplugin/gn.vim
%{_datadir}/vim/vimfiles/syntax/gn.vim

%{_emacs_sitestartdir}/gn-mode.el


%files doc
%license LICENSE LICENSE-2.0.txt
%doc AUTHORS
%doc OWNERS
%doc README*.md
%doc docs/
%doc examples/
%doc infra/
%doc tools/


%changelog
%autochangelog
