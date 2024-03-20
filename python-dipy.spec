%global desc %{expand: \
DIPY is a python library for the analysis of MR diffusion imaging.

DIPY is for research only; please contact admins@dipy.org if you plan
to deploy in clinical settings.

Current information can always be found on the DIPY website:
https://dipy.org/}

# Full documentation downloads 100+MB of data, so we'd rather users look at the
# upstream documentation
%bcond docs 0

# There are a lot of tests and they take a while to complete.
%bcond tests 1

%global forgeurl https://github.com/nipy/dipy/

Name:           python-dipy
Version:        1.9.0
Release:        %autorelease
Summary:        Diffusion MRI Imaging in Python

%global tag %{version}
%forgemeta

# SPDX
License:        BSD-3-Clause
URL:            https://dipy.org/
Source0:        %forgesource

BuildRequires:      python3-devel
BuildRequires:      gcc-c++
%if %{with tests}
BuildRequires:      %{py3_dist pytest}
%endif
# Required for some modules but not in Fedora yet
# BuildRequires:      %%{py3_dist cvxpy}

# Drop i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
#
# Also exclude s390x due to failing tests.
# https://github.com/dipy/dipy/issues/2886#issuecomment-2003567594
ExcludeArch:        %{ix86} s390x

%description
%{desc}

%package -n python3-dipy
Summary:            %{summary}
Suggests:           %{py3_dist ipython}

%description -n python3-dipy
%{desc}

%package doc
BuildArch:      noarch
Summary:        %{summary}

%description doc
Documentation for %{name}.


%prep
%forgesetup

# Correct interpreter for these---used in building docs and so on
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' doc/tools/docgen_cmd.py
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' doc/tools/build_modref_templates.py
find tools/ -name "*.py" -exec sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' '{}' \;

# Other shebangs and permission fixes
for f in "dipy/stats/resampling.py" "dipy/reconst/dki.py" "dipy/reconst/dti.py"  "dipy/workflows/mask.py" "dipy/workflows/tracking.py" "dipy/reconst/dki_micro.py" "dipy/reconst/msdki.py" "dipy/workflows/tests/test_stats.py"
do
    chmod -x "$f"
    sed -i '/^#!\/usr\/bin\/env python/ d' "$f"
    sed -i '/^#!\/usr\/bin\/python/ d' "$f"
done

# Remove executable bit from examples
chmod a-x doc/examples/*.py

%generate_buildrequires
%pyproject_buildrequires -w

%build
%pyproject_wheel

%if %{with docs}
pushd doc
    export PYTHONPATH=../build/
    make SPHINXBUILD=sphinx-build-3 PYTHON=%{__python3} html
    rm -rf _build/html/.doctrees
    rm -rf _build/html/.buildinfo
popd
%endif

%install
%pyproject_install
%pyproject_save_files dipy

# Examples are installed in /usr/doc by the build backend. Let's fix that!
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
mv %{buildroot}/usr/doc/dipy/examples %{buildroot}%{_docdir}/%{name}-doc/

%check
%if %{with tests}
# These tests appear to hang or are very slow
k="${k-}${k+ and }not test_peaksFromModelParallel"
k="${k-}${k+ and }not test_reconst_csa"
k="${k-}${k+ and }not test_reconst_rumba"
# Individual tests requiring network
k="${k-}${k+ and }not test_syn_registration"
k="${k-}${k+ and }not test_register_dwi_to_template"
k="${k-}${k+ and }not test_affine_registration"
k="${k-}${k+ and }not test_single_transforms"
k="${k-}${k+ and }not test_register_series"
k="${k-}${k+ and }not test_register_dwi_series_and_motion_correction"
k="${k-}${k+ and }not test_streamline_registration"
k="${k-}${k+ and }not test_register_dwi_series_multi_b0"
k="${k-}${k+ and }not test_ptt_tracking"
k="${k-}${k+ and }not test_io_fetch"
k="${k-}${k+ and }not test_concatenate"
k="${k-}${k+ and }not test_io_info"
k="${k-}${k+ and }not test_concatenate_flow"
k="${k-}${k+ and }not test_convert_tractogram_flow"
# Ignore test scripts requiring network (for downloading test data)
%pytest -v --import-mode=importlib \
  --ignore=dipy/io/tests/test_stateful_tractogram.py \
  --ignore=dipy/io/tests/test_streamline.py \
  --ignore=dipy/io/tests/test_utils.py \
  "${k:+-k $k}"
%endif

%files -n python3-dipy -f %{pyproject_files}
%doc README.rst Changelog AUTHOR
%license LICENSE
%{_bindir}/dipy_align_affine
%{_bindir}/dipy_align_syn
%{_bindir}/dipy_apply_transform
%{_bindir}/dipy_buan_lmm
%{_bindir}/dipy_buan_profiles
%{_bindir}/dipy_buan_shapes
%{_bindir}/dipy_correct_motion
%{_bindir}/dipy_denoise_lpca
%{_bindir}/dipy_denoise_mppca
%{_bindir}/dipy_denoise_nlmeans
%{_bindir}/dipy_denoise_patch2self
%{_bindir}/dipy_fetch
%{_bindir}/dipy_fit_csa
%{_bindir}/dipy_fit_csd
%{_bindir}/dipy_fit_dki
%{_bindir}/dipy_fit_dti
%{_bindir}/dipy_fit_ivim
%{_bindir}/dipy_fit_mapmri
%{_bindir}/dipy_gibbs_ringing
%{_bindir}/dipy_horizon
%{_bindir}/dipy_info
%{_bindir}/dipy_labelsbundles
%{_bindir}/dipy_mask
%{_bindir}/dipy_median_otsu
%{_bindir}/dipy_recobundles
%{_bindir}/dipy_reslice
%{_bindir}/dipy_slr
%{_bindir}/dipy_snr_in_cc
%{_bindir}/dipy_track
%{_bindir}/dipy_track_pft
%{_bindir}/dipy_split
%{_bindir}/dipy_bundlewarp
%{_bindir}/dipy_evac_plus
%{_bindir}/dipy_concatenate_tractograms
%{_bindir}/dipy_convert_tensors
%{_bindir}/dipy_convert_tractogram
%{_bindir}/dipy_fit_dsi
%{_bindir}/dipy_sh_convert_mrtrix

%files doc
%license LICENSE
# Installed by package
%{_docdir}/%{name}-doc
%if %{with docs}
%doc doc/_build/html
%endif

%changelog
%autochangelog
