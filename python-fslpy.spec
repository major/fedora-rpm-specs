# These are problematic, sometimes they randomly fail or hang
%bcond_with xvfb_tests

%global desc \
The fslpy project is a FSL programming library written in Python. It is used by \
FSLeyes.

%global forgeurl https://github.com/pauldmccarthy/fslpy

Name:           python-fslpy
Version:        3.15.2
Release:        %autorelease
Summary:        The FSL Python Library

%global tag %{version}

%forgemeta


License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch
# fsleyes dropped it already, so this is a leaf package
# F40+
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  help2man

BuildRequires:  dcm2niix
BuildRequires:  %{py3_dist pytest}
%if %{with xvfb_tests}
BuildRequires:  xorg-x11-server-Xvfb
%endif


%description
%{desc}

%package -n python3-fslpy
Summary:        %{summary}

%description -n python3-fslpy
%{desc}

%pyproject_extras_subpkg -n python3-fslpy extra

%prep
%forgesetup

# remove pytest coverage etc bits
sed -i -e '/"coverage"/ d' \
    -e '/"pytest-cov"/ d' \
    -e '/addopts/ d' \
    pyproject.toml

# remove unneeded shebangs
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env python$/ d' {} 2>/dev/null ';'
sed -i '/^#![  ]*\/usr\/bin\/env python3$/ d' fsl/wrappers/tbss.py
# some scripts have the shebang, so we correct these
find . -type f -name "*.py" -exec sed -i 's/#![  ]*\/usr\/bin\/env python$/#!\/usr\/bin\/python3/' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires -x extra -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fsl

# Remove test packages that are installed in site packages
rm -rvf %{buildroot}%{python3_sitelib}/fsl/tests
sed -r -i '/\bfsl\/tests\b/d' %{pyproject_files}

# generate man pages
# imglob does not have a --help
for binary in "atlasq" "atlasquery" "fsl_apply_x5" "fsl_ents" "fsl_convert_x5" "imcp" "immv" "resample_image" "Text2Vest" "Vest2Text" "fsl_abspath" "imln" "imtest" "remove_ext"
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done

# do not have a --help
for binary in "imglob" "imrm"
do
    echo "Generating man page for ${binary// /-/}"
    PYTHONPATH="$PYTHONPATH:%{buildroot}/%{python3_sitelib}/" PATH="$PATH:%{buildroot}/%{_bindir}/" help2man --help-option=" " --no-info --no-discard-stderr --name="${binary}" --version-string="${binary} %{version}" --output="${binary// /-}.1" "${binary}"
    cat "${binary// /-}.1"
    install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D "${binary// /-}.1"
done

%check
%if %{with xvfb_tests}
# From https://git.fmrib.ox.ac.uk/fsl/fslpy/blob/master/.ci/test_template.sh
xvfb-run pytest-3 tests/test_idle.py
sleep 10
# Sometimes fails, sometimes passes
xvfb-run pytest-3 tests/test_platform.py || exit 0
%endif

# https://github.com/pauldmccarthy/fslpy/issues/17
# Ignore tests that have already been done
# Ignore immv_imcp because it requires a "nobody" user
# Ignore tests that require downloading data.
# Ignore tests requiring trimesh
# Ignore test using dcm2niix
# Ignore intermittently failing test: https://github.com/pauldmccarthy/fslpy/issues/10
# Ignore submit tests
k="not longtest and not test_submit"
k="${k} and not test_FEATFSFDesign_firstLevelVoxelwiseEV"
k="${k} and not test_compressed_voxelwise_ev"
k="${k} and not test_image_readonly_compressed"
k="${k} and not test_runfunc"
k="${k} and not test_fslmaths_load"
k="${k} and not test_fileOrImage"
k="${k} and not test_fileOrThing_outprefix"
k="${k} and not test_fileOrThing_outprefix_pathlib"
k="${k} and not test_fileOrThing_outprefix_differentTypes"
k="${k} and not test_fileOrThing_outprefix_directory"
k="${k} and not test_chained_fileOrImageAndArray"
k="${k} and not test_fileOrThing_submit_cmdonly"
k="${k} and not test_fileOrImage_all_tempfiles_cleared"
k="${k} and not test_atlas"
k="${k} and not test_read_nifti"
k="${k} and not test_VoxelwiseEVs"
k="${k} and not test_imcp_shouldPass"
k="${k} and not test_immv_shouldPass"
k="${k} and not test_fileOrThing_chained_outprefix"
# requires an FSL installation
k="${k} and not test_cluster"
# unable to find tests module
k="${k} and not test_func_to_cmd"
%{pytest} fsl/tests  -k "${k}" \
  --ignore=fsl/tests/test_idle.py --ignore=fsl/tests/test_platform.py \
  --ignore=fsl/tests/test_atlases.py \
  --ignore=fsl/tests/test_atlases_query.py \
  --ignore=fsl/tests/test_scripts/test_atlasq_list_summary.py \
  --ignore=fsl/tests/test_scripts/test_atlasq_ohi.py \
  --ignore=fsl/tests/test_scripts/test_atlasq_query.py \
  --ignore=fsl/tests/test_dicom.py \
  --ignore=fsl/tests/test_scripts/test_fsl_apply_x5.py \
  --ignore=fsl/tests/test_scripts/test_fsl_convert_x5.py \
  --ignore=fsl/tests/test_scripts/test_immv_imcp.py

%files -n python3-fslpy -f %{pyproject_files}
%doc README.rst
%{_bindir}/atlasq
%{_bindir}/atlasquery
%{_bindir}/fsl_apply_x5
%{_bindir}/fsl_ents
%{_bindir}/fsl_convert_x5
%{_bindir}/imcp
%{_bindir}/imglob
%{_bindir}/immv
%{_bindir}/resample_image
%{_bindir}/Text2Vest
%{_bindir}/Vest2Text
%{_bindir}/fsl_abspath
%{_bindir}/imln
%{_bindir}/imrm
%{_bindir}/imtest
%{_bindir}/remove_ext
%{_mandir}/man1/*.*

%changelog
%autochangelog
