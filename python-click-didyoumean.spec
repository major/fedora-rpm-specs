# Created by pyp2rpm-3.3.4
%global pypi_name click-didyoumean

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        5%{?dist}
Summary:        Enable git-like did-you-mean feature in click

License:        MIT
URL:            https://github.com/timofurrer/click-didyoumean
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files click_didyoumean

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.11

* Wed May 11 2022 František Zatloukal <fzatlouk@redhat.com> - 0.3.0-1
- Update to 0.3.0
- Switch to pyproject

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 František Zatloukal <fzatlouk@redhat.com> - 0.0.3-1
- Initial package.
