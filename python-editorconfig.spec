# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

# The tests are stored in a separate repository, which is normally accessed
# as a git submodule.
%global tests_commit e407c1592df0f8e91664835324dea85146f20189

Name:           python-editorconfig
Version:        0.12.4
Release:        %autorelease
Summary:        EditorConfig File Locator and Interpreter for Python

# See COPYING: the overall license is BSD-2-Clause, but the following files are derived
# from the Python standard library under the PSF-2.0 license:
#   - editorconfig/fnmatch.py
#   - editorconfig/ini.py
License:        BSD-2-Clause AND PSF-2.0
URL:            https://github.com/editorconfig/editorconfig-core-py
Source0:        %{url}/archive/v%{version}/editorconfig-core-py-%{version}.tar.gz
%global tests_url https://github.com/editorconfig/editorconfig-core-test
Source1:        %{tests_url}/archive/%{tests_commit}/editorconfig-core-test-%{tests_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# For tests:
BuildRequires:  cmake

BuildRequires:  make
BuildRequires:  python3dist(sphinx)
%if %{with doc_pdf}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
EditorConfig Python Core provides the same functionality as the EditorConfig C
Core.}

%description %{common_description}


%package     -n python3-editorconfig
Summary:        %{summary}

%description -n python3-editorconfig %{common_description}


%package        doc
Summary:        Documentation for python-editorconfig

%description    doc %{common_description}


%prep
%setup -q -n editorconfig-core-py-%{version}

rm -vrf tests
%setup -q -n editorconfig-core-py-%{version} -T -D -b 1
mv ../editorconfig-core-test-%{tests_commit}/ tests/


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%make_build -C docs text SPHINXOPTS='-j%{?_smp_build_ncpus}'
%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%cmake -DPYTHON_EXECUTABLE='%{python3}'

%install
%pyproject_install
%pyproject_save_files -l editorconfig

# The command-line tool would conflict with the one from the C version of
# EditorConfig. It could be installed under a different name, if anyone ever
# reports a need for it.
rm -vf '%{buildroot}%{_bindir}/editorconfig'


%check
export %{py3_test_envvars}
%ctest


%files -n python3-editorconfig -f %{pyproject_files}
%doc README.rst


%files doc
%license COPYING LICENSE.BSD LICENSE.PSF
%doc README.rst
%doc docs/_build/text/
%if %{with doc_pdf}
%doc docs/_build/latex/EditorConfigPythonCore.pdf
%endif


%changelog
%autochangelog
