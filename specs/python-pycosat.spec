%global srcname pycosat
%global sum Python bindings to picosat (a SAT solver)
%global pkgdesc \
PicoSAT is a popular SAT solver written by Armin Biere in pure C. This \
package provides efficient Python bindings to picosat on the C level, i.e. \
when importing pycosat, the picosat solver becomes part of the Python process \
itself.

Name:           python-%{srcname}
Version:        0.6.6
Release:        %autorelease
Summary:        %{sum}

License:        MIT
URL:            https://github.com/ContinuumIO/%{srcname}
Source0:        https://github.com/ContinuumIO/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  picosat-devel

%description
%{pkgdesc}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
%{pkgdesc}


%prep
%setup -q -n %{srcname}-%{version}
sed -i -e s/distutils.core/setuptools/ setup.py
rm picosat.*

# upstream only applies proper flags when build is invoked with --inplace
sed -i "s/if .--inplace. in sys.argv:/if True:/" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pycosat
find %{buildroot}%{python3_sitearch} -name test_pycosat.\* -delete

%check
%pytest -vv

%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc AUTHORS.md CHANGELOG.md README.rst

%changelog
%autochangelog
