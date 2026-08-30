%bcond_with check
%global srcname photutils

Name:           python-%{srcname}
Version:        3.0.0
Release:        %autorelease
Summary:        Astropy affiliated package for image photometry tasks
License:        BSD-3-Clause
URL:            https://photutils.readthedocs.io/en/stable/
Source0:        %{pypi_source}
ExcludeArch:    %{ix86}
BuildRequires:  gcc

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

Recommends: %{py3_dist matplotlib} >= 3.9
Recommends: %{py3_dist scikit-image} >= 0.23

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%if %{with check}
    %pyproject_buildrequires -r -x test
%else
    %pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files photutils

%if %{with check}
%check
%pytest --pyargs -p no:cacheprovider -W ignore::numpy.exceptions.ComplexWarning -k "not test_centroids_nan_withmask" photutils
%endif 

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
