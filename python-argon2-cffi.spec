Name:           python-argon2-cffi
Version:        21.3.0
Release:        %autorelease
Summary:        The secure Argon2 password hashing algorithm

License:        MIT
URL:            https://argon2-cffi.readthedocs.io/
Source:         %{pypi_source argon2-cffi}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
CFFI-based Argon2 Bindings for Python.}

%description %_description


%package -n     python3-argon2-cffi
Summary:        %{summary}

%description -n python3-argon2-cffi %_description


%prep
%autosetup -n argon2-cffi-%{version}
# don't BR coverage, we will not measure it
sed -Ei 's/"coverage[^"]+", //' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files argon2


%check
%pytest


%files -n python3-argon2-cffi -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
%autochangelog
