%global proj_name gbinder-python

Name:           python-gbinder
Version:        1.1.2
Release:        7%{?dist}
Summary:        Python bindings for libgbinder

License:        GPL-3.0-only
URL:            https://github.com/erfanoabdi/%{proj_name}
Source:         %{url}/archive/%{version}/%{proj_name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.2-5
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Alessandro Astone <ales.astone@gmail.com> - 1.1.2-4
- Drop i686 support (leaf package)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 16 2023 Alessandro Astone <ales.astone@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 21 2023 Alessandro Astone <ales.astone@gmail.com> - 1.1.1-5
- Avoid building against Cython 3

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Alessandro Astone <ales.astone@gmail.com> - 1.1.1-2
- Re-enable s390x builds

* Sun Oct 30 2022 Alessandro Astone <ales.astone@gmail.com> - 1.1.1-1
- Initial changelog
