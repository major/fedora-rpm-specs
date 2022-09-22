%global modname aiofiles

Name:           python-%{modname}
Version:        0.7.0
Release:        5%{?dist}
Summary:        File support for asyncio

License:        ASL 2.0
URL:            https://github.com/Tinche/aiofiles
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# For tests, from pyproject.toml [tool.poetry.dev-dependencies]:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
# We do not require coverage and tox simply to run pytest.

%global _description \
aiofiles is an Apache2 licensed library, written in Python, for handling\
local disk files in asyncio applications.

%description %{_description}

%generate_buildrequires
%pyproject_buildrequires -r

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %{_description}

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.7.0-1
- Update to 0.7.0 (fix RHBZ#1823140); this release adds Python 3.10 support
  (fixes RHBZ#1906349)
- Switch to pyproject-rpm-macros, since upstream has replaced setup.py with
  pyproject.toml
- Drop obsolete %%python_provide macro

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.10

* Sun Apr 11 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-1
- Update to 0.6.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-2
- Enable python dependency generator

* Mon Sep 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
