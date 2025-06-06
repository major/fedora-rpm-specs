# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc %[ %{defined fc42} || %{defined fc41} ]

# For now, we treat https://github.com/wtclarke/mrs_nifti_standard as a bundled
# dependency. However, it’s not clear if it makes sense to try to unbundle it
# or if (since what is bundled is merely a data file) it even makes sense to
# consider it as a bundled dependency. The only part that might be used by
# other packages is the machine-readable specification, definitions.json; this
# is also the only part we need.
%global std_version 0.10

Name:           python-nifti-mrs
Version:        1.3.3
Release:        %autorelease
Summary:        Software tools for the NIfTI-MRS data format

# The entire package is BSD-3-Clause:
# - The generated %%{python3_sitelib}/nifti_mrs/_version.py in
#   python3-nifti-mrs is Unlicense because it is generated by Versioneer
#   (python-versioneer).
# - Content from Source1 is CC-BY-4.0 (any code is BSD-3-Clause and is not
#   included in the binary distributions). Specifically, we distribute
#   definitions.json under CC-BY-4.0.
License:        BSD-3-Clause AND Unlicense AND CC-BY-4.0
URL:            https://github.com/wtclarke/nifti_mrs_tools
# The GitHub archive contains API documentation and a changelog file, which the
# PyPI sdists lack. (On the other hand, if we switched to the PyPI sdists, we
# would not need a second source for the standard specification.)
Source0:        %{url}/archive/%{version}/nifti_mrs_tools-%{version}.tar.gz
%global std_url https://github.com/wtclarke/mrs_nifti_standard
Source1:        %{std_url}/archive/v%{std_version}/mrs_nifti_standard-%{std_version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source10:       mrs_tools.1
Source11:       mrs_tools-conjugate.1
Source12:       mrs_tools-info.1
Source13:       mrs_tools-merge.1
Source14:       mrs_tools-reorder.1
Source15:       mrs_tools-reshape.1
Source16:       mrs_tools-split.1
Source17:       mrs_tools-vis.1

BuildSystem:            pyproject
BuildOption(install):   -l nifti_mrs mrs_tools
# - nifti_mrs.vis requires (via the VIS extra), the nonfree fsl-mrs
BuildOption(check):     -e nifti_mrs.vis

# The base package is arched due to endian-dependent test failures, but the
# binary packages are noarch and contain no compiled code.
%global debug_package %{nil}

# Requires python3dist(fslpy), which requires python3dist(h5py), which is
# ExcludeArch: %%{ix86}.
ExcludeArch:    %{ix86}
 
BuildRequires:  %{py3_dist pytest}

%if %{with doc}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
This package contains python-based tools for representing, validating, and
manipulating the NIfTI-MRS format. NIfTI-MRS is a standardized format for
storing Magnetic Resonance Spectroscopy data.

These tools are used extensively in the spec2nii format conversion program and
the FSL-MRS analysis software. However, this library can also be used as a
stand-alone set of tools.

If you use these tools please cite: Clarke, WT, Bell, TK, Emir, UE, et al.
NIfTI-MRS: A standard data format for magnetic resonance spectroscopy. Magn
Reson Med. 2022; 88: 2358- 2370. doi:10.1002/mrm.29418}

%description %{common_description}


%package -n     python3-nifti-mrs
Summary:        %{summary}
License:        BSD-3-Clause AND Unlicense

BuildArch:      noarch

%py_provides python3-mrs-tools

# See notes at the top of the spec file; this should perhaps not really be
# considered a bundled dependency, but it is useful to annotate it.
Provides:       bundled(mrs_nifti_standard) = %{std_version}

# The mrs_tools subpackage was merged back into this one because it turns out
# that the nifti_mrs package imports from the mrs_tools package, even though
# the latter is basically just the implementation of the command-line tool.
# Since the libraries import each other, there is no value (and some risk) in
# packaging them separately – and there is little point in maintaining an
# mrs_tools subpackage solely for the entry point and man pages. The following
# Provides/Obsoletes may be removed after F44 reaches EOL:
Provides:       mrs_tools = %{version}-%{release}
Obsoletes:      mrs_tools < 1.3.0-3

%if %{without doc}
# Removed for F43, so we can drop the Obsoletes after F45:
Obsoletes:      python-nifti-mrs-doc < 1.3.3-5
%endif

%description -n python3-nifti-mrs %{common_description}


# We don’t generate a metapackage for the “VIS” extra because it requires
# fsl-mrs, which (1) is not packaged, (2) is not on PyPI, (3) is non-free
# (non-commercial use only).


%if %{with doc}
%package        doc
Summary:        Documentation for python-nifti-mrs
# This subpackage contains neither _version.py (under Unlicense) nor content
# from the standard specification, Source1, under CC-BY-4.0.
License:        BSD-3-Clause

BuildArch:      noarch

%description    doc %{common_description}
%endif


%prep
%autosetup -n nifti_mrs_tools-%{version}
%setup -q -T -D -b 1 -n nifti_mrs_tools-%{version}
# Upstream uses a git submodule. Since "exclude src/nifti_mrs/standard/*/*"
# appears in MANIFEST.in, which means only top-level contents of the submodule
# appear in the sdist, we imitate this with the find command.
find ../mrs_nifti_standard-%{std_version} -mindepth 1 -maxdepth 1 -type f \
    -exec ln '{}' src/nifti_mrs/standard/ ';'
# We do also want to package a copy of the license text for the standard.
ln ../mrs_nifti_standard-%{std_version}/LICENSE LICENSE-mrs_nifti_standard


%build -a
%if %{with doc}
PYTHONPATH="${PWD}/src" %make_build -C apidoc latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C apidoc/_build/latex LATEXMKOPTS='-quiet'
%endif


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE15}' '%{SOURCE16}' '%{SOURCE17}'


%check -a
%ifarch s390x
# Tests fail when file endianness does not match host endianness
# https://github.com/wtclarke/nifti_mrs_tools/issues/16
# Nevertheless, the software may still be useful on this architecture for
# processing big-endian NIfTI files, so we skip the tests rather than adding
# ExcludeArch.
k="${k-}${k+ and }not test_nifti_mrs_save"
k="${k-}${k+ and }not test_merge"
k="${k-}${k+ and }not test_split"
k="${k-}${k+ and }not test_reorder"
k="${k-}${k+ and }not test_reshape"
k="${k-}${k+ and }not test_conjugate"
%endif

# Skip tests that require FSL-MRS tools, which are nonfree (restricted to
# noncommercial use).
m="${m-}${m+ and }not with_fsl_mrs"

%pytest -k "${k-}" -m "${m-}" -v


%files -n python3-nifti-mrs -f %{pyproject_files}
%if %{without doc}
%doc CHANGELOG.md
%doc README.md
%endif
%{_bindir}/mrs_tools
%{_mandir}/man1/mrs_tools*.1*


%if %{with doc}
%files doc
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc apidoc/_build/latex/nifti-mrs.pdf
%endif


%changelog
%autochangelog
