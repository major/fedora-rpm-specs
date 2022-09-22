Name:           python-wcag-contrast-ratio
Version:        0.9
Release:        4%{?dist}
Summary:        A library for computing contrast ratios, as required by WCAG 2.0
License:        MIT
URL:            https://github.com/gsnedders/wcag-contrast-ratio
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
A library for computing contrast ratios, as required by WCAG 2.0.}


%description %_description

%package -n     python3-wcag-contrast-ratio
Summary:        %{summary}

%description -n python3-wcag-contrast-ratio %_description


%prep
%autosetup -p1 -n wcag-contrast-ratio-%{version}

# - functionality of hypothesis-pytest is now included into hypothesis
# - let our tox set the correct path to py.test
# both issues reported: https://github.com/gsnedders/wcag-contrast-ratio/pull/5
sed -i 's/hypothesis-pytest/hypothesis/g' tox.ini
sed -i 's/{envbindir}\/py.test/py.test/g' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files wcag_contrast_ratio


%check
%tox


%files -n python3-wcag-contrast-ratio -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Karolina Surma <ksurma@redhat.com> - 0.9-1
- Initial package
