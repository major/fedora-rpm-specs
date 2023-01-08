%global proj_name gbinder-python

Name:           python-gbinder
Version:        1.1.1
Release:        2%{?dist}
Summary:        Python bindings for libgbinder

License:        GPL-3.0-only
URL:            https://github.com/erfanoabdi/%{proj_name}
Source:         %{url}/archive/%{version}/%{proj_name}-%{version}.tar.gz

%global libgbinder_version 1.1.20
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  gcc
BuildRequires:  pkgconfig(libgbinder) >= %{libgbinder_version}

%global _description %{expand:
Cython extension module for libgbinder.
Provides IPC comunication over the /dev/binder protocol for python scripts.}

%description %{_description}

%package -n python3-gbinder
Summary:        %{summary}
Requires:       libgbinder >= %{libgbinder_version}

%description -n python3-gbinder %{_description}

%prep
%autosetup -p1 -n %{proj_name}-%{version}
sed -i "/^USE_CYTHON =/s/False/True/" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gbinder

%files -n python3-gbinder -f %{pyproject_files}

%changelog
* Fri Jan 06 2023 Alessandro Astone <ales.astone@gmail.com> - 1.1.1-2
- Re-enable s390x builds

* Sun Oct 30 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.1-1
- Initial changelog
