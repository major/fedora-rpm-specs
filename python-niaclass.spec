%bcond_without tests

%global pypi_name niaclass
%global pretty_name NiaClass

%global _description %{expand:
NiaClass is a framework for solving classification tasks using nature-inspired
algorithms. The framework is written fully in Python. Its goal is to find the
best possible set of classification rules for the input data using the NiaPy
framework, which is a popular Python collection of nature-inspired algorithms.
The NiaClass classifier support numerical and categorical features.}

Name:           python-%{pypi_name}
Version:        0.1.4
Release:        1%{?dist}
Summary:        Python framework for building classifiers using nature-inspired algorithms

License:        MIT
URL:            https://github.com/lukapecnik/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires: %{py3_dist lockfile}
BuildRequires: %{py3_dist packaging}
BuildRequires: %{py3_dist pep517}
BuildRequires: %{py3_dist poetry}
BuildRequires:  %{py3_dist toml-adapt}

#For documentation
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

#tests
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version}
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo} -vf

%install
%pyproject_install
%pyproject_save_files niaclass

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/LICENSE
rm -rf %{buildroot}/%{python3_sitelib}/CHANGELOG.md

%check	
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CITATION.md

%files doc
%license LICENSE
%doc docs/_build/html
%doc examples/ CITATION.md

%changelog
* Tue Feb 7 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.4-1
- Update to the latest upstream's release

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 26 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.3-1
- Update to the latest upstream's release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 0.1.2-7
- Rebuilt for Python 3.11

* Mon Jan 24 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.2-6
- Remove dependency (pyproject-rpm-macros)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.2-2
- Minor corrections

* Mon Jun 28 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.2-1
- Update to the latest upstream's major release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.10

* Tue May 25 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.1-1
- Update to the latest upstream's release
- Remove patch

* Thu Apr 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.0-1
- Initial package
