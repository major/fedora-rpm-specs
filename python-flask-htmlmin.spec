%global desc Minify flask text/html mime types responses. Just add MINIFY_PAGE = True to \
your deployment config to minify html and text responses of your flask \
application.

%global pkg_name flask-htmlmin
%global mod_name Flask-HTMLmin

Name:       python-%{pkg_name}
Version:    2.2.1
Release:    5%{?dist}
Summary:    Flask html response minifier
License:    BSD
URL:        https://github.com/hamidfzm/%{mod_name}
Source0:    %{url}/archive/v%{version}/%{mod_name}-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  python%{python3_pkgversion}-htmlmin
BuildRequires:  python%{python3_pkgversion}-cssmin
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest

%description
%{desc}

%package -n python%{python3_pkgversion}-%{pkg_name}
Summary:    %{summary}
BuildRequires:   python%{python3_pkgversion}-flask

Requires:  python%{python3_pkgversion}-flask
Requires:  python%{python3_pkgversion}-htmlmin

%description -n python%{python3_pkgversion}-%{pkg_name}
%{desc}

%prep
%autosetup -n %{mod_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files flask_htmlmin

%check
%pytest

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 26 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.1-1
- Update to the latest release
- Remove pytest-runner dependency

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.2.0-6
- Rebuilt for Python 3.11

* Tue Mar 22 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.0-5
- Switch to GitHub Source0
- Enable tests

* Tue Mar 22 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.0-4
- Switch to pyproject-rpm-macros

* Tue Mar 22 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.0-3
- Remove obsolete macro

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.2.0-1
- Update to the latest release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.10

* Sat Mar 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.1.0-2
- Cosmetic changes

* Mon Mar 08 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.1.0-1
- New version - 2.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.0.2-1
- 2.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.0-3
- Subpackage python2-flask-htmlmin has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Aug 26 2018  Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.4.0-2
- include pytest-runner in builrequires

* Sun Aug 26 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.4.0-1
- 1.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.7

* Tue Mar 06 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.3.1-1
- Initial package
