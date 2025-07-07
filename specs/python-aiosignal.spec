Name:           python-aiosignal
Version:        1.4.0
Release:        %autorelease
Summary:        List of registered asynchronous callbacks

License:        Apache-2.0
URL:            https://github.com/aio-libs/aiosignal
Source:         %{pypi_source aiosignal}

# Downstream-only: do not fail on warnings
# This is too strict for downstream packaging.
Patch:          0001-Downstream-only-patch-out-coverage-options.patch
# Downstream-only: patch out coverage options
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0002-Downstream-only-do-not-fail-on-warnings.patch

BuildSystem:            pyproject
BuildOption(install):   -l aiosignal

BuildArch:      noarch

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%global common_description %{expand:
A project to manage callbacks in asyncio projects.}

%description %{common_description}


%package -n python3-aiosignal
Summary:        %{summary}

Obsoletes:      python-aiosignal-doc < 1.3.1-15

%description -n python3-aiosignal %{common_description}


%check -a
%pytest


%files -n python3-aiosignal -f %{pyproject_files}
%doc CHANGES.rst
%doc CONTRIBUTORS.txt
%doc README.rst


%changelog
%autochangelog
