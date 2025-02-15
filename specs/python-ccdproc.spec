%global srcname ccdproc
%global summary Astropy affiliated package for reducing optical/IR CCD data

Name:           python-%{srcname}
Version:        2.4.3
Release:        %autorelease
Summary:        %{summary}

License:        BSD-3-Clause
URL:            http://ccdproc.readthedocs.io/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The ccdproc package is a collection of code that will be helpful in basic CCD
processing. These steps will allow reduction of basic CCD data as either a
stand-alone processing or as part of a pipeline.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files ccdproc

%check
# Tests require memory-profiler, not in Fedora
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
# https://github.com/astropy/ccdproc/issues/872
#license LICENSE.rst licenses/LICENSE_STSCI_TOOLS.txt
%license LICENSE.rst 
%doc AUTHORS.rst README.rst

%changelog
%autochangelog
