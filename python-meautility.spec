%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%global pypi_name meautility
%global pretty_name MEAutility

%global _description %{expand:
Python package for multi-electrode array (MEA) handling and stimulation.
Documentation is available at https://meautility.readthedocs.io/}

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        %autorelease
Summary:        Package for multi-electrode array (MEA) handling and stimulation

License:        GPLv3
URL:            https://github.com/alejoe91/%{pretty_name}/
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%package        doc
Summary:        Documentation for %{pretty_name}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description doc %_description

%prep
%autosetup -n %{pretty_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}:${PWD}/MEAutility" \
    %make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files -l %{pretty_name}

%check
%if %{with tests}
%{pytest}
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitelib}/MEAutility/tests

%files doc
%license LICENSE
%doc notebooks
%if %{with doc_pdf}
%doc docs/build/latex/MEAutility.pdf
%endif

%changelog
%autochangelog
