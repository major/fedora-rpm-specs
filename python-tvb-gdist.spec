%global pypi_name tvb-gdist
%global module_name tvb_gdist

%global desc %{expand: \
The Virtual Brain Project (TVB Project) has the purpose of offering some modern
tools to the Neurosciences community, for computing, simulating and analyzing
functional and structural data of human brains.

The gdist module is a Cython interface to a C++ library
(http://code.google.com/p/geodesic/) for computing geodesic distance which is
the length of shortest line between two vertices on a triangulated mesh in
three dimensions, such that the line lies on the surface.

The algorithm is due Mitchell, Mount and Papadimitriou, 1987; the
implementation is due to Danil Kirsanov and the Cython interface to Gaurav
Malhotra and Stuart Knock.

Original library (published under MIT license):
http://code.google.com/p/geodesic/

We added a python wrapped and made small fixes to the original library, to make
it compatible with cython.
}

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        7%{?dist}
Summary:        Cython interface to geodesic

License:        GPLv3+
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source %{pypi_name}

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  gcc-c++

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
# They delete the build folder for some reason
sed -i '/rmtree/ d' setup.py

rm -rf %{module_name}.egg-info

# Set cython language level
sed -i '2 a # cython: language_level=3' gdist.pyx


%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{module_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/gdist.cpython-*.so

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.1.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.1.0-1
- Update to 2.1.0

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.2-1
- Update to new release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.9

* Sat May 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.1-1
- Update to latest release

* Sun Feb 02 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-1
- Update to latest release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.8-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.8-1
- Update to 1.5.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-3
- Update license to GPLv3+

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-2
- add setuptools BR
- remove empty check section

* Sat Dec 29 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.6-1
- Initial build
