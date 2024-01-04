# Only supports Matlab at the moment
# https://github.com/chlubba/catch22/issues/12
%bcond octave 0

# Package native R package separately:
# https://github.com/chlubba/catch22/wiki/Installation-and-Testing#r says that is to be preferred
# https://github.com/hendersontrent/Rcatch22

# Downstream .so version; see comment above Source2, and make sure to increment
# the following integer each time there is an ABI change upstream.
%global downstream_so_number 1
Name:           catch22
Version:        0.4.0
Release:        %autorelease
Summary:        CAnonical Time-series CHaracteristics

# The Matlab code is clearly documented as GPL-3.0-or-later. In “Please clarify
# GPL version,” https://github.com/DynamicsAndNeuralSystems/catch22/issues/32,
# upstream clarified that GPL-3.0-or-later is intended for but everything else,
# as well.
License:        GPL-3.0-or-later
URL:            https://github.com/chlubba/catch22
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Helper script for content-aware comparison of CSV file output from tests
Source1:        compare_output
# Hand-written for Fedora in groff_man(7) format based on --help text
Source2:        run_features.1
# Upstream does not provide any build system at all. This Makefile allows us to
# build a shared library and link the run_features executable to it. We must
# therefore use downstream .so versioning.
Source3:        Makefile

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3-devel

# Drop python3-catch22 (https://pypi.org/project/catch22/) beginning with F40
# since these bindings are obsolete; replaced by python-pycatch22.
Obsoletes:      python3-catch22 < 0.4.0-9

%global _description %{expand:
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

Requires:       %{name}-libs = %{version}-%{release}

%description %_description

This package contains the command-line tool run_features.


%package libs
Summary:        %{summary}

%description libs %{_description}

This package contains the implementation compiled as a shared library.


%package devel
Summary:        %{summary}

Requires:       %{name}-libs = %{version}-%{release}

%description devel %{_description}

This package contains headers and other files required for developing
applications that link against the implementation as a shared library.


%if %{with octave}
%global octpkg %{name}
%package -n octave-%{name}
Summary:        %{summary}

BuildRequires:  octave-devel

Requires:       octave(api) = %{octave_api}
Requires(post):   octave
Requires(postun): octave

%description -n octave-%{name} %_description
%endif


%prep
%autosetup -p1
cp -p '%{SOURCE3}' C/
find . -name ".gitignore" -print -delete

%if %{with octave}
# Set up for Octave install
echo "Does not yet support Octave."
%endif


%build
%set_build_flags
%make_build -C C DOWNSTREAM_SO_NUMBER='%{downstream_so_number}'

%if %{with octave}
echo "Does not yet support Octave."
%endif


%install
%make_install -C C \
    DOWNSTREAM_SO_NUMBER='%{downstream_so_number}' \
    PREFIX='%{_prefix}' \
    INCLUDEDIR='%{_includedir}' \
    LIBDIR='%{_libdir}' \
    BINDIR='%{_bindir}'
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE2}'

%if %{with octave}
echo "Does not yet support Octave."
%endif


%check
find testData -type f -name '*_output.txt' \
    -execdir cp -v -p '{}' '{}.expected' ';'
env LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
    PATH="${PATH}:%{buildroot}%{_bindir}" \
    ./testData/runtests.sh

for x in testData/*.expected
do
  %{python3} '%{SOURCE1}' \
      --ignore-extra='DN_Mean' \
      --ignore-extra='DN_Spread_Std' \
      "${x}" "$(echo "${x}" | sed -r 's/\.expected$//')"
done


%if %{with octave}
%post
%octave_cmd pkg rebuild


%preun
%octave_pkg_preun


%postun
%octave_cmd pkg rebuild
%endif


%files
%{_bindir}/run_features
%{_mandir}/man1/run_features.1*


%files libs
%license LICENSE

%{_libdir}/lib%{name}.so.0.%{downstream_so_number}


%files devel
%doc README.md featureList.txt

%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so


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
