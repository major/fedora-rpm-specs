Name:           python-jaraco-path
Version:        3.3.1
Release:        7%{?dist}
Summary:        Miscellaneous path functions

License:        MIT
URL:            https://github.com/jaraco/jaraco.path
Source0:        https://github.com/jaraco/jaraco.path/archive/v%{version}/jaraco.path-%{version}.tar.gz
# We do not have a correct version of singledispatch in Fedora that jaraco.path needs.
# Instead of backporting and updating singledispatch it is better to not to use
# it at all and use functools from the standard library with Python 3.7 and higher.
# Upstream PR: https://github.com/jaraco/jaraco.path/pull/1
Patch1:         https://github.com/jaraco/jaraco.path/pull/1.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-41
BuildRequires:  pytest

%global _description %{expand:
jaraco.path provides cross platform hidden file detection}

%description %_description

%package -n     python3-jaraco-path
Summary:        %{summary}
Requires:       python3-jaraco

%description -n python3-jaraco-path %_description

%prep
%autosetup -p1 -n jaraco.path-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jaraco

%check
%pytest

%files -n python3-jaraco-path -f %{pyproject_files}
%license LICENSE
%doc README.rst
%exclude %dir %{python3_sitelib}/jaraco
%exclude %dir %{python3_sitelib}/jaraco/__pycache__
%pycached %exclude %{python3_sitelib}/jaraco/__init__.py

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.1-2
- Rebuilt for Python 3.10

* Tue Mar 02 2021 Tomas Hrnciar <thrnciar@redhat.com> - 3.3.1-1
- Initial package
