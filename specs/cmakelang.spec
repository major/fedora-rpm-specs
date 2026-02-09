%global srcname cmake_format

Name:           cmakelang
Version:        0.6.13
Release:        %autorelease
Summary:        Quality Assurance (QA) tools for cmake
License:        GPL-3.0-only AND Python-2.0.1
URL:            https://github.com/cheshirekow/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Debian patches:
# https://salsa.debian.org/debian/cmake_format/-/tree/master/debian/patches
# Copyright 2020, Ian Campbell, GPL-3.0-only
Patch:          0002-Disable-tests-which-don-t-make-sense-for-packaging.patch
Patch:          0004-Compatibility-with-argparse-manpage.patch
Patch:          0006-Update-TestConfigInclude._test_passed-to-support-Pyt.patch

# Non-Debian but in line with `0004-Compatibility-with-argparse-manpage.patch`:
Patch:          0008-Make-ctest_to.py-compatible-with-argparse-manpage.patch

# Fix compatibility with Python 3.15 (#2433805); added code licensed under
# `Python-2.0.1`:
Patch:          0009-Make-lexer-compatible-with-Python-3.15.patch

# Make pip editable installs work (avoid multiple .egg_infos):
# https://github.com/cheshirekow/cmake_format/pull/338
Patch:          12b0bd557bbecf3d2dcf7d59cbd5d3ec77cf1878.diff

BuildArch:      noarch

BuildRequires:  argparse-manpage
BuildRequires:  python3-devel

Requires:       python3-libs

%description
* cmake-annotate can generate pretty HTML from your listfiles.
* cmake-format can format your listfiles nicely.
* cmake-lint can check your listfiles for problems.
* ctest-to can parse a ctest output tree and translate it into a more structured
  format (either JSON or XML).


%prep
%autosetup -n %{srcname}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%global create_manpage PYTHONPATH=. argparse-manpage --function get_argparser
%{create_manpage} --pyfile cmakelang/annotate.py --output cmake-annotate.1
%{create_manpage} --pyfile cmakelang/format/__main__.py --output cmake-format.1
%{create_manpage} --pyfile cmakelang/genparsers.py --output cmake-genparsers.1
%{create_manpage} --pyfile cmakelang/lint/__main__.py --output cmake-lint.1
%{create_manpage} --pyfile cmakelang/ctest_to.py --output ctest-to.1


%install
%pyproject_install
%pyproject_save_files -L %{name}
install -D -m 644 -t "%{buildroot}%{_mandir}/man1" *.1


%check
PYTHONPATH=. %{py3_test_envvars} %{python3} %{name}/tests.py


%files -f %{pyproject_files}
%doc %{name}/doc/README.rst
%{_bindir}/cmake-annotate
%{_bindir}/cmake-format
%{_bindir}/cmake-genparsers
%{_bindir}/cmake-lint
%{_bindir}/ctest-to
%{_mandir}/man1/cmake-annotate.1*
%{_mandir}/man1/cmake-format.1*
%{_mandir}/man1/cmake-genparsers.1*
%{_mandir}/man1/cmake-lint.1*
%{_mandir}/man1/ctest-to.1*


%changelog
%autochangelog
