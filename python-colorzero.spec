%global srcname colorzero

Name:           python-%{srcname}
Version:        2.0
Release:        6%{?dist}
Summary:        Yet another Python color library

License:        BSD
URL:            https://github.com/waveform80/colorzero
Source0:        %{url}/archive/release-%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Colorzero is a color manipulation library for Python (yes, another one)
which aims to be reasonably simple to use and "pythonic" in nature.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-release-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files colorzero

%check
%{python3} -m pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.0-1
- Update to 2.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.1-4
- Use pyproject-rpm-macros in specfile

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.9

* Sun Apr 12 2020 Tomas Hrnciar <thrnciar@redhat.com> - 1.1-1
- Initial package
