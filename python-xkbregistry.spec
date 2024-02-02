Name:           python-xkbregistry
Version:        0.3
Release:        %autorelease
Summary:        Bindings for libxkbregistry using cffi

License:        MIT
URL:            https://github.com/sde1000/python-xkbregistry
Source:         %{pypi_source xkbregistry}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  libxkbcommon-devel

Requires:  libxkbcommon


%global _description %{expand:
Python bindings for libxkbregistry using cffi.}


%description %_description

%package -n     python3-xkbregistry
Summary:        %{summary}

%description -n python3-xkbregistry %_description


%prep
%autosetup -n xkbregistry-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%python3 xkbregistry/ffi_build.py


%install
%pyproject_install
%pyproject_save_files xkbregistry


%check
%pyproject_check_import -t
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-xkbregistry -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
