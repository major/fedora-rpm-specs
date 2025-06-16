# Not yet packaged: python3dist(pettingzoo)
%bcond gymnasium 0

# F43FailsToInstall: python3-torch
# https://bugzilla.redhat.com/show_bug.cgi?id=2372164
%bcond torch 0

Name:           python-ratinabox
Version:        1.15.3
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

%if %{with torch}
%ifarch %{x86_64} %{arm64}
%global can_test_torch 1
%endif
%endif

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x test%{?with_gymnasium:,gymnasium}
BuildOption(install):   -l ratinabox
# Outer conditional avoids an empty BuildOption, which would be an error.
%if %{without gymnasium} || !0%{?can_test_torch}
BuildOption(check):     %{shrink:
                        %{?!can_test_torch:-e '*.contribs.NeuralNetworkNeurons'}
                        %{?!with_gymnasium:-e '*.contribs.TaskEnvironment'}
                        }
%endif

# The package is arched so that the BR and weak dependency on python-torch can
# be conditionalized. It does not contain compiled machine code, so there are
# no debugging symbols.
%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# (Plus, python-scikit-learn has dropped i686.)
ExcludeArch:    %{ix86}

# Run tests in parallel (“-n auto”)
BuildRequires:  %{py3_dist pytest-xdist}
%if %{with torch}
BuildRequires:  (%{py3_dist torch} if (python3(x86-64) or python3(aarch-64)))
%endif

%global common_description %{expand:
RatInABox is a toolkit for generating locomotion trajectories and complementary
neural data for spatially and/or velocity selective cell types in complex
continuous environments.}

%description %{common_description}


%package -n     python3-ratinabox
Summary:        %{summary}

BuildArch:      noarch

%if %{with torch}
Recommends:     (%{py3_dist torch} if (python3(x86-64) or python3(aarch-64)))
%endif

%description -n python3-ratinabox %{common_description}


%if %{with gymnasium}
%pyproject_extras_subpkg -n python3-ratinabox gymnasium
%endif


%check -a
%if %{without gymnasium}
# Indirectly (via ratinabox/contribs/TaskEnvironment.py) requires pettingzoo:
ignore="${ignore-} --ignore=tests/test_taskenv.py"
%endif
%pytest ${ignore-} -v -n auto


%files -n python3-ratinabox -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
