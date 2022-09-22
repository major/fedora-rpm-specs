# Conditionals for different bindings
%bcond_without Py
# Only supports Matlab at the moment
# https://github.com/chlubba/catch22/issues/12
%bcond_with octave

# Package native R package separately:
# https://github.com/chlubba/catch22/wiki/Installation-and-Testing#r says that is to be preferred
# https://github.com/hendersontrent/Rcatch22

%global _description %{expand: \
catch22 is a collection of 22 time-series features coded in C that can be run
from Python, R, Matlab, and Julia. The catch22 features are a high-performing
subset of the over 7000 features in hctsa.

Features were selected based on their classification performance across a
collection of 93 real-world time-series classification problems, as described
in our open-access paper:

- Lubba et al. (2019). catch22: CAnonical Time-series CHaracteristics
  (https://doi.org/10.1007/s10618-019-00647-x)

The computational pipeline used to generate the catch22 feature set is in the
op_importance (https://github.com/chlubba/op_importance) repository.

For catch22-related information and resources, including a list of publications
using catch22, see the catch22 wiki (https://github.com/chlubba/catch22/wiki).}

Version:        0.4.0

Name:           catch22
Release:        %autorelease
Summary:        CAnonical Time-series CHaracteristics

License:        GPLv3
URL:            https://github.com/chlubba/catch22
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Helper script for content-aware comparison of CSV file output from tests
Source1:        compare_output

# Backport upstream commit 135fb01bbd71c98fea01a7a2612abdca531b44f6 “Python
# version numbering fixed”
#
# Fixes:
#
# Python package version mismatch
# https://github.com/DynamicsAndNeuralSystems/catch22/issues/27
Patch:          %{url}/commit/135fb01bbd71c98fea01a7a2612abdca531b44f6.patch

BuildRequires:  gcc
BuildRequires:  python3-devel

%description
%_description


%if %{with Py}
%package -n python3-%{name}
Summary:        %{summary}
License:        GPLv3

%description -n python3-%{name}
%_description
%endif


%if %{with octave}
%global octpkg %{name}
%package -n octave-%{name}
Summary:        %{summary}
License:        GPLv3+

BuildRequires:  octave-devel

Requires:       octave(api) = %{octave_api}
Requires(post):   octave
Requires(postun): octave

%description -n octave-%{name}
%_description
%endif


%prep
%autosetup -p1
find . -name ".gitignore" -print -delete

%if %{with Py}
pushd wrap_Python
# Default setup.py should be the Python 2 version:
mv setup.py setup_P2.py
mv setup_P3.py setup.py
popd
%endif

%if %{with octave}
# Set up for Octave install
echo "Does not yet support Octave."
%endif


%generate_buildrequires
%if %{with Py}
pushd wrap_Python >/dev/null
%pyproject_buildrequires
popd >/dev/null
%endif


%build
pushd C
%set_build_flags
# https://github.com/chlubba/catch22/wiki/Installation-and-Testing
"${CC-gcc}" ${CFLAGS} -o run_features \
    main.c \
    CO_AutoCorr.c \
    DN_HistogramMode_10.c \
    DN_HistogramMode_5.c \
    DN_OutlierInclude.c \
    FC_LocalSimple.c \
    IN_AutoMutualInfoStats.c \
    MD_hrv.c \
    PD_PeriodicityWang.c \
    SB_BinaryStats.c \
    SB_CoarseGrain.c \
    SB_MotifThree.c \
    SB_TransitionMatrix.c \
    SC_FluctAnal.c \
    SP_Summaries.c \
    DN_Mean.c \
    DN_Spread_Std.c \
    butterworth.c \
    fft.c \
    helper_functions.c \
    histcounts.c \
    splinefit.c \
    stats.c \
    ${LDFLAGS} -lm
popd

%if %{with Py}
pushd wrap_Python
%pyproject_wheel
popd
%endif

%if %{with octave}
echo "Does not yet support Octave."
%endif


%install
pushd C
install -p -m 0755 run_features -Dt %{buildroot}/%{_bindir}
popd

%if %{with Py}
pushd wrap_Python
%pyproject_install
%pyproject_save_files %{name} %{name}_C
popd
%endif

%if %{with octave}
echo "Does not yet support Octave."
%endif


%check
find testData -type f -name '*_output.txt' \
    -execdir cp -v -p '{}' '{}.expected' ';'
PATH="${PATH}:%{buildroot}%{_bindir}" ./testData/runtests.sh

for x in testData/*.expected
do
  %{python3} '%{SOURCE1}' \
      --ignore-extra='DN_Mean' \
      --ignore-extra='DN_Spread_Std' \
      "${x}" "$(echo "${x}" | sed -r 's/\.expected$//')"
done

%if %{with Py}
pushd wrap_Python
PYTHONPATH='%{buildroot}/%{python3_sitearch}' %{python3} testing.py
popd
%endif


%if %{with octave}
%post
%octave_cmd pkg rebuild


%preun
%octave_pkg_preun


%postun
%octave_cmd pkg rebuild
%endif


%files
%license LICENSE
%doc README.md featureList.txt
%{_bindir}/run_features


%if %{with Py}
%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE
%doc README.md featureList.txt
%endif

%if %{with octave}
%files -n octave-%{name}
%license LICENSE
%doc featureList.txt
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo
%endif


%changelog
%autochangelog
