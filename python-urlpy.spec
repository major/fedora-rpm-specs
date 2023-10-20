%global pypi_name urlpy

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        %autorelease
Summary:        URL Transformation, Sanitization

License:        MIT
URL:            https://github.com/nexB/urlpy
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# Remove useless shebang lines
# https://github.com/nexB/urlpy/pull/12
Patch:          %url/pull/12.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global common_description %{expand:
urlpy is a small library for URL parsing, cleanup, canonicalization and
equivalence.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires requirements-tests.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# https://github.com/nexB/urlpy/issues/11
%pytest -k "not test_unknown_protocol"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
