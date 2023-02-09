# These are problematic, sometimes they randomly fail or hang
%bcond_with xvfb_tests

%global desc \
The fslpy project is a FSL programming library written in Python. It is used by \
FSLeyes.

Name:           python-fslpy
Version:        3.10.0
Release:        %autorelease
Summary:        The FSL Python Library


License:        ASL 2.0
URL:            https://pypi.python.org/pypi/fslpy
Source0:        %{pypi_source fslpy}

# fix with nilabel 5.x
# https://github.com/pauldmccarthy/fslpy/commit/a22b05e0d771e99ec25a22ff16c36da02067e698
# backported to 3.10.0
Patch0:         0001-TEST-use-int32-instead-of-int64.patch
Patch1:         0002-TEST-nibabel.info-no-longer-has-version-components.patch
# for numpy 1.23
Patch2:         0003-MNT-np.object-has-been-deprecatad-for-a-long-time-an.patch

BuildRequires:  git-core

BuildArch:      noarch
BuildRequires:  python3-devel

BuildRequires:  dcm2niix
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
%if %{with xvfb_tests}
BuildRequires:  xorg-x11-server-Xvfb
%endif


%description
%{desc}

%package -n python3-fslpy
Summary:        %{summary}

%description -n python3-fslpy
%{desc}


%prep
%autosetup -n fslpy-%{version} -S git

# For the dep generator to pick up
cat requirements-extra.txt >> requirements.txt

# remove unneeded shebangs
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env python$/ d' {} 2>/dev/null ';'
# some scripts have the shebang, so we correct these
find . -type f -name "*.py" -exec sed -i 's/#![  ]*\/usr\/bin\/env python$/#!\/usr\/bin\/python3/' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fsl

# Remove test packages that are installed in site packages
rm -rfv %{buildroot}/%{python3_sitelib}/tests/


%check
%if %{with xvfb_tests}
# From https://git.fmrib.ox.ac.uk/fsl/fslpy/blob/master/.ci/test_template.sh
xvfb-run pytest-3 tests/test_idle.py
sleep 10
# Sometimes fails, sometimes passes
xvfb-run pytest-3 tests/test_platform.py || exit 0
%endif

# Ignore tests that have already been done
# Ignore immv_imcp because it requires a "nobody" user
# Ignore tests that require downloading data.
# Ignore tests requiring trimesh
# Ignore test using dcm2niix
# Ignore intermittently failing test: https://github.com/pauldmccarthy/fslpy/issues/10
# Ignore submit tests
%{pytest} tests  -m "not longtest and not test_submit" \
  --ignore=tests/test_idle.py --ignore=tests/test_platform.py \
  --ignore=tests/test_immv_imcp.py --ignore=tests/test_atlases.py \
  --ignore=tests/test_atlases_query.py \
  --ignore=tests/test_scripts/test_atlasq_list_summary.py \
  --ignore=tests/test_scripts/test_atlasq_ohi.py \
  --ignore=tests/test_scripts/test_atlasq_query.py --ignore=tests/test_callfsl.py \
  --ignore=tests/test_mesh.py --ignore=tests/test_dicom.py \
  --ignore=tests/test_parse_data.py \
  --ignore=tests/test_scripts/test_fsl_apply_x5.py

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

%changelog
%autochangelog
