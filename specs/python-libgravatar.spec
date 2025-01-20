Name:           python-libgravatar
Version:        1.0.4
Release:        4%{?dist}
Summary:        Python interface for the Gravatar APIs

License:        GPL-3.0-or-later
URL:            https://github.com/pabluk/libgravatar
BuildArch:      noarch
# PyPI source is incomplete
Source0:        %{pypi_source libgravatar}

BuildRequires:  python3-devel


%description
Python interface for the Gravatar API.


%package -n python3-libgravatar
Summary:        Python 3 interface for the Gravatar API


%description -n python3-libgravatar
Python 3 interface for the Gravatar API.


%prep
%autosetup -p1 -n libgravatar-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l libgravatar


%check
%py3_check_import libgravatar


%files -n python3-libgravatar -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0.4-2
- Rebuilt for Python 3.13

* Sat May 11 2024 Sandro Mani <manisandro@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Tue May 07 2024 Sandro Mani <manisandro@gmail.com> - 1.0.3-1
- Initial package
