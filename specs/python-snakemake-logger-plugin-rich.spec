# Temporarily package a post-release snapshot, fixing a missing license file
# and implementing the emit() method for compatibility with
# snakemake-interface-logger-plugins 2.0.0.
%global commit 4dd90dd5f799eed71af2204a3f6978ecabd60a03
%global snapdate 20251001

Name:           python-snakemake-logger-plugin-rich
Version:        0.4.0^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Log plugin for snakemake using Rich

# SPDX
License:        MIT
URL:            https://github.com/cademirch/snakemake-logger-plugin-rich
# Source:         %%{url}/archive/v%%{version}/snakemake-logger-plugin-rich-%%{version}.tar.gz
Source:         %{url}/archive/%{commit}/snakemake-logger-plugin-rich-%{commit}.tar.gz

# Add the license to the package metadata (PEP 639)
# https://github.com/cademirch/snakemake-logger-plugin-rich/pull/27
Patch:          %{url}/pull/27.patch

BuildSystem:            pyproject
BuildOption(install):   -l snakemake_logger_plugin_rich

BuildArch:      noarch

# See: [project.optional-dependencies], which also contains unwanted linters
# and typecheckers
BuildRequires:  %{py3_dist pytest} >= 8.3.5
BuildRequires:  snakemake >= 9.0.1

%global common_description %{expand:
A logging plugin for Snakemake that utilizes rich for enhanced terminal styling
and progress bars.}

%description %{common_description}


%package -n python3-snakemake-logger-plugin-rich
Summary:        %{summary}

%description -n python3-snakemake-logger-plugin-rich %{common_description}


%check -a
%pytest -v


%files -n python3-snakemake-logger-plugin-rich -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
