# Tests need internet connection;
# correctly executed in local.
%global with_check 0

##  Filtering of private libraries 
%global _privatelibs  ^%{python3_sitearch}/prody/.*\\.so$
%global __provides_exclude_from ^(%{_privatelibs})$
%global __requires_exclude_from ^(%{_privatelibs})$

Name: ProDy
Summary: Application for protein structure, dynamics and sequence analysis
Version: 2.4.1
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

BuildRequires: gcc, gcc-c++

# Patch for NumPy 2.x compatibility (backported)
# https://github.com/prody/ProDy/pull/1959
# This includes previous patch dropping version pinnings.
Patch0: Fix-rtbtools-to-permit-numpy-upgrade.patch

# Patch for SciPy >= 1.14 (backported)
# https://github.com/prody/ProDy/issues/1955
# https://github.com/prody/ProDy/pull/1958
Patch1: eigh-evd-when-no-turbo.patch

%description
ProDy is a free and open-source Python package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis.

%package -n python3-%{name}
Summary: Application for protein structure, dynamics and sequence analysis
%{?python_provide:%python_provide python3-%{name}}
Provides: ProDy = 0:%{version}-%{release}

BuildRequires: python3-devel
BuildRequires: python3-nose
BuildRequires: python3-urllib3
BuildRequires: python3-scipy
BuildRequires: python3-numpy
BuildRequires: python3-matplotlib
BuildRequires: python3-biopython
BuildRequires: python3-setuptools
BuildRequires: pyproject-rpm-macros

%description -n python3-%{name}
This is ProDy Python3 package for protein structure, dynamics,
and sequence analysis.  It allows for comparative analysis and modeling of 
protein structural dynamics and sequence co-evolution.  Fast and flexible ProDy
API is for interactive usage as well as application development.  ProDy also  
comes with several analysis applications and a graphical user interface for 
visual analysis. 
- Visit http://www.csb.pitt.edu/ProDy/ -

%prep
%autosetup -p1

# Fix permissions
find prody/proteins/ccealign -name '*.h' -exec chmod 0644 '{}' \;
find prody/proteins/ccealign -name '*.cpp' -exec chmod 0644 '{}' \;

%generate_buildrequires
%pyproject_buildrequires -r

%build
#py3_build
%pyproject_wheel

%install
#py3_install
%pyproject_install
%pyproject_save_files prody

mkdir -p $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/*

cd scripts
cp -pr ./prody ./python%{python3_version}-prody
cp -pr ./evol  ./python%{python3_version}-evol
# Fix shebangs
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' \
 ./prody \
 ./evol \
 ./python%{python3_version}-prody \
 ./python%{python3_version}-evol

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
