ExcludeArch: %{ix86}

# Tests need internet connection;
# correctly executed in local.
%global with_check 0

##  Filtering of private libraries 
%global _privatelibs  ^%{python3_sitearch}/prody/.*\\.so$
%global __provides_exclude_from ^(%{_privatelibs})$
%global __requires_exclude_from ^(%{_privatelibs})$

Name: ProDy
Summary: Application for protein structure, dynamics and sequence analysis
Version: 2.6.1
Release: %autorelease
# MIT is the main license for ProDy
# part of prody/dynamics/editing.py is MIT-Modern-Variant
# Biopython is MIT-CMU
# prody/utilities/tnt/* code is NIST-PD
# CEalign module is distributed under BSD-2-Clause license
# scikit-learn is BSD-3-Clause
License: MIT AND MIT-CMU AND MIT-Modern-Variant AND BSD-2-Clause AND BSD-3-Clause AND Python-2.0.1 AND NIST-PD
URL: http://www.bahargroup.org/prody
Source0: https://github.com/prody/ProDy/archive/v%{version}/ProDy-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: gcc-c++

# ProDy is ready for Numpy-2/Python-3.12+, but build required versions are not updated
Patch0: ProDy-2.6.1-remove_requires_limits.patch

%description
ProDy is a free and open-source Python package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis.

%package -n python3-%{name}
Summary: Application for protein structure, dynamics and sequence analysis
%py_provides   python3-%{name}
%py_provides   ProDy
BuildRequires: python3-devel
BuildRequires: python3-urllib3
BuildRequires: python3-scipy
BuildRequires: python3-numpy
BuildRequires: python3-matplotlib
BuildRequires: python3-biopython
BuildRequires: python3-setuptools
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-sklearn-genetic
%description -n python3-%{name}
ProDy is for protein structure, dynamics, and sequence analysis.
It allows for comparative analysis and modeling of protein structural
dynamics and sequence co-evolution. Fast and flexible ProDy
API is for interactive usage as well as application development.
ProDy also comes with several analysis applications and a graphical
user interface for visual analysis.

%prep
%autosetup -p1

# Fix permissions
find prody/proteins/ccealign -name '*.h' -exec chmod 0644 '{}' \;
find prody/proteins/ccealign -name '*.cpp' -exec chmod 0644 '{}' \;

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

# Following command compile ProDy's extensions
#%%{__python3} setup.py build_ext --inplace --force

%install
%pyproject_install
%pyproject_save_files prody

#cp -a prody/dynamics $RPM_BUILD_ROOT%%{python3_sitearch}/prody/
#cp -a prody/sequence $RPM_BUILD_ROOT%%{python3_sitearch}/prody/
#cp -a prody/kdtree $RPM_BUILD_ROOT%%{python3_sitearch}/prody/
#cp -a prody/proteins $RPM_BUILD_ROOT%%{python3_sitearch}/prody/

mkdir -p $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/*

cd scripts
cp -pr ./prody ./python%{python3_version}-prody
cp -pr ./evol  ./python%{python3_version}-evol

# Fix shebangs
%py3_shebang_fix ./prody ./evol ./python%{python3_version}-prody ./python%{python3_version}-evol

for i in prody-%{python3_version}; do
  touch -r ./python%{python3_version}-prody $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  install -p ./prody $RPM_BUILD_ROOT%{_bindir}
  install -p ./python%{python3_version}-prody $RPM_BUILD_ROOT%{_bindir}
  ln -srf python%{python3_version}-prody $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in evol-%{python3_version}; do
  touch -r ./python%{python3_version}-evol $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  install -p ./evol $RPM_BUILD_ROOT%{_bindir}
  install -p ./python%{python3_version}-evol $RPM_BUILD_ROOT%{_bindir}
  ln -srf python%{python3_version}-evol $RPM_BUILD_ROOT%{_bindir}/$i
done
cd ..

%if 0%{?with_check}
%check
%pyproject_check_import
%pytest -m "not network"
%endif

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/prody
%{_bindir}/prody-%{python3_version}
%{_bindir}/python%{python3_version}-prody
%{_bindir}/evol
%{_bindir}/evol-%{python3_version}
%{_bindir}/python%{python3_version}-evol

%changelog
%autochangelog
