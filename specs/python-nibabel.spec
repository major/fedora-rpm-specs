%global forgeurl https://github.com/nipy/nibabel

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
Version:        5.3.3
Release:        %autorelease
Summary:        Python package to access a cacophony of neuro-imaging file formats
%global tag %{version}
%forgemeta
License:        MIT and PDDL-1.0
URL:            http://nipy.org/nibabel/
Source0:        %forgesource

# Adapt to functools.partial becoming a method descriptor in Python 3.14
# https://github.com/nipy/nibabel/pull/1391
#
# Fixes:
#
# Python 3.14: failing test
# https://github.com/nipy/nibabel/issues/1390
#
# python-nibabel fails to build with Python 3.14:
# TestDeprecatorMaker.test_deprecator_maker: TypeError: Deprecator.__init__()
# got multiple values for argument 'warn_class'
# https://bugzilla.redhat.com/show_bug.cgi?id=2328709
Patch:          %{forgeurl}/pull/1391.patch

# fix: Ignore warning that may not be emitted
# https://github.com/nipy/nibabel/commit/ac0b38851ad9505c863b56e64c2c4131cf97847c
#
# Fixes:
#
# test_resample fails with scipy 1.16
# https://github.com/nipy/nibabel/issues/1428
Patch:          %{forgeurl}/commit/ac0b38851ad9505c863b56e64c2c4131cf97847c.patch

BuildArch:      noarch

%description %_description

%package -n python3-nibabel
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-httpserver
BuildRequires:  help2man
Recommends:     python3-scipy
Recommends:     python3-pydicom
# Bundles their own version of netcdf reader
# that is different from Scipy version
Provides:       bundled(python%{python3_version}dist(netcdf))

%description -n python3-nibabel %_description

%prep
# warning: don't use -S git/git_am here, or hatchling/hatch-vcs generates a wrong version
%forgeautosetup -p1

# delete shebangs from files that don't need it
find nibabel/cmdline/  -name "*.py" -execdir sed -i '/^#!python/ d' '{}' \;

# correct other shebangs
# upstream uses #!python as a shebang, correct it
find . -name "*.py" -execdir sed -i 's|^#!python|#!%{python3}|' '{}' \;

# delete .gitignore files
rm -fv nibabel/{tests/data/,}.gitignore


%generate_buildrequires
%pyproject_buildrequires -x dicom,minc2,spm

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l nibabel

for binary in "parrec2nii" "nib-conform" "nib-convert" "nib-diff" "nib-dicomfs" "nib-ls" "nib-nifti-dx" "nib-roi" "nib-stats" "nib-tck2trk" "nib-trk2tck"
do
    echo "Generating man page for ${binary}"
    %py3_test_envvars help2man --no-info --no-discard-stderr --output="${binary}.1" "${binary}"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary}.1"
done

%check
%pytest -v --pyargs nibabel

%files -n python3-nibabel -f %{pyproject_files}
%{_bindir}/parrec2nii
%{_bindir}/nib-conform
%{_bindir}/nib-convert
%{_bindir}/nib-diff
%{_bindir}/nib-dicomfs
%{_bindir}/nib-ls
%{_bindir}/nib-nifti-dx
%{_bindir}/nib-roi
%{_bindir}/nib-stats
%{_bindir}/nib-tck2trk
%{_bindir}/nib-trk2tck
%{_mandir}/man1/nib*
%{_mandir}/man1/parrec2nii.*

%changelog
%autochangelog
