%global srcname pocketlint

Name:      python-%{srcname}
Version:   0.25
Release:   %autorelease
Summary:   Support for running pylint against projects

License:   GPL-2.0-or-later
Url:       https://github.com/rhinstaller/%{srcname}
Source0:   https://github.com/rhinstaller/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch: noarch

%description
Addon pylint modules and configuration settings for checking the validity of
Python-based source projects.

%package -n python3-%{srcname}
Summary: Support for running pylint against projects (Python 3 version)
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-packaging
BuildRequires: python3-pylint
BuildRequires: python3-setuptools

Requires: python3-packaging
Requires: python3-polib
Requires: python3-pylint

%description -n python3-%{srcname}
Addon pylint modules and configuration settings for checking the validity of
Python-based source projects.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
make PYTHON=%{__python3}

%install
make DESTDIR=%{buildroot} PYTHON=%{__python3} install

%check
make PYTHON=%{__python3} check

%files -n python3-%{srcname}
%license COPYING
%{python3_sitelib}/%{srcname}*egg*
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
