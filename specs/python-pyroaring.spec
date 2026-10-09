# We don’t normally run benchmarks, but it’s nice to be able to.
%bcond benchmarks 0

Name:           python-pyroaring
Version:        1.0.4
Release:        %autorelease
Summary:        Library for handling efficiently sorted integer sets

# The source contains a bundled, amalgamated copy of croaring in
# pyroaring/roaring.{h,c}; these two files are (Apache-2.0 OR MIT). We remove
# them in %%prep, so they do not contribute to the licenses of the binary RPMs.
License:        MIT
SourceLicense:  %{license} AND (Apache-2.0 OR MIT)
URL:            https://github.com/Ezibenroc/PyRoaringBitMap
Source:         %{url}/archive/%{version}/PyRoaringBitMap-%{version}.tar.gz

# Respect system compiler flags (no -O3)
#
# Downstream-only because upstream validly wants to add -O3, but we have not
# proven it is justified. A casual comparative benchmark on x86_64 showed no
# consistent and measurable improvement, and perhaps a small loss in some
# microbenchmarks. This makes sense because we use the system croaring library,
# and if there are any routines that benefit from -O3, they are likely to be in
# those inner “hot” loops, not in the surrounding “glue” in the Python
# extension.
Patch:          0001-Respect-system-compiler-flags-no-O3.patch
# Do not build bundled croaring library; link libroaring
#
# Removing the bundled copy and dealing with include paths are outside the
# scope of this patch.
#
# Downstream-only for now; it would be nice to suggest an easy way to use a
# system copy upstream, but it’s not immediately obvious how best to do this in
# an upstreamable way.
Patch:          0002-Do-not-build-bundled-croaring-library-link-libroarin.patch

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --tox --toxenv=cython3
BuildOption(install): --assert-license pyroaring

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(roaring)
%if %{with benchmarks}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist tabulate}
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global common_description %{expand:
An efficient and light-weight ordered set of integers. This is a Python wrapper
for the C library CRoaring.}

%description %{common_description}

%package -n python3-pyroaring
Summary:        %{summary}

%description -n python3-pyroaring %{common_description}


%prep -a
# Unbundle croaring
rm pyroaring/roaring.c
printf '#include <%s>\n' 'roaring/roaring.h' > pyroaring/roaring.h


%check -a
%tox --toxenv=%{toxenv}

%if %{with benchmarks}
%{py3_test_envvars} %{python3} ./quick_bench.py
%endif


%files -n python3-pyroaring -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
