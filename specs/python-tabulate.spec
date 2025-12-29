# python-pandas creates a cyclic dependency on python-Bottleneck;
# we need to be able to break it during the new Python bootstrap
%bcond bootstrap 0
%bcond pandas_tests %{without bootstrap}

Name:           python-tabulate
Version:        0.9.0
Release:        %autorelease
Summary:        Pretty-print tabular data in Python, a library and a command-line utility

# SPDX
License:        MIT
URL:            https://github.com/astanin/python-tabulate
Source0:        %{pypi_source tabulate}
# Hand-written for Fedora based on --help output using groff_man(7) format
Source1:        tabulate.1

BuildArch:      noarch

BuildRequires:  python3-devel

# Additional test deps; see tox.ini, not in the sdist
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
%if ! 0%{?el9} && %{with pandas_tests}
# The pandas backport is not finished yet in EPEL 9. See BZ 2032550.
# The BR is needed only for Pandas integration tests.
BuildRequires:  python3dist(pandas)
%endif

%global _description %{expand:
The main use cases of the library are:

• printing small tables without hassle: just one function call, formatting is
  guided by the data itself
• authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
• readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point}

%description %{_description}


%package -n python3-tabulate
Summary:        %{summary}

Recommends:     python3-tabulate+widechars

%description -n python3-tabulate %{_description}


%pyproject_extras_subpkg -n python3-tabulate widechars


%prep
%autosetup -n tabulate-%{version}


%generate_buildrequires
%pyproject_buildrequires -x widechars


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l tabulate

install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p '%{SOURCE1}'


%check
%pyproject_check_import

# Failing tests test_wrap_multiword_non_wide* in current Pythons
# https://github.com/astanin/python-tabulate/issues/389
k="${k-}${k+ and }not test_wrap_multiword_non_wide"
k="${k-}${k+ and }not test_wrap_multiword_non_wide_with_hyphens"

%pytest --doctest-modules --ignore benchmark.py -k "${k-}"


%files -n python3-tabulate -f %{pyproject_files}
%doc CHANGELOG
%doc README.md

%{_bindir}/tabulate
%{_mandir}/man1/tabulate.1*


%changelog
%autochangelog
