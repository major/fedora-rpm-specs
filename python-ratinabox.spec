# Not yet packaged: python3dist(pettingzoo)
%bcond gymnasium 0

Name:           python-ratinabox
Version:        1.11.4
Release:        %autorelease
Summary:        A package for simulating motion and ephys data in continuous environments

# SPDX
License:        MIT
URL:            https://github.com/TomGeorge1234/RatInABox
# If we switched to the GitHub archive from the PyPI sdist, we could add a
# CITATION.bib file, a demos/ directory, and Sphinx-generated documentation;
# however, we consider this not worthwhile, especially since the demos are so
# large that it is doubtful whether it is worth packaging them.
Source:         %{pypi_source ratinabox}

BuildArch:      noarch

BuildRequires:  python3-devel

# Run tests in parallel (“-n auto”)
BuildRequires:  %{py3_dist pytest-xdist}
BuildRequires:  %{py3_dist torch}
Recommends:     %{py3_dist torch}

%global common_description %{expand:
RatInABox is a toolkit for generating locomotion trajectories and complementary
neural data for spatially and/or velocity selective cell types in complex
continuous environments.}

%description %{common_description}


%package -n     python3-ratinabox
Summary:        %{summary}

%description -n python3-ratinabox %{common_description}


%if %{with gymnasium}
%pyproject_extras_subpkg -n python3-ratinabox gymnasium
%endif


%prep
%autosetup -n ratinabox-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test%{?with_gymnasium:,gymnasium}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ratinabox


%check
# Let’s do this in addition to running the tests, so we can be aware of any
# issues in contribs that may not be tested.
%{pyproject_check_import \
    %{?!with_gymnasium:-e '*.contribs.TaskEnvironment'} }

%if %{without gymnasium}
# Indirectly (via ratinabox/contribs/TaskEnvironment.py) requires pettingzoo:
ignore="${ignore-} --ignore=tests/test_taskenv.py"
%endif
%pytest ${ignore-} -v -n auto


%files -n python3-ratinabox -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
