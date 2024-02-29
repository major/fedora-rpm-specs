# We must use a GitHub snapshot because the PyPI sdist lacks the LICENSE file
# (https://github.com/MobileDynasty/pytest-env/issues/6) and releases are not
# tagged on GitHub.
%global commit afb13a0e908f649b69273f299262ac12f1b71113
%global snapdate 20170617

Name:           python-pytest-env
Version:        0.6.2^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Plugin for pytest that allows you to add environment variables

# SPDX
License:        MIT
URL:            https://github.com/MobileDynasty/pytest-env
Source:         %{url}/archive/%{commit}/pytest-env-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
This is a py.test plugin that enables you to set environment variables in the
pytest.ini file.}

%description %{common_description}


%package -n     python3-pytest-env
Summary:        %{summary}

%description -n python3-pytest-env %{common_description}


%prep
%autosetup -n pytest-env-%{commit}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pytest_env


%check
# Upstream has no tests.
%pyproject_check_import


%files -n python3-pytest-env -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
