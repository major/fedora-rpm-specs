# These are problematic, sometimes they randomly fail or hang
%bcond xvfb_tests 0

%global desc \
The fslpy project is a FSL programming library written in Python. It is used by \
FSLeyes.

%global forgeurl https://github.com/pauldmccarthy/fslpy

Name:           python-fslpy
Version:        3.24.0
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
BuildRequires:  %{py3_dist wxpython}
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

# Don't run coverage when calling `pytest`
sed -i 's/--cov=fsl //' pyproject.toml

# remove unneeded shebangs
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env python$/ d' {} 2>/dev/null ';'
sed -i '/^#![  ]*\/usr\/bin\/env python3$/ d' fsl/wrappers/tbss.py
# some scripts have the shebang, so we correct these
find . -type f -name "*.py" -exec sed -i 's/#![  ]*\/usr\/bin\/env python$/#!\/usr\/bin\/python3/' {} 2>/dev/null ';'

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x extra

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fsl

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
%{py3_test_envvars} xvfb-run pytest fsl/tests/test_idle.py
sleep 10
%{py3_test_envvars} xvfb-run pytest fsl/tests/test_platform.py
%endif

# Disable tests we cannot run using markers as per
# https://github.com/pauldmccarthy/fslpy/issues/17
#
# From pyproject.toml, as of 3.20.0:
#   fsltest:    Requires FSL
# We cannot package the non-free FSL (FMRIB Software Library),
# https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
m="${m-}${m+ and }not fsltest"
#   wxtest:     Requires wxPython
#m="${m-}${m+ and }not wxtest"
#   dicomtest:  Requires dcm2niix
#   meshtest:   Requires trimesh and rtree
#   igziptest:  Requires indexed_gzip
#   piltest:    Requires Pillow
#   noroottest: Need to be executed as non-root user (will fail otherwise)
# RPM builds using mock are executed as the root user within the chroot.
m="${m-}${m+ and }not noroottest"
#   longtest:   Takes a long time
# The “longtest” tests do not run by default anyway, so we would have to run
# them separately, but this would require atlases from the non-free FSL.
#   unixtest:   Only works on *nix systems
# Exclude tests requiring network (URLError)
k="${k-}${k+ and }not test_enabled"
k="${k-}${k+ and }not test_installedVersion"
k="${k-}${k+ and }not test_loadSeries"
k="${k-}${k+ and }not test_scanDir"
# Requires a (non-free) FSL installation; see notes about the fsltest marker
k="${k-}${k+ and }not test_cluster"

# See: “TEST: Some kind of regression in pytest 8.2 w.r.t. namespace packages”
# https://github.com/pauldmccarthy/fslpy/commit/048e33cb23b06f1b6d315b124ee544147d520643
touch fsl/__init__.py

# Ignore tests that were (conditionally) run under xvfb-run.
ignore="${ignore-} --ignore=fsl/tests/test_idle.py"
ignore="${ignore-} --ignore=fsl/tests/test_platform.py"

%{pytest} ${k+-k }"${k-}" ${m+-m }"${m-}" ${ignore-}

# Remove test packages that are installed in site packages
# We do that here, since above tests require the installed tests and data
rm -rvf %{buildroot}%{python3_sitelib}/fsl/tests
sed -r -i '/\bfsl\/tests\b/d' %{pyproject_files}


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
