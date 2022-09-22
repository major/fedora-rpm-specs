%global desc %{expand: \
DIPY is a python toolbox for analysis of MR diffusion imaging.
DIPY is for research only; please do not use results from DIPY for clinical
decisions.

Current information can always be found from the DIPY website - http://dipy.org}

# Full documentation downloads 100+MB of data, so we'd rather users look at the
# upstream documentation
%bcond_with docs

# Fail because of xvfb related errors, also still depends on nose
%bcond_with tests

%global forgeurl https://github.com/nipy/dipy/

Name:           python-dipy
Version:        1.5.0
Release:        %autorelease
Summary:        Diffusion MRI utilities in python

%global tag %{version}
%forgemeta


License:        BSD
URL:            http://nipy.org/dipy/
Source0:        %forgesource

%description
%{desc}

%package -n python3-dipy
Summary:        %{summary}
BuildRequires:      python3-devel
BuildRequires:      gcc
%if %{with tests}
BuildRequires:      %{py3_dist xvfbwrapper}
BuildRequires:      xorg-x11-server-Xvfb
# Not mentioned in setup scripts
BuildRequires:      %{py3_dist nose}
# Not mentioned in build scripts
BuildRequires:      %{py3_dist pytest}
%endif
Suggests:           %{py3_dist ipython}

# Required for some modules but not in Fedora yet
# BuildRequires:      %%{py3_dist cvxpy}


%description -n python3-dipy
%{desc}

%package doc
BuildArch:      noarch
Summary:        %{summary}

%description doc
Documentation for %{name}.


%prep
%forgesetup
export TEST_WITH_XVFB=true
# clean it all up (from the Makefile)
find . -name "*.so" -print -delete
find . -name "*.pyd" -print -delete
find . -name "*.c" -print -delete
find . -name "*.html" -print -delete
rm -rf build
rm -rf docs/_build
rm -rf docs/dist
rm -rf dipy/dipy.egg-info

# Correct interpreter for these---used in building docs and so on
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' doc/tools/docgen_cmd.py
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' doc/tools/build_modref_templates.py
find tools/ -name "*.py" -exec sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' '{}' \;

# Other shebangs and permission fixes
for f in "dipy/boots/resampling.py" "dipy/reconst/benchmarks/bench_csd.py" "dipy/reconst/dki.py" "dipy/reconst/dti.py"  "dipy/workflows/mask.py" "dipy/workflows/tracking.py" "dipy/reconst/dki_micro.py" "dipy/reconst/msdki.py" "dipy/workflows/tests/test_stats.py"
do
    chmod -x "$f"
    sed -i '/^#!\/usr\/bin\/env python/ d' "$f"
    sed -i '/^#!\/usr\/bin\/python/ d' "$f"
done

%generate_buildrequires
%pyproject_buildrequires -r

%build
export TEST_WITH_XVFB=true
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

%check
export TEST_WITH_XVFB=True
%if %{with tests}
export PYTHONPATH="%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}"
%{__python3} -c 'import dipy; dipy.test()'
%endif

%files -n python3-dipy -f %{pyproject_files}
%doc README.rst Changelog AUTHOR
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

%files doc
%license LICENSE
# Installed by package
%{_docdir}/dipy/examples
%if %{with docs}
%doc doc/_build/html
%endif

%changelog
%autochangelog
