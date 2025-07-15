%global pname periodictable

%bcond_without check

%global _description %{expand:
This package provides a periodic table of the elements
with support for mass, density and xray/neutron
scattering information.

Masses, densities and natural abundances come from
the NIST Physics Laboratory, but do not represent a
critical evaluation by NIST scientists.

Neutron scattering calculations use values collected
by the Atomic Institute of the Austrian Universities.
These values do corresponding to those from other packages,
though there are some differences depending to the tables used.
Bound coherent neutron scattering for gold in particular is
significantly different from older value: 7.63(6) as 
easured in 1974 compared to 7.90(7) as measured in 1990.

X-ray scattering calculations use a combination of empirical
and theoretical values from the LBL Center for X-ray Optics.
These values differ from those given in other sources such as
the International Tables for Crystallography, Volume C, and so
may give different results from other packages.}

Name:           python-%{pname}
Version:        2.0.2
Release:        %autorelease
Summary:        Extensible periodic table of the elements
License:        BSD-3-Clause AND/OR Public Domain
URL:            http://www.reflectometry.org/danse/elements.html
Source0:        https://github.com/pkienzle/%{pname}/archive/v%{version}/%{pname}-%{version}.tar.gz
BuildArch:      noarch
Patch0:         %{name}-remove_unrecognized_flag.patch

%description
%{_description}.

%package -n python3-%{pname}
Summary: Extensible periodic table of the elements

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-pyparsing
%py_provides python3-%{pname}

%description -n python3-%{pname}
%{_description}.


%prep
%autosetup -n %{pname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pname}

%if %{with check}
%check
%pytest -m "not network"
%endif

%files -n python3-%{pname} -f %{pyproject_files}

%changelog
%autochangelog
