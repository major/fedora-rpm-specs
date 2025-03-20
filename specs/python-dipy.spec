# Full documentation downloads 100+MB of data, so we'd rather users look at the
# upstream documentation
%bcond docs 0

# There are a lot of tests and they take a while to complete.
%bcond tests 1

# Slow tests can take more than 30s to complete, addding considerably
# To the overall build time. Disable them to speed up the build.
%bcond slow_tests 1

Name:           python-dipy
Version:        1.11.0
Release:        %autorelease
Summary:        Diffusion MRI Imaging in Python

%global forgeurl https://github.com/nipy/dipy/
%global tag %{version}
%forgemeta

# SPDX
License:        BSD-3-Clause
URL:            https://dipy.org/
Source:         %forgesource

BuildRequires:      python3-devel
BuildRequires:      gcc-c++
%if %{with tests}
BuildRequires:      %{py3_dist pytest}
%endif
# Required for some modules but not in Fedora yet
# BuildRequires:      %%{py3_dist cvxpy}

# Drop i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:        %{ix86}

%global desc %{expand: \
DIPY is a python library for the analysis of MR diffusion imaging.

DIPY is for research only; please contact admins@dipy.org if you plan
to deploy in clinical settings.

Current information can always be found on the DIPY website:
https://dipy.org/}

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
%forgeautosetup -p1

# Correct interpreter for these---used in building docs and so on
sed -i 's/#!\/usr\/bin\/env python[0-9]?/#!\/usr\/bin\/python3/' doc/tools/docgen_cmd.py
sed -i 's/#!\/usr\/bin\/env python[0-9]?/#!\/usr\/bin\/python3/' doc/tools/build_modref_templates.py
find tools/ -name "*.py" -exec sed -i 's/#!\/usr\/bin\/env python[0-9]?/#!\/usr\/bin\/python3/' '{}' \;

# Remove shebangs from modules
find dipy/ -name \*.py -exec sed -r -i '/#!.*python/d' '{}' \;

# Other shebangs and permission fixes
for f in "dipy/stats/resampling.py" "dipy/reconst/dki.py" "dipy/reconst/dti.py"  "dipy/workflows/mask.py" "dipy/workflows/tracking.py" "dipy/reconst/dki_micro.py" "dipy/reconst/msdki.py" "dipy/workflows/tests/test_stats.py"
do
    chmod -x "$f"
    sed -i '/^#!\/usr\/bin\/env python/ d' "$f"
    sed -i '/^#!\/usr\/bin\/python/ d' "$f"
done

# Remove executable bit
chmod a-x doc/examples/*.py
chmod a-x dipy/data/files/func_coef.nii.gz

# Allow building with NumPy 1.x
# Current stable branches won't be updated to 2.x.
sed -r -i 's/(numpy)[>=].*;/\1;/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -p

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
%if %{without slow_tests}
# These tests are very slow (> 30s)
# Note: List order is not related to slowness
k="${k-}${k+ and }not test_affreg_all_transforms"
k="${k-}${k+ and }not test_apply_affine_transform"
k="${k-}${k+ and }not test_classify"
k="${k-}${k+ and }not test_em_3d_demons"
k="${k-}${k+ and }not test_em_3d_gauss_newton"
k="${k-}${k+ and }not test_exponential_iso"
k="${k-}${k+ and }not test_image_registration"
k="${k-}${k+ and }not test_nlmeans_4d_3dsigma_and_threads"
k="${k-}${k+ and }not test_reconst_csa"
k="${k-}${k+ and }not test_reconst_csd"
k="${k-}${k+ and }not test_reconst_dki"
k="${k-}${k+ and }not test_reconst_opdt"
k="${k-}${k+ and }not test_reconst_qball"
k="${k-}${k+ and }not test_reconst_rumba"
k="${k-}${k+ and }not test_reconst_sdt"
k="${k-}${k+ and }not test_reconst_sfm"
k="${k-}${k+ and }not test_rumba"
k="${k-}${k+ and }not test_sfm"
k="${k-}${k+ and }not test_warping_3d"
%endif
# Individual tests requiring network
k="${k-}${k+ and }not test_concatenate_flow"
k="${k-}${k+ and }not test_convert_tractogram_flow"
k="${k-}${k+ and }not test_deterministic_performances"
k="${k-}${k+ and }not test_io_fetch"
k="${k-}${k+ and }not test_io_info"
k="${k-}${k+ and }not test_probabilistic_performances"
k="${k-}${k+ and }not test_ptt_performances"
k="${k-}${k+ and }not test_ptt_tracking"
%ifarch s390x
# https://github.com/dipy/dipy/issues/2886#issuecomment-2003567594
k="${k-}${k+ and }not test_bundlewarp"
k="${k-}${k+ and }not test_bundlewarp_vector_filed"
k="${k-}${k+ and }not test_bundle_shape_profile"
%endif
# Mimic what upstream does for testing
mkdir test && pushd test
ln -s ../pyproject.toml .
# Ignore test scripts requiring network (for downloading test data)
%pytest -r fEs "${k:+-k $k}" \
    --ignore-glob="/**/align/tests/test_api.py" \
    --ignore-glob="/**/io/tests/test_stateful_tractogram.py" \
    --ignore-glob="/**/io/tests/test_streamline.py" \
    --ignore-glob="/**/io/tests/test_utils.py" \
    --ignore-glob="/**/nn/tests/test_cnn_1denoiser.py" \
    --ignore-glob="/**/tracking/tests/test_tracker.py" \
    --ignore-glob="/**/tracking/tests/test_tractogen.cpython-313-*-linux-gnu.so" \
    --ignore-glob="/**/utils/tests/test_tractogram.py" \
    --pyargs dipy 
%endif

%files -n python3-dipy -f %{pyproject_files}
%doc README.rst Changelog AUTHOR
%license LICENSE
%{_bindir}/dipy_*

%files doc
%license LICENSE
# Installed by package
%{_docdir}/%{name}-doc
%if %{with docs}
%doc doc/_build/html
%endif

%changelog
%autochangelog
