%global _description %{expand:
ppft is a fork of Parallel Python, and is developed as part of pathos:
https://github.com/uqfoundation/pathos

Parallel Python module (pp) provides an easy and efficient way to create
parallel-enabled applications for SMP computers and clusters. pp module
features cross-platform portability and dynamic load balancing. Thus
application written with pp will parallelize efficiently even on heterogeneous
and multi-platform clusters (including clusters running other application with
variable CPU loads). Visit http://www.parallelpython.com for further
information.

ppft is part of pathos, a python framework for heterogeneous computing. ppft is
in active development, so any user feedback, bug reports, comments, or
suggestions are highly appreciated. A list of issues is located at
https://github.com/uqfoundation/ppft/issues, with a legacy list maintained at
https://uqfoundation.github.io/project/pathos/query.}

Name:           python-ppft
Version:        1.7.6.6
Release:        %autorelease
Summary:        Distributed and parallel python

License:        BSD
URL:            https://pypi.org/pypi/ppft
Source0:        %{pypi_source ppft}

BuildArch:      noarch

%description %_description

%package -n python3-ppft
Summary:        %{summary}
BuildRequires:  python3-devel
# For the tests
BuildRequires:  %{py3_dist pox}

# ppft is a drop in replacement of pp
Provides:   python3-pp = %{version}-%{release}
# Latest build before retirement was 1.6.0-18
# https://koji.fedoraproject.org/koji/packageinfo?packageID=5272
Obsoletes:  python3-pp < 1.6.0-19

%description -n python3-ppft %_description


%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%autosetup -n ppft-%{version}

# remove shebangs
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'


%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ppft pp

%check
# run the tests
# needs to be run from a directory that does not contain a ppft folder
cd ppft/tests
PYTHONPATH="$RPM_BUILD_ROOT/%{python3_sitelib}:$RPM_BUILD_ROOT/%{python3_sitearch}" %{python3} -m ppft.tests

%files -n python3-ppft -f %{pyproject_files}
%doc README.md CHANGELOG
%{_bindir}/ppserver

%files doc
%license COPYING LICENSE
%doc ppft/tests

%changelog
%autochangelog
