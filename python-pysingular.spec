Name:           python-pysingular
Version:        0.9.7
Release:        12%{?dist}
Summary:        Python interface to Singular

License:        GPLv2+
URL:            https://github.com/sebasguts/PySingular
Source0:        %{url}/archive/v%{version}/PySingular-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Singular)
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}

%global _description %{expand:
This package contains a basic interface to call Singular from python.
It is meant to be used in the Jupyter interface to Singular.}

%description %_description

%package     -n python3-pysingular
Summary:        Python 3 interface to Singular

%description -n python3-pysingular %_description

%prep
%autosetup -n PySingular-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files PySingular

%check
%pyproject_check_import

%files -n python3-pysingular -f %{pyproject_files}
%doc README
%license GPLv2

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.7-11
- Rebuilt for Python 3.11

* Mon Mar 21 2022 Jerry James <loganjerry@gmail.com> - 0.9.7-10
- Rebuild for Singular 4.2.1p3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 0.9.7-7
- Rebuild for Singular 4.2.0p2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.7-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 0.9.7-1
- Initial RPM
