# Build doc by default
%bcond_without doc

# mailman3's TestableMaster can't be used outside of a
# source checkout?
%bcond_with tests

%global srcname hyperkitty
%global pypi_name HyperKitty

Name:           python-%{srcname}
Version:        1.3.7
Release:        %autorelease
Summary:        A web interface to access GNU Mailman v3 archives
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/hyperkitty
Source0:        %{pypi_source %{pypi_name}}
# don't check out modules from git
Patch0:         %{pypi_name}-tox-localdeps.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with doc}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%global _description %{expand:
HyperKitty is an open source Django application under development. It aims to
provide a web interface to access GNU Mailman v3 archives.}

%description %{_description}


%package -n %{srcname}
Summary:        %{summary}

%description -n %{srcname} %{_description}


%package -n %{srcname}-doc
Summary:        Documentation for %{srcname}
Suggests:       %{srcname} = %{version}-%{release}

%description -n %{srcname}-doc %{_description}

This package contains the documentation for %{srcname}.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel

%if %{with doc}
(cd doc && PYTHONPATH=..:${PYTHONPATH} make html)
%endif


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
PYTHONPATH=$(pwd)/src:${PYTHONPATH} \
%tox
%endif


%files -n %{srcname} -f %{pyproject_files}
%license COPYING.txt
%doc AUTHORS.txt README.rst

%if %{with doc}
%files -n %{srcname}-doc
%license COPYING.txt
%doc doc/_build/html/*
%endif


%changelog
%autochangelog
