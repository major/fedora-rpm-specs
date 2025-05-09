# Shall we re-generate the code using jschema-to-python? The Fedora guidelines
# suggest but do not require that we do so.
%bcond regenerate 1

Name:           python-sarif-om
Summary:        Classes implementing the SARIF 2.1.0 object model
Version:        1.0.4
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/microsoft/sarif-python-om
Source:         %{pypi_source sarif_om}

# Fix deprecated dash-separated names in setup.cfg
# https://github.com/microsoft/sarif-python-om/pull/7
# Rebased on the released PyPI sdist (with different whitespace in setup.cfg)
Patch:          sarif_om-1.0.4-setuptools-deprecations.patch

BuildSystem:            pyproject
BuildOption(install):   -l sarif_om

BuildArch:      noarch

%if %{with regenerate}
BuildRequires:  %{py3_dist jschema-to-python}
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


%prep -a
%if %{with regenerate}
rm -rf sarif_om
%endif
# Fix CRNL line termination
find . -type f -exec dos2unix --keepdate '{}' '+'


%build -p
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


# Upstream does not provide any tests


%files -n python3-sarif-om -f %{pyproject_files}
%doc README.rst
%doc SECURITY.md


%changelog
%autochangelog
