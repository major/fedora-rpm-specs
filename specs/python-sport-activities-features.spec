%global pypi_name sport-activities-features

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        %autorelease
Summary:        A minimalistic toolbox for extracting features from sports activity files

%global forgeurl https://github.com/firefly-cpp/sport-activities-features
%global tag %{version}
%forgemeta

# SPDX
License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global _description %{expand:
A minimalistic toolbox for extracting features from sport activity files
written in Python. Proposed software supports the extraction of following
topographic features from sport activity files: number of hills, average
altitude of identified hills, total distance of identified hills, climbing
ratio (total distance of identified hills vs. total distance), average ascent
of hills, total ascent, total descent and many others.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
%if !0%{?fc39} && !0%{?fc40}
Obsoletes:      python3-%{pypi_name}-tests < 0.4.2-1
%endif

%description -n python3-%{pypi_name} %_description

%if 0%{?fc39} || 0%{?fc40}
%package -n python3-%{pypi_name}-tests
Summary:        Tests for python3-%{pypi_name}

Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
%{summary}.
%endif

%package doc
Summary:        Documentation and examples for %{name}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%forgeautosetup -p1
rm -fv poetry.lock

#make dependencies consistent with Fedora versions
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sport_activities_features

%check
%if %{with tests}
# Upstream excludes some tests. We follow suit.
k="${k-}${k+ and }not test_overpy_node_manipulation"
k="${k-}${k+ and }not test_weather"
k="${k-}${k+ and }not test_data_analysis"
%pytest ${k:+-k "$k"}
%else
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%if 0%{?fc39} || 0%{?fc40}
%files -n python3-%{pypi_name}-tests
%doc tests/
%endif

%files doc
# Depends on base package, which provides the LICENSE file
%doc AUTHORS.rst
%doc CHANGELOG.md
%doc CITATION.cff
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc docs/preprints/A_minimalistic_toolbox.pdf
%doc examples/

%changelog
%autochangelog
