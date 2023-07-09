%global srcname jupyter-kernel-test
%global srcname_ jupyter_kernel_test

Name:           python-%{srcname}
Version:        0.5.0
Release:        %autorelease
Summary:        Machinery for testing Jupyter kernels via the messaging protocol

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
jupyter_kernel_test is a tool for testing Jupyter kernels. It tests kernels for
successful code execution and conformance with the Jupyter Messaging Protocol
(currently 5.0).

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
jupyter_kernel_test is a tool for testing Jupyter kernels. It tests kernels for
successful code execution and conformance with the Jupyter Messaging Protocol
(currently 5.0).

%generate_buildrequires
%pyproject_buildrequires -w -x test

%prep
%autosetup -n %{srcname_}-%{version} -p1
sed -i -e '/"pre-commit"/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname_}

%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    %{python3} -m unittest -v

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
