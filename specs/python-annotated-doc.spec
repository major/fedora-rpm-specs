Name:           python-annotated-doc
Version:        0.0.3
Release:        %autorelease
Summary:        Document parameters, class attributes, return types, and variables inline

License:        MIT
URL:            https://github.com/fastapi/annotated-doc
Source:         %{url}/archive/%{version}/annotated-doc-%{version}.tar.gz

# Add typing-extensions to test deps. for Python <3.9
# https://github.com/fastapi/annotated-doc/pull/12
Patch:          %{url}/pull/12.patch

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
# Do not upper-bound (SemVer-bound) the version of uv_build; we must work with
# what we have, and compatibility across SemVer boundaries is good in practice.
sed -r -i 's/"(uv_build *>= *[^:]+), *<[^"]+"/"\1"/' pyproject.toml


%check -a
%pytest -v


%files -n python3-annotated-doc -f %{pyproject_files}
%doc CITATION.cff
%doc README.md


%changelog
%autochangelog
