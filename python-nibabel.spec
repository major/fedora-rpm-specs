%global _description %{expand:
Read / write access to some common neuroimaging file formats

This package provides read +/- write access to some common medical and
neuroimaging file formats, including: ANALYZE (plain, SPM99, SPM2 and
later), GIFTI, NIfTI1, NIfTI2, MINC1, MINC2, MGH and ECAT as well as Philips
PAR/REC. We can read and write Freesurfer geometry, and read Freesurfer
morphometry and annotation files. There is some very limited support for DICOM.
NiBabel is the successor of PyNIfTI.

The various image format classes give full or selective access to header (meta)
information and access to the image data is made available via NumPy arrays.
}

Name:           python-nibabel
Version:        3.2.2
Release:        %autorelease
Summary:        Python package to access a cacophony of neuro-imaging file formats

License:        MIT and PDDL-1.0
URL:            http://nipy.org/nibabel/
Source0:        https://github.com/nipy/nibabel/archive/%{version}/nibabel-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-nibabel
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
Recommends:     python3-scipy
Recommends:     python3-pydicom
# Bundles their own veresion of netcdf reader
# that is different from Scipy version
Provides:       bundled(python%{python3_version}dist(netcdf))

%description -n python3-nibabel %_description

%prep
%autosetup -n nibabel-%{version}

%generate_buildrequires
%pyproject_buildrequires -x dicom,minc2,spm

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nibabel nisext

%check
# TestCifti2ImageAPI.test_filenames fails due to setuptools-bundled distutils'
# LooseVersion issue: https://github.com/pypa/distutils/issues/122
# This can be worked around by setting the environment variable to point
# to distutils from Python's standard library instead.
# The workaround may be removed once nibabel disposes of distutils:
# https://github.com/nipy/nibabel/pull/1073
export SETUPTOOLS_USE_DISTUTILS=stdlib
%{pytest} -v

%files -n python3-nibabel -f %{pyproject_files}
%{_bindir}/parrec2nii
%{_bindir}/nib-conform
%{_bindir}/nib-diff
%{_bindir}/nib-dicomfs
%{_bindir}/nib-ls
%{_bindir}/nib-nifti-dx
%{_bindir}/nib-roi
%{_bindir}/nib-stats
%{_bindir}/nib-tck2trk
%{_bindir}/nib-trk2tck

%changelog
%autochangelog
