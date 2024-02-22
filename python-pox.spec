# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%global forgeurl https://github.com/uqfoundation/pox

Name:           python-pox
Version:        0.3.4
Release:        %autorelease
Summary:        Utilities for filesystem exploration and automated builds

%global tag     %{version}
%forgemeta

# spdx
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global _description %{expand:
pox provides a collection of utilities for navigating and manipulating
filesystems. This module is designed to facilitate some of the low level
operating system interactions that are useful when exploring a filesystem on a
remote host, where queries such as "what is the root of the filesystem?", "what
is the user's name?", and "what login shell is preferred?" become essential in
allowing a remote user to function as if they were logged in locally. While pox
is in the same vein of both the os and shutil builtin modules, the majority of
its functionality is unique and compliments these two modules.

pox provides python equivalents of several unix shell commands such as which
and find. These commands allow automated discovery of what has been installed
on an operating system, and where the essential tools are located. This
capability is useful not only for exploring remote hosts, but also locally as a
helper utility for automated build and installation.

Several high-level operations on files and filesystems are also provided.
Examples of which are: finding the location of an installed python package,
determining if and where the source code resides on the filesystem, and
determining what version the installed package is.

pox also provides utilities to enable the abstraction of commands sent to a
remote filesystem. In conjunction with a registry of environment variables and
installed utilities, pox enables the user to interact with a remote filesystem
as if they were logged in locally.

pox is part of pathos, a python framework for heterogeneous computing. pox is
in active development, so any user feedback, bug reports, comments, or
suggestions are highly appreciated. A list of issues is located at
https://github.com/uqfoundation/pox/issues, with a legacy list maintained at
https://uqfoundation.github.io/project/pathos/query.

Major Features

pox provides utilities for discovering the user's environment:

- return the user's name, current shell, and path to user's home directory
- strip duplicate entries from the user's $PATH
- lookup and expand environment variables from ${VAR} to value

pox also provides utilities for filesystem exploration and manipulation:

- discover the path to a file, executable, directory, or symbolic link
- discover the path to an installed package
- parse operating system commands for remote shell invocation
- convert text files to platform-specific formatting}

%description %_description

%package -n python3-pox
Summary:        %{summary}

%description -n python3-pox %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%forgesetup
# Remove shebangs from (installed) non-script sources. The find-then-modify
# pattern preserves mtimes on sources that did not need to be modified.
find 'pox' 'tests' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
%if %{with doc_pdf}
# Makefile contains no “latex” target, so we invoke sphinx-build manually
PYTHONPATH="${PWD}" sphinx-build -b latex %{?_smp_mflags} \
    docs/source %{_vpath_builddir}/_latex
%make_build -C %{_vpath_builddir}/_latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files -l pox

# remove shebang from generated file
sed -r -i '1{/^#!/d}' $RPM_BUILD_ROOT/%{python3_sitelib}/pox/__info__.py

%check
# There is a check in test_shutils that the user’s home directory ends with the
# username, which is by no means always true, and which is not true in the
# mock/koji build environment. We work around this by faking the home directory
# environment variable with an empty directory.
BOGUSHOME="${PWD}/_bogus/$(id --user --name)"
mkdir -p "${BOGUSHOME}"
HOME="${BOGUSHOME}" %pytest

%files -n python3-pox -f %{pyproject_files}
%doc README.md
%{_bindir}/pox

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc %{_vpath_builddir}/_latex/pox.pdf
%endif

%changelog
%autochangelog
