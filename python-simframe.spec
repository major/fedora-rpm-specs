%bcond_with tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.

# We do not generate docs, due to the missing dependencies
# sphinx-automodapi is missing
%bcond_with doc_pdf

%global pypi_name simframe

%global _description %{expand:
Simframe is a Python framework to facilitate scientific simulations.
The scope of the software is to provide a framework which can hold
data fields, which can be used to integrate differential equations,
and which can read and write data files.}

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        6%{?dist}
Summary:        Python framework for setting up and running scientific simulations
License:        BSD
URL:            https://github.com/stammler/%{pypi_name}
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif


%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation and examples for %{name}

%description doc
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# fix file permissions
find . -type f -perm /0111 -exec chmod -v a-x '{}' '+'

%generate_buildrequires
%pyproject_buildrequires -r %{?with_doc:docs/requirements.txt}

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%if %{with tests}
%check
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files doc
%doc README.md
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/%{pypi_name}.pdf
%endif
%doc examples/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.0.2-2
- Rebuilt for Python 3.11

* Wed Mar 30 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.0.2-1
- Update to the latest release
- Remove patch

* Tue Jan 18 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.0.1-1
- Initial package
