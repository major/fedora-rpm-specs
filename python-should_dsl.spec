Summary:	Should assertions in Python in as clear and readable a way as possible
Name:		python-should_dsl
Version:	2.1.2
Release:	13%{?dist}
License:	MIT
URL:		https://github.com/nsi-iff/should-dsl
Source0:	https://files.pythonhosted.org/packages/source/s/should_dsl/should_dsl-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel

%global _description %{expand:
The goal of Should-DSL is to write should expectations in Python in as clear
and readable a way as possible, using "almost" natural language (limited -
sometimes - by the Python language constraints).}

%description %_description

%package -n python3-should_dsl
Summary:	Should assertions in Python in as clear and readable a way as possible

%description -n python3-should_dsl %_description

%prep
%setup -q -n should_dsl-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files should_dsl

%check
# run_all_examples.py references non-existent files and hence fails
%{py3_test_envvars} %{python3} run_examples.py README.rst

%files -n python3-should_dsl -f %{pyproject_files}
%license LICENSE
%doc CONTRIBUTORS README.rst

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.1.2-13
- Rebuilt for Python 3.12

* Mon Jun  5 2023 Paul Howarth <paul@city-fan.org> - 2.1.2-12
- SPDX license migration
- Update to current Python packaging guidelines, as far as possible

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 2.1.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Paul Howarth <paul@city-fan.org> - 2.1.2-1
- Initial RPM version
