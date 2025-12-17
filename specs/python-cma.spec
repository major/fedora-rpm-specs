%global srcname cma
Name:           python-cma
Version:        4.4.1
Release:        %autorelease
Summary:        Covariance Matrix Adaptation Evolution Strategy numerical optimizer

License:        BSD-3-Clause
URL:            https://cma-es.github.io/
Source0:        %{pypi_source}
Patch:          license.patch

BuildRequires:  python3-devel
BuildArch:      noarch

%global _description %{expand:
A stochastic numerical optimization algorithm for difficult (non-convex,
ill-conditioned, multi-modal, rugged, noisy) optimization problems in continuous
search spaces, implemented in Python.}

%description %_description

%package -n     python3-cma
Summary:        %{summary}

%description -n python3-cma %_description

%prep
%autosetup -n cma-%{version}
#Fix line-endings
sed -i 's/\r//' README.rst
#Remove unneeded shebang
sed -i '1d' cma/{bbobbenchmarks.py,purecma.py,test.py}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l cma

%files -n python3-cma -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
