Name:          python-allpairspy
Version:       2.5.1
Release:       3%{?dist}
Summary:       Pairwise test combinations generator

License:       MIT
URL:           https://github.com/thombashi/allpairspy
Source0:       %{pypi_source allpairspy}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-allpairspy
Summary:        %{summary}

%description -n python3-allpairspy
%{summary}.

%prep
%setup -q -n allpairspy-%{version}
rm -rf allpairspy.egg-info


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l allpairspy


%check
%{pytest}


%files -n python3-allpairspy -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.5.1-2
- Rebuilt for Python 3.14

* Fri Apr 11 2025 Jonny Heggheim <hegjon@gmail.com> - 2.5.1-1
- Updated to version 2.5.1

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.5.0-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.5.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Jonny Heggheim <hegjon@gmail.com> - 2.5.0-7
- Added missing BuildRequires for python3-setuptools
  Fixes rhbz#2142044

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.5.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.5.0-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Jonny Heggheim <hegjon@gmail.com> - 2.5.0-1
- Initial package
