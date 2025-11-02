# Optional integration tests:
%bcond matplotlib 1
%bcond numpy 1
%bcond pandas 1
%bcond scipy 1
%bcond sklearn 1
%bcond statsmodels 1
# Not packaged:
%bcond pymvpa2 0
%bcond psychopy 0

%global _description %{expand: \
duecredit is being conceived to address the problem of inadequate citation of
scientific software and methods, and limited visibility of donation requests
for open-source software.

It provides a simple framework (at the moment for Python only) to embed
publication or other references in the original code so they are automatically
collected and reported to the user at the necessary level of reference detail,
i.e. only references for actually used functionality will be presented back if
software provides multiple citeable implementations.}

Name:           python-duecredit
Version:        0.10.2
Release:        %autorelease
Summary:        Automated collection and reporting of citations

License:        BSD-2-Clause-Views
URL:            https://github.com/duecredit/duecredit
Source0:        %{pypi_source duecredit}

BuildArch:      noarch

%description
%{_description}

%package -n python3-duecredit
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
%if %{with matplotlib}
BuildRequires:  %{py3_dist matplotlib}
%endif
%if %{with numpy}
BuildRequires:  %{py3_dist numpy}
%endif
%if %{with pandas}
BuildRequires:  %{py3_dist pandas}
%endif
%if %{with scipy}
BuildRequires:  %{py3_dist scipy}
%endif
%if %{with sklearn}
BuildRequires:  %{py3_dist scikit-learn}
%endif
%if %{with statsmodels}
BuildRequires:  %{py3_dist statsmodels}
%endif
%if %{with pymvpa2}
BuildRequires:  %{py3_dist pymvpa2}
%endif
%if %{with psychopy}
BuildRequires:  %{py3_dist psychopy}
%endif
BuildRequires:  help2man


%description -n python3-duecredit
%{_description}

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -n duecredit-%{version}

# remove coverage stuff
sed -i '/--cov/ d' tox.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l duecredit

# Create man pages from --help and --version
mkdir man
%{py3_test_envvars} help2man --section 1 --no-discard-stderr \
--no-info --output man/duecredit.1 duecredit
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 man/duecredit.1 %{buildroot}%{_mandir}/man1

%check
# It’s not entirely clear why this fails here but not in a virtualenv. That
# makes it hard to usefully report upstream.
#
# ____________ test_noincorrect_import_if_no_lxml_numpy[kwargs1-env2] ____________
# duecredit/tests/test_api.py:229: in test_noincorrect_import_if_no_lxml_numpy
#     assert "For formatted output we need citeproc" in out + err
# E   assert 'For formatted output we need citeproc' in ('done123\n\nDueCredit
#         Report:\n  - Multivariate pattern analysis of neural data /
#         __main__:method (v None) [1]\n\n0 packages cited\n0 modules cited\n1
#         function cited\n\nReferences\n----------\n\n[1] ' + '2024-06-04
#         18:24:49,497 [WARNING] DueCredit internal failure while running
#         <function DueSwitch.dump at 0x7f0052cd4c20... name resolution\'))")).
#         Please report to developers at
#         https://github.com/duecredit/duecredit/issues (utils.py:211)\n')
k="${k-}${k+ and }not test_noincorrect_import_if_no_lxml_numpy[kwargs1-env2]"

%{pytest} duecredit/tests --ignore=duecredit/tests/test_io.py -rs -k "${k-}"

%files -n python3-duecredit -f %{pyproject_files}
%{_bindir}/duecredit
%{_mandir}/man1/duecredit.1*

%files doc
%license LICENSE
%doc examples/

%changelog
%autochangelog
