%global srcname pymoc
%global sum Multi-Order Coverage map module for Python
%global desc PyMOC is a module for manipulating Multi-Order Coverage (MOC) maps. \
It includes support for reading and writing the three encodings mentioned in     \
the IVOA recommendation: FITS, JSON and ASCII.                                   \
                                                                                 \
PyMOC also includes a utility program pymoctool to allow MOC files to be         \
manipulated from the command line.

# Is a noarch package in reality, see below, therefore: no debuginfo
%global debug_package %{nil}


Name:           python-%{srcname}
Version:        0.5.0
Release:        22%{?dist}
Summary:        %{sum}

License:        GPLv3+
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

# Cannot build as noarch because healpy does not support 32 bit architectures
# and we need that to execute tests. At runtime healpy is optional though,
# thereforce subpackages are noarch
ExclusiveArch:  aarch64 ppc64 ppc64le x86_64 s390x
# Also explicitly exclude known unsupported architectures
ExcludeArch:    %{ix86} %{arm}

# Python3
BuildRequires:  python3-astropy
BuildRequires:  python3-devel
BuildRequires:  python3-healpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildArch:      noarch
Requires:       python3-astropy
Recommends:     python3-healpy
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m unittest discover

%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/pymoctool

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.5.0-21
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.5.0-9
- drop python2 subpackage (#1628776)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-7
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.5.0-6
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Christian Dersch <lupinix@mailbox.org> - 0.5.0-2
- have to make the package ExclusiveArch limited to healpy arches (to run tests)

* Thu Jun 01 2017 Christian Dersch <lupinix@mailbox.org> - 0.5.0-1
- new version

* Thu Apr 20 2017 Christian Dersch <lupinix@mailbox.org> - 0.4.2-1
- initial package

