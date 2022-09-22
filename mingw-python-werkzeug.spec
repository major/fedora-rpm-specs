%{?mingw_package_header}

%global pkgname werkzeug
%global pypi_name Werkzeug

Name:          mingw-python-%{pkgname}
Summary:       MinGW Windows Python %{pkgname} library
Version:       2.2.2
Release:       1%{?dist}
BuildArch:     noarch

# Code is BSD, bundled icons are CC-BY
License:       BSD and CC-BY
URL:           https://palletsprojects.com/p/werkzeug/
Source0:       %{pypi_source}

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-python3
BuildRequires: mingw32-python3-setuptools

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-python3
BuildRequires: mingw64-python3-setuptools


%description
MinGW Windows Python %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python3 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python3 %{pkgname} library.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pkgname}
%license LICENSE.rst src/werkzeug/debug/shared/ICON_LICENSE.md
%{mingw32_python3_sitearch}/%{pkgname}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pkgname}
%license LICENSE.rst src/werkzeug/debug/shared/ICON_LICENSE.md
%{mingw64_python3_sitearch}/%{pkgname}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}-py%{mingw64_python3_version}.egg-info/


%changelog
* Tue Aug 09 2022 Sandro Mani <manisandro@gmail.com> - 2.2.2-1
- Update to 2.2.2

* Fri Jul 29 2022 Sandro Mani <manisandro@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Sandro Mani <manisandro@gmail.com> - 2.0.3-1
- Update to 2.0.3

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.0.2-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.0.2-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Sandro Mani <manisandro@gmail.coM> - 2.0.1-1
- Update to 2.0.1

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 1.0.1-7
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Sandro Mani <manisandro@gmail.com> - 1.0.1-5
- Switch to py3_build/py3_install macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Sandro Mani <manisandro@gmail.com> - 1.0.1-3
- Be more specific in %%files
- Add FONT_LICENSE to %%license
- Add OFL to License

* Tue Jun 02 2020 Sandro Mani <manisandro@gmail.com> - 1.0.1-2
- Rebuild (python-3.9)

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Wed Oct 30 2019 Sandro Mani <manisandro@gmail.com> - 0.16.0-1
- Update to 0.16.0
- Switch to python3

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 0.11.10-1
- Initial package
