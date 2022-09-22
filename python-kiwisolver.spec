%global srcname kiwisolver

Name:           python-%{srcname}
Version:        1.4.4
Release:        %autorelease
Summary:        A fast implementation of the Cassowary constraint solver

License:        BSD
URL:            https://github.com/nucleic/kiwi
Source0:        %pypi_source

%global _description \
Kiwi is an efficient C++ implementation of the Cassowary constraint solving \
algorithm. Kiwi is an implementation of the algorithm based on the seminal \
Cassowary paper. It is *not* a refactoring of the original C++ solver. Kiwi has \
been designed from the ground up to be lightweight and fast.

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} py/tests/

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
