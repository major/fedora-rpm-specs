%global pkg_name jsonformatter

Name:           python-%{pkg_name}
Version:        0.3.4
Release:        2%{?dist}
Summary:        Formatter to output json logs

License:        BSD-2-Clause
URL:            https://github.com/MyColorfulDays/jsonformatter
BuildArch:      noarch
# PyPI source is incomplete
Source0:        https://github.com/MyColorfulDays/jsonformatter/archive/v%{version}/%{pkg_name}-%{version}.tar.gz


BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description
jsonformatter is a formatter for python to output json logs.


%package -n python3-%{pkg_name}
Summary:        Formatter to output json logs


%description -n python3-%{pkg_name}
jsonformatter is a formatter for python to output json logs.


%prep
%autosetup -p1 -n %{pkg_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pkg_name}


%check
%pytest


%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 23 2024 Sandro Mani <manisandro@gmail.com> - 0.3.4-1
- Update to 0.3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Sandro Mani <manisandro@gmail.com> - 0.3.2-4
- Add patch for python3.13 compatibility

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.13

* Sat Mar 09 2024 Sandro Mani <manisandro@gmail.com> - 0.3.2-2
- Cleanup leftovers, use %%pyproject_save_files -l %%{pkg_name}

* Fri Mar 08 2024 Sandro Mani <manisandro@gmail.com> - 0.3.2-1
- Initial package
