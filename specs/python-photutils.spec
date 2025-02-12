%bcond_without check

%global srcname photutils

Name: python-%{srcname}
Version: 2.1.0
Release: %autorelease
Summary: Astropy affiliated package for image photometry tasks
License: BSD-3-Clause

URL: http://photutils.readthedocs.org/en/latest/index.html
Source0: %{pypi_source}

ExcludeArch: %{ix86}
BuildRequires: gcc


%global _description %{expand:
Photutils contains functions for:
 * estimating the background and background rms in astronomical images
 * detecting sources in astronomical images
 * estimating morphological parameters of those sources (e.g., 
    centroid and shape parameters)
 * performing aperture and PSF photometry}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

BuildRequires: python3-devel

Recommends: %{py3_dist scipy}  >= 1.7.2
Recommends: %{py3_dist scikit-image} >= 0.19   
Recommends: %{py3_dist scikit-learn} >= 1.0
Recommends: %{py3_dist matplotlib} >= 3.5

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t -e %{toxenv}-test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files photutils

%if %{with check}
%check
%{tox} 
%endif 

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
