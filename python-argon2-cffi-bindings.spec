Name:           python-argon2-cffi-bindings
Version:        21.2.0
Release:        %autorelease
Summary:        Low-level CFFI bindings for Argon2

License:        MIT
URL:            https://github.com/hynek/argon2-cffi-bindings
Source:         %{pypi_source argon2-cffi-bindings}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(libargon2)


%global _description %{expand:
This package provides low-level CFFI bindings to the Argon2 password hashing
algorithm.

If you want to hash passwords in an application,
this package is not for you.
Have a look at argon2-cffi with its high-level abstractions!

These bindings have been extracted from argon2-cffi and it remains its main
consumer. However, they may be used by other packages that want to use the
Argon2 library without dealing with C-related complexities.}


%description %_description

%package -n     python3-argon2-cffi-bindings
Summary:        %{summary}

%description -n python3-argon2-cffi-bindings %_description


%prep
%autosetup -p1 -n argon2-cffi-bindings-%{version}
# using system libargon
rm -r extras/libargon2


%generate_buildrequires
export ARGON2_CFFI_USE_SYSTEM=1
%pyproject_buildrequires -x tests


%build
export ARGON2_CFFI_USE_SYSTEM=1
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files _argon2_cffi_bindings


%check
%pytest -v

%files -n python3-argon2-cffi-bindings -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog
