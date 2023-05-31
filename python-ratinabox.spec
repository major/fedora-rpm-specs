Name:           python-ratinabox
Version:        1.6.3
Release:        %autorelease
Summary:        A package for simulating motion and ephys data in continuous environments

# SPDX
License:        MIT
URL:            https://github.com/TomGeorge1234/RatInABox
# If we switched to the GitHub archive from the PyPI sdist, we could add a
# CITATION.bib file and a demos/ directory; however, we consider this not
# worthwhile, especially since the demos are so large that it is doubtful
# whether it is worth packaging them.
Source:         %{pypi_source ratinabox}

BuildArch:      noarch

BuildRequires:  python3-devel

# Add scikit-learn to “test” extra
# https://github.com/TomGeorge1234/RatInABox/pull/48
BuildRequires:  %{py3_dist scikit-learn}
# Run tests in parallel (“-n auto”)
BuildRequires:  %{py3_dist pytest-xdist}

%global common_description %{expand:
RatInABox is a toolkit for generating locomotion trajectories and complementary
neural data for spatially and/or velocity selective cell types in complex
continuous environments.}

%description %{common_description}


%package -n     python3-ratinabox
Summary:        %{summary}

%description -n python3-ratinabox %{common_description}


%prep
%autosetup -n ratinabox-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ratinabox


%check
%pytest -n auto


%files -n python3-ratinabox -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
