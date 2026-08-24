Name:           python-annotated-doc
Version:        0.0.5
Release:        %autorelease
Summary:        Document parameters, class attributes, return types, and variables inline

License:        MIT
URL:            https://github.com/fastapi/annotated-doc
Source:         %{url}/archive/%{version}/annotated-doc-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install): --assert-license annotated_doc

BuildArch:      noarch

# See the “tests” dependency group. Since it contains many unwanted
# dependencies for things like linting and coverage, we list these manually:
BuildRequires:  %{py3_dist pytest} >= 8.3.5

%global common_description %{expand:
Document parameters, class attributes, return types, and variables inline, with
Annotated.}

%description %{common_description}


%package -n     python3-annotated-doc
Summary:        %{summary}

%description -n python3-annotated-doc %{common_description}


%prep -a
# We must work with what we have, and compatibility is good in practice.
%pyproject_patch_dependency uv_build:drop_upper


%check -a
# These tests pertain to upstream workflow and don’t really add value
# downstream, and they would require a circular dependency on python-typer.
ignore="${ignore-} --ignore=tests/test_prepare_release.py"

%pytest ${ignore-} --verbose


%files -n python3-annotated-doc -f %{pyproject_files}
%doc CITATION.cff
%doc README.md


%changelog
%autochangelog
