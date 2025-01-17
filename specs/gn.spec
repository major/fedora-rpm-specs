# Build HTML docs from markdown using pandoc?
%bcond html_docs 1

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
%global commit ed1abc107815210dc66ec439542bee2f6cbabc00
%global access 20250116
%global shortcommit %{sub %{commit} 1 12}
%global position 2207
Version:        %{position}^%{access}git%{shortcommit}
Release:        %autorelease
Summary:        Meta-build system that generates build files for Ninja

# The entire source is BSD-3-Clause, except:
#   - src/base/third_party/icu/ is (Unicode-DFS-2016 AND ICU); see
#     src/base/third_party/icu/LICENSE and also the header comment in
#     src/base/third_party/icu/icu_utf.h.
#
# Note that src/util/test/gn_test.cc, which is licensed Apache-2.0, does not
# contribute to the binary RPMs, only to the gn_unittests executable, which is
# not installed; you may verify this with:
#   gdb -ex 'set pagination off' -ex 'info sources' gn | grep -F gn_test.cc
License:        BSD-3-Clause AND Unicode-DFS-2016 AND ICU
SourceLicense:  %{license} AND Apache-2.0
URL:            https://gn.googlesource.com/gn
Source0:        %{url}/+archive/%{commit}.tar.gz#/gn-%{shortcommit}.tar.gz
# Generated using script update-version:
Source1:        last_commit_position.h
Source2:        update-version

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

%if %{with html_docs}
BuildRequires:  pandoc
BuildRequires:  parallel
%endif
BuildRequires:  help2man

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

%description
GN is a meta-build system that generates build files for Ninja.


%package doc
Summary:        Documentation for GN
BuildArch:      noarch

%description doc
The gn-doc package contains detailed documentation for GN.


%prep
%autosetup -c -n gn-%{commit} -p1

# Use pre-generated last_commit_position.h.
mkdir -p ./out
cp -vp '%{SOURCE1}' ./out

# Copy and rename vim extensions readme for use in the main documentation
# directory.
cp -vp misc/vim/README.md README-vim.md

# Fix shebangs in examples and such.
%py3_shebang_fix .


%conf
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
ninja -j %{_smp_build_ncpus} -C out -v

%if %{with html_docs}
# There is a script, misc/help_as_html.py, that generates some HTML help, but
# pandoc does a better job and we can cover more Markdown sources.
find . -type f -name '*.md' | parallel -v pandoc -o '{.}.html' '{}'
%endif

help2man \
    --name='%{summary}' \
    --version-string="gn $(./out/gn --version)" \
    --no-info \
    ./out/gn |
  # Clean up a couple of stray binary bytes in the help output
  tr -d '\302\240' |
  # Format the entries within the sections as tagged paragraphs, and italicise
  # [placeholders in square brackets].
  sed -r -e 's/(^[[:alnum:]_]+:)/.TP\n.B \1\n/' \
      -e 's/\[([^]]+)\]/\\fI[\1]\\fR/g' > out/gn.1


%install
install -t '%{buildroot}%{_bindir}' -D -p out/gn

install -d '%{buildroot}%{_datadir}/vim/vimfiles'
cp -vrp misc/vim/* '%{buildroot}%{_datadir}/vim/vimfiles'
find '%{buildroot}%{_datadir}/vim/vimfiles' \
    -type f -name 'README.*' -print -delete
%py_byte_compile %{python3} '%{buildroot}%{_datadir}/vim/vimfiles/gn-format.py'

install -t '%{buildroot}%{_emacs_sitestartdir}' -D -p -m 0644 misc/emacs/*.el

install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p out/gn.1


%check
out/gn_unittests

# Verify consistency of the version header with the spec file
grep -E '^#define[[:blank:]]+LAST_COMMIT_POSITION_NUM[[:blank:]]+'\
'%{position}[[:blank:]]*' \
    'out/last_commit_position.h' >/dev/null
grep -E '^#define[[:blank:]]+LAST_COMMIT_POSITION[[:blank:]]+'\
'"%{position} \(%{shortcommit}\)"[[:blank:]]*' \
    'out/last_commit_position.h' >/dev/null


%files
%license LICENSE
%{_bindir}/gn

%{_mandir}/man1/gn.1*

%{_datadir}/vim/vimfiles/gn-format.py
%{_datadir}/vim/vimfiles/autoload/gn.vim
%{_datadir}/vim/vimfiles/ftdetect/gnfiletype.vim
%{_datadir}/vim/vimfiles/ftplugin/gn.vim
%{_datadir}/vim/vimfiles/syntax/gn.vim

%{_emacs_sitestartdir}/gn-mode.el


%files doc
%license LICENSE src/base/third_party/icu/README.chromium
%doc AUTHORS
%doc OWNERS
%doc README*.md
%if %{with html_docs}
%doc README*.html
%endif
%doc docs/
%doc examples/
%doc infra/
%doc tools/


%changelog
%autochangelog
