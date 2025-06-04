%bcond tests 1

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

%global pypi_name meautility
%global pretty_name MEAutility

Name:           python-%{pypi_name}
Version:        1.5.3
Release:        %autorelease
Summary:        Package for multi-electrode array (MEA) handling and stimulation

%global forgeurl https://github.com/alejoe91/MEAutility
%global tag %{version}
%forgemeta

License:        GPL-3.0-only
URL:            %forgeurl
Source:         %forgesource
# Upstream switched to pyproject.toml but declared a wrong license (MIT).
# The shipped license is GPL-3.0-only as before.
# https://github.com/alejoe91/MEAutility/pull/47
Patch:          https://github.com/alejoe91/MEAutility/pull/47.patch

BuildArch:      noarch

%global _description %{expand:
Python package for multi-electrode array (MEA) handling and stimulation.
Documentation is available at:
https://meautility.readthedocs.io/}

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
%forgeautosetup -p1

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

%files doc
%license LICENSE
%doc notebooks
%if %{with doc_pdf}
%doc docs/build/latex/MEAutility.pdf
%endif

%changelog
%autochangelog
