# Not packaged: python3dist(pydeface)
%bcond deface 0
# Not packaged: python3dist(dicom-parser), python3dist(psychopy)
%bcond extras 0

# Not packaged: python3dist(drmaa)
#
# Even though it is not an optional dependency, upstream writes[1] that “the
# drmaa dependency is not really important (only for speeding up a few
# applications)”; furthermore, it is in no condition to be packaged, as the
# last release was in 2018, the tests require (deprecated) nose, and they don’t
# currently pass.
# [1] https://github.com/Donders-Institute/multiecho/pull/19#issuecomment-1621503955
%bcond drmaa 0

Name:           bidscoin
Version:        4.6.2
Release:        %autorelease
Summary:        Converts and organizes raw MRI data-sets according to BIDS

License:        GPL-3.0-or-later
URL:            https://github.com/Donders-Institute/bidscoin
Source:         %{url}/archive/%{version}/bidscoin-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l bidscoin
BuildOption(generate_buildrequires): %{shrink:
                                     -x dcm2niix2bids
                                     -x spec2nii2bids
                                     %{?with_deface:-x deface}
                                     %{?with_deface:-x all}
                                     %{?with_extras:-x extras}
                                     }
BuildOption(check):     %{shrink:
                        %{?!with_deface:-e 'bidscoin.bidsapps.*deface'}
                        }

BuildArch:      noarch

BuildRequires:  tomcli

# We do not generate BuildRequires from the “dev” extra because it depends on
# other extras that may be disabled by build conditionals, and because it
# includes documentation dependencies and other dependencies that may be
# unwanted.
BuildRequires:  %{py3_dist pytest}

%description
BIDScoin is a user-friendly Python application suite that converts (“coins”)
source-level (raw) neuroimaging data sets to standardized data sets that are
organized according to the Brain Imaging Data Structure (BIDS) specification.
Rather than depending on complex programmatic logic for source data-type
identification, BIDScoin uses a mapping approach to discover the different
source data types in your repository and convert them into BIDS data types.
Different runs of source data are uniquely identified by their file system
properties (e.g. file name or size) and by their attributes (e.g. ProtocolName
from the DICOM header). Mapping information can be pre-specified (e.g. per
site), allowing BIDScoin to make intelligent first suggestions on how to
classify and convert the data. While this command-line procedure exploits all
information available on disk, BIDScoin offers a Graphical User Interface (GUI)
for researchers to check and edit these mappings – bringing in the missing
knowledge that often exists in their heads only. This interactive step can also
be skipped for employment in fully automated dataflow pipelines.

BIDScoin requires no programming knowledge in order to use it, but users can
use regular expressions and plug-ins to further enhance BIDScoin’s power and
flexibility, and readily handle a wide variety of source data types.


%pyproject_extras_subpkg -n bidscoin dcm2niix2bids
%pyproject_extras_subpkg -n bidscoin spec2nii2bids
%if %{with deface}
%pyproject_extras_subpkg -n bidscoin deface
%endif
%if %{with deface}
%pyproject_extras_subpkg -n bidscoin all
%endif
%if %{with extras}
%pyproject_extras_subpkg -n bidscoin extras
%endif


%prep -a
%if %{without drmaa}
tomcli set pyproject.toml lists delitem project.dependencies drmaa
%endif

# Remove shebangs from sources that will be installed in site-packages and
# therefore will not have executable permissions. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find bidscoin/ -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'


%check -a
# Requires network access:
k="${k-}${k+ and }not test_check_version"
# Tries to access the man page outside the buildroot:
k="${k-}${k+ and }not test_list_executables"

%pytest -k "${k-}" -v


%files -f %{pyproject_files}
%doc README.rst

%{_bindir}/bidscoin
%{_bindir}/bidscoiner
%{_bindir}/bidseditor
%{_bindir}/bidsmapper
%{_bindir}/bidsparticipants
%{_bindir}/deface
%{_bindir}/dicomsort
%{_bindir}/echocombine
%{_bindir}/fixmeta
%{_bindir}/medeface
%{_bindir}/physio2tsv
%{_bindir}/plotphysio
%{_bindir}/rawmapper
%{_bindir}/skullstrip
%{_bindir}/slicereport

%{_mandir}/man1/bidscoin.1*
%{_mandir}/man1/bidscoiner.1*
%{_mandir}/man1/bidseditor.1*
%{_mandir}/man1/bidsmapper.1*
%{_mandir}/man1/bidsparticipants.1*
%{_mandir}/man1/deface.1*
%{_mandir}/man1/dicomsort.1*
%{_mandir}/man1/echocombine.1*
%{_mandir}/man1/fixmeta.1*
%{_mandir}/man1/medeface.1*
%{_mandir}/man1/physio2tsv.1*
%{_mandir}/man1/plotphysio.1*
%{_mandir}/man1/rawmapper.1*
%{_mandir}/man1/skullstrip.1*
%{_mandir}/man1/slicereport.1*


%changelog
%autochangelog
