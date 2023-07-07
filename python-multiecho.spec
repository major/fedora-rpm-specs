# The sole test does not seem to work
# https://github.com/Donders-Institute/multiecho/issues/16
#
# Upstream, not the original author, agrees that it appears to be a placeholder
# rather than a usable test.
%bcond tests 0

# We temporarily package a post-release snapshot, with the following changes.
# The justification is that we would have needed to apply most of this as
# patches anyway, and the snapshot is cleaner and easier since it contains no
# unwanted changes from the release (no functional changes to the
# implementation or API).
#
# - Minor bugfixes to setup.py
# - Do not install tests in site-packages
# - Clarified the license usage
# - Use argparse-manpage
# - Minor cleanup in README.md
%global commit b4078f0c3505be692279a6c322d687ed47d1f1bf
%global snapdate 20230704

Name:           python-multiecho
Version:        0.28^%{snapdate}git%(c='%{commit}'; echo "${c:0:7}")
Release:        %autorelease
Summary:        Combine multi-echoes from a multi-echo fMRI acquisition

# In response to:
#
# Please clarify licenses
# https://github.com/Donders-Institute/multiecho/issues/15
#
# Upstream confirmed disjunctive dual-licensing was intended in:
#
# Clarified the license usage (github issue #15)
# https://github.com/Donders-Institute/multiecho/commit/70cc802c11dc051d122d42e9062a19fa275068ee
License:        Apache-2.0 OR MIT
URL:            https://github.com/Donders-Institute/multiecho
Source:         %{url}/archive/%{commit}/multiecho-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# setup.py: tests_require
BuildRequires:  %{py3_dist pytest}
%endif

%global common_description %{expand:
MRI data acquisitions can involve multiple volumes acquired at different echo
times. Typically, subsequent processing pipelines assume data to be acquired at
a singl echo time. This package provides a library and command-line tool to
combine multiple echoes from a multi-echo (BOLD f)MRI acquisition.}

%description %{common_description}


%package -n python3-multiecho
Summary:        %{summary}

%description -n python3-multiecho %{common_description}


%prep
%autosetup -n multiecho-%{commit}
# Remove the shebang from the multiecho.combination module; upstream seems to
# have intended it to be directly executable as a script when working on the
# source, but it will not be installed with the executable bit set, so the
# shebang is useless. When packaged, we have the entry point “mecombine”
# anyway.
sed -r -i '1{/^#!/d}' multiecho/combination.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files multiecho
#install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-multiecho -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc README.md

%{_bindir}/mecombine
%{_mandir}/man1/mecombine.1*


%changelog
%autochangelog
