%global modname h5io

Name:           python-%{modname}
Version:        0.1.2
Release:        11%{?dist}
Summary:        Read and write simple Python objects using HDF5

License:        BSD
URL:            https://github.com/h5io/h5io
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
h5io is a package designed to facilitate saving some standard Python objects
into the forward-compatible HDF5 format.
It is a higher-level package than h5py.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
Requires:       python%{python3_version}dist(numpy)
Requires:       python%{python3_version}dist(h5py)
Recommends:     python%{python3_version}dist(scipy)

%description -n python3-%{modname}
h5io is a package designed to facilitate saving some standard Python objects
into the forward-compatible HDF5 format.
It is a higher-level package than h5py.

Python 3 version.

%prep
%autosetup -n %{modname}-%{modname}-%{version}

%build
%py3_build

%install
%py3_install

%check
pytest-%{python3_version} -v

%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{modname}*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.1.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-3
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.1.2-2
- Added dist to release tag

* Wed Apr 29 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.1.2-1
- Version update to v0.1.2
- Use pytest instead of nose

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8.git1a1849d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-7.git1a1849d
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-6.git1a1849d
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5.git1a1849d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4.git1a1849d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-3.git1a1849d
- Subpackage python2-h5io has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2.git1a1849d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1.git1a1849d
- Update to latest snapshot

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.10.gita73bba4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.gita73bba4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.8.gita73bba4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.7.gita73bba4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-0.6.gita73bba4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.gita73bba4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.gita73bba4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1-0.3.git173bba4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1-0.2.gita73bba4
- Massage versioning a bit

* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1-0.1.gita73bba4
- Initial package
