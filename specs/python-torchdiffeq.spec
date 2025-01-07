%global pypi_name torchdiffeq

Name:           python-%{pypi_name}
Version:        0.2.5
Release:        %autorelease
Summary:        Differentiable ODE solvers with full GPU support and O(1)-memory backpropagation

License:        MIT
URL:            https://github.com/rtqichen/%{pypi_name}
# No tags, need to look through the commit logs to find when the release changed
%global commit a88aac53cae738addee44251288ce5be9a018af3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source:         %{url}/archive/%{commit}/%{pypi_name}-%{shortcommit}.tar.gz

BuildArch:      noarch
ExclusiveArch:  x86_64 aarch64

BuildRequires:  python3-devel

%description 
This library provides ordinary differential equation (ODE) solvers
implemented in PyTorch. Backpropagation through ODE solutions is
supported using the adjoint method for constant memory cost. For
usage of ODE solvers in deep learning applications.

As the solvers are implemented in PyTorch, algorithms in this
repository are fully supported to run on the GPU.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This library provides ordinary differential equation (ODE) solvers
implemented in PyTorch. Backpropagation through ODE solutions is
supported using the adjoint method for constant memory cost. For
usage of ODE solvers in deep learning applications.

As the solvers are implemented in PyTorch, algorithms in this
repository are fully supported to run on the GPU.

%prep
%autosetup -p1 -n %{pypi_name}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
# No pytests, need to use run_all.py script
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitelib}/%{pypi_name}
%__python3 tests/run_all.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%doc examples
%doc FURTHER_DOCUMENTATION.md
%doc FAQ.md

%changelog
%autochangelog
