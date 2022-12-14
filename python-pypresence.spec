Name:           python-pypresence
Version:        4.2.1
Release:        1%{?dist}
Summary:        A Discord Rich Presence Client in Python 
License:        MIT
URL:            https://qwertyquerty.github.io/pypresence/html/index.html
Source0:        https://github.com/qwertyquerty/pypresence/archive/%{version}/pypresence-%{version}.tar.gz
# Fix licensing issues, merge upstream
Patch:          https://github.com/qwertyquerty/pypresence/commit/b5dc7308a0.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%global _description \
Python-pypresence is a simple Discord Rich Presence Client in Python. \
Note that in order to use most of it's functions, an authorized app \
is required.


%description %{_description}


%package -n python3-pypresence
Summary:        %{summary}


%description -n python3-pypresence %{_description}


%prep
%autosetup -p1 -n pypresence-%{version}
# docs include files that are under a different license model, omitting them
rm -rf %{buildroot}/docs


%build
%py3_build


%install
%py3_install


%check
%py3_check_import pypresence


%files -n python3-pypresence
%license LICENSE
%doc README.md
%{python3_sitelib}/pypresence/
%{python3_sitelib}/pypresence-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Dec 2 2022 Steve Cossette <farchord@gmail.com> - 4.2.1-1
- Initital release of pypresence (4.2.1)
