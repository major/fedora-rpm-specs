Name:           python-throttler
Version:        1.2.2
Release:        %autorelease
Summary:        Easy throttling with asyncio support

# SPDX
License:        MIT
URL:            https://github.com/uburuntu/throttler
# GitHub archive contains tests and examples; PyPI sdist does not
Source:         %{url}/archive/v%{version}/throttler-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# Run tests in parallel; this speeds up the build quite a bit.
BuildRequires:  python3dist(pytest-xdist)

%global common_description %{expand:
Zero-dependency Python package for easy throttling with asyncio support.}

%description %{common_description}


%package -n python3-throttler
Summary:        %{summary}

%description -n python3-throttler %{common_description}


%prep
%autosetup -n throttler-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^(codecov|flake8|pytest-cov)/# &/' requirements-dev.txt


%generate_buildrequires
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l throttler


%check
%pytest -n auto -v


%files -n python3-throttler -f %{pyproject_files}
%doc examples/


%changelog
%autochangelog
