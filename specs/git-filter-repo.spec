%global gitexecdir %{_libexecdir}/git-core

Name:           git-filter-repo
Version:        2.47.0
Release:        %autorelease
Summary:        Quickly rewrite git repository history (git-filter-branch replacement)
License:        GPL-2.0-only OR MIT
Group:          Development/Tools/Version Control
Url:            https://github.com/newren/git-filter-repo
#
Source0:        https://github.com/newren/git-filter-repo/releases/download/v%{version}/%{name}-%{version}.tar.xz
#
Patch0:         git-filter-repo-metadata.patch
# Don't crash on multi-line config values
Patch1:         4697eeb37b7c3c30b0492e344f6b89f7139cef26.patch
#
BuildArch:      noarch
#
BuildRequires:  git-core >= 2.26.0
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-devel
# test deps
BuildRequires:  perl-interpreter
BuildRequires:  rsync
#
Requires:       git-core >= 2.26.0

%description
git filter-repo is a versatile tool for rewriting history, which includes
capabilities not found anywhere else. It roughly falls into the same space of
tool as git filter-branch but without the capitulation-inducing poor
performance, with far more capabilities, and with a design that scales
usability-wise beyond trivial rewriting cases.

%prep
%autosetup -p1

# Remove shebang from the python module to avoid rpmlint warnings
# (this is a symlink, but sed -i will break it, conveniently for us)
sed -i '1,2d' git_filter_repo.py

# Change shebang in all relevant files in this directory and all subdirectories
find -type f -exec sed -i '1s=^#!%{_bindir}/\(python\|env python\)[23]\?=#!%{_bindir}/python3=' {} +

# Fix shebang print_my_version(); it affects the --version output
sed -Ei "s=#!/usr/bin/env python3=#!%{_bindir}/python3=" %{name} git_filter_repo.py

# Fix links to git docs since we don't install git-filter-repo.html into the
# git htmldir
sed -Ei 's,(a href=")(git),\1%{_docdir}/git/\2,g' Documentation/html/git-filter-repo.html

# https://bugzilla.redhat.com/show_bug.cgi?id=2365637
# TODO FIXME https://github.com/newren/git-filter-repo/issues/673
rm -f t/t9394-filter-repo-sanity-checks-and-bigger-repo-setup.sh

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l git_filter_repo

# Move to right directory, looks like you can't specify the bindir
install -d -m 0755 %{buildroot}%{gitexecdir}
mv %{buildroot}%{_bindir}/git-filter-repo %{buildroot}%{gitexecdir}

install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 Documentation/man1/git-filter-repo.1 %{buildroot}%{_mandir}/man1/git-filter-repo.1

%check
t/run_tests

%files -f %{pyproject_files}
%license COPYING
%doc README.md Documentation/*.md Documentation/html/*.html contrib/filter-repo-demos
%{gitexecdir}/git-filter-repo
%{_mandir}/man1/git-filter-repo.1*

%changelog
%autochangelog
