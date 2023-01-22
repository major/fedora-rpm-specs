# Created by pyp2rpm-3.3.2
%global pypi_name qtsass

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        6%{?dist}
Summary:        Compile SCSS files to valid Qt stylesheets

License:        MIT
URL:            https://github.com/spyder-ide/qtsass
Source0:        https://files.pythonhosted.org/packages/source/q/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

# fix py3.10 issues
# https://github.com/spyder-ide/qtsass/pull/54/commits
Patch0:         fix_tests_py310.patch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
SASS brings countless amazing features to CSS. Besides being used in web 
development, CSS is also the way to stylize Qt-based desktop applications. 
However, Qt's CSS has a few variations that prevent the direct use of 
SASS compiler. The purpose of this tool is to fill the gap between SASS 
and Qt-CSS by handling those variations.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(libsass)
Requires:       python3dist(setuptools)
Requires:       python3dist(watchdog)

%description -n python3-%{pypi_name}
SASS brings countless amazing features to CSS. Besides being used in web 
development, CSS is also the way to stylize Qt-based desktop applications. 
However, Qt's CSS has a few variations that prevent the direct use of 
SASS compiler. The purpose of this tool is to fill the gap between SASS 
and Qt-CSS by handling those variations.


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{_bindir}/qtsass
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 05 2021 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.9

* Sat Dec 21 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.1.1-1
- Initial package.
