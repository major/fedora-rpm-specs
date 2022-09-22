# Shall we re-generate the code using jschema-to-python? The Fedora guidelines
# suggest but do not require that we do so.
%bcond_without regenerate

Name:           python-sarif-om
Summary:        Classes implementing the SARIF 2.1.0 object model
Version:        1.0.4
Release:        %autorelease

License:        MIT
URL:            https://github.com/microsoft/sarif-python-om
Source0:        %{pypi_source sarif_om}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with regenerate}
BuildRequires:  python3dist(jschema-to-python)
%endif
BuildRequires:  dos2unix

%global common_description %{expand:
This module contains classes for the object model defined by the Static
Analysis Results Interchange Format (SARIF) Version 2.1.0 file format, an OASIS
Committee Specification.

To learn more about SARIF and find resources for working with it, you can visit
the SARIF Home Page (https://sarifweb.azurewebsites.net/).}

%description %{common_description}


%package -n     python3-sarif-om
Summary:        %{summary}

%description -n python3-sarif-om %{common_description}


%prep
%autosetup -n sarif_om-%{version}
%if %{with regenerate}
rm -rf sarif_om
%endif
# Fix CRNL line termination
find . -type f -exec dos2unix '{}' '+'


%generate_buildrequires
%pyproject_buildrequires -r


%build
%if %{with regenerate}
# See the “Generation” section in README.rst.
%{python3} -m jschema_to_python \
    --schema-path sarif-2.1.0-rtm.4.json \
    --module-name sarif_om \
    --output-directory sarif_om \
    --root-class-name SarifLog \
    --hints-file-path code-gen-hints.json \
    --force \
    -vv
%endif
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sarif_om


%check
# Upstream does not provide any tests
%pyproject_check_import


%files -n python3-sarif-om -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE; verify with “rpm -qL -p …”
%doc CODE_OF_CONDUCT.md
%doc README.rst
%doc SECURITY.md


%changelog
%autochangelog
