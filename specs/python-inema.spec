%global         srcname  inema
%global         desc     This is a python module for interfacing the "Internetmarke" API provided by the\
German postal company "Deutsche Post". It implements V3 of this API.\
\
The Internetmarke API allows you to buy online franking for national and\
international postal products like post cards and letters of all weight\
classes and service classes (normal, registered, ...).

Name:           python-%{srcname}
Version:        1.0.4
Release:        %autorelease
Summary:        A Python interface to the Deutsche Post Internetmarke Online Franking

License:        LGPL-3.0-or-later
URL:            https://codeberg.org/gms/python-inema
Source0:        %pypi_source

BuildArch:      noarch

# required for python macros
BuildRequires:  python3-devel


%description
%{desc}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
sed -i '1,1s@^#!.*$@@' inema/frank.py inema/inema.py
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{srcname}


%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/frank
%doc README.rst


%changelog
%autochangelog
