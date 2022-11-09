%global srcname colcon-alias

Name:           python-%{srcname}
Version:        0.0.2
Release:        2%{?dist}
Summary:        Extension for colcon to create and modify command aliases

License:        ASL 2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to create and modify command aliases.

Aliases condense any number of colcon command invocations made up of a verb
followed by all associated arguments down to another 'alias' verb. When
invoking the alias verb, additional arguments can be appended to the original
invocations.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
Conflicts:      python%{python3_pkgversion}-colcon-mixin < 0.2.2
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core
Requires:       python%{python3_pkgversion}-filelock
Requires:       python%{python3_pkgversion}-PyYAML
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to create and modify command aliases.

Aliases condense any number of colcon command invocations made up of a verb
followed by all associated arguments down to another 'alias' verb. When
invoking the alias verb, additional arguments can be appended to the original
invocations.


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
%{python3_sitelib}/colcon_alias/
%{python3_sitelib}/colcon_alias-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Nov 04 2022 Scott K Logan <logans@cottsay.net> - 0.0.2-2
- Update description
- Update project URL

* Sun Feb 20 2022 Scott K Logan <logans@cottsay.net> - 0.0.2-1
- Initial package (rhbz#2056369)
