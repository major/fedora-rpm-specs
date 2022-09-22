%global pypi_name Nik4

Name:		nik4
Version:	1.6.0
Release:	19%{?dist}
Summary:	Command-line interface to a Mapnik rendering toolkit

License:	WTFPL
URL:		https://github.com/Zverik/Nik4
Source0:	https://files.pythonhosted.org/packages/source/N/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

# We cannot provide the Python 3 version for F23 since there is only a
# Python 2 version of the Python mapnik bindings available
%if 0%{?fedora} >= 24
Requires:	python3-mapnik
%else
Requires:	mapnik-python
%endif

%if 0%{?fedora} >= 24
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
%else
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
%endif

%description
Nik4 is a mapnik-to-image exporting script.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%if 0%{?fedora} >= 24
%py3_build
%else
%py2_build
%endif

%install
%if 0%{?fedora} >= 24
%py3_install
%else
%py2_install
%endif

mv %{buildroot}/%{_bindir}/nik4.py %{buildroot}/%{_bindir}/nik4

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/nik4
%if 0%{?fedora} >= 24
%{python3_sitelib}/*
%else
%{python2_sitelib}/*
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.0-18
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.6.0-15
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-12
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-10
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-6
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2
- Rebuild for Python 3.6

* Sat Jul 09 2016 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 1.6.0-1
- Initial packaging
