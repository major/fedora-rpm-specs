Name:           python-annotated-doc
Version:        0.0.4
Release:        %autorelease
Summary:        Document parameters, class attributes, return types, and variables inline

License:        MIT
URL:            https://github.com/fastapi/annotated-doc
Source:         %{url}/archive/%{version}/annotated-doc-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l annotated_doc

BuildArch:      noarch

# See requirements-tests.txt:
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
%pytest -v


%files -n python3-annotated-doc -f %{pyproject_files}
%doc CITATION.cff
%doc README.md


%changelog
%autochangelog
