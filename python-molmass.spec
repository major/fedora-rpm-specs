Name:           python-molmass
Version:        2021.6.18
Release:        %autorelease
Summary:        Calculate molecular mass properties from elemental composition

License:        BSD 
URL:            https://www.lfd.uci.edu/~gohlke/molmass/
Source0:        %{pypi_source molmass}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  dos2unix
BuildRequires:  sed

%global _description %{expand:
Molmass is a Python library and console script to calculate the molecular mass
(average, nominal, and isotopic pure), the elemental composition, and the mass
distribution spectrum of a molecule given by its chemical formula, relative 
element weights, or sequence.}

%description %_description

%package -n python3-molmass
Summary:        %{summary}

%description -n python3-molmass %_description


%prep
%autosetup -p1 -n molmass-%{version}

# fix line endings
dos2unix -k README.rst

#remove shebang from non-executable
sed s/#!.*$// molmass/molmass_web.py > molmass/molmass_web.py.noenv && touch -r molmass/molmass_web.py molmass/molmass_web.py.noenv && mv molmass/molmass_web.py.noenv molmass/molmass_web.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files molmass


%files -n python3-molmass -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/molmass
%{_bindir}/molmass_web
%{_bindir}/elements_gui


%changelog
%autochangelog
