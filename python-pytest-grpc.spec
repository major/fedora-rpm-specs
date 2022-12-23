# Upstream publishes to PyPI but does not tag releases. This commit includes
# the LICENSE file.
%global commit 3f21554fd821074c2836f65078eaace5c0569c2a
%global snapdate 20210806

Name:           python-pytest-grpc
Version:        0.8.0^%{snapdate}git%(echo '%{commit}' | cut -b -7)
Release:        %autorelease
Summary:        Allow testing gRPC with pytest

# SPDX
License:        MIT
URL:            https://github.com/kataev/pytest-grpc
Source0:        %{url}/archive/%{commit}/pytest-grpc-%{commit}.tar.gz

BuildArch:      noarch
 
BuildRequires:  python3-devel

# Not specified in setup.py metadata, but required for tests:
BuildRequires:  python3dist(grpcio)

%global common_description %{expand:
Write tests for gRPC with pytest.}

%description %{common_description}


%package -n     python3-pytest-grpc
Summary:        %{summary}

# Not specified in setup.py metadata, but required for any practical use:
Requires:       python3dist(grpcio)

%description -n python3-pytest-grpc %{common_description}


%prep
%autosetup -n pytest-grpc-%{commit}
# We do not want or need to install this zero-length hidden file, which is
# present upstream so that git will preserve the directory.
rm -vf example/src/stub/.keepdir


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_grpc


%check
# Upstream has no tests.
%pyproject_check_import


%files -n python3-pytest-grpc -f %{pyproject_files}
%doc README.md
%doc example/


%changelog
%autochangelog
