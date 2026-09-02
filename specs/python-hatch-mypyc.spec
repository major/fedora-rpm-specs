# Run tests that would require network access? We cannot do so in Koji, but we
# can use something like
#   fedpkg mockbuild --enable-network --with network_tests
# to try out these tests locally.
%bcond network_tests 0

Name:           python-hatch-mypyc
Version:        0.16.0
Release:        %autorelease
Summary:        Hatch build hook plugin for Mypyc

License:        MIT
URL:            https://github.com/ofek/hatch-mypyc
Source:         %{pypi_source hatch_mypyc}

BuildArch:      noarch
BuildRequires:  python3-devel

# See [envs.default.dependencies] in hatch.toml. We don’t need everything from
# that list.
%if %{with network_tests}
BuildRequires:  gcc
%endif
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist packaging}
BuildRequires:  %{py3_dist build[virtualenv]}

%global _description %{expand:
This provides a build hook plugin for Hatch that compiles code with Mypyc}

%description %_description

%package -n     python3-hatch-mypyc
Summary:        %{summary}

%description -n python3-hatch-mypyc %_description


%prep
%autosetup -p1 -n hatch_mypyc-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l hatch_mypyc


%check
%pyproject_check_import
%if %{without network_tests}
# All of these require network access.
ignore="${ignore-} --ignore=tests/test_build.py"
ignore="${ignore-} --ignore=tests/test_clean.py"
%else
# Upstream expects a wheel name like:
#   my_app-1.2.3-cp314-cp314-manylinux_2_43_x86_64.whl
# but we get something like:
#   my_app-1.2.3-cp314-cp314-linux_x86_64.whl
# which is not incorrect; the discrepancy is an artifact of the RPM build
# environment, and the tests work in a git checkout. It makes more sense to
# skip these tests than to try to get upstream to support our environment.
k="${k-}${k+ and }not test_no_exclusion"
k="${k-}${k+ and }not test_exclusion"
k="${k-}${k+ and }not test_separation"
k="${k-}${k+ and }not test_src_layout"
k="${k-}${k+ and }not test_dependency"
k="${k-}${k+ and }not test_build_dir"
%endif
# Similarly, the following tests work in a git checkout, but in our environment
# we get:
# E       ValueError: Unable to determine which files to ship inside the wheel
# E       using the following heuristics:
# E       https://hatch.pypa.io/latest/plugins/builder/wheel/#default-file-selection
# E       
# E       The most likely cause of this is that there is no directory that
# E        matches the name of your project (my_app).
# This does not seem worth chasing down.
k="${k-}${k+ and }not (TestPatternMatching and test_default_exclude)"
k="${k-}${k+ and }not (TestPatternMatching and test_exclude)"

%pytest -k "${k-}" ${ignore-} -v

%files -n python3-hatch-mypyc -f %{pyproject_files}
%doc README.md HISTORY.md

%changelog
%autochangelog
