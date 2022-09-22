%global pkgname click-help-colors

Name:           python-click-help-colors
Version:        0.9.1
Release:        4%{?dist}
Summary:        Colorization of help messages in Click
License:        MIT
URL:            https://github.com/click-contrib/click-help-colors
Source0:        %{url}/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires: python3-click
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools

%{?python_enable_dependency_generator}

%description
Colorization of help messages in Click


%package -n python3-%{pkgname}
Summary:        %{summary}

%description -n python3-%{pkgname}
Colorization of help messages in Click

%prep
%autosetup -n %{pkgname}-%{version}

%build
%{py3_build}

%install
%{py3_install}

%check
py.test-3 -vv

%files -n python3-%{pkgname}
%license LICENSE.txt
%doc examples README.rst
%{python3_sitelib}/click_help_colors*/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.9.1-1
- Update to version 0.9.1 (#1986612)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Lumír Balhar <lbalhar@redhat.com> - 0.9-1
- Update to 0.9

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-2
- Rebuilt for Python 3.9

* Mon Apr 6 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.8-1
- initial package
