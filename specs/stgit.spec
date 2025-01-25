%bcond_without check

Name:       stgit
Version:    2.5.1
Release:    %autorelease
Summary:    Stack-based patch management for Git

SourceLicense:    GPL-2.0-only
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# GPL-2.0-only
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        Apache-2.0 AND BSD-3-Clause AND GPL-2.0-only AND MIT AND Unicode-DFS-2016 AND (0BSD OR Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense)

URL:        https://stacked-git.github.io/
Source:     https://github.com/stacked-git/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Relax clap dependency to allow building with clap 4.5+
# Relax thiserror dependency
Patch:      stgit-fix-metadata.diff

BuildRequires:  cargo-rpm-macros
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  xmlto

%if %{with check}
BuildRequires:  procps-ng
BuildRequires:  git-core
BuildRequires:  git-email
%endif

Requires:   git-core
Requires:   git-email
Requires:   emacs-filesystem
Requires:   vim-filesystem

%description
Stacked Git, StGit for short, is an application for managing Git commits as a
stack of patches.

With a patch stack workflow, multiple patches can be developed concurrently and
efficiently, with each patch focused on a single concern, resulting in both a
clean Git commit history and improved productivity.

%prep
%autosetup -n %{name}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# The build.rs file only adds an environment variable with the current git
# hash. The tarball is not a git repo so the build script doesn't do anything.
# This also means, it doesn't emit any rerun-if* directives. This makes cargo
# rebuild the whole application if any file changes. This causes frequent
# recompiles in the documentation, etc. leading to very long build times.
rm build.rs
# The Makefile uses some combination of --locked and --offline which only work
# with Cargo.lock present. Regenerating it after cargo_prep should be fine.
%{__cargo} generate-lockfile

make all CARGO="%{__cargo}" STG_PROFILE=rpm
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
make install install-man install-completion install-contrib CARGO="%{__cargo}" STG_PROFILE=rpm DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}

# Install data files
install -m 644 -D contrib/stgbashprompt.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib/stgbashprompt.sh

%if %{with check}
%check
%cargo_test
# Use the same profile to prevent a rebuild of the application
make test CARGO="%{__cargo}" STG_PROFILE=rpm
%endif

%files
%license COPYING
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md
%{_bindir}/stg
%{_mandir}/man1/stg*
%{_datadir}/%{name}/
%{_datadir}/emacs/site-lisp/stgit.el
%{_datadir}/vim/vimfiles/ftdetect/stg.vim
%{_datadir}/vim/vimfiles/syntax/stg*.vim
%{bash_completions_dir}/stg
%{fish_completions_dir}/stg.fish
%{zsh_completions_dir}/_stg

%changelog
%autochangelog
