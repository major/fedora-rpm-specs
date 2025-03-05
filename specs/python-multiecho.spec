# The sole test does not seem to work
# https://github.com/Donders-Institute/multiecho/issues/16
#
# Upstream, not the original author, agrees that it appears to be a placeholder
# rather than a usable test.
%bcond tests 0

Name:           python-multiecho
Version:        0.30
Release:        %autorelease
Summary:        Combine multi-echoes from a multi-echo fMRI acquisition

License:        Apache-2.0 OR MIT
URL:            https://github.com/Donders-Institute/multiecho
Source:         %{url}/archive/%{version}/multiecho-%{version}.tar.gz

# Minor setup fix
# https://github.com/Donders-Institute/multiecho/commit/c9d355d012c4603700489d5a192abc1e8818cba9
Patch:          %{url}/commit/c9d355d012c4603700489d5a192abc1e8818cba9.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# setup.py: tests_require
BuildRequires:  %{py3_dist pytest}
%endif

%global common_description %{expand:
MRI data acquisitions can involve multiple volumes acquired at different echo
times. Typically, subsequent processing pipelines assume data to be acquired at
a single echo time. This package provides a library and command-line tool to
combine multiple echoes from a multi-echo (BOLD f)MRI acquisition.}

%description %{common_description}


%package -n python3-multiecho
Summary:        %{summary}

%description -n python3-multiecho %{common_description}


%prep
%autosetup -n multiecho-%{version} -p1
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
%pyproject_save_files -l multiecho


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python3-multiecho -f %{pyproject_files}
%doc README.md

%{_bindir}/mecombine
%{_mandir}/man1/mecombine.1*


%changelog
%autochangelog
