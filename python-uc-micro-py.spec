Name:           python-uc-micro-py
Version:        1.0.1
Release:        2%{?dist}
Summary:        Micro subset of Unicode data files for linkify-it.py projects

License:        MIT
URL:            https://github.com/tsutsu3/uc.micro-py
Source0:        %{url}/archive/v%{version}/uc.micro-py-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Micro subset of Unicode data files for linkify-it.py projects.  This is
a Python port of uc.micro (https://github.com/markdown-it/uc.micro).}

%description %_description

%package     -n python3-uc-micro-py
Summary:        Micro subset of Unicode data files for linkify-it.py projects

%description -n python3-uc-micro-py %_description

%prep
%autosetup -n uc.micro-py-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files uc_micro

%check
%pytest

%files -n python3-uc-micro-py -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 1.0.1-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Initial RPM
