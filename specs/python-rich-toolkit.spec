%bcond inline_snapshot 1
# Currently, all tests are snapshot-based.
%bcond tests %{with inline_snapshot}

Name:           python-rich-toolkit
Version:        0.19.0
Release:        %autorelease
Summary:        Rich toolkit for building command-line applications

# SPDX
License:        MIT
URL:            https://github.com/patrick91/rich-toolkit
Source:         %{pypi_source rich_toolkit}

BuildSystem:            pyproject
BuildOption(install):   -l rich_toolkit

BuildArch:      noarch

%if %{with tests}
# Testing dependencies; these are included in the “dev” dependency group, but
# this also includes a number of dependencies that are only used for debugging,
# typechecking, running the examples, etc.; we therefore maintain this list
# manually rather than attempting to generate it.
BuildRequires:  %{py3_dist pytest} >= 8.3.2
%if %{with inline_snapshot}
BuildRequires:  %{py3_dist inline-snapshot} >= 0.12.1
%endif
# For tests/test_input_validator.py:
BuildRequires:  %{py3_dist pydantic}
%endif

%global common_description %{expand:
This is a very opinionated set of components for building CLI applications. It
is based on Rich.}

%description %common_description


%package -n     python3-rich-toolkit
Summary:        %{summary}

%description -n python3-rich-toolkit %common_description


%check -a
%if %{with tests}
%if %{without inline_snapshot}
ignore="${ignore-} --ignore=tests/test_toolkit.py"
ignore="${ignore-} --ignore=tests/test_tagged_style.py"
%endif

%pytest ${ignore-} -v
%endif


%files -n python3-rich-toolkit -f %{pyproject_files}
%doc README.md
%doc examples/


%changelog
%autochangelog
