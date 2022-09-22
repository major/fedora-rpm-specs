%global pypi_name restview

Name:           %{pypi_name}
Version:        2.9.2
Release:        10%{?dist}
Summary:        ReStructuredText viewer

License:        GPLv3+
URL:            https://mg.pov.lt/restview/
Source0:        %{pypi_source}

# Support mock >= 4 and unittest.mock on new Python
# https://github.com/mgedmin/restview/commit/a1ded30a87
# Merged upstream in 2.9.3
Patch1:         newmock.patch

# Use unittest.mock instead of deprecated mock
# Proposed upstream
# https://github.com/mgedmin/restview/pull/62
Patch2:         nomock.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  python3-readme-renderer
BuildRequires:  python3-setuptools

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
A viewer for ReStructuredText documents that renders them on the fly. Pass
the name of a ReStructuredText document to restview, and it will launch a
web server on localhost:random-port and open a web browser. Every time you
reload the page, restview will reload the document from disk and render it.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A library for ReStructuredText documents that renders them.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.9.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Miro Hrončok <mhroncok@redhat.com> - 2.9.2-8
- Use unittest.mock instead of deprecated mock

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.9.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9.2-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.2-1
- Initial package for Fedora
