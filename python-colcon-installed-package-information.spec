%global srcname colcon-installed-package-information

Name:           python-%{srcname}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Extensions for colcon to inspect packages which have already been installed

License:        ASL 2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Extensions for colcon-core to inspect packages which have already been
installed.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core
%endif

%description -n python%{python3_pkgversion}-%{srcname}
These colcon extensions provide a mechanism which can be used for getting
information about packages outside of the workspace, which have already been
built and installed prior to the current operation.

In general, they work similarly to and are based on the
PackageDiscoveryExtensionPoint and PackageAugmentationExtensionPoint
extensions provided by colcon_core.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_installed_package_information/
%{python3_sitelib}/colcon_installed_package_information-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Oct 19 2022 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Update to 0.1.0
- Change URL to point to GitHub repository
- Improve description

* Wed Mar 16 2022 Scott K Logan <logans@cottsay.net> - 0.0.1-1
- Initial package
