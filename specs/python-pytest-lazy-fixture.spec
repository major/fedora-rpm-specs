# Enabled by default
%bcond_without tests

Name:           python-pytest-lazy-fixture
Version:        0.6.3
Release:        %autorelease
Summary:        Use fixtures in pytest.mark.parametrize

# spdx
License:        MIT
URL:            https://github.com/tvorog/pytest-lazy-fixture
Source0:        %{pypi_source pytest-lazy-fixture}

# Minimal patch for compatibility with pytest 8.
# Downstream only patch, upstream seems dead.
# https://github.com/TvoroG/pytest-lazy-fixture/issues/65#issuecomment-1915829980
Patch:          Minimal-patch-for-compatibility-with-pytest-8.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Use fixtures in pytest.mark.parametrize.}

%description %_description

%package -n python3-pytest-lazy-fixture
Summary:        %{summary}

%description -n python3-pytest-lazy-fixture %_description

%prep
%autosetup -n pytest-lazy-fixture-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_lazyfixture

%check
%if %{with tests}
%pytest
%endif

%files -n python3-pytest-lazy-fixture -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
